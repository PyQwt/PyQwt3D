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
import shutil

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


def check_numarray(py_inc_dir, excluded_features, extra_defines, skip = False):
    """See if the numarray extension has been installed.
    """
    if skip:
        excluded_features.append("-x HAS_NUMARRAY")
        return excluded_features, extra_defines
       
    try:
        import numarray
        # Try to find numarray/arrayobject.h.
        numarray_inc = os.path.join(py_inc_dir, "numarray", "arrayobject.h")
        if os.access(numarray_inc, os.F_OK):
            print "Found numarray-%s.\n" % numarray.__version__
            extra_defines.append("HAS_NUMARRAY")
        else:
            print ("numarray has been installed, "
                   "but its headers are not in the standard location.\n"
                   "PyQwt will be build without support for numarray.\n"
                   "(Linux users may have to install a development package)\n"
                   )
            raise ImportError
    except ImportError:
        excluded_features.append("-x HAS_NUMARRAY")
        print ("Failed to import numarray: "
               "PyQwt will be build without support for numarray.\n"
               )
        
    return excluded_features, extra_defines

# check_numarray()


def check_numeric(py_inc_dir, excluded_features, extra_defines, skip = False):
    """See if the Numeric extension has been installed.
    """
    if skip:
        excluded_features.append("-x HAS_NUMERIC")
        return excluded_features, extra_defines
       
    try:
        import Numeric
        # Try to find Numeric/arrayobject.h.
        numeric_inc = os.path.join(py_inc_dir, "Numeric", "arrayobject.h")
        if os.access(numeric_inc, os.F_OK):
            print "Found Numeric-%s.\n" % Numeric.__version__
            extra_defines.append("HAS_NUMERIC")
        else:
            print ("Numeric has been installed, "
                   "but its headers are not in the standard location.\n"
                   "PyQwt will be build without support for Numeric.\n"
                   "(Linux users may have to install a development package)\n"
                   )
            raise ImportError
    except ImportError:
        excluded_features.append("-x HAS_NUMERIC")
        print ("Failed to find Numeric: "
               "PyQwt will be build without support for Numeric.\n"
               )
        
    return excluded_features, extra_defines

# check_numeric()


def check_sip(configuration, excluded_features):
    """Adapt to SIP differences by means of mutually excluding features
    """
    print "Found SIP-%s.\n" % configuration.sip_version_str

    sip_version = configuration.sip_version
    if sip_version & 0xffff00 == 0x040000: 
        excluded_features.extend(["-x SIP0401", "-x OLDSIP"])
    elif sip_version & 0xffff00 == 0x040100:
        excluded_features.extend(["-x SIP0400", "-x OLDSIP"])
    elif sip_version & 0xffff00 == 0x030b00:
        # SIP-3.11.x works like SIP-4.1.x (except for bugs)
        excluded_features.extend(["-x SIP0401", "-x NEWSIP"])
    else:
        raise SystemExit, (
            "PyQwt3D requires SIP-4.1.x, -4.0.x, or -3.11.x.\n"
            )

    return excluded_features

# check_sip()


def check_compiler(configuration, excluded_features):
    """Adapt to different compilers by means of mutually excluding features
    """
    makefile = sipconfig.Makefile(configuration=configuration)
    generator = makefile.optional_string('MAKEFILE_GENERATOR', 'UNIX')
    if generator == 'MSVC':
        excluded_features.append('-x NO_MSVC')
    else:
        excluded_features.append('-x IS_MSVC')
    
    return excluded_features

# check_compiler()


