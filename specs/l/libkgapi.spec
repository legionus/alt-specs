%add_findpackage_path %_kde4_bindir

%define kgapi_sover 1
%define kgapi_libver 2
%define libkgapi libkgapi%kgapi_sover
%define kgapi2_sover 2
%define kgapi2_libver 2
%define libkgapi2 libkgapi2%kgapi2_sover

%define rname libkgapi
Name: libkgapi
Version: 2.2.0
Release: alt2

Group: System/Libraries
Summary: Google services APIs
Url: http://projects.kde.org/projects/kde/kdeedu/libkdeedu
License: GPLv2


Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jul 10 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4pimlibs-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 python-module-distribute qjson-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4pimlibs-devel >= 4.14 qjson-devel

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs for
various Google services

%package common
Summary: %name common package
Group: System/Configuration/Other
%description common
%name common package

%package -n %libkgapi
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkgapi
%name library.

%package -n %libkgapi2
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libkgapi2
%name library.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
License: LGPLv2 or GPLv3
Requires: %name-common = %EVR
Provides: libkgapi4-devel = %EVR
Obsoletes: libkgapi4-devel < %EVR
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build \
  -DKDE4_BUILD_TESTS:BOOL=OFF


%install
%K4install

%files common
%doc README

#%files -n %libkgapi
#%_K4libdir/libkgapi.so.%kgapi_sover
#%_K4libdir/libkgapi.so.%kgapi_libver.*

%files -n %libkgapi2
%_K4libdir/libkgapi2.so.%kgapi2_sover
%_K4libdir/libkgapi2.so.%kgapi2_libver.*

%files devel
%_K4link/lib*.so
#%_libdir/cmake/LibKGAPI/
#%_K4includedir/libkgapi/
#%_pkgconfigdir/libkgapi.pc
%_libdir/cmake/LibKGAPI2/
%_K4includedir/libkgapi2/
%_K4includedir/LibKGAPI2/
#%_pkgconfigdir/libkgapi2.pc


%changelog
* Thu Oct 22 2015 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt2
- update from LibKGAPI/2.2 branch

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- new version

* Thu May 29 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt0.M70P.1
- built for M70P

* Thu May 29 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt0.M70P.1
- built for M70P

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt0.M70P.1
- built for M70P

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Thu Jul 25 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version (ALT#29228)

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.4-alt0.M60P.1
- built for M60P

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.4-alt1
- new version

* Mon Oct 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.3-alt0.M60P.1
- built for M60P

* Mon Oct 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.3-alt1
- new version

* Fri Aug 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt0.M60P.1
- built for M60P

* Fri Aug 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt0.M60P.1
- built for M60P

* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt1
- initial build
