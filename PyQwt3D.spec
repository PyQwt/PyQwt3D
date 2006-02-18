# Make sure that you have installed the development packages for PyQt and sip

%{expand:%define buildForMandrake %(if [ -e /etc/mandrake-release ]; then echo 1; else echo 0; fi)}
%{expand:%define buildForSuSE %(if [ -e /etc/SuSE-release ]; then echo 1; else echo 0; fi)}

%{expand: %%define pyver %(python -c 'import sys; print sys.version[:3]')}
%{expand: %%define qtver %(python -c 'import qt; print qt.QT_VERSION_STR')}
%{expand: %%define sipver %(rpm -q sip --qf "%{VERSION}")}

%define name	PyQwt3D
%define version	0.1.1
%define release 1


Summary:	Python bindings for QwtPlot3D 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.gz
License:	GPL 
Group:		Development/Languages/Python
Url:		http://pyqwt.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  python >= %{pyver}
BuildRequires:  sip = %{sipver}
Requires:       python >= %{pyver}
Requires:       sip = %{sipver}
%if %buildForMandrake
BuildRequires:  libqt3-devel = %{qtver}
Requires:       libqt3 = %{qtver}
%endif
%if %buildForSuSE
BuildRequires:  qt3-devel = %{qtver}
Requires:       qt3 = %{qtver}
%endif

%description
PyQwt is a set of Python bindings for the QwtPlot3D C++ class library.
The QwtPlot3D library (http://qwtplot3d.sourceforge.net) extends the Qt
framework with widgets to visualize 3-dimensional data.

%prep
%setup -n %{name}-%{version}

%build
cd configure
python configure.py -j $(getconf _NPROCESSORS_ONLN) -I /usr/include/qwtplot3d
make -j $(getconf _NPROCESSORS_ONLN)

%install
rm -rf %{buildroot}
cd configure
make install DESTDIR=%{buildroot}
python \
    %{_libdir}/python%{pyver}/compileall.py \
    -d {_libdir}/python%{pyver}/site-packages/ \
    %{buildroot}/%{_libdir}/python%{pyver}/site-packages/

cd ..


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README Doc/html examples
%dir %{_datadir}/sip/Qwt3D
%{_datadir}/sip/Qwt3D/*
%dir %{_libdir}/python%{pyver}/site-packages/Qwt3D/
%{_libdir}/python%{pyver}/site-packages/Qwt3D/*

# EOF
