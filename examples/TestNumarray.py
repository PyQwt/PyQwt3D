#!/usr/bin/env python

if False:
    from Numeric import *
else:
    from numarray import *

import sys
from Qwt3D import *
from qt import *

# enable all tracing options of the SIP generated bindings (requires -r option)
try:
    import sip
    sip.settracemask(0x3f)
except ImportError:
    import libsip
    libsip.settracemask(0x3f)


def matrix2d(nx, ny, minx, maxx, miny, maxy, function):
    """Return a data matrix for the interface to the C++ member function 
    bool SurfacePlot::loadFromData(
        double **, unsigned int, unsigned int,
        double , double , double, double);
    """
    # columns
    xs = multiply.outer(
        minx + ((maxx-minx)/(nx-1))*arange(nx), ones(ny, Float))
    # rows
    ys = multiply.outer(
        ones((nx,), Float), miny+((maxy-miny)/(ny-1))*arange(ny))
    return function(xs, ys)

# matrix2d()


def matrix3d(nx, ny, minx, maxx, miny, maxy, function):
    """Return a data matrix to test the interface to the C++ member function
    bool SurfacePlot::loadFromData(
        Triple **, unsigned int, unsigned int, bool = false, bool = false);
    """
    xyzs = zeros((nx, ny, 3), Float)
    # columns
    xyzs[:,:,0] = multiply.outer(
        minx + ((maxx-minx)/(nx-1))*arange(nx), ones(ny, Float))
    # rows
    xyzs[:,:,1] = multiply.outer(
        ones((nx,), Float), miny+((maxy-miny)/(ny-1))*arange(ny))
    # result
    xyzs[:,:,2] = function(xyzs[:,:,0], xyzs[:,:,1])
    return xyzs

# matrix3d()


def saddle(x, y):
    return x*y

# saddle()


class Plot(SurfacePlot):

    def __init__(self, *args):
        SurfacePlot.__init__(self, *args)
        
        self.setRotation(30, 0, 15)
        self.setScale(1.0, 1.0, 1.0)

        nx, ny, minx, maxx, miny, maxy = 3, 5, -1.0, 1.0, -1.0, 1.0
        if True:
            zs = matrix2d(nx, ny, minx, maxx, miny, maxy, saddle)
            print type(zs)
            print zs
            self.loadFromData(zs, minx, maxx, miny, maxy)
        else:
            xyzs = matrix3d(nx, ny, minx, maxx, miny, maxy, saddle)
            print xyzs
            self.loadFromData(xyzs)
        
        axes = self.coordinates().axes # alias

        for axis in axes:
            axis.setAutoScale(False)
            axis.setMajors(5) # 6 major ticks
            axis.setMinors(3) # 2 minor ticks

        axes[X1].setLabelString("x")
        axes[Y1].setLabelString("y")
        axes[Z1].setLabelString("z")
        axes[X2].setLabelString("x")
        axes[Y2].setLabelString("y")
        axes[Z2].setLabelString("z")
        axes[X3].setLabelString("x")
        axes[Y3].setLabelString("y")
        axes[Z3].setLabelString("z")
        axes[X4].setLabelString("x")
        axes[Y4].setLabelString("y")
        axes[Z4].setLabelString("z")

        self.setCoordinateStyle(BOX)
        self.coordinates().setGridLines(True, True)
        self.coordinates().setLineSmooth(True)

        self.updateData()
        self.updateGL()

    # __init__()

# class Plot


def make():
    demo = Plot()
    demo.show()
    # Matrox cards on Linux work better with a resize() after show()
    demo.resize(600, 400)
    return demo

# make()


def main(args):
    app = QApplication(args)
    demo = make()
    app.setMainWidget(demo)
    app.exec_loop()

# main()


# Admire
if __name__ == '__main__':
    main(sys.argv)


# Local Variables: ***
# mode: python ***
# End: ***


                        
                       
