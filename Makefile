# GNU-Makefile for PyQwt3D

# Edit INCDIR and LIBDIR to suit your QwtPlot3D installation.
INCDIR := /usr/include/qwtplot3d
LIBDIR := /usr/lib
# To compile and link the QwtPlot3D sources statically into PyQwt3D.
QWT3DDIR := /home/packer/RPM/BUILD/qwtplot3d

PKG := $(shell basename $$(pwd))

.PHONY: dist

all:
	(cd configure; python configure.py -I $(INCDIR) -L $(LIBDIR))
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

static:
	(cd configure; python configure.py -Q $(QWT3DDIR))
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

clean:
	rm -f *~ */*~ */*/*~

distclean: clean
	rm -rf configure/Makefile configure/Qwt3D configure/tmp-Qwt3D
	rm -f Qwt3D examples/Qwt3D 

dist:
	python setup.py sdist
