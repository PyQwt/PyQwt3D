#!/usr/bin/python
#
# Generate the build tree and Makefiles for PyQwt3D.
#
# Copyright (C) 2004 Gerard Vermeulen
#
# This file is part of PyQwt3D.
#
# PyQwt3D is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# PyQwt3D is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along
# with PyQwt3D; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In addition, as a special exception, Gerard Vermeulen gives permission to
# link PyQwt3D dynamically with commercial, non-commercial or educational
# versions of Qt, PyQt and sip, and distribute PyQwt in this form, provided
# that equally powerful versions of Qt, PyQt and sip have been released under
# the terms of the GNU General Public License.
#
# If PyQwt3D is dynamically linked with commercial, non-commercial or
# educational versions of Qt, PyQt and sip, PyQwt3D becomes a free plug-in for
# a non-free program.


import compileall
import glob
import os
import pprint
import re
import shutil
import sys

from optparse import OptionParser

import sipconfig
import pyqtconfig


def lazy_copy_sip_output_file(source, target):
    """Lazy copy a sip output file to another sip output file: 
    - check if source and target sip do really differ,
    - copy the source file to the target if they do,
    - return True on copy and False on no copy.
    """
    if not os.path.exists(target):
        shutil.copy2(source, target)
        return True

    sourcelines = open(source).readlines()
    targetlines = open(target).readlines()

    # global length check
    if len(sourcelines) != len(targetlines):
        shutil.copy2(source, target)
        return True
    
    # skip header comments by looking for the first '#define'
    line = 0
    while line < len(sourcelines):
        if sourcelines[line][0] == "#":
            break
        line = line + 1
        
    # line by line check
    while line < len(sourcelines):
        if sourcelines[line] != targetlines[line]:
            shutil.copy2(source, target)
            return True
        line = line + 1
        
    return False

# lazy_copy_sip_output_file()


def check_numarray(configuration, options):
    """See if the numarray extension has been installed.
    """
    if options.disable_numarray:
        options.excluded_features.append("-x HAS_NUMARRAY")
        return options
       
    try:
        import numarray
        # Try to find numarray/arrayobject.h.
        numarray_inc = os.path.join(
            configuration.py_inc_dir, "numarray", "arrayobject.h")
        if os.access(numarray_inc, os.F_OK):
            print "Found numarray-%s.\n" % numarray.__version__
            options.extra_defines.append("HAS_NUMARRAY")
        else:
            print ("numarray has been installed, "
                   "but its headers are not in the standard location.\n"
                   "PyQwt will be build without support for numarray.\n"
                   "(Linux users may have to install a development package)\n"
                   )
            raise ImportError
    except ImportError:
        options.excluded_features.append("-x HAS_NUMARRAY")
        print ("Failed to import numarray: "
               "PyQwt will be build without support for numarray.\n"
               )
        
    return options

# check_numarray()


def check_numeric(configuration, options):
    """See if the Numeric extension has been installed.
    """
    if options.disable_numeric:
        options.excluded_features.append("-x HAS_NUMERIC")
        return options
           
    try:
        import Numeric
        # Try to find Numeric/arrayobject.h.
        numeric_inc = os.path.join(
            configuration.py_inc_dir, "Numeric", "arrayobject.h")
        if os.access(numeric_inc, os.F_OK):
            print "Found Numeric-%s.\n" % Numeric.__version__
            options.extra_defines.append("HAS_NUMERIC")
        else:
            print ("Numeric has been installed, "
                   "but its headers are not in the standard location.\n"
                   "PyQwt will be build without support for Numeric.\n"
                   "(Linux users may have to install a development package)\n"
                   )
            raise ImportError
    except ImportError:
        options.excluded_features.append("-x HAS_NUMERIC")
        print ("Failed to find Numeric: "
               "PyQwt will be build without support for Numeric.\n"
               )
        
    return options

# check_numeric()


