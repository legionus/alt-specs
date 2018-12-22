Name: libkgeomap
Version: 3.1.0
Release: alt4

Group: System/Libraries
Summary: Libkgeomap is a wrapper around different world-map components
Url: https://projects.kde.org/projects/extragear/libs/libkgeomap
License: GPL-2.0-only

Requires: %name-common >= %EVR
Conflicts: libkmap

Source: %name-%version.tar
Source1: po.tar

BuildRequires(pre): kde-common-devel
BuildRequires: boost-devel gcc-c++ kde4libs-devel kde4-marble-devel libkexiv24-devel

%description
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap.

%package common
BuildArch: noarch
Group: Graphical desktop/KDE
Summary: Common files for %name package
%description common
Common files for %name package

%package devel
Group: Development/KDE and QT
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup -a1
if ! grep -qe '^add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

%build
%K4build

%install
%K4install

rm -rf %buildroot/%_K4i18n/*/*/*kipi*
rm -rf %buildroot/%_K4i18n/*/*/digikam*
%K4find_lang %name

%files common -f %name.lang
%files
#%_K4bindir/*
%_K4libdir/%name.so*
%_K4apps/%name

%files devel
%_pkgconfigdir/%name.pc
%_K4includedir/*
%_K4link/*.so
%_K4apps/cmake/modules/FindKGeoMap.cmake


%changelog
* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt4
- digikam-4.11.0

* Wed Apr 29 2015 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt3
- update build requires

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- rebuild with new marble

* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Thu Dec 18 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.M70P.1
- built for M70P

* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt12
- digikam-4.2.0

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt11
- rebuilt with new KDE

* Mon May 19 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt10
- digikam-4.0.0

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt9
- rebuilt with new KDE

* Fri Mar 14 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt7.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt8
- rebuilt with new KDE

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt6.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt7
- update from digikam-3.4.0

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt6
- update from digikam-3.2.0

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt5
- update from digikam-3.1.0
- package translatons (ALT#26565)

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt4
- update from digikam-3.0.0-beta3

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- rebuilt with KDE-4.9

* Sat Apr 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.3
- rebuilt with KDE-4.8

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- rebuilt with new kde

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.2
- rebuilt with KDE-4.7

* Tue Oct 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt0.M60P.1
- backport to ALTLinux 6.0P (by rpmbph script)

* Tue Oct 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt1
- Update to 2.0.0
  + Rename to libkgeomap

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Initial build for sysiphus

