%def_disable static
%def_enable threads
%def_disable tcpd
%def_with ssl
%def_with xml
#-------------------------------------------------------------
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}

Name: yaz
Version: 5.25.0
Release: alt2

Summary: Z39.50/SRW/SRU toolkit

License: Revised BSD License
Group: Development/Other
URL: http://www.indexdata.dk/%name/

# Source-url: http://ftp.indexdata.dk/pub/%name/%name-%version.tar.gz
Source: %name-%version.tar

%define lname lib%name
Requires: %lname = %version-%release

# Automatically added by buildreq on Thu Jul 14 2011 (-bi)
# optimized out: docbook-dtds libcom_err-devel libgpg-error libkrb5-devel libstdc++-devel libtinfo-devel libxml2-devel pkg-config
BuildRequires: docbook-style-dsssl gcc-c++ libicu-devel libncurses-devel libreadline-devel libxslt-devel tcl

BuildRequires: docbook-style-dsssl gcc-c++ libncurses-devel
BuildRequires: libreadline-devel libxslt-devel tcl
%{?_with_ssl:BuildRequires: libssl-devel}
%{?_enable_tcpd:BuildRequires: libwrap-devel}

%description
YAZ is a programmers toolkit supporting the development of Z39.50/SRW/SRU 
clients and servers.  Z39.50-2003 (version 3) as well as SRW/SRU version
1.1 are supported in both the client and server roles.

This package contains both a test-server and clients (normal & ssl) for
the ANSI/NISO Z39.50 protocol for Information Retrieval.


%package -n %lname
Summary: Z39.50 shared libraries
Group: System/Libraries

%description -n %lname
YAZ is a programmers toolkit supporting the development of Z39.50/SRW/SRU 
clients and servers.  Z39.50-2003 (version 3) as well as SRW/SRU version
1.1 are supported in both the client and server roles.

This packages contains YAZ shared libraries.

%package -n %lname-devel
Summary: Development files for the Z39.50 library YAZ
Group: Development/C
Requires: %lname = %version-%release
Requires: libxml2-devel

%description -n %lname-devel
YAZ is a programmers toolkit supporting the development of Z39.50/SRW/SRU 
clients and servers.  Z39.50-2003 (version 3) as well as SRW/SRU version
1.1 are supported in both the client and server roles.

This package contains development files for for %lname.

%if_enabled static
%package -n %lname-devel-static
Summary: Z39.50 static library YAZ
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
Z39.50 static library YAZ.
%endif

%package doc
Summary: Documentation for YAZ
Group: Documentation
BuildArch: noarch

%description doc
Online documentation for the %name package, a Z39.50 protocol
server and client.

%prep
%setup
# Fix tests linking.
sed -i 's| ../src/libyaz_icu\.la | ../src/libyaz.la&|' test/Makefile*

%build
%autoreconf
%configure --enable-shared \
    %{subst_enable static} \
    %{subst_enable threads} \
    %{subst_enable tcpd} \
    %{subst_with_to xml xml2} \
    %{subst_with_to ssl openssl}
%make_build

%install
%makeinstall_std docdir=%_docdir/%name
bzip2 --best --force --keep NEWS

%check
%make_build -k check

%files
%doc README.md LICENSE NEWS
%_bindir/*
%exclude %_bindir/%name-config
%exclude %_bindir/%name-asncomp
%_man1dir/*
%exclude %_man1dir/%name-asncomp.*
%_man7dir/%name-log.*
%_man8dir/%name-ztest.*

%files -n %lname
%_libdir/*.so.*
%dir %_datadir/%name/
%_datadir/%name/etc
%_man7dir/%name.*
%_man7dir/bib1-attr.7.*

%files -n %lname-devel
%_bindir/%name-config
%_bindir/%name-asncomp
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/aclocal/*
%_datadir/%name/
%exclude %_datadir/%name/etc
%_man1dir/%name-asncomp.*

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%files doc
%_docdir/%name/

%changelog
* Tue Sep 18 2018 Vitaly Lipatov <lav@altlinux.ru> 5.25.0-alt2
- build without libwrap-devel

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 5.25.0-alt1
- new version 5.25.0 (with rpmrb script)
- rebuild with libicu60

* Thu Feb 25 2016 Vitaly Lipatov <lav@altlinux.ru> 5.13.0-alt2
- rebuilt with libicuuc.so.56

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 5.13.0-alt1
- new version 5.13.0 (with rpmrb script)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0.53-alt1.qa1
- NMU: rebuilt with libicuuc.so.50.

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.53-alt1
- Updated to 3.0.53.
- Enabled test suite.

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 3.0.36-alt2.1
- rebuild (with the help of girar-nmu utility)

* Mon Dec 21 2009 Pavel Vainerman <pv@altlinux.ru> 3.0.36-alt2
- cleaned post and postun section

* Wed Oct 08 2008 Led <led@altlinux.ru> 3.0.36-alt1
- 3.0.36

* Mon Aug 04 2008 Led <led@altlinux.ru> 3.0.34-alt1
- 3.0.34
- removed patches (fixed in upstream)
- removed subpackage ziffy

* Sun Jun 29 2008 Led <led@altlinux.ru> 2.1.56-alt0.1
- 2.1.56
- cleaned up and fixed spec
- added %name-2.1.56-configure.patch
- added %name-2.1.56-tcl.patch
- fixed Requires
- fixed BuildRequires
- added subpackages: %lname-devel-static, %lname-doc, ziffy

* Thu Apr 12 2007 Pavel Vainerman <pv@altlinux.ru> 2.1.54-alt1
- new version
- change license (bug #11482)

* Tue Jan 30 2007 Pavel Vainerman <pv@altlinux.ru> 2.1.48-alt1
- new version (2.1.48)

* Sun Oct 16 2005 Pavel Vainerman <pv@altlinux.ru> 2.1.8-alt1
- first build for ALT Linux Sisyphus
