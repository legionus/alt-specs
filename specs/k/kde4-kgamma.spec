%add_findpackage_path %_kde4_bindir

%define rname kgamma
Name: kde4-kgamma
Version: 4.11.1
Release: alt4

Group: Graphical desktop/KDE
Summary: Color profiling
Url: http://projects.kde.org/projects/kdegraphics/kgamma
License: GPLv2

Provides: kde4graphics-kgamma = %version-%release
Obsoletes: kde4graphics-kgamma < %version-%release

Source: %rname-%version.tar
Patch1: alt-config-paths.patch
Patch2: alt-xf86gammacfg-args-clear.patch
Patch3: alt-fix-build.patch

# Automatically added by buildreq on Fri Sep 09 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel

%description
Color profiling fo KDE

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K4build


%install
%K4install


%files

%doc AUTHORS ChangeLog
%_K4bindir/xf86gammacfg
%_K4lib/kcm_kgamma.so
%_K4apps/kgamma/
%_K4srv/kgamma.desktop
%_K4doc/en/kcontrol/kgamma/

#%files devel
#%_K4includedir/kgamma/
#%_K4link/lib*.so


%changelog
* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt4
- fix to build with new cmake

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 4.11.1-alt3.qa1
- Rebuilt for gcc5 C++11 ABI.

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt3
- don't treat spaces as arguments for xf86gammacfg

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- add /etc/X11/xorg.conf.d/10-monitor.conf to configs search list

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Mon Nov 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
