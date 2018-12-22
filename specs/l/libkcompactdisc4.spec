%add_findpackage_path %_kde4_bindir

%define rname libkcompactdisc
Name: libkcompactdisc4
Version: 4.12.3
Release: alt1

Group: System/Libraries
Summary: KDE CDDB library
Url: http://projects.kde.org/projects/kde/kdeedu/libkcompactdisc
License: GPL-2.0-only or LGPLv2

Source: %rname-%version.tar
Patch1: libkcompactdisc-4.8.4-alt-build.patch

# Automatically added by buildreq on Fri Jun 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libalsa-devel libicu libqt3-devel python-module-distribute qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libalsa-devel kde-common-devel

%description -n libkcompactdisc4
KDE CDDB library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build


%install
%K4install

%files
#doc TODO
%_K4libdir/libkcompactdisc.so.*

%files devel
%_libdir/cmake/libkcompactdisc/
%_K4link/lib*.so
%_K4includedir/libkcompactdisc/

%changelog
* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- initial build
