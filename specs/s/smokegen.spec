%add_findpackage_path %_kde4_bindir

Name: smokegen
Version: 4.14.1
Release: alt2

Group: Graphical desktop/Other
Summary: Smoke Generator
Url: http://www.kde.org
License: LGPLv2 and GPLv2+

#Obsoletes: kde4bindings < %version
#Provides: kde4bindings = %version

Source: %name-%version.tar
# ALT
Patch1000: smokegen-4.7.1-fix-compile-smokekde.patch
Patch1001: alt-find-generator.patch

# Automatically added by buildreq on Wed Sep 14 2011 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel python-base ruby
#BuildRequires: cmake gcc-c++ libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libqt4-devel kde-common-devel

%description
This package includes Smoke Generator.

%package -n libsmokebase4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokebase4
Qt generic bindings library.

%package devel
Group: Development/KDE and QT
Summary: Header files for Smoke Generator
Conflicts: smoke4-devel < 4.7
Requires: libqt4-devel
Requires: libsmokebase4 = %version-%release
%description devel
This package includes the header files you will need to compile
applications for KDE 4.

%prep
%setup
%patch1000 -p1 -b .fix-compile-smokekde
%patch1001 -p1

%build
%Kcmake
%Kmake VERBOSE=1

%install
%Kinstall
mkdir -p %buildroot/%_includedir/smoke/

%files -n libsmokebase4
%_K4libdir/libsmokebase.so.*

%files devel
%doc README
%_bindir/*
%_libdir/lib*.so
%_libdir/smokegen/
%_includedir/smoke.h
%_includedir/smoke/
%_includedir/smokegen/
%_datadir/smoke/
%_datadir/smokegen/

%changelog
* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt2
- fix find generator

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version
- rebuild with gcc5

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- built for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
