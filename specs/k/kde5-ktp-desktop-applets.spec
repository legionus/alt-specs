%define rname ktp-desktop-applets

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init altplace

Group: Graphical desktop/KDE
Summary: Telepathy plasmoids
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Requires: kde5-ktp-common-internals-core

Source: %rname-%version.tar
Patch1: alt-person-applet.patch

# Automatically added by buildreq on Wed Jun 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel libdb4-devel python-module-google qt5-declarative-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwindowsystem-devel
BuildRequires: kf5-plasma-framework-devel kf5-ki18n-devel

%description
%summary

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

%package -n libkf5tp-desktop-applets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5tp-desktop-applets
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data plasma/plasmoids/org.kde.ktp-contactlist
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5qml/org/kde/*/
%_K5data/plasma/plasmoids/org.kde.*/
%_K5srv/plasma-applet-*.desktop

#%files devel
#%_K5inc/ktp-desktop-applets_version.h
#%_K5inc/ktp-desktop-applets/
#%_K5link/lib*.so
#%_K5lib/cmake/ktp-desktop-applets
#%_K5archdata/mkspecs/modules/qt_ktp-desktop-applets.pri

#%files -n libkf5tp-desktop-applets
#%_K5lib/libktp-desktop-applets.so.*

%changelog
* Wed Jul 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt2%ubt
- fix unconfigured Person applet (thanks pak@alt)

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 05 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Jul 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt2
- fix requires

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
