REM Batch file to build PyQwt3D for QtWin230-NonCommercial.exe on Windows:
REM (1) use a version of QwtPlot3D backported to Qt-2.3,
REM (2) compile and link QwtPlot3D and zlib-1.2.1 into PyQwt3D,
REM (3) patch the output of moc (Qt-230NC) so that MSVC does not choke on it.

python configure.py -Q ..\qwtplot3d-0.2.4-beta-patched -Z ..\zlib-1.2.1
python fix-nc-moc.py
nmake
nmake install
