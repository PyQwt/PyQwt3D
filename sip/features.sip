// The SIP feature definitions for PyQwt3D.
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


// Identify SIP
%Feature SIP0400 // SIP-4.0.x
%Feature SIP0401 // SIP-4.1.x
%Feature SIP0402 // SIP-4.2.x

// Identify compiler
%Feature IS_MSVC // is MSVC-6.0
%Feature NO_MSVC // no MSVC-6.0

// Numerical Python extensions
%Feature HAS_NUMARRAY
%Feature HAS_NUMERIC


// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
