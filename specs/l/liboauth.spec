Name: liboauth
Version: 1.0.3
Release: alt1

Summary: OAuth functions library
Group: System/Libraries
License: MIT
Url: http://%name.sourceforge.net/
Source: http://liboauth.sourceforge.net/pool/liboauth-%version.tar.gz

BuildRequires: libcurl-devel libnss-devel doxygen

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and encode
parameters according to OAuth specification and offers high-level
functionality to sign requests or verify OAuth signatures as well as
perform HTTP requests.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package provides libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%configure --disable-static \
        --enable-nss

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog COPYING.MIT README

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/oauth.pc
%_man3dir/oauth.*

%changelog
* Fri Apr 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Thu Nov 01 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- 0.9.7

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Sun Dec 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- first build for Sisyphus

