%add_findpackage_path %_kde4_bindir

%define rname libmediawiki
Name: libmediawiki
Version: 1.0.0
Release: alt9

Group: System/Libraries
Summary: KDE C++ interface for MediaWiki
Url: http://www.digikam.org/
License: GPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Apr 19 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde-common-devel

%description
KDE C++ interface for MediaWiki based web service as wikipedia.org

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
#Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build \
    -DKDE4_BUILD_TESTS=OFF \
    #

%install
%K4install

%files
%_K4libdir/libmediawiki.so.*
#%_K4iconsdir/hicolor/*/apps/mediawiki.*
#%_K4apps/libmediawiki/

%files devel
%_K4includedir/libmediawiki/
%_K4link/lib*.so
%_pkgconfigdir/libmediawiki.pc
%_K4apps/cmake/modules/FindMediawiki.cmake


%changelog
* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt9
- digikam-4.6.0

* Thu Dec 18 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt7.M70P.1
- built for M70P

* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt8
- digikam-4.5.0

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt7
- digikam-4.2.0

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt5.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt6
- digikam-3.4.0

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt5
- digikam-3.2.0

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt4
- digikam-3.1.0

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt3
- digikam-3.0.0

* Thu Jun 28 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- digikam-2.6.0

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.M60P.1
- build for M60P

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
