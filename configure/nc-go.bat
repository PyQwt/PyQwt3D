REM Example for "python configure.py [options]" on Windows
REM Edit the argument for the -Q option to suit your system

python configure.py -Q ..\qwtplot3d-0.2.4-beta-patched -Z ..\zlib-1.2.1
python fix-nc-moc.py
nmake
nmake install
