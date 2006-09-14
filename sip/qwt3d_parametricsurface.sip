// The SIP interface definition for:
// - class ParametricSurface
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


class ParametricSurface: GridMapping /Abstract/
{

%TypeHeaderCode
#include <qwt3d_parametricsurface.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    ParametricSurface();
    ParametricSurface(SurfacePlot &);
    ParametricSurface(SurfacePlot *);

    virtual Triple operator()(double, double) = 0;

    virtual bool create(SurfacePlot &);
    virtual bool create();
    void assign(SurfacePlot &);
    void assign(SurfacePlot *);
    void setPeriodic(bool, bool);

}; // class ParametricSurface


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
