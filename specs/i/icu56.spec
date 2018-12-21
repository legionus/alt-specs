%define real_ver_major 56
%define real_ver_minor 1
%define real_ver %{real_ver_major}.%{real_ver_minor}

%def_without doc

Name: icu%real_ver_major
Version: %(echo %real_ver_major | sed -e 's|\(.\)|\1.|').%real_ver_minor
Release: alt2
Epoch: 1

Summary: International Components for Unicode
Group: System/Libraries
License: X License
Url: http://www.icu-project.org/

Source: http://download.icu-project.org/files/icu4c/%real_ver/icu4c-%{real_ver_major}_%{real_ver_minor}-src.tgz
# fc
Patch1: icu.8198.revert.icu5431.patch
Patch2: icu.8800.freeserif.crash.patch
Patch3: icu.7601.Indic-ccmp.patch
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
Patch6: armv7hl-disable-tests.patch

BuildRequires: gcc-c++ libstdc++-devel
%{?_with_doc:BuildRequires: doxygen}

%define libicu libicu%real_ver_major

%description
ICU is a C++ and C library that provides robust and full-featured Unicode
support

%package -n %libicu
Summary: International Components for Unicode (libraries)
Group: System/Libraries
Provides: libicu = %epoch:%version-%release
Obsoletes: libicu < %epoch:%version-%release

%description -n %libicu
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU

%prep
%setup -c
%setup -DT -n %name-%version/icu
%patch1 -p2 -R -b .icu8198.revert.icu5431.patch
%patch2 -p1 -b .icu8800.freeserif.crash.patch
%patch3 -p1 -b .icu7601.Indic-ccmp.patch
%patch4 -p1 -b .gennorm2-man.patch
%patch5 -p1 -b .icuinfo-man.patch
%ifarch armv7hl
%patch6 -p1 -b .armv7hl-disable-tests.patch
%endif

%build
cd source
%autoreconf
%configure \
	--disable-samples \
	--disable-static
%make_build

%install
cd source
%makeinstall_std

%files -n %libicu
%_libdir/*.so.*

%exclude %_bindir/*
%exclude %_sbindir/*
%exclude %_libdir/*.so
%exclude %_libdir/icu/
%exclude %_includedir/*
%exclude %_pkgconfigdir/*.pc
%_datadir/icu/*
%exclude %_man1dir/*
%exclude %_man8dir/*

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1:5.6.1-alt2
- icu56 compat library

* Thu Jan 12 2017 Michael Shigorin <mike@altlinux.org> 1:5.6.1-alt1.1.1
- BOOTSTRAP: drop unused BR: doxygen

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1:5.6.1-alt1.1
- fixed altbug #31778

* Mon Feb 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1:5.6.1-alt1
- 5.6.1 (ALT #30950)

* Mon May 13 2013 Dmitry V. Levin <ldv@altlinux.org> 1:5.1.1-alt3
- Renamed libicu to libicu50 (closes: #28941).

* Thu Dec 27 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.1.1-alt2
- fixed ABI breakage in previous release

* Wed Dec 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.1-alt1
- 5.1.1

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1:5.1-alt2
- disabled C++ 2011 test (https://bugs.gentoo.org/show_bug.cgi?id=439892)

* Tue Nov 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1-alt1
- 5.1

* Wed Oct 17 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:4.8.1.1-alt2
- support locale and fix NaN in cromium (loses: #2599)

* Tue Jan 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:4.8.1.1-alt1
- 4.8.1.1

* Wed Jul 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:4.8.1-alt1
- 4.8.1

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:4.8-alt1
- 4.8

* Sat Mar 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:4.6.1-alt1
- 4.6.1

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 1:4.6-alt2
- rebuilt for debuginfo

* Sun Dec 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.6-alt1
- 4.6

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.4.2-alt1
- 4.4.2

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.4.1-alt2
- rebuild

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.4.1-alt1
- 4.4.1

* Wed Mar 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.4-alt1
- 4.4 release

* Wed Mar 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.4-alt0.rc1
- 4.4 RC1

* Sun Jan 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:4.3.3-alt1
- 4.3.3

* Thu Jul 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:4.2.1-alt1
- 4.2.1

* Tue Jun 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:4.2.0.1-alt1
- 4.2.0.1

* Sun May 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:4.2-alt1
- 4.2

* Fri May 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt2
- fixed build with gcc 4.4

* Sat Jan 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt1
- 4.0.1

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sun Jul 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0-alt1
- 4.0 release

* Tue Jul 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 4.0.d03-alt1
- 4.0.d03:
  + CLDR 1.6 update, Unicode 5.1 update, ICU4J charset

* Sun Jun 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 4.0.d02-alt1
- 4.0.d02

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.8.1-alt2
- fixed CVE-2007-4770, CVE-2007-4771

* Mon Dec 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.8.1-alt1
- 3.8.1:
  + Updated time zone data to Olson 2007j
  + Updated to CLDR 1.5.1 data
  + Various string search fixes
  + Various collation fixes
  + Various time zone parsing, formatting and calculation fixes
  + Various font layout engine fixes
  + Various platform specific fixes
  + Improved BiDi implementation to handle multiple levels
- update URL

* Wed Dec 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.8-alt2
- setBreakType to public

* Sat Oct 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 3.8-alt1
- 3.8

* Mon Nov 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.6-alt1
- 3.6

* Mon May 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.4.1-alt1
- Updated to 3.4.1

* Mon Sep 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.4-alt1
- Updated to 3.4
- Removed binaries from the samples directory
- Added URL

* Thu Feb 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.2-alt1
- Updated to 3.2
- Major spec cleanup
- Introduced samples subpackage

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.0-alt3.1
- Rebuilt with libstdc++.so.6.

* Tue Sep 21 2004 Pavel S. Mironchik <tibor@altlinux.ru> 3.0-alt3
- Fixed dependece

* Tue Sep  7 2004 Pavel S. Mironchik <tibor@altlinux.ru> 3.0-alt2
- fixed [Bug 5048]

* Mon Aug  9 2004 Pavel S. Mironchik <tibor@altlinux.ru> 3.0-alt1
- release

* Thu Apr 29 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.8-alt1
- initial build for Sisyphus 
