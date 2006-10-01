#!/usr/bin/env python

# A Python translation of the "enrichments" example of QwtPlot3D

import sys
from PyQt4.Qt import QApplication
from PyQt4.Qwt3D import *
from PyQt4.Qwt3D.OpenGL import *

class Bar(VertexEnrichment):

    def __init__(self, radius = 0.0, level = 1.0):
        VertexEnrichment.__init__(self)
        self.configure(radius, level)

    # init()
    
    def clone(self):
        return self

    # clone()
     
    def configure(self, radius, level):
        self.radius = radius
        self.level = level

    # configure()
        
    def drawBegin(self):
        self.diag = self.radius*(self.plot.hull().maxVertex
                                 - self.plot.hull().minVertex).length()
        glLineWidth(0)
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1, 1)

    # drawBegin()
     
    def drawEnd(self):
        pass

    # drawEnd()

    def draw(self, pos):
        interval = self.plot.hull().maxVertex.z - self.plot.hull().minVertex.z
        numlevel = self.plot.hull().minVertex.z + self.level * interval
        interval /= 100
        if pos.z > numlevel - interval and pos.z < numlevel + interval:
            Label3D().draw(pos, self.diag, 2*self.diag)
         
        minz = self.plot.hull().minVertex.z
        
        rgbat = RGBA(pos.x, pos.y, pos.z)
        rgbab = RGBA(pos.x, pos.y, minz)
         
        # Not sure about this part
##        color = self.plot.dataColor()
##        color(1.0, 2.0, 1.0)
 
        glBegin(GL_QUADS)
        glColor4d(rgbab.r, rgbab.g, rgbab.b, rgbab.a)
        glVertex3d(pos.x - self.diag, pos.y - self.diag, minz)
        glVertex3d(pos.x + self.diag, pos.y - self.diag, minz)
        glVertex3d(pos.x + self.diag, pos.y + self.diag, minz)
        glVertex3d(pos.x - self.diag, pos.y + self.diag, minz)
        
         
        if pos.z > numlevel - interval and pos.z < numlevel + interval:
            glColor3d(0.7, 0.0, 0.0)
        else:
            glColor4d(rgbat.r, rgbat.g, rgbat.b, rgbat.a)
             
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        
        glColor4d(rgbab.r, rgbab.g,rgbat.b, rgbab.a)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, minz)
        glColor4d(rgbat.r,rgbat.g, rgbat.b, rgbat.a)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        
        glColor4d(rgbab.r, rgbab.g, rgbat.b, rgbab.a)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, minz)
        glColor4d(rgbat.r, rgbat.g, rgbat.b, rgbat.a)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        
        glColor4d(rgbab.r, rgbab.g, rgbat.b, rgbab.a)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, minz)
        glColor4d(rgbat.r, rgbat.g, rgbat.b, rgbat.a)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        
        glColor4d(rgbab.r, rgbab.g, rgbat.b, rgbab.a)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, minz)
        glColor4d(rgbat.r, rgbat.g, rgbat.b, rgbat.a)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glEnd()
         
        glColor3d(0, 0, 0)
        glBegin(GL_LINES)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, minz)
 
        glVertex3d(pos.x-self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        
        glVertex3d(pos.x-self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x-self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y-self.diag, pos.z)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x+self.diag, pos.y+self.diag, pos.z)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, minz)
        glVertex3d(pos.x-self.diag, pos.y+self.diag, pos.z)
        glEnd()

    # draw()

# class Bar


class Hat(Function):
 
    def __init__(self, *args):
        Function.__init__(self, *args)

    # __init__()
    
    def __call__(self, x, y):
        return 1.0/(x*x + y*y + 0.5)

    # __call__()

    def name(self):
        return QString('$\\frac{1}{x^2+y^2+\\frac{1}{2}}$')

    # name()

# class Hat

 
class Label3D:
 
    def __init__(self):
        pass

    # __init__()
     
    def draw(self, pos, w, h):
        gap = 0.3
        glColor3d(1,1,1)
        glBegin(GL_QUADS)
        glVertex3d(pos.x - w, pos.y, pos.z + gap);
        glVertex3d(pos.x + w, pos.y, pos.z + gap);
        glVertex3d(pos.x + w, pos.y, pos.z + gap + h)
        glVertex3d(pos.x - w, pos.y, pos.z + gap + h)
        glEnd()
        glColor3d(0.4,0,0)
        glBegin(GL_LINE_LOOP)
        glVertex3d(pos.x - w, pos.y,pos.z + gap)
        glVertex3d(pos.x + w, pos.y,pos.z + gap)
        glVertex3d(pos.x + w, pos.y,pos.z + gap + h)
        glVertex3d(pos.x - w, pos.y, pos.z + gap + h)
        glEnd()
        glBegin(GL_LINES)
        glVertex3d(pos.x, pos.y, pos.z)
        glVertex3d(pos.x, pos.y, pos.z + gap)
        glEnd()


class Plot(SurfacePlot):
     
    def __init__(self, *args):
        SurfacePlot.__init__(self, *args)

        self.setTitle('Bar Style (Vertex Enrichment)')
        self.setTitleFont('Arial', 12)
        self.setBackgroundColor(RGBA(1.0, 1.0, 0.6))
        
        self.setZoom(0.8);
        self.setRotation(30.0, 0.0, 15.0)

        self.setCoordinateStyle(BOX)
        bar = self.setPlotStyle(Bar(0.007, 0.5))
   
        hat = Hat(self)
        hat.setMesh(23, 21)
        hat.setDomain(-1.8, 1.7, -1.6, 1.7)
        hat.create()
        
        self.setFloorStyle(FLOORDATA)
        
        #self.createEnrichment(bar)

        axes = self.coordinates().axes # alias
        for axis in axes:
            axis.setMajors(5)
            axis.setMinors(4)
             
        axes[X1].setLabelString('x1-axis')
        axes[X2].setLabelString('x2-axis')
        axes[X3].setLabelString('x3-axis')
        axes[X4].setLabelString('x4-axis')
        axes[Y1].setLabelString('y1-axis')
        axes[Y2].setLabelString('y2-axis')
        axes[Y3].setLabelString('y3-axis')
        axes[Y4].setLabelString('y1-axis')
        axes[Z1].setLabelString(u'\u038f')
 
        self.updateData();
        self.updateGL();
         
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
    app.exec_()
 
# main()
 
 
# Admire
if __name__ == '__main__':
    main(sys.argv)
    
# Local Variables: ***
# mode: python ***
# End: ***
