// qwt3d_numarray.cpp: encapsulates all PyQwt3D's calls to the numarray C-API.
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


#ifdef HAS_NUMARRAY

#include <Python.h>

#undef NO_IMPORT // to force: void **PyQwt3D_Numarray_PyArray_API;
#define PY_ARRAY_UNIQUE_SYMBOL PyQwt3D_Numarray_PyArray_API
#include <numarray/arrayobject.h>

void qwt3d_import_libnumarray() {
    import_array();
}

int try_PyObject_to_NumarrayArrayContiguousFloat2D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny)
{
    if (!PyArray_Check(in))
        return 0;

    *out = PyArray_ContiguousFromObject(in, PyArray_DOUBLE, 2, 2);

    if (!*out) {
        PyErr_SetString(
            PyExc_RuntimeError,
            "Failed to make contiguous 2D array of PyArray_DOUBLE");

        return -1;
    }
    
    *data = reinterpret_cast<double *>(
        reinterpret_cast<PyArrayObject *>(*out)->data);
    *nx = reinterpret_cast<PyArrayObject *>(*out)->dimensions[0];
    *ny = reinterpret_cast<PyArrayObject *>(*out)->dimensions[1];

    return 1;
}

int try_PyObject_to_NumarrayArrayContiguousFloat3D(
    PyObject *in,
    PyObject **out, double **data, size_t *nx, size_t *ny, size_t *nz)
{
    if (!PyArray_Check(in))
        return 0;

    *out = PyArray_ContiguousFromObject(in, PyArray_DOUBLE, 3, 3);

    if (!*out) {
        PyErr_SetString(
            PyExc_RuntimeError,
            "Failed to make contiguous 3D array of PyArray_DOUBLE");

        return -1;
    }

    *data = reinterpret_cast<double *>(
        reinterpret_cast<PyArrayObject *>(*out)->data);
    *nx = reinterpret_cast<PyArrayObject *>(*out)->dimensions[0];
    *ny = reinterpret_cast<PyArrayObject *>(*out)->dimensions[1];
    *nz = reinterpret_cast<PyArrayObject *>(*out)->dimensions[2];

    return 1;
}

#endif // HAS_NUMARRAY

// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
