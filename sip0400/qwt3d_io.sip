// The SIP interface definition for:
// - class IO
// - class PixmapWriter
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


class IO
{

%TypeHeaderCode
#include <qwt3d_io.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    // FIXME: typedef bool (*Function)(Plot3D*, QString const& fname);

    // SIP-4.0.x does not handle nested classes
    //class Functor /Abstract/
    //{
    //public:
    //    virtual ~Functor();
    //    virtual IO::Functor * clone() const = 0;
    //    // SIP-4.0.x does not handle a virtual abstract operator().
    //    // virtual bool operator()(Plot3D *, const QString &) = 0;
    //};

    IO();

    // FIXME: static bool defineInputHandler(const QString &, Function);
    // FIXME: static bool defineOutputHandler(const QString &, Function);

    // SIP-4.0.x does not handle nested classes
    // static bool defineInputHandler(const QString &, const Functor &);
    // static bool defineOutputHandler(const QString &, const Functor &);

    static bool save(Plot3D *, const QString &, const QString &);
    static bool load(Plot3D *, const QString &, const QString &);
    static QStringList inputFormatList();
    static QStringList outputFormatList();

    // SIP-4.0.x does not handle nested classes
    // static IO::Functor * outputHandler(const QString &);
    // static IO::Functor * inputHandler(const QString &);

}; // class IO


class PixmapWriter //: IO::Functor
{

%TypeHeaderCode
#include <qwt3d_io.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    PixmapWriter();
    void setQuality(int);

};  // class PixmapWriter


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
