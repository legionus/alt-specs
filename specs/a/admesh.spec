Name:    admesh
Summary: Diagnose and/or repair problems with STereo Lithography files
Version: 0.98.1
Release: alt1

Group:   Engineering
License: GPLv2+
URL:     https://github.com/admesh/admesh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
# https://github.com/admesh/admesh.git
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

%description
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files. It can remove degenerate
and unconnected facets, connect nearby facets, fill holes by adding facets,
and repair facet normals. Simple transformations such as scaling,
translation and rotation are also supported. ADMesh can read both
ASCII and binary format STL files, while the output can be in
AutoCAD DXF, Geomview OFF, STL, or VRML format.

%package -n lib%name
Summary:  Runtime library for the %{name} application
Group:    Development/C

%description -n lib%name
This package contains the %{name} runtime library.

%package -n lib%{name}-devel
Summary:  Development files for the lib%{name} library
Group:    Development/C
Requires: lib%name = %version-%release

%description -n lib%{name}-devel
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%prep
%setup
cp README{.md,}

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_datadir/doc

%files
%doc COPYING ChangeLog* README *.stl %{name}-doc.txt
%_bindir/*
%doc %_man1dir/*

%files -n lib%name
%doc COPYING
%_libdir/lib%name.so.*

%files -n lib%{name}-devel
%_includedir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/*

%changelog
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98.1-alt1
- Version 0.98.1

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.97.3-alt1
- New version from upstream Git
- Add libadmesh and devel packages

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt2
- Rebuilt for debuginfo

* Fri Jun 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Initial build for Sisyphus

