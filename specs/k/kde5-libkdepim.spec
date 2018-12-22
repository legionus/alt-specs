%define rname libkdepim

%define sover 5
%define libkf5libkdepim libkf5libkdepim%sover
%define libkf5libkdepimakonadi libkf5libkdepimakonadi%sover

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: System/Libraries
Summary: PIM base library
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Apr 27 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils gcc-c++ kde5-akonadi-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libical-devel libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-akonadi-search-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kldap-devel kde5-kmime-devel kde5-pimlibs-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libldap-devel libsasl2-devel python-module-google python3-dev qt5-quick1-devel qt5-tools-devel-static rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-quick1-devel qt5-tools-devel-static
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: kde5-akonadi-search-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kldap-devel kde5-kmime-devel
BuildRequires: boost-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-contacts-devel kde5-akonadi-notes-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkf5libkdepim
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5libkdepim
KF5 library

%package -n %libkf5libkdepimakonadi
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5libkdepimakonadi
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kdepimwidgets
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%config(noreplace) %_K5xdgconf/*.*categories
%_K5data/kdepimwidgets/

%files devel
%_K5plug/designer/*.so
%_K5inc/libkdepim_version.h
%_K5inc/libkdepim*/
%_K5inc/Libkdepim*/
%_K5link/lib*.so
%_K5lib/cmake/KF5Libkdepim*/
%_K5lib/cmake/MailTransportDBusService/
%_K5archdata/mkspecs/modules/qt_Libkdepim*.pri
%_K5dbus_iface/org.kde.*.service.xml

%files -n %libkf5libkdepim
%_K5lib/libKF5Libkdepim.so.%sover
%_K5lib/libKF5Libkdepim.so.*
%_K5plug/kcm_ldap.so
%_K5srv/kcmldap.desktop

%files -n %libkf5libkdepimakonadi
%_K5lib/libKF5LibkdepimAkonadi.so.%sover
%_K5lib/libKF5LibkdepimAkonadi.so.*

%changelog
* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- rebuild

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
