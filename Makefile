# GNU-Makefile for PyQwt3D

# Edit INCDIR and LIBDIR to suit your QwtPlot3D installation.
INCDIR := /usr/include/qwtplot3d
LIBDIR := /usr/lib

PKG := $(shell basename $$(pwd))

.PHONY: dist

all:
	(cd configure; python configure.py -I $(INCDIR) -L $(LIBDIR))
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

clean:
	rm -f *~ */*~ */*/*~

distclean: clean
	rm -rf configure/Makefile configure/Qwt3D configure/tmp-Qwt3D
	rm -f Qwt3D examples/Qwt3D 

dist: distclean
	python setup.py sdist

pack: distclean
	(cd ..; tar cvfzh $(PKG).tar.gz $(PKG))
