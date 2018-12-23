%add_findpackage_path %_kde4_bindir

%define rname kdegraphics-thumbnailers
Name: kde4-graphics-thumbnailers
Version: 15.4.2
Release: alt1

Group: Graphics
Summary: Thumbnailers for various graphics types
Url: http://projects.kde.org/projects/kdegraphics/kdegraphics-thumbnailers
License: LGPLv2 and GPL-2.0-only

Provides: kde4graphics-core = %version-%release
Obsoletes: kde4graphics-core < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Sep 13 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel libkdcraw4-devel libkexiv24-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel libkdcraw4-devel libkexiv24-devel libqt4-devel zlib-devel kde-common-devel kde4libs-devel

%description
Thumbnailers for various graphics types

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n libkdegraphics-thumbnailers4
Summary: KDE 4 core library
Group: System/Libraries
%description -n libkdegraphics-thumbnailers4
KDE 4 core library.

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%_K4lib/*thumbnail.so
%_K4srv/*thumbnail.desktop

#%files -n libkdegraphics-thumbnailers4
#%_K4libdir/libkdegraphics-thumbnailers.so.*

#%files devel
#%_K4includedir/kdegraphics-thumbnailers/
#%_K4link/lib*.so


%changelog
* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- bump version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
