Name: libofa
Version: 0.9.3
Release: alt4.1.qa3
Summary: Open Fingerprint Architecture library
License: APLv1 or GPLv2
Group: System/Libraries
Url: http://www.musicip.com/dns/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: http://musicip-libofa.googlecode.com/files/%name-%version.tar.gz
Patch1: libofa-0.9.3-gcc43.patch
Patch2: libofa-0.9.3-alt-curl.patch
Patch3: libofa-0.9.3-fedora-pkgconfig.patch
Patch4: libofa-0.9.3-alt-glibc-2.16.patch

BuildRequires: gcc-c++ libcurl-devel libexpat-devel libfftw3-devel

%description
MusicDNS (Music Digital Naming Service) offers a simple and
cost-effective method for identifying digital music and acquiring
metadata. As the largest fingerprint-based music database in the world,
MusicDNS is quickly becoming a standard for the global identification of
digital music.

MusicDNS is structured software as a service (SaaS), and leverages the
extensive platform and infrastructure that MusicIP has put in place to
provide the most reliable services possible.

At its core, MusicDNS accepts four data types in order to identify
tracks and return the according information. For example, MusicDNS can
be provided with an acoustic fingerprint, which will then provide back
our universal unique ID that corresponds to that fingerprint as well as
all associated metadata that we have in our database.

%package devel
Summary: Development header files and library for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development header files and library for %name.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 02 2017 Michael Shigorin <mike@altlinux.org> 0.9.3-alt4.1.qa3
- E2K: revert last change (not needed anymore)

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 0.9.3-alt4.1.qa2
- E2K: fix linking by avoiding -nostdlib

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.9.3-alt4.1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt4.1
- Fixed build with glibc 2.16

* Thu Aug 04 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt4
- Fixed build with libcurl-devel >= 7.21.7.

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt3
- rebuild

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt2
- fixed build with gcc 4.4

* Sun Dec 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1.1
- NMU: fixed build with gcc 4.3

* Sun Mar 18 2007 Mikhail Yakshin <greycat@altlinux.org> 0.9.3-alt1
- Initial build for ALT Linux

