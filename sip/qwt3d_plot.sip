// The SIP interface definition for:
// - class Plot3D
//
// Copyright (C) 2004-2006 Gerard Vermeulen
//
// This file is part of PyQwt3D.
//
// PyQwt3D is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// PyQwt3D is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along
// with PyQwt3D; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


class Plot3D: QGLWidget
{

%TypeHeaderCode
#include <qwt3d_plot.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:

//%If (NO_MSVC)
%ConvertToSubClassCode
    // The table of Python class objects indexed by their names.
    // The table must be sorted by name.
    static sipStringTypeClassMap map[] = {
        { sipName_Plot3D, &sipClass_Plot3D },
        { sipName_SurfacePlot, &sipClass_SurfacePlot },
    };

    sipClass = sipMapStringToClass(
        sipCpp->className(), map, sizeof(map)/sizeof(map[0]));
%End // ConvertToSubClassCode
//%End

    Plot3D(QWidget * /TransferThis/ = 0, const char * = 0);
    virtual ~Plot3D();

    void updateData();
    void createCoordinateSystem(Triple, Triple);
    CoordinateSystem * coordinates();
    ColorLegend * legend();

    double xRotation() const;
    double yRotation() const;
    double zRotation() const;

    double xShift() const;
    double yShift() const;
    double zShift() const;

    double xViewportShift() const;
    double yViewportShift() const;

    double xScale() const;
    double yScale() const;
    double zScale() const;

    double zoom() const;

    bool ortho() const;
    void setPlotStyle(PLOTSTYLE);
    Enrichment * setPlotStyle(const Enrichment &);
    PLOTSTYLE plotStyle() const;
    Enrichment * userStyle() const;
    void setShading(SHADINGSTYLE);
    SHADINGSTYLE shading() const;
    void setIsolines(int);
    int isolines() const;
    
    void setSmoothMesh(bool);
    bool smoothDataMesh() const;
    void setBackgroundColor(RGBA);
    RGBA backgroundRGBAColor() const;
    void setMeshColor(RGBA);
    RGBA meshColor() const;
    void setMeshLineWidth(double);
    double meshLineWidth() const;
    void setDataColor(Color *);
    const Color * dataColor() const;

    virtual Enrichment * addEnrichment(const Enrichment &);
    virtual bool degrade(Enrichment *);

    ParallelEpiped hull() const;

    void showColorLegend(bool);

    void setCoordinateStyle(COORDSTYLE);
    void setPolygonOffset(double);
    double polygonOffset() const;

    void setTitlePosition(double, double = 0.5, ANCHOR = TopCenter);
    void setTitleFont(const QString &, int, int = QFont::Normal, bool = false);
    void setTitleColor(RGBA);

    void setTitle(const QString &);

    void assignMouse(int, int, int,
                     int, int, int,
                     int, int, int);

    bool mouseEnabled() const;
    void assignKeyboard(int, int,
                        int, int,
                        int, int,
                        int, int,
                        int, int,
                        int, int,
                        int, int,
                        int, int,
                        int, int);

    bool keyboardEnabled() const;
    void setKeySpeed(double, double, double);
    void keySpeed(double &, double &, double &) const;

    bool lightingEnabled() const;
    void illuminate(unsigned = 0);
    void blowout(unsigned = 0);

    void setMaterialComponent(GLenum, double, double, double, double = 1.0);
    void setMaterialComponent(GLenum, double);
    void setShininess(double);

signals:
    void rotationChanged(double, double, double);
    void shiftChanged(double, double, double);
    void vieportShiftChanged(double, double);
    void scaleChanged(double, double, double);
    void zoomChanged(double);
    void projectionChanged(bool);

public slots:
    void setRotation(double, double, double);
    void setShift(double, double, double);
    void setViewportShift(double, double);
    void setScale(double, double, double);
    void setZoom(double);
    
    void setOrtho(bool);
    void enableMouse(bool = true);
    void disableMouse(bool = true);
    void enableKeyboard(bool = true);
    void disableKeyboard(bool = true);
    void enableLighting(bool = true);
    void disableLighting(bool = true);
    void setLightRotation(double, double, double, unsigned = 0);
    void setLightShift(double, double, double, unsigned = 0);
    virtual bool savePixmap(const QString &, const QString &);
    virtual bool saveVector(const QString &, const QString &,
                            VectorWriter::TEXTMODE, VectorWriter::SORTMODE);
    virtual bool save(const QString &, const QString &);

protected:
    //typedef std::list<Qwt3D::Enrichment*> EnrichmentList;
    //typedef EnrichmentList::iterator ELIT;
    //CoordinateSystem coordinates_p;
    //Color* datacolor_p;
    //Enrichment* userplotstyle_p;
    //EnrichmentList elist_p;
    //std::vector<GLuint> displaylists_p;
    //Qwt3D::Data* actualData_p;

    void initializeGL();
    void paintGL();
    void resizeGL(int, int);

    void mousePressEvent(QMouseEvent *);
    void mouseReleaseEvent(QMouseEvent *);
    void mouseMoveEvent(QMouseEvent *);
    void wheelEvent(QWheelEvent *);

    void keyPressEvent(QKeyEvent *);

    virtual void calculateHull() = 0;
    virtual void createData() = 0;
    virtual void createEnrichment(Enrichment &);
    virtual void createEnrichments();

    void createCoordinateSystem();
    void setHull(ParallelEpiped);

    bool initializedGL() const;

    enum OBJECTS {
        DataObject,
        LegendObject,
        NormalObject,
        DisplayListSize,
    };
    
}; // class Plot3D


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
