// The SIP interface definition for:
// - class Scale
// - class LinearScale
// - class LogScale
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

class Scale
{

%TypeHeaderCode
#include <qwt3d_scale.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

protected:

%ConvertToSubClassCode
    // traverse the inheritance tree left->right and bottom->up.
    if (dynamic_cast<const LinearScale *>(sipCpp))
        sipClass = sipClass_LinearScale;
    else if (dynamic_cast<const LogScale *>(sipCpp))
        sipClass = sipClass_LogScale;
    else if (dynamic_cast<const Scale *>(sipCpp))
        sipClass = sipClass_Scale;
    else
        sipClass = 0;
%End

    Scale();
    virtual ~Scale();
    virtual QString ticLabel(unsigned int) const;

    virtual void setLimits(double, double);
    virtual void setMajors(int);
    virtual void setMinors(int);
    virtual void setMajorLimits(double, double);

    int majors() const;
    int minors() const;

    virtual Scale* clone() const = 0;
    virtual void calculate() = 0;
    virtual int autoscale(double &, double &, double, double, int);

    //std::vector<double> majors_p, minors_p;
    //double start_p, stop_p;
    //int majorintervals_p, minorintervals_p;
    //double mstart_p, mstop_p;
}; // class Scale


class LinearScale: Scale
{

%TypeHeaderCode
#include <qwt3d_scale.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

protected:
    int autoscale(double &, double &, double, double, int);
    Scale* clone() const;
    void calculate();
    //LinearAutoScaler autoscaler_p;
}; // class LinearScale


class LogScale: Scale
{

%TypeHeaderCode
#include <qwt3d_scale.h>
using namespace Qwt3D;
%End // %TypeHeaderCode

protected:
    QString ticLabel(unsigned int) const;
    void setMinors(int);
    LogScale();
    Scale* clone() const;
    void calculate();
}; // class LogScale


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