def main():
    
    from optparse import OptionParser
    usage = 'python configure.py [options] or ./configure.py [options]'
    parser = OptionParser(usage=usage)
    parser.add_option(
        '-I', '--extra-include-dirs', default=[], action='append',
        type='string', metavar='/usr/include/qwtplot3d',
        help=('add an extra directorys to search for headers'
              ' (the compiler must be able to find the QwtPlot3D headers)'))
    parser.add_option(
        '-L', '--extra-lib-dirs', default=[], action='append',
        type='string', metavar='/usr/lib/qt3/lib',
        help=('add the directory to search for libraries'
              ' (the linker must be able to find the QwtPlot3D library)'))
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
        '--extra-cflags', default=[], action='append', type='string',
        help='add extra C compiler flags')
    parser.add_option(
        '--extra-cxxflags', default=[], action='append', type='string',
        metavar='-GR',
        help=('add extra C++ compiler flags'
              ' (MSVC may need the -GR flag to enforce'
              ' RTTI or runtime type information)'))
    parser.add_option(
        '--extra-defines', default=[], action='append', type='string',
        help='add extra preprocessor definitions')
    parser.add_option(
        '--extra-lflags', default=[], action='append', type='string',
        help='add extra linker flags')
    parser.add_option(
        '--extra-libs', default=[], action='append', type='string',
        help='add extra libraries')
                      
    options, args = parser.parse_args()
    print "Command line options:"
    pprint.pprint(options.__dict__)
    print

    if 'qwtplot3d' not in options.extra_libs:
        options.extra_libs.append('qwtplot3d')

    # configuration
    configuration = pyqtconfig.Configuration()
    build_dir = "Qwt3D"
    tmp_build_dir = "tmp-" + build_dir
    build_file = "qwt3d.sbf"
    mod_dir = os.path.join(configuration.default_mod_dir, 'Qwt3D')
    sip_dir = os.path.join(configuration.pyqt_sip_dir, 'Qwt3D')
    
    excluded_features = []
    excluded_features = check_sip(configuration, excluded_features)
    excluded_features = check_compiler(configuration, excluded_features)
    excluded_features, options.extra_defines = check_numarray(
        configuration.py_inc_dir,
        excluded_features, options.extra_defines,
        options.disable_numarray)
    excluded_features, options.extra_defines = check_numeric(
        configuration.py_inc_dir,
        excluded_features, options.extra_defines,
        options.disable_numeric)    

    # generate code into a temporary directory
    if not os.path.exists(tmp_build_dir):
        os.mkdir(tmp_build_dir)
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)
        open(os.path.join(build_dir, '__init__.py'), 'w').write(
            'from _Qwt3D import *\n'
            '\n'
            '# Alias the helper classes away.\n'
            'del PyFunction;\n'
            'from _Qwt3D import PyFunction as Function\n'
            'del PyParametricSurface\n'
            'from _Qwt3D import PyParametricSurface as ParametricSurface\n'
            )
        compileall.compile_dir(build_dir, 1, mod_dir)

    print "Extended options:"
    pprint.pprint(options.__dict__)
    print
    
    cmd = " ".join(
        [configuration.sip_bin,
         # SIP assumes POSIX style path separators
         "-I", os.path.join(os.pardir, "sip").replace("\\", "/"),
         "-I", configuration.pyqt_sip_dir.replace("\\", "/"),
         "-b", os.path.join(build_dir, build_file),
         "-c", tmp_build_dir,
         ]
        + excluded_features
        + configuration.pyqt_qt_sip_flags.split()
        # SIP assumes POSIX style path separators
        + [os.path.join(os.pardir, "sip", "qwt3dmod.sip").replace("\\", "/")]
        )

    print "sip invokation:"
    pprint.pprint(cmd)
    print
    
    os.system(cmd)

    # fill the build directory lazily
    copies = 0
    for pattern in ('*.cpp', '*.h'):
        for source in glob.glob(os.path.join(tmp_build_dir, pattern)):
            target = os.path.join(build_dir, os.path.basename(source))
            if lazy_copy_sip_output_file(source, target):
                print "Copy %s -> %s." % (source, target)
                copies += 1
    print "%s file(s) copied." % copies

    # add the interface to the numerical Python extensions and fix build_file
    extra_sources = glob.glob(os.path.join(os.pardir, 'numpy', '*.cpp'))
    extra_headers = glob.glob(os.path.join(os.pardir, 'numpy', '*.h'))
    lines = open(os.path.join(build_dir, build_file)).readlines()
    output = open(os.path.join(build_dir, build_file), "w")
    for line in lines:
        if line.startswith('sources'):
            chunks = [line.rstrip()]
            for source in extra_sources:
                target = os.path.basename(source)
                chunks.append(target)
                shutil.copy2(source, os.path.join(build_dir, target))
            line = ' '.join(chunks)
        if line.startswith('headers'):
            chunks = [line.rstrip()]
            for source in extra_headers:
                target = os.path.basename(source)
                chunks.append(target)
                shutil.copy2(source, os.path.join(build_dir, target))
            line = ' '.join(chunks)
        print >> output, line
    output.close()
    
    # files to be installed
    installs = []
    installs.append([[os.path.basename(f) for f in glob.glob(
        os.path.join(build_dir, '*.py*'))], mod_dir])
    installs.append([[os.path.join(os.pardir, f) for f in glob.glob(
        os.path.join(os.pardir, "sip", "*.sip"))], sip_dir])

    # module makefile
    makefile = pyqtconfig.QtModuleMakefile(
        configuration = configuration,
        build_file = build_file,
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
