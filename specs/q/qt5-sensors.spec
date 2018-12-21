
%global qt_module qtsensors
%def_disable bootstrap

Name: qt5-sensors
Version: 5.11.3
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtSensors component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Fri Feb 28 2014 (-bi)
# optimized out: elfutils libGL-devel libcloog-isl4 libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glibc-devel qt5-declarative-devel qt5-xmlpatterns-devel
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces.  The Qt Sensors API also provides a motion gesture recognition
API for devices.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
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

%package -n libqt5-sensors
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-sensors
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version 

%build
%qmake_qt5
%make_build
%if_disabled bootstrap
export QT_HASH_SEED=0
%make docs
%endif

%install
%install_qt5
%if_disabled bootstrap
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common
%files -n libqt5-sensors
%_qt5_libdir/libQt?Sensors.so.*
%_qt5_plugindir/sensorgestures/
%_qt5_plugindir/sensors/
%_qt5_archdatadir/qml/QtSensors/

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_*.pri

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%endif

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

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Fri Mar 07 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Fri Feb 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- initial build
