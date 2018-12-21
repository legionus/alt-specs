%add_findpackage_path %_kde4_bindir

%define rname ksnapshot
Name: kde4-ksnapshot
Version: 15.4.0
Release: alt1

Group: Graphics
Summary: KDE screenshots maker
Url: http://projects.kde.org/projects/kdegraphics/ksnapshot
License: BSD

Provides: kde4graphics-ksnapshot = %version-%release
Obsoletes: kde4graphics-ksnapshot < %version-%release

Source: %rname-%version.tar


# Automatically added by buildreq on Fri Sep 23 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xml-common xml-utils xorg-fixesproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel libkipi4-devel libqt3-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel libkipi4-devel kde4libs-devel zlib-devel kde-common-devel libXfixes-devel

%description
Make snapshots of the screen contents.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n libksnapshot4
Summary: KDE 4 core library
Group: System/Libraries
%description -n libksnapshot4
KDE 4 core library.

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%doc COPYING
%_K4bindir/ksnapshot
%_K4bindir/kbackgroundsnapshot
#%_K4apps/ksnapshot/
%_K4xdg_apps/ksnapshot.desktop
%_K4iconsdir/hicolor/*/apps/ksnapshot.*
%_K4doc/*/ksnapshot/


#%files -n libksnapshot4
#%_K4libdir/libksnapshot.so.*

%files devel
#%_K4includedir/ksnapshot/
#%_K4link/lib*.so
%_K4dbus_interfaces/org.kde.ksnapshot.xml

%changelog
* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Wed Jan 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

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
