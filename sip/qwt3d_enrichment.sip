// The SIP interface definition for:
// - class Enrichment
// - class VertexEnrichment
//
// Copyright (C) 2004-2005 Gerard Vermeulen
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


class Enrichment
{

%TypeHeaderCode
#include <qwt3d_enrichment.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    enum TYPE {
        VERTEXENRICHMENT,
        EDGEENRICHMENT,
        FACEENRICHMENT,
        VOXELENRICHMENT,
    };

%ConvertToSubClassCode
    // traverse the inheritance tree left->right and bottom->up.
    if (dynamic_cast<const Arrow *>(sipCpp))
        sipClass = sipClass_Arrow;
    else if (dynamic_cast<const Cone *>(sipCpp))
        sipClass = sipClass_Cone;
    else if (dynamic_cast<const CrossHair *>(sipCpp))
        sipClass = sipClass_CrossHair;
    else if (dynamic_cast<const Dot *>(sipCpp))
        sipClass = sipClass_Dot;
    else if (dynamic_cast<const VertexEnrichment *>(sipCpp))
        sipClass = sipClass_VertexEnrichment;
    else if (dynamic_cast<const Enrichment *>(sipCpp))
        sipClass = sipClass_Enrichment;
    else
        sipClass = 0;
%End

    Enrichment();
    virtual ~Enrichment();
    virtual Enrichment * clone() const = 0;
    virtual void drawBegin();
    virtual void drawEnd();
    virtual void assign(const Plot3D &);
    virtual TYPE type() const = 0;

protected:
    //const Plot3D *plot;

}; // class Enrichment


class VertexEnrichment: Enrichment
{

%TypeHeaderCode
#include <qwt3d_enrichment.h>
using namespace Qwt3D;
%End

public:
    VertexEnrichment();
    virtual Enrichment * clone() const = 0;
    virtual void draw(const Triple &) = 0;
    virtual TYPE type() const;

}; // class VertexEnrichment


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
