%define _unpackaged_files_terminate_build 1

%define ver 8.1
Name: vtk-data%ver
Version: %ver.1
Release: alt1
Summary: Data files for examples of The Visualization Toolkit (VTK)
License: MIT
Group: Development/Tools
Url: https://www.vtk.org/

Source: vtkdata-%version.tar

BuildArch: noarch

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains data files for examples of VTK.

%install
install -d %buildroot%_datadir
cd %buildroot%_datadir
tar -xf %SOURCE0

%files
%_datadir/vtk-%ver

%changelog
* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.0-alt1
- Version 6.2.0

* Sun Jul 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1
- Version 6.0.0

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt1
- Version 5.10.1

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1
- Version 5.10.0

* Mon Sep 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt1
- Version 5.8.0

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1
- Version 5.6.1

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt1
- Version 5.6.0

* Wed Jun 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt1
- Initial build for Sisyphus

