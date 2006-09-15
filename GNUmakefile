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
QWT3DDIR := $(shell pwd)/qwtplot3d-0.2.6
# QWT3DDIR := /home/packer/RPM/BUILD/qwtplot3d

# To compile and link the zlib sources statically into PyQwt3D.
ZLIBDIR := $(shell pwd)/zlib-1.2.3
# ZLIBDIR := /home/packer/RPM/BUILD/zlib-1.2.1

# Do not edit below this line, unless you know what you are doing.
JOBS := $(shell getconf _NPROCESSORS_ONLN)
UNAME := $(shell uname)

ifeq ($(UNAME),Linux)
JOBS := $(shell getconf _NPROCESSORS_ONLN)
endif

ifeq ($(UNAME),Darwin)
JOBS := $(shell sysctl -n hw.ncpu)
endif

.PHONY: dist

# Build and link PyQwt3D including the local source tree of Qwt3D.
all: 3 4

3:
	cd configure \
	&& python configure.py -3 -Q $(QWT3DDIR) -Z $(ZLIBDIR) \
	&& $(MAKE)

4:
	cd configure \
	&& python configure.py -4 -Q $(QWT3DDIR) -Z $(ZLIBDIR) \
	&& $(MAKE)

# Installation
install-3: 3
	make -C configure install

install-4: 4
	make -C configure install

install: install-3 install-4

# Documentation
doc:
	(cd Doc && make doc && make htdoc)

clean:
	rm -f *~ */*~ */*/*~

distclean: clean
	rm -rf configure/Makefile
	rm -rf configure/Qwt3D_Qt3 configure/tmp-Qwt3D_Qt3
	rm -rf configure/Qwt3D_Qt4 configure/tmp-Qwt3D_Qt4

dist: doc
	python setup.py sdist

# EOF
