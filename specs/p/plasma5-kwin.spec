%define rname kwin

%def_enable compositing

%define kwin4_effect_builtins_sover 1
%define libkwin4_effect_builtins libkwin4_effect_builtins%kwin4_effect_builtins_sover
%define kwineffects_sover 11
%define libkwineffects libkwineffects%kwineffects_sover
%define kwinglutils_sover 11
%define libkwinglutils libkwinglutils%kwinglutils_sover
%define kwin_sover 5
%define libkwin libkwin%kwin_sover
%define kwinxrenderutils_sover 11
%define libkwinxrenderutils libkwinxrenderutils%kwinxrenderutils_sover

Name: plasma5-%rname
Version: 5.12.7
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Window Manager
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: libqt5-multimedia kf5-kscreenlocker
#Requires: xorg-xwayland
Requires(post): /sbin/setcap

Source: %rname-%version.tar
Patch1: alt-def-compositing.patch
Patch2: alt-def-window-buttons.patch

# Automatically added by buildreq on Thu Mar 05 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libxcb-devel libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxcbutil-keysyms-devel libxkbfile-devel pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-tools-devel ruby ruby-stdlibs wayland-devel xml-common xml-utils xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdecoration-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-devel python-module-google qt5-multimedia-devel qt5-script-devel qt5-tools-devel-static qt5-x11extras-devel rpm-build-gir rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel-static qt5-declarative-devel
BuildRequires: libcap-utils libcap-devel
BuildRequires: libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-cursor-devel libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-devel libgbm-devel libdrm-devel
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libepoxy-devel libinput-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: qt5-multimedia-devel qt5-script-devel qt5-tools-devel-static qt5-x11extras-devel qt5-sensors-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel plasma5-kdecoration-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel kf5-kidletime-devel
BuildRequires: plasma5-kscreenlocker-devel plasma5-breeze-devel

Provides: kf5-kwin = %EVR
Obsoletes: kf5-kwin < %EVR

%description
KDE Window Manager

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-kwin-common = %EVR
Obsoletes: kf5-kwin-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-kwin-devel = %EVR
Obsoletes: kf5-kwin-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkwin4_effect_builtins
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwin4_effect_builtins
KF5 library

%package -n %libkwineffects
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwineffects
KF5 library

%package -n %libkwinglutils
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwinglutils
KF5 library

%package -n %libkwin
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwin
KF5 library

%package -n %libkwinxrenderutils
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwinxrenderutils
KF5 library

%prep
%setup -n %rname-%version
%if_disabled compositing
%patch1 -p1 -b .compositing
%endif
%patch2 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%post
/sbin/setcap CAP_SYS_NICE=+ep %_K5bin/kwin_wayland ||:

%files common -f %name.lang
%doc COPYING*
%_K5icon/*/*/apps/*.*

%files
%config(noreplace) %_K5xdgconf/*.knsrc
%config(noreplace) %_K5xdgconf/*.*categories
%_K5bin/kwin*
%_K5exec/*kwin*
%_K5lib/libkdeinit5_*.so
%_K5plug/platforms/KWinQpaPlugin.so
%_K5plug/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWin*.so
%_K5plug/kpackage/packagestructure/kwin_packagestructure_*.so
%_K5plug/kwin/
%_K5plug/org.kde.kglobalaccel5.platforms/
%_K5plug/org.kde.kdecoration2/
%_K5plug/org.kde.kwin.*/
%_K5plug/*.so
%_K5cf_bin/kwin5*
%_K5qml/org/kde/kwin/
%_K5cfg/*.kcfg
%_K5data/kwin/
%_K5data/kwincompositing/
%_K5srv/*.desktop
%_K5srv/kwin/
%_K5srvtyp/*.desktop
%_K5notif/*.notifyrc

%files devel
%_K5inc/kwin*.h
%_K5link/lib*.so
%_K5lib/cmake/KWinDBusInterface/
%_K5dbus_iface/*.xml

%files -n %libkwin4_effect_builtins
%_K5lib/libkwin4_effect_builtins.so.%kwin4_effect_builtins_sover
%_K5lib/libkwin4_effect_builtins.so.*

%files -n %libkwineffects
%_K5lib/libkwineffects.so.%kwineffects_sover
%_K5lib/libkwineffects.so.*

%files -n %libkwinglutils
%_K5lib/libkwingl*utils.so.%kwinglutils_sover
%_K5lib/libkwingl*utils.so.*

%files -n %libkwin
%_K5lib/libkwin.so.%kwin_sover
%_K5lib/libkwin.so.*

%files -n %libkwinxrenderutils
%_K5lib/libkwinxrenderutils.so.%kwinxrenderutils_sover
%_K5lib/libkwinxrenderutils.so.*


%changelog
* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt2%ubt
- rebuild with new Qt

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2%ubt
- rebuild with new libwayland-egl

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-kwin -> plasma5-kwin

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt.1
- rebuild with new Qt

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Wed Oct 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2%ubt
- rebuild with new Qt

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2%ubt
- enable compositing by default

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Mon Jul 03 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt.1
- rebuild

* Mon Jun 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt
- update from 5.9 branch

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt2%ubt
- rebuild with new Qt

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt2
- setup default window buttons

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt2
- fix package on arm
- disable compositing by default

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
