%def_disable static
%def_disable debug
%def_enable gtk_doc

Name: loudmouth
Version: 1.5.3
Release: alt2

Summary: Jabber library for C
Group: System/Libraries
License: LGPLv2.1+
Url: https://mcabber.com

#VCS: https://github.com/mcabber/loudmouth.git
Source: %url/files/loudmouth/%name-%version.tar.bz2

BuildRequires: libgio-devel >= 2.26 gtk-doc libcheck-devel
BuildRequires: libgnutls-devel >= 1.2.0 libkrb5-devel libasyncns-devel

%description
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It is designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package -n lib%name
Summary: Jabber library for C
Group: System/Libraries

%description -n lib%name
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It is designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains files needed to develop applications using Loudmouth.
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It's designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for Loudmouth.
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It's designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static library for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
This package contains a statically-linked variant of Loudmouth.
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It's designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.
%endif	# enabled static

%prep
%setup

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-ssl=gnutls \
	--with-asyncns=yes \
	%{subst_enable debug} \
	%{subst_enable static}

%make_build

%check
%make check

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif # enabled static

%changelog
* Thu Nov 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.3-alt2
- Rebuild without libidn support.

* Mon Oct 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3
- dropped unneeded alt-certs_location.patch

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt2
- NMU: fixed build with new toolchain.

* Sun Feb 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2 (new upstream)
- dropped upstreamed patches
- updated buildreqs for krb5/asyncns support

* Wed Oct 07 2015 Sergey V Turchin <zerg at altlinux dot org> 1.4.3-alt4.1.1
- rebuild against new gnutls

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt4.1
- Fixed build

* Thu Nov 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt4
- rebuild for soname set-versions

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt3
- rebuild with latest gnutls
- add patch to search correct location for ssl certs.
- add patch to fix async assertion.
- add patch to fix digest uri bug.
- add patch to drop stanzas that can't be parsed instead of blocking the parser

* Tue Dec 02 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt2
- rebuild with gnutls-2.6
- change Packager
- removed obsolete post scripts

* Thu Oct 30 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.0 -> 1.4.2

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 1.4.0-alt1
- 1.3.4 -> 1.4.0

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 1.3.4-alt1
- 1.2.3 -> 1.3.4
- disable debug

* Mon Mar 17 2008 Igor Zubkov <icesik@altlinux.org> 1.2.3-alt3
- enable debug

* Mon Jun 25 2007 Igor Zubkov <icesik@altlinux.org> 1.2.3-alt2
- add libidn-devel to libloudmouth-devel requires
- update Url

* Mon Jun 18 2007 Igor Zubkov <icesik@altlinux.org> 1.2.3-alt1
- 1.0.5 -> 1.2.3
- buildreq and update build requires

* Wed Sep 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.5-alt1
- Release 1.0.5

* Wed Jun 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- Release 1.0.4

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt2
- Rebuild with gnutls 1.4

* Sun Apr 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Release 1.0.3

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt2
- Patch0: make --disable-debug configure option work as expected

* Wed Dec 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt1
- Renamed the source package to loudmouth
- Separated gtk-doc into -devel-doc package
- Really disabled debug by default

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt1
- New upstream release

* Wed Jun 01 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.90-alt1
- New upstream release

* Tue Jan 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.17.2-alt1
- New upstream release and new GnuTLS

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.17.1-alt1
- Updated to the new upstream release

* Thu Apr 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.16-alt2
- Rebuilt against GnuTLS 1.0.10

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.16-alt1
- New upstream release
- Built against libgcrypt 1.1.93

* Fri Jan 30 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.1-alt1
- New upstream release
- Minimum required version of libgnutls pushed to 1.0

* Fri Jan 23 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15-alt1
- New upstream release
- Rebuild configure script to eliminate the cpp problem

* Fri Jan 02 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.14.1-alt1
- Updated to upstream release 0.14.1
- Removed the OpenSSL patch, as the author's decision to stay
  with GnuTLS is firm
- Removed a .la file

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.13.2-alt1
- New version
- Updated Patch0

* Tue Aug 05 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.13-alt1
- New version
- Updated the SSL patch [Patch0]

* Sun Aug 03 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.12-alt2
- Replaced Patch0 with a more generic patch that adds OpenSSL support
  as a primary SSL implementation, plus cleans up connection shutdown [Patch0]

* Sun Jul 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.12-alt1
- Ported to ALT Linux
- Replaced unreliable GnuTLS configure stuff with aclocal-based one [Patch0]
