// qwt3d_numarray.h: encapsulates all PyQwt3D's calls to the numarray C-API.
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


#ifndef QWT3D_NUMARRAY_H
#define QWT3D_NUMARRAY_H

#include <Python.h>

#ifdef HAS_NUMARRAY

// Numeric's C-API pointer
extern void **PyQwt3D_Numarray_PyArray_API;

int try_PyObject_to_NumarrayArrayContiguousFloat2D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny);

int try_PyObject_to_NumarrayArrayContiguousFloat3D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny, size_t *nz);

#endif // HAS_NUMARRAY

#endif // QWT3D_NUMARRAY_H

// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
