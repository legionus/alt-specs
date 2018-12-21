Name: tcl-trf
Version: 2.1
Release: alt8

Summary: A tcl extension called Tcl Data transformations
License: BSD
Group: Development/Tcl
Url: http://tcltrf.sourceforge.net/

# git://git.altlinux.org/gears/t/tcl-trf.git
Source: %name-%version-%release.tar

Requires: tcl >= 8.6.7-alt2
BuildRequires: bzlib-devel zlib-devel libssl-devel tcl-devel >= 8.6.7-alt2 tcl-memchan rpm-build-tcl >= 0.5-alt1

%description
%name is a collection of data transformation:
- generation of message digests (hash values, checksums)
  MD2, MD5, SHA/SHS, SHA-1, HAVAL, RIPEMD-128, -160,
  CRC (polynomial used by PGP),  ADLER (based upon zlib)
- conversion from and to various data encodings:
  dual, octal, hexadecimal representation, uuencoding,
  base64-encoding, ASCII85-encoding
- a reed-solomon error correcting coder
- (de)compression based on zlib and bzlib

%prep
%setup -n %name-%version-%release
%teapatch

%build
aclocal -I .
autoconf
%configure \
    --enable-shared-zlib \
    --enable-shared-bzlib
%make_build

%install
%makeinstall

%files
%doc ChangeLog README doc/license.terms
%_tcllibdir/libTrf%version.so
%_tcllibdir/Trf%version/pkgIndex.tcl
%_tcldatadir/Trf%version

%changelog
* Mon Oct 02 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1-alt8
- adapted for new Tcl/Tk extenstion packaging policy
- rebuilt without shared libcrypt and fixed bugs in static md5

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1-alt7.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt7
- updated from CVS @20060124
- fixed build on x86_64

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt6
- updated from CVS @ 20051006

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt5
- rebuilt against new shiny reqprov finder

* Sat May 15 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt4
- updated from CVS @ 200402018
- dynamically linked with zlib, bzlib, libcrypt instead of dlopen()

* Sat Mar  8 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.1-alt3
- bzlib bindings fixed

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt2
- rebuilt in new env

* Tue Aug  6 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1-alt1
- first build for %distribution
