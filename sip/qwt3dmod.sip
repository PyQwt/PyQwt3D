// The SIP interface definition for the _Qwt3D module of PyQwt3D.
//
// Copyright (C) 2004 Gerard Vermeulen
//
// This file is part of PyQwt3D.
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


%Module _Qwt3D 0

%Include features.sip
%Include types.sip

%Import qt/qtmod.sip
%Import qtgl/qtglmod.sip

%ModuleHeaderCode
#include <qwt3d_python.h>
// #include <iostream>
// using namespace std;
%End

%PostInitialisationCode
#ifdef HAS_NUMARRAY
    qwt3d_import_libnumarray();
#endif
#ifdef HAS_NUMERIC
    qwt3d_import_array();
#endif
%End

// automagically generated
%Include qwt3d_axisvector.sip
%Include qwt3d_cell.sip
%Include qwt3d_cellfield.sip
%Include qwt3d_colorvector.sip
%Include qwt3d_doublevector.sip
%Include qwt3d_freevectorfield.sip
%Include qwt3d_triplefield.sip

// blood, sweat and tears
%Include qwt3d_autoscaler.sip
%Include qwt3d_axis.sip
%Include qwt3d_color.sip
%Include qwt3d_colorlegend.sip
%Include qwt3d_coordsys.sip
%Include qwt3d_drawable.sip
%Include qwt3d_enrichment.sip
%Include qwt3d_enrichment_std.sip
%Include qwt3d_function.sip
%Include qwt3d_gridmapping.sip
%Include qwt3d_io.sip
%Include qwt3d_io_gl2ps.sip
%Include qwt3d_io_reader.sip
%Include qwt3d_label.sip
%Include qwt3d_mapping.sip
%Include qwt3d_openglhelper.sip
%Include qwt3d_parametricsurface.sip
%Include qwt3d_plot.sip
%Include qwt3d_scale.sip
%Include qwt3d_surfaceplot.sip
%Include qwt3d_types.sip


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
