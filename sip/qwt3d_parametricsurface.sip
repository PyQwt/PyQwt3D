// The SIP interface definition for:
// - class ParametricSurface
// - class PyParametricSurface
//
// Copyright (C) 2004 Gerard Vermeulen
//
// This file is part of PyQwt3D.
//
// -- LICENSE --
//
// PyQwt3D is free software; you can redistribute it and/or modify it under the
// terms of the GNU General Public License as published by the Free Software
// Foundation; either version 2 of the License, or (at your option) any later
// version.
//
// PyQwt3D is distributed in the hope that it will be useful, but WITHOUT ANY
// WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
// details.
//
// You should have received a copy of the GNU General Public License along
// with PyQwt3D; if not, write to the Free Software Foundation, Inc.,
// 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
//
// In addition, as a special exception, Gerard Vermeulen gives permission to
// link PyQwt3D dynamically with commercial, non-commercial or educational
// versions of Qt, PyQt and sip, and distribute PyQwt in this form, provided
// that equally powerful versions of Qt, PyQt and sip have been released under
// the terms of the GNU General Public License.
//
// If PyQwt3D is dynamically linked with commercial, non-commercial or
// educational versions of Qt, PyQt and sip, PyQwt3D becomes a free plug-in for
// a non-free program.
//
// -- LICENSE --


class ParametricSurface: GridMapping
{

%TypeHeaderCode
#include <qwt3d_parametricsurface.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    // virtual Qwt3D::Triple operator()(double u, double v) = 0;
    virtual bool create(SurfacePlot &);
    virtual bool create();
    void assign(SurfacePlot &);
    void assign(SurfacePlot *);
    void setPeriodic(bool, bool);
private:
    ParametricSurface();
    ParametricSurface(SurfacePlot &);
    ParametricSurface(SurfacePlot *);

}; // class ParametricSurface


class PyParametricSurface: ParametricSurface
{

%TypeHeaderCode
#include <qwt3d_parametricsurface.h>
using namespace Qwt3D;

class PyParametricSurface: public ParametricSurface
{
public:
    PyParametricSurface(): ParametricSurface() {}
    PyParametricSurface(SurfacePlot &sp): ParametricSurface(sp) {}
    PyParametricSurface(SurfacePlot *sp): ParametricSurface(sp) {}

    virtual Triple __call__(double x, double y) { return Triple(); }
    virtual Triple operator()(double x, double y) { return __call__(x, y); }
};
%End // %TypeHeaderCode

public:
    PyParametricSurface();
    PyParametricSurface(SurfacePlot &);
    PyParametricSurface(SurfacePlot *);

    virtual Triple operator()(double, double);
%MethodCode
    sipRes = new Triple(sipCpp -> __call__(a0, a1));
%End    

}; // class PyParametricSurface


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
