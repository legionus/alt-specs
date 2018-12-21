
%global qt_module qt3d

Name: qt5-3d
Version: 5.11.3
Release: alt1

Group: System/Libraries
Summary: Qt5 - Qt3D QML bindings and C++ APIs
Url: http://qt.io/
License: LGPLv2 / GPLv3

Requires: qt5-imageformats

Source: %qt_module-opensource-src-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: qt5-base-devel-static qt5-tools
BuildRequires: zlib-devel
BuildRequires: pkgconfig(Qt5Quick) pkgconfig(Qt5XmlPatterns) pkgconfig(Qt5Qml) pkgconfig(Qt5Network) pkgconfig(Qt5Core) pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(assimp)

%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-3dcore
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dcore
%summary

%package -n libqt5-3dinput
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dinput
%summary

%package -n libqt5-3dlogic
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dlogic
%summary

%package -n libqt5-3dquick
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquick
%summary

%package -n libqt5-3dquickinput
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquickinput
%summary

%package -n libqt5-3dquickrender
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquickrender
%summary

%package -n libqt5-3drender
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3drender
%summary

%package -n libqt5-3dextras
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dextras
%summary

%package -n libqt5-3dquickextras
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquickextras
%summary

%package -n libqt5-3danimation
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3danimation
%summary

%package -n libqt5-3dquickanimation
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquickanimation
%summary

%package -n libqt5-3dquickscene2d
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-3dquickscene2d
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version 

%build
%qmake_qt5
%make_build
export QT_HASH_SEED=0
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%dir %_qt5_plugindir/sceneparsers
%dir %_qt5_plugindir/geometryloaders/
%dir %_qt5_plugindir/renderplugins/

%files
%_bindir/qgltf-qt5
%_qt5_bindir/qgltf
%_qt5_qmldir/Qt3D/
%_qt5_qmldir/QtQuick/Scene?D/
%_qt5_plugindir/sceneparsers/*.so
%_qt5_plugindir/geometryloaders/*.so
%_qt5_plugindir/renderplugins/*.so

%files -n libqt5-3dcore
%_qt5_libdir/libQt?3DCore.so.*
%files -n libqt5-3dinput
%_qt5_libdir/libQt?3DInput.so.*
%files -n libqt5-3dlogic
%_qt5_libdir/libQt?3DLogic.so.*
%files -n libqt5-3dquick
%_qt5_libdir/libQt?3DQuick.so.*
%files -n libqt5-3dquickinput
%_qt5_libdir/libQt?3DQuickInput.so.*
%files -n libqt5-3dquickrender
%_qt5_libdir/libQt?3DQuickRender.so.*
%files -n libqt5-3drender
%_qt5_libdir/libQt?3DRender.so.*
%files -n libqt5-3dextras
%_qt5_libdir/libQt?3DExtras.so.*
%files -n libqt5-3dquickextras
%_qt5_libdir/libQt?3DQuickExtras.so.*
%files -n libqt5-3danimation
%_qt5_libdir/libQt?3DAnimation.so.*
%files -n libqt5-3dquickanimation
%_qt5_libdir/libQt?3DQuickAnimation.so.*
%files -n libqt5-3dquickscene2d
%_qt5_libdir/libQt?3DQuickScene2D.so.*

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdatadir/libQt*.so
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_*.pri

%files doc
%_qt5_docdir/*

%changelog
* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Wed Jul 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- initial build
