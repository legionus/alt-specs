%define rname akonadi-import-wizard

%define sover 5
%define libkpimimportwizard libkpimimportwizard%sover

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Graphical desktop/KDE
Summary: Akonadi Import Wizard
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 17 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kde5-libkleo-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-messagelib-devel kde5-pimcommon-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemmodels-devel kf5-ktextwidgets-devel kf5-kwallet-devel libassuan-devel libdb4-devel libsasl2-devel python-module-google python3-dev ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: boost-devel libassuan-devel libdb4-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel
BuildRequires: kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel
BuildRequires: kde5-mailimporter-devel kde5-messagelib-devel kde5-pimcommon-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwallet-devel kf5-karchive-devel


%description
Import Wizard allows to import emails, settings, addressbook and calendar data detected in
your user account to Akonadi.

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

%package -n %libkpimimportwizard
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkpimimportwizard
%name library

%prep
%setup -n %rname-%version
sed -i '/DESTINATION/s/\${KDE_INSTALL_INCLUDEDIR}\/KPim\//${KDE_INSTALL_INCLUDEDIR_KF5}/' src/libimportwizard/CMakeLists.txt

%build
%K5build

%install
%K5install
%K5install_move data kconf_update importwizard
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files
%doc COPYING*
%config(noreplace) %_K5xdgconf/*importwizard*.*categories
%_K5bin/*importwizard*
%_K5plug/importwizard/
%_K5data/*importwizard*/
%_K5xdgapp/*importwizard*.desktop
%_K5icon/*/*/apps/*import-wizard*
%_K5conf_up/*importwizard*

%files devel
%_K5inc/importwizard_version.h
%_K5inc/KPim/?mport?izard/
%_K5link/lib*.so
%_K5lib/cmake/KPimImportWizard/
#%_K5archdata/mkspecs/modules/qt_*ImportWizard*.pri

%files -n %libkpimimportwizard
%_K5lib/libKPimImportWizard.so.%sover
%_K5lib/libKPimImportWizard.so.*

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
