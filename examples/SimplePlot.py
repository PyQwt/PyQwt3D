#!/usr/bin/env python

import sys
from Qwt3D import *
from qt import *
from math import log

class Rosenbrock(Function):

    def __init__(self, *args):
        Function.__init__(self, *args)

    # __init__()

    def __call__(self, x, y):
        return log((1-x)*(1-x) + 100*(y-x*x)*(y-x*x)) / 8

    # __call__()

# class Rosenbrock


class Plot(SurfacePlot):
    
    def __init__(self, *args):
        SurfacePlot.__init__(self, *args)
        self.setTitle('A Simple SurfacePlot Demonstration');

        rosenbrock = Rosenbrock(self)

        rosenbrock.setMesh(41, 31)
        rosenbrock.setDomain(-1.73, 1.5, -1.5, 1.5)
        rosenbrock.setMinZ(-10)
        
        rosenbrock.create()

        self.setRotation(30,0,15)
        self.setScale(1,1,1)
        self.setShift(0.15,0,0)
        self.setZoom(0.9)

        axes = self.coordinates().axes # alias
        for axis in axes:
            axis.setMajors(7)
            axis.setMinors(4)
            
        axes[X1].setLabelString('x-axis')
        axes[Y1].setLabelString('y-axis')
        axes[Z1].setLabelString(u'\u038f')

        self.setCoordinateStyle(BOX);

        self.updateData();
        self.updateGL();

    # __init__()

# class Plot


def make():
    demo = Plot()
    #demo.resize(800, 600) # resize makes title and part of axes disappear
    demo.show()
    demo.paintGL()
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

