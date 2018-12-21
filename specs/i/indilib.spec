%define shortname indi


Name: indilib
Version: 1.6.2
Release: alt1%ubt

%add_verify_elf_skiplist %_libdir/libindidriver.so.%version
%add_verify_elf_skiplist %_libdir/libindimain.so.%version
%add_verify_elf_skiplist %_libdir/libindiAlignmentDriver.so.%version

Group: Development/C
Summary: Library to control astronomical devices
Url: http://indi.sourceforge.net/
License: LGPLv2+

Provides: %shortname = %version-%release
Conflicts: kde4edu-kstars < 4.1.60
Conflicts: kdeedu-kstars <= 3.5.10-alt2

# http://nchc.dl.sourceforge.net/sourceforge/indi/
Source: lib%{shortname}_%version.tar

# Automatically added by buildreq on Wed Oct 05 2011 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel pkg-config zlib-devel
#BuildRequires: boost-devel-headers cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel-static
BuildRequires(pre): rpm-build-ubt
BuildRequires: boost-devel cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel
BuildRequires: libusb-devel libjpeg-devel libgsl-devel libcurl-devel
BuildRequires: kde-common-devel

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Conflicts: indilib <= 1.5.0-alt2
%description common
%name common package

%package -n libsbigudrv
Summary: Librar file for INDI
Group: Development/C
Requires: %name-common = %EVR
%description -n libsbigudrv
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains library files of indilib.

%package -n lib%shortname
Group: System/Libraries
Summary: Library to control astronomical devices
Requires: %name-common = %EVR
%description -n lib%shortname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n lib%shortname-devel
Summary: INDI devellopment files
Group: Development/C
Requires: %name-common = %EVR
Provides: %shortname-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release
%description -n lib%shortname-devel
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains files need to build applications using indilib.

%prep
%setup -q -n lib%{shortname}_%version
chmod -x drivers/telescope/lx200fs2.{h,cpp}

%build
%Kbuild \
    -DUDEVRULES_INSTALL_DIR=%_udevrulesdir \
    #

%install
%Kinstall

%files common
%doc ChangeLog README
# an essential part of libindi according to FindINDI.cmake
%_datadir/%shortname/

%files
%_bindir/*
%_udevrulesdir/*.rules

%files -n lib%shortname
#%_libdir/libindi.so.1
#%_libdir/libindi.so.1.*
%_libdir/libindiAlignmentDriver.so.1
%_libdir/libindiAlignmentDriver.so.1.*
%_libdir/libindidriver.so.1
%_libdir/libindidriver.so.1.*
# an essential part of libindi according to FindINDI.cmake
%_libdir/%shortname/

#%files -n libsbigudrv
#%_libdir/libsbigudrv.so.*

%files -n lib%shortname-devel
%doc TODO
#%doc src/examples
%_libdir/*.so
%_libdir/*.a
%_includedir/libindi
%_pkgconfigdir/libindi.pc

%changelog
* Fri Apr 13 2018 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt1%ubt
- new version

* Wed Oct 25 2017 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt3%ubt
- move data to common subpackage

* Mon Oct 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2
- NMU: moved %%_libdir/indi, %_datadir/indi to libindi.
- * they are an essential part of libindi according to FindINDI.cmake

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- NMU: new version (closes: #33997)

* Mon Sep 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt2%ubt
- rebuild with new libgsl

* Fri Apr 07 2017 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1%ubt
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt3
- rebuild with new cfitsio

* Sat Mar 19 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- fix build requires

* Fri Mar 18 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- new version

* Thu Nov 27 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.9-alt1
- new version

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.8-alt1
- new version

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version

* Fri Jul 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1.M60P.1
- new version

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt2
- rebuilt whith new libnova

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2.M60P.1
- built for M60P

* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt3
- rebuilt whith new libnova

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1.M60P.1
- built for M60P

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- fix build requires

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M60P.1
- built for M60P

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt3
- rebuilt

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt2
- rebuilt

* Fri Aug 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.6-alt4
- rebuilt with new libnova

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt3
- remove ExclusiveArch from specfile

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- fix conflicts

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- initial specfile

