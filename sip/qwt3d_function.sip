// The SIP interface definition for:
// - class Function
// - class PyFunction
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


class Function: GridMapping
{

%TypeHeaderCode
#include <qwt3d_function.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

public:
    // SIP does not handle an 'abstract virtual operator()' well
    // virtual double operator()(double x, double y) = 0;
    void setMinZ(double);
    void setMaxZ(double);

    virtual bool create(SurfacePlot &);
    virtual bool create();
    void assign(SurfacePlot &);
    void assign(SurfacePlot *);
private:
    Function();
    Function(SurfacePlot &);
    Function(SurfacePlot *);

}; // class Function


class PyFunction: Function
{

%TypeHeaderCode
#include <qwt3d_function.h>
using namespace Qwt3D;

class PyFunction: public Function
{
public:
    PyFunction(): Function() {}
    PyFunction(SurfacePlot &sp): Function(sp) {}
    PyFunction(SurfacePlot *sp): Function(sp) {} 

    // (1) __call__ anticipates a code generation bug in SIP-4.0 and SIP-4.1
    // (2) __call__ is defined as a 'negative hat' to show that redefining
    // __call__ in a subclass has no effect when using SIP-3.11.
    virtual double __call__(double x, double y) { return -x*y; }
    virtual double operator()(double x, double y) { return __call__(x, y); }
}; // class PyFunction

%End // %TypeHeaderCode

public:
    PyFunction();
    PyFunction(SurfacePlot &);
    PyFunction(SurfacePlot *);

    virtual double operator()(double, double);
%MethodCode
    sipRes = sipCpp->__call__(a0, a1);
%End // %MethodCode

}; // class PyFunction


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
