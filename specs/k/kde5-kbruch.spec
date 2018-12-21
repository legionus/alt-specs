%define rname kbruch

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Education
Summary: Exercise Fractions
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 01 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel python-module-google python3-base qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel

%description
KBruch is a small program to practice calculating with fractions and percentages.
Different exercises are provided for this purpose and you can use the learning mode
to practice with fractions. The program checks the user's input and gives feedback.

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

%package -n libkf5bruch
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5bruch
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kbruch
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kbruch
%_K5data/kbruch/
%_K5xmlgui/kbruch/
%_K5icon/*/*/apps/kbruch.*
%_K5xdgapp/org.kde.kbruch.desktop
%_K5cfg/kbruch.kcfg

#%files devel
#%_K5inc/kbruch_version.h
#%_K5inc/KBruch/
#%_K5link/lib*.so
#%_K5lib/cmake/KF5Bruch
#%_K5archdata/mkspecs/modules/qt_KBruch.pri

#%files -n libkf5bruch
#%_K5lib/libKF5Bruch.so.*

%changelog
* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

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

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
