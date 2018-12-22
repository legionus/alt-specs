%define _kde_alternate_placement 1

%define rname declarative-plasmoids
Name: kde4-declarative-plasmoids
Version: 4.10.5
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE declarative plasmoids
License: GPL-2.0-or-later or LGPLv2
Url: http://kde.org/

BuildArch: noarch

Requires: plasma-applet-rssnow

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-network libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel
BuildRequires: kde-common-devel

%description
KDE declarative plasmoids


%prep
%setup -qn %rname-%version
#sed -i \
#    's|\(^cmake_minimum_required.*\)$|\1\n\nset(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )|' \
#    CMakeLists.txt

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

find %buildroot -type d -name \*rssnow\* | while read d; do rm -rf $d; done
find %buildroot -type f -name \*rssnow\* | while read f; do rm -f $f; done

%files -f %rname.lang
#%_K4lib/plasma_applet_*.so
%_kde4_xdg_apps/*
%_kde4_iconsdir/hicolor/*/apps/active-news.*
%_K4apps/plasma/plasmoids/*
#%_K4apps/plasma/packages/*/
%_K4srv/*

%changelog
* Thu Sep 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt2
- fix conflict with plasma-applet-rssnow

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Tue Oct 16 2012 Sergey V Turchin <zerg@altlinux.org> 4.10-alt1
- new version

* Wed Apr 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.9-alt0.M60P.1
- build for M60P

* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.9-alt1
- initial specfile
