# GNU-Makefile for PyQwt3D
#
# There are at least two options to log the output of make:
#
# (1) Invoke make and tie stderr to stdout and redirect stdout to LOG.txt:
#       make all-static 2&>1 >LOG.txt
#     However, you do not see what is going on.
#
# (2) Use script to capture all screen output of make to LOG.txt:
#       script -c 'make all-static' LOG.txt
#     The script command appeared in 3.0BSD and is part of util-linux.
#
#
# Edit INCDIR and LIBDIR to suit your QwtPlot3D installation.
INCDIR := /usr/include/qwtplot3d
LIBDIR := /usr/lib

# To compile and link the QwtPlot3D sources statically into PyQwt3D.
QWT3DDIR := $(shell pwd)/qwtplot3d-0.2.4-beta-patched
# QWT3DDIR := /home/packer/RPM/BUILD/qwtplot3d

# To compile and link the zlib sources statically into PyQwt3D.
ZLIBDIR := $(shell pwd)/zlib-1.2.1
# ZLIBDIR := /home/packer/RPM/BUILD/zlib-1.2.1

# Do not edit below this line, unless you know what you are doing.
CXX  := $(shell which ccache) $(CXX)
CC   := $(shell which ccache) $(CC)
JOBS := $(shell getconf _NPROCESSORS_ONLN)

.PHONY: dist

# Build and link PyQwt3D against a shared Qwt3D library.
all: symlinks
	(cd configure \
	&& python configure.py -j $(JOBS) -I $(INCDIR) -L $(LIBDIR) \
	&& $(MAKE) -j $(JOBS) CC="$(CC)" CXX="$(CXX)")

install:
	(cd configure && make install)

# Build and link PyQwt3D including the local source tree of Qwt3D.
all-static: symlinks
	(cd configure \
	&& python configure.py -Q $(QWT3DDIR) -Z $(ZLIBDIR) \
	&& $(MAKE) CC="$(CC)" CXX="$(CXX)")

debug: symlinks
	(cd configure \
	&& python configure.py \
		-Q $(QWT3DDIR) -D PYQWT3D_DEBUG --debug --tracing \
	&& $(MAKE) CC="$(CC)" CXX="$(CXX)")

symlinks:
	(ln -sf configure/Qwt3D)
	(cd examples && ln -sf ../configure/Qwt3D)

doc:
	(cd Doc && make doc && make htdoc)

clean:
	rm -f *~ */*~ */*/*~

distclean: clean
	rm -rf configure/Makefile configure/Qwt3D configure/tmp-Qwt3D
	rm -f Qwt3D examples/Qwt3D 

dist: doc
	python setup.py sdist

# EOF
