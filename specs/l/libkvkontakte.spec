%add_findpackage_path %_kde4_bindir

%define rname libkvkontakte
Name: libkvkontakte
Version: 4.12.0
Release: alt1

Group: System/Libraries
Summary: vk.com access library
Url: http://www.digikam.org/
License: GPLv2+

Source: %rname-%version.tar
Patch1: alt-fix-compile.patch

# Automatically added by buildreq on Thu Apr 19 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel python-module-distribute qjson-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde-common-devel qjson-devel

%description
VKontakte access library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
#Requires: %name = %version-%release
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
%_K4libdir/libkvkontakte.so.1
%_K4libdir/libkvkontakte.so.*
#%_K4iconsdir/hicolor/*/apps/kvkontakte.*
#%_K4apps/libkvkontakte/

%files devel
%_K4includedir/libkvkontakte/
%_K4link/lib*.so
#%_pkgconfigdir/libkvkontakte.pc
%_libdir/cmake/LibKVkontakte/


%changelog
* Fri Sep 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.12.0-alt1
- new version

* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.11.90-alt1
- new version

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt5
- digikam-3.1.0

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt4
- digikam-3.0.0-rc

* Wed Jul 11 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2.M60P.1
- built for M60P

* Wed Jul 11 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt3
- digikam 2.7.0

* Thu Jun 28 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- digikam 2.6.0

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.M60P.1
- build for M60P

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
