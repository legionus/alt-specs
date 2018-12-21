%define rname kdepim-apps-libs

%define sover 5
%define libkf5composereditorng libkf5composereditorng%sover
%define libkf5followupreminder libkf5followupreminder%sover
%define libkf5kaddressbookgrantlee libkf5kaddressbookgrantlee%sover
%define libkf5kdepimdbusinterfaces libkf5kdepimdbusinterfaces%sover
%define libkf5sendlater libkf5sendlater%sover
%define libkf5kaddressbookimportexport libkf5kaddressbookimportexport%sover

Name: kde5-pim-apps-libs
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: System/Libraries
Summary: KDE5 %rname libraries
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Apr 28 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils gcc-c++ kde5-akonadi-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgst-plugins1.0 libical-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules grantlee5-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkleo-devel kde5-pimcommon-devel kde5-pimlibs-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libgpgme-devel libsasl2-devel python-module-google python3-dev qt5-tools-devel-static rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-tools-devel-static
BuildRequires: grantlee5-devel
BuildRequires: libgpgme-devel libassuan-devel libsasl2-devel
BuildRequires: kde5-grantleetheme-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel
BuildRequires: kde5-kpimtextedit-devel kde5-libkleo-devel kde5-pimcommon-devel
BuildRequires: boost-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-contacts-devel kde5-akonadi-notes-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-prison-devel

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

%package -n %libkf5composereditorng
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5composereditorng
KF5 library

%package -n %libkf5followupreminder
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5followupreminder
KF5 library

%package -n %libkf5kaddressbookgrantlee
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kaddressbookgrantlee
KF5 library

%package -n %libkf5kdepimdbusinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kdepimdbusinterfaces
KF5 library

%package -n %libkf5sendlater
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5sendlater
KF5 library

%package -n %libkf5kaddressbookimportexport
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5kaddressbookimportexport
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data composereditor
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%config(noreplace) %_K5xdgconf/*.*categories
#%_K5data/composereditor/

%files devel
#%_K5inc/kdepim-apps-libs_version.h
%_K5inc/*/
%_K5link/lib*.so
%_K5lib/cmake/KF*/
%_K5archdata/mkspecs/modules/qt_*.pri

#%files -n %libkf5composereditorng
#%_K5lib/libKF5ComposerEditorNG.so.%sover
#%_K5lib/libKF5ComposerEditorNG.so.*
%files -n %libkf5followupreminder
%_K5lib/libKF5FollowupReminder.so.%sover
%_K5lib/libKF5FollowupReminder.so.*
%files -n %libkf5kaddressbookgrantlee
%_K5lib/libKF5KaddressbookGrantlee.so.%sover
%_K5lib/libKF5KaddressbookGrantlee.so.*
%files -n %libkf5kdepimdbusinterfaces
%_K5lib/libKF5KdepimDBusInterfaces.so.%sover
%_K5lib/libKF5KdepimDBusInterfaces.so.*
%files -n %libkf5sendlater
%_K5lib/libKF5SendLater.so.%sover
%_K5lib/libKF5SendLater.so.*
%files -n %libkf5kaddressbookimportexport
%_K5lib/libKF5KaddressbookImportExport.so.*
%_K5lib/libKF5KaddressbookImportExport.so.%sover


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
