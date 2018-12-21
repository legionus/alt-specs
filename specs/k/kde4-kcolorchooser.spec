%add_findpackage_path %_kde4_bindir

%define rname kcolorchooser
Name: kde4-kcolorchooser
Version: 4.11.1
Release: alt1

Group: Graphics
Summary: KDE color chooser
Url: http://projects.kde.org/projects/kdegraphics/kcolorchooser
License: BSD

Provides: kde4graphics-kcolorchooser = %version-%release
Obsoletes: kde4graphics-kcolorchooser < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel

%description
KDE color chooser

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%doc COPYING
%_K4bindir/kcolorchooser
%_K4xdg_apps/kcolorchooser.desktop
%_K4iconsdir/hicolor/*/apps/kcolorchooser.*

#%files devel
#%_K4includedir/kcolorchooser/
#%_K4link/lib*.so


%changelog
* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
