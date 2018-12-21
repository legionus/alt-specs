%add_findpackage_path %_kde4_bindir

%define rname analitza
Name: kde4-analitza
Version: 4.14.0
Release: alt2%ubt

Group: System/Libraries
Summary: Mathematical features
Url: http://projects.kde.org/projects/kde/kdeedu/analitza
License: GPLv2

Requires: kde4-calgebra = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Jan 25 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libreadline-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libreadline-devel zlib-devel kde-common-devel
BuildRequires: libncursesw-devel libGL-devel

%description
The analitza library will let you add mathematical features to your program.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
Common package for %name

%package -n libanalitza4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libanalitza4
KDE 4 library

%package -n libanalitzagui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libanalitzagui4
KDE 4 library

%package -n libanalitzaplot4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libanalitzaplot4
KDE 4 library

%package -n kde4-calgebra
Summary: Console MathML-based graph calculator
Url: http://edu.kde.org/kalgebra
Group: Education
Requires: %name-common = %version-%release
Conflicts: kde4edu-kcalgebra < 4.8
%description -n kde4-calgebra
Console MathML-based graph calculator

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%files common
%_K4apps/libanalitza/

%files -n kde4-calgebra
%_K4bindir/calgebra

%files -n libanalitza4
%_K4libdir/libanalitza.so.*
%files -n libanalitzagui4
%_K4libdir/libanalitzagui.so.*
%files -n libanalitzaplot4
%_K4libdir/libanalitzaplot.so.*

%files devel
%doc TODO
%_K4libdir/cmake/analitza/
%_K4includedir/analitza*/
%_K4link/lib*.so
#%_pkgconfigdir/analitza.pc


%changelog
* Wed Jul 11 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2%ubt
- fix build requires

* Thu Aug 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Jun 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Tue Nov 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Wed Jun 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- inittial build
