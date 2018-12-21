%define qt_module qtwebview

Name: qt5-webview
Version: 5.11.3
Release: alt1

Group: System/Libraries
Summary: Qt Web View
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-webengine-devel qt5-tools

%description
%summary

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
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-webview
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-webview
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version 

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common

%files -n libqt5-webview
%_qt5_libdir/libQt5WebView.so.*
%_qt5_plugindir/webview/
%_qt5_qmldir/QtWebView/

%files devel
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pr*
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?WebView.pc

%files doc
%_qt5_docdir/*

%changelog
* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Tue Aug 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2%ubt
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Feb 15 2018 Oleg Solovyov <mcpain@altlinux.org> 5.9.4-alt3%ubt
- restore dir & move to libqt5-webview

* Thu Feb 15 2018 Oleg Solovyov <mcpain@altlinux.org> 5.9.4-alt2%ubt
- remove unnecessary dir from common pkg

* Wed Feb 14 2018 Oleg Solovyov <mcpain@altlinux.org> 5.9.4-alt1%ubt
- initial build
