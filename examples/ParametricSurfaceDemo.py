#!/usr/bin/env python

import sys
from Qwt3D import *
from qt import *
from math import cos, pi, sin


class Sphere(ParametricSurface):

    def __init__(self, *args):
        ParametricSurface.__init__(self, *args)
        self.setMesh(41, 31)
        self.setDomain(0, 2*pi, 0, pi)
        self.setPeriodic(False, False)

    # __init__()

    def __call__(self, u, v):
        r = 1.0
        return Triple(r*cos(u)*sin(v), r*sin(u)*sin(v), r*cos(v))

    # __call__()

# class Sphere

        
class Plot(SurfacePlot):

    def __init__(self, *args):
        SurfacePlot.__init__(self, *args)
        self.setTitle("A Simple SurfacePlot Demonstration")

        sphere = Sphere(self)
        sphere.create()

        self.setRotation(0,0,0)
        self.setCoordinateStyle(NOCOORD);
        self.updateData()
        self.updateGL()

    # __init__()

# class Plot


def make():
    demo = Plot()
    demo.resize(800, 600)
    demo.show()
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
