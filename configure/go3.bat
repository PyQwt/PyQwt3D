REM Example for "python configure.py [options]" on Windows
REM Edit the argument for the -Q option to suit your system

python configure.py -3 -Q ..\qwtplot3d-0.2.6 -Z ..\zlib-1.2.3 -D GL2PS_HAVE_ZLIB
nmake
nmake install
