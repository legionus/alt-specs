
%define rname konversation
Name: kde5-%rname
Version: 1.7.5
Release: alt3
%define beta %nil
%K5init altplace

%add_findreq_skiplist %_K5data/%rname/scripts/bug

Group: Networking/IRC
Summary: Konversation is a user friendly Internet Relay Chat client.
License: GPLv2
Url: http://konversation.kde.org
Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: qca-qt5-ossl

Source0: %rname-%version.tar

# Automatically added by buildreq on Tue Jun 30 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libqca-qt5-devel python-module-google qt5-phonon-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libqca-qt5-devel qt5-phonon-devel rpm-build-python
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel
BuildRequires: kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
Konversation is a simple and easy-to-use IRC client for KDE with support for 
SSL connections, strikeout, multi-channel joins, away/unaway messages, 
ignore list functionality, full Unicode support, the ability to auto-connect 
to a server, optional timestamps in chat windows, configurable background colors, 
and much more. 

%prep
%setup -q -n %rname-%version


%build
%K5build

%install
%K5install
%K5install_move data konversation kconf_update
%find_lang --with-kde %rname


%files -f %rname.lang
%doc AUTHORS README NEWS ChangeLog
%_K5bin/*
%_K5xdgapp/org.kde.%rname.desktop
%_K5icon/hicolor/*/*/*.*
%_K5cf_upd/*
%_K5data/%rname/
#%_K5srv/*
%_K5notif/*
%_K5xmlgui/*


%changelog
* Mon Oct 29 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt3
- update russian translation

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt2
- update russian translation

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 1.7.5-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 1.7.4-alt1%ubt
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 1.6-alt2
- fix docs placement

* Mon Jun 29 2015 Sergey V Turchin <zerg@altlinux.org> 1.6-alt1
-  initial build
