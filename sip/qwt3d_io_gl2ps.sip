// The SIP interface definition for:
// - class VectorWriter
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


class VectorWriter: IO::Functor
{

%TypeHeaderCode
#include <qwt3d_io_gl2ps.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    enum TEXTMODE {
        PIXEL,
        NATIVE,
        TEX,
    };
    enum LANDSCAPEMODE {
        ON,
        OFF,
        AUTO,
    };
    enum SORTMODE {
        NOSORT,
        SIMPLESORT,
        BSPSORT,
    };

    VectorWriter();
    
    void setLandscape(LANDSCAPEMODE);
    LANDSCAPEMODE landscape() const;

    void setTextMode(TEXTMODE, QString = QString::null);
    TEXTMODE textMode() const;

    void setSortMode(SORTMODE);
    SORTMODE sortMode() const;

    void setCompressed(bool);
    bool compressed() const;

    bool setFormat(const QString &);

}; // class VectorWriter


%ModuleHeaderCode
#include <qwt3d_io_gl2ps.h>
using namespace Qwt3D;
%End // %ModuleHeaderCode

GLint setDeviceLineWidth(GLfloat);
GLint setDevicePointSize(GLfloat);
// FIXME: GLint drawDevicePixels(
// GLsizei, GLsizei, GLenum, GLenum, const void *pixels);
GLint drawDeviceText(
    const char *, const char *, int, Triple, RGBA, ANCHOR, double);
void setDevicePolygonOffset(GLfloat, GLfloat);


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
