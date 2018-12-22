%global qt_module qtquickcontrols2
#qml_req_skipall 0
#qml_add_req_skip HelperWidgets

Name: qt5-quickcontrols2
Version: 5.11.3
Release: alt1

Group: System/Libraries
Summary: Qt5 - module with set of QtQuick Controls 2
License: LGPLv2 or GPL-3.0-only
Url: http://qt.io/

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Tue Jul 12 2016 (-bi)
# optimized out: elfutils fontconfig gcc-c++ kde5-akonadi-devel kde5-libkleo-devel kf5-attica-devel kf5-kjs-devel libGL-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-quick libqt5-sql libqt5-widgets libstdc++-devel perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-phonon-devel qt5-script-devel qt5-tools qt5-webchannel-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: kde5-akonadi-calendar-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kdgantt2-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkdepim-devel kde5-libksieve-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-pimlibs-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel python-module-google python3-dev qt5-connectivity-devel qt5-multimedia-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-qml
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-tools

%description
The Qt Quick Controls 2 module delivers the next generation user interface
controls based on Qt Quick. In comparison to the desktop-oriented Qt Quick
Controls 1, Qt Quick Controls 2 are an order of magnitude simpler, lighter and
faster, and are primarily targeted towards embedded and mobile platforms.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common qt5-declarative-common
%description common
Common package for %name

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-labstemplates
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-labstemplates
%summary

%package -n libqt5-quickcontrols2
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-quickcontrols2
%summary

%package -n libqt5-quicktemplates2
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-quicktemplates2
%summary

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version 

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%doc README.md
%_qt5_qmldir/Qt/labs/
%_qt5_qmldir/QtQuick/Controls.2/
%_qt5_qmldir/QtQuick/Templates.2/

%files doc
%_qt5_docdir/qtquickcontrols2.qch
%_qt5_docdir/qtquickcontrols2/
%_qt5_docdir/qtlabsplatform.qch
%_qt5_docdir/qtlabsplatform/
%_qt5_docdir/qtlabscalendar.qch
%_qt5_docdir/qtlabscalendar/

%files -n libqt5-quicktemplates2
%_qt5_libdir/libQt?QuickTemplates2.so.*

%files -n libqt5-quickcontrols2
%_qt5_libdir/libQt?QuickControls2.so.*


%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_*.pri

%files devel-static
#%_qt5_libdir/libQt*.a
#%_qt5_libdatadir/libQt*.a

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

* Wed Oct 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- require rpm-build-qml for devel subpackage

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Tue Jul 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- initial build