def check_sip(configuration, options):
    """Adapt to SIP differences by means of mutually excluding features
    """
    print "Found SIP-%s.\n" % configuration.sip_version_str

    sip_version = configuration.sip_version
    if sip_version & 0xffff00 == 0x040000: 
        options.excluded_features.extend(["-x SIP0401", "-x OLDSIP"])
    elif sip_version & 0xffff00 == 0x040100:
        options.excluded_features.extend(["-x SIP0400", "-x OLDSIP"])
    elif sip_version & 0xffff00 == 0x030b00:
        # SIP-3.11.x works like SIP-4.1.x (except for bugs)
        options.excluded_features.extend(["-x SIP0400", "-x NEWSIP"])
    else:
        raise SystemExit, (
            "PyQwt3D requires SIP-4.1.x, -4.0.x, or -3.11.x.\n"
            )

    return options

# check_sip()


def check_compiler(configuration, options):
    """Adapt to different compilers by means of mutually excluding features
    """
    makefile = sipconfig.Makefile(configuration=configuration)
    generator = makefile.optional_string('MAKEFILE_GENERATOR', 'UNIX')
    # FIXME: 'MSVC' should be worse than 'MSVC.NET'
    if generator in ['MSVC', 'MSVC.NET']:
        options.excluded_features.append('-x NO_MSVC')
        options.extra_cxxflags.extend(['-GR', '-GX'])
    else:
        options.excluded_features.append('-x IS_MSVC')
    
    return options

# check_compiler()


def check_os(configuration, options):
    """Adapt to different operating systems
    """
    print "Found '%s' operating system:" % os.name
    print sys.version
    print

    if os.name == 'nt':
        options.extra_defines.append('WIN32')

    return options

# check_os()


def parse_args():
    """Return the parsed options and args from the command line
    """

    usage = (
        'python configure.py [options]'
        '\n\nEach option takes at most one argument, but some options'
        '\naccumulate arguments when repeated. For example, invoke:'
        '\n\n\tpython configure.py -I %s -I %s'
        '\n\nto search the current *and* parent directories for headers.'
        ) % (os.curdir, os.pardir)

    parser = OptionParser(usage=usage)
    
    parser.add_option(
        '-Q', '--qwtplot3d-sources', default='', action='store',
        type='string', metavar='/sources/of/qwtplot3d',
        help=('compile and link the QwtPlot3D source files in'
              ' /sources/of/qwtplot3d statically into PyQwt3D'
              ' (required on Windows)'))
    parser.add_option(
        '-D', '--extra-defines', default=[], action='append',
        type='string', metavar='GL2PS_HAVE_ZLIB',
        help='add an extra preprocessor definition')
    parser.add_option(
        '-I', '--extra-include-dirs', default=[], action='append',
        type='string', metavar='/usr/include/qwtplot3d',
        help=('add an extra directory to search for headers'
              ' (the compiler must be able to find the QwtPlot3D headers'
              ' if you did not specify the -Q option)'))
    parser.add_option(
        '-L', '--extra-lib-dirs', default=[], action='append',
        type='string', metavar='/usr/lib/qt3/lib',
        help=('add an extra directory to search for libraries'
              ' (the linker must be able to find the QwtPlot3D library'
              ' if you did not specify the -Q option)'))
    parser.add_option(
        '-j', '--jobs', default=0, action='store',
        type='int', metavar='N',
        help=('concatenate the SIP generated code into N files'
              ' [default 1 per class] (speeds up compilation and allows to'
              ' take advantage of multiprocessor systems)'))
    parser.add_option(
        '-l', '--extra-libs', default=[], action='append',
        type='string', metavar='z',
        help=('add an extra library (to link the zlib library, you must'
              ' specify "zlib" on Windows and "z" on POSIX and MacOS/X)'))
    parser.add_option(
        '-x', '--excluded-features', default=[], action='append',
        type='string', metavar='EXTRA_SENSORY_PERCEPTION',
        help=('add a feature for SIP to exclude'
              ' (normally one of the features in sip/features.sip)'))
    parser.add_option(
        '--debug', default=False, action='store_true',
        help='build with debugging symbols [default disabled]')              
    parser.add_option(
        '--disable-numarray', default=False, action='store_true',
        help='disable detection and use of numarray [default enabled]')
    parser.add_option(
        '--disable-numeric', default=False, action='store_true',
        help='disable detection and use of Numeric [default enabled]')
    parser.add_option(
        '--extra-cflags', default=[], action='append',
        type='string', metavar='EXTRA_CFLAG',
        help='add an extra C compiler flags')
    parser.add_option(
        '--extra-cxxflags', default=[], action='append',
        type='string', metavar='EXTRA_CXXFLAG',
        help='add an extra C++ compiler flag')
    parser.add_option(
        '--extra-lflags', default=[], action='append',
        type='string', metavar='EXTRA_LFLAG',
        help='add an extra linker flag')
    
    options, args =  parser.parse_args()
    
    # 'normalize' some options
    if options.jobs < 1:
        options.jobs = ''
    else:
        options.jobs = '-j %s' % options.jobs
    options.excluded_features = [
        ('-x %s' % f) for f in options.excluded_features
        ]

    return options, args

