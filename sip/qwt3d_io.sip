// The SIP interface definition for:
// - class IO
// - class PixmapWriter
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


class IO
{

%TypeHeaderCode
#include <qwt3d_io.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    typedef bool (*Function)(Plot3D*, const QString &);

    class Functor /Abstract/
    {
    public:
        virtual ~Functor();
        virtual IO::Functor * clone() const = 0 /Factory/;
        virtual bool operator()(Plot3D *, const QString &) = 0;
    };

    // FIXME: static bool defineInputHandler(const QString &, Function);
    // FIXME: static bool defineOutputHandler(const QString &, Function);

    static bool defineInputHandler(const QString &, const Functor &);
    static bool defineOutputHandler(const QString &, const Functor &);

    static bool save(Plot3D *, const QString &, const QString &);
    static bool load(Plot3D *, const QString &, const QString &);
    static QStringList inputFormatList();
    static QStringList outputFormatList();

    static IO::Functor * outputHandler(const QString &);
    static IO::Functor * inputHandler(const QString &);
private:
    IO();

}; // class IO


class PixmapWriter: IO::Functor
{

%TypeHeaderCode
#include <qwt3d_io.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    PixmapWriter();
    void setQuality(int);

}; // class PixmapWriter


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End: