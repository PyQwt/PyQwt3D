// qwt3d_python.cpp:
// - return a handle to the data of contiguous numarray and Numeric arrays.
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


#include <qwt3d_python.h>
#include <qwt3d_numarray.h>
#include <qwt3d_numeric.h>

int try_PyObject_to_PyArrayContiguousFloat2D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny)
{
    int result;

#ifdef HAS_NUMERIC
    if ((result = try_PyObject_to_NumericArrayContiguousFloat2D(
             in, out, data, nx, ny)))
        return result;
#endif

#ifdef HAS_NUMARRAY
    if ((result = try_PyObject_to_NumarrayArrayContiguousFloat2D(
             in, out, data, nx, ny)))
        return result;
#endif

    PyErr_SetString(PyExc_TypeError, "expected is a sequency convertible to\n"
#ifdef HAS_NUMERIC
                    "(*) a Numeric 2D array of PyArray_DOUBLE.\n"
#else
                    "(!) rebuild PyQwt3D to support Numeric arrays.\n"
#endif
#ifdef HAS_NUMARRAY
                    "(*) a numarray 2D array of PyArray_DOUBLE.\n"
#else
                    "(!) rebuild PyQwt3D to support numarray arrays.\n"
#endif
        );

    return -1;
}

int try_PyObject_to_PyArrayContiguousFloat3D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny, size_t *nz)
{
    int result;

#ifdef HAS_NUMERIC
    if ((result = try_PyObject_to_NumericArrayContiguousFloat3D(
             in, out, data, nx, ny, nz)))
        return result;
#endif

#ifdef HAS_NUMARRAY
    if ((result = try_PyObject_to_NumarrayArrayContiguousFloat3D(
             in, out, data, nx, ny, nz)))
        return result;
#endif

    PyErr_SetString(PyExc_TypeError, "expected is a sequency convertible to\n"
#ifdef HAS_NUMERIC
                    "(*) a contiguous Numeric 3D array of PyArray_DOUBLE.\n"
#else
                    "(!) rebuild PyQwt3D to support Numeric arrays.\n"
#endif
#ifdef HAS_NUMARRAY
                    "(*) a contiguous numarray 3D array of PyArray_DOUBLE.\n"
#else
                    "(!) rebuild PyQwt3D to support numarray arrays.\n"
#endif
        );

    return -1;
}


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