# parse_args()


def main():
    
    # parse the command line
    options, args = parse_args()

    print "Command line options:"
    pprint.pprint(options.__dict__)
    print

    # initialize
    configuration = pyqtconfig.Configuration()
    build_dir = "Qwt3D"
    tmp_build_dir = "tmp-" + build_dir
    build_file = os.path.join(build_dir, "qwt3d.sbf")
    mod_dir = os.path.join(configuration.default_mod_dir, 'Qwt3D')
    sip_dir = os.path.join(configuration.pyqt_sip_dir, 'Qwt3D')
    extra_sources = []
    extra_headers = []
    extra_moc_headers = []

    # extend the options
    options = check_sip(configuration, options)
    options = check_os(configuration, options)
    options = check_compiler(configuration, options)
    options = check_numarray(configuration, options)
    options = check_numeric(configuration, options)

    # do we link against a QwtPlot3D library?
    if options.qwtplot3d_sources:
        # yes, zap all 'qwtplot3d'
        while options.extra_libs.count('qwtplot3d'):
            options.extra_libs.remove('qwtplot3d')
    elif 'qwtplot3d' not in options.extra_libs:
        # no, add 'qwtplot3d' if needed
        options.extra_libs.append('qwtplot3d')

    print "Extended options:"
    pprint.pprint(options.__dict__)
    print
    
    # do we compile and link the sources of QwtPlot3D statically into PyQwt3D?
    if options.qwtplot3d_sources:
        extra_sources += glob.glob(os.path.join(
            options.qwtplot3d_sources, 'src', '*.cpp'))
        extra_sources += glob.glob(os.path.join(
            options.qwtplot3d_sources, '3rdparty', 'gl2ps', '*.c'))
        extra_headers += glob.glob(os.path.join(
            options.qwtplot3d_sources, 'include', '*.h'))
        extra_headers += glob.glob(os.path.join(
            options.qwtplot3d_sources, '3rdparty', 'gl2ps', '*.h'))
        extra_moc_headers = []
        for header in extra_headers:
            text = open(header).read()
            if re.compile(r'^\s*Q_OBJECT', re.M).search(text):
                extra_moc_headers.append(header)

    # add the interface to the numerical Python extensions
    extra_sources += glob.glob(os.path.join(os.pardir, 'numpy', '*.cpp'))
    extra_headers += glob.glob(os.path.join(os.pardir, 'numpy', '*.h'))

    # generate code into a clean temporary directory
    try:
        shutil.rmtree(tmp_build_dir)
    except:
        pass
    os.mkdir(tmp_build_dir)
    # generate the build file into the build directory
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)
        
    cmd = " ".join(
        [configuration.sip_bin,
         # SIP assumes POSIX style path separators
         "-I", os.path.join(os.pardir, "sip").replace("\\", "/"),
         "-I", configuration.pyqt_sip_dir.replace("\\", "/"),
         "-b", build_file,
         "-c", tmp_build_dir,
         options.jobs,
         configuration.pyqt_qt_sip_flags,
         ]
        + options.excluded_features
        # SIP assumes POSIX style path separators
        + [os.path.join(os.pardir, "sip", "qwt3dmod.sip").replace("\\", "/")]
        )

    print "sip invokation:"
    pprint.pprint(cmd)
    print

    if os.path.exists(build_file):
        os.remove(build_file)
    os.system(cmd)
    if not os.path.exists(build_file):
        raise SystemExit, 'SIP failed to generate the C++ code.'

    # Windows fix: resolve the scope of POINTS in enumValues[]
    for source in glob.glob(os.path.join(tmp_build_dir, '*.cpp')):
        text = open(source).read()
        if (-1 != text.find('{sipNm__Qwt3D_POINTS, POINTS}')):
            text = text.replace('{sipNm__Qwt3D_POINTS, POINTS}',
                                '{sipNm__Qwt3D_POINTS, Qwt3D::POINTS}')
            open(source, 'w').write(text)

    # copy lazily to the build directory
    lazy_copies = 0
    for pattern in ('*.cpp', '*.h'):
        for source in glob.glob(os.path.join(tmp_build_dir, pattern)):
            target = os.path.join(build_dir, os.path.basename(source))
            if lazy_copy_sip_output_file(source, target):
                print "Copy %s -> %s." % (source, target)
                lazy_copies += 1
    print "%s file(s) lazily copied." % lazy_copies

    # fix the sip-build-file
    lines = open(build_file).readlines()
    output = open(build_file, "w")
    for line in lines:
        if line.startswith('sources'):
            chunks = [line.rstrip()]
            for source in extra_sources:
                target = os.path.basename(source)
                chunks.append(target)
                shutil.copy2(source, os.path.join(build_dir, target))
            line = ' '.join(chunks)
        elif line.startswith('headers'):
            chunks = [line.rstrip()]
            for source in extra_headers:
                target = os.path.basename(source)
                chunks.append(target)
                shutil.copy2(source, os.path.join(build_dir, target))
            line = ' '.join(chunks)
        elif line.startswith('moc_headers'):
            chunks = [line.rstrip()]
            for source in extra_moc_headers:
                target = os.path.basename(source)
                chunks.append(target)
                shutil.copy2(source, os.path.join(build_dir, target))
            line = ' '.join(chunks)
        print >> output, line
    output.close()

    # fix #include statement
    if options.qwtplot3d_sources:
        for header in [os.path.join('Qwt3D', 'qwt3d_io_gl2ps.cpp')]:
            text = open(header).read()
            if -1 != text.find('../3rdparty/gl2ps/'): 
                open(header, 'w').write(text.replace('../3rdparty/gl2ps/', ''))
    
    # generate __init__.py'
    init_file = os.path.join(build_dir, '__init__.py')
    if not os.path.exists(init_file):
        open(init_file, 'w').write(os.linesep.join([
            'from _Qwt3D import *',
            '',
            '# Alias the helper classes away.',
            'del PyFunction;',
            'from _Qwt3D import PyFunction as Function',
            'del PyParametricSurface',
            'from _Qwt3D import PyParametricSurface as ParametricSurface',
            ]))

    # byte-compile the Python files
    compileall.compile_dir(build_dir, 1, mod_dir)

    # files to be installed
    installs = []
    installs.append([[os.path.basename(f) for f in glob.glob(
        os.path.join(build_dir, '*.py*'))], mod_dir])
    installs.append([[os.path.join(os.pardir, f) for f in glob.glob(
        os.path.join(os.pardir, "sip", "*.sip"))], sip_dir])

    # module makefile
    makefile = pyqtconfig.QtModuleMakefile(
        configuration = configuration,
        build_file = os.path.basename(build_file),
        dir = build_dir,
        install_dir = mod_dir,
        installs = installs,
        qt = 1,
        opengl = 1,
        warnings = 1,
        debug = options.debug,
        )
    makefile.extra_cflags.extend(options.extra_cflags)
    makefile.extra_cxxflags.extend(options.extra_cxxflags)
    makefile.extra_defines.extend(options.extra_defines)
    makefile.extra_include_dirs.extend(options.extra_include_dirs)
    makefile.extra_lflags.extend(options.extra_lflags)
    makefile.extra_libs.extend(options.extra_libs)
    makefile.extra_lib_dirs.extend(options.extra_lib_dirs)
    makefile.generate()

    # main makefile
    sipconfig.ParentMakefile(
        configuration = configuration,
        subdirs = [build_dir],
    ).generate()

# main()


if __name__ == "__main__":
    main()

# Local Variables: ***
# mode: python ***
# End: ***
