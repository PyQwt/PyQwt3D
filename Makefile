# GNU-Makefile for PyQwt3D

# Edit INCDIR and LIBDIR to suit your QwtPlot3D installation.
INCDIR := /usr/include/qwtplot3d
LIBDIR := /usr/lib
# To compile and link the QwtPlot3D sources statically into PyQwt3D.
QWT3DDIR := $(shell pwd)/qwtplot3d-0.2.4-beta-patched
# QWT3DDIR := /home/packer/RPM/BUILD/qwtplot3d


.PHONY: dist

all:
	(cd configure; python configure.py -I $(INCDIR) -L $(LIBDIR))
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

install:
	(cd configure; make install)

static:
	(cd configure; python configure.py -Q $(QWT3DDIR))
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

debug:
	(cd configure; \
         python configure.py -Q $(QWT3DDIR) -D PYQWT3D_DEBUG --debug --tracing)
	(cd configure; $(MAKE))
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

links:
	(ln -sf configure/Qwt3D)
	(cd examples; ln -sf ../configure/Qwt3D)

doc:
	(cd Doc; make doc; make htdoc)

clean:
	rm -f *~ */*~ */*/*~

distclean: clean
	rm -rf configure/Makefile configure/Qwt3D configure/tmp-Qwt3D
	rm -f Qwt3D examples/Qwt3D 

dist: doc
	python setup.py sdist
