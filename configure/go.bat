REM Example for "python configure.py [options]" on Windows
REM Edit the argument for the -Q option to suit your system

python configure.py -Q ..\qwtplot3d-0.2.6 -Z ..\zlib-1.2.3
nmake
nmake install
