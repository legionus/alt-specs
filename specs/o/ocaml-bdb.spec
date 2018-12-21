%set_verify_elf_method textrel=relaxed
%define oname ocamlbdb
Name: ocaml-bdb
Version: 4.3.21
Release: alt10
Summary: OCaml interface to Berkeley-DB
Packager: Boris Savelev <boris@altlinux.org>
Source: http://www.eecs.harvard.edu/~stein/%oname-%version.tar.gz
#Url: http://www.eecs.harvard.edu/~stein/ is not valid anymore!
License: GPL
Group: Development/Other

# Automatically added by buildreq on Sat Aug 23 2008
BuildRequires: libdb4-devel ocaml
Requires: %name-runtime = %version-%release
Obsoletes: %name-devel
Provides: %name-devel = %version-%release

%description
OCaml interface to Berkeley-DB.

This package contains the development files needed to build applications
using %name-runtime.

%package runtime
Summary: OCaml interface to Berkeley-DB
Group: Development/Other

%description runtime
OCaml interface to Berkeley-DB.

%prep
%setup -n %oname-%version

%build
%__subst 's:BDB_DIR=/usr/local/BerkeleyDB.4.3/:BDB_DIR=%prefix:g' Makefile
%__subst 's:/usr/local/lib:%_libdir:g' Makefile
%__subst 's:-ldb-4.1:-ldb:g' Makefile
%make

%install
mkdir -p %buildroot%_libdir/ocaml/bdb
install -m 644 bdb.cma bdb.cmi libcamlbdb.a %buildroot%_libdir/ocaml/bdb/

%files runtime
%doc CREDITS README
%dir %_libdir/ocaml/bdb
%_libdir/ocaml/bdb/*.cmi

%files
%_libdir/ocaml/bdb/*
%exclude %_libdir/ocaml/bdb/*.cmi

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.3.21-alt10
- rebuilt with ocaml-4.07.1

* Sun Oct 07 2018 Ivan Zakharyaschev <imz@altlinux.org> 4.3.21-alt9
- Removed the description, which used to be wrong.
- Removed the project URL, which is not valid anymore.
- (.spec) Dropped ubt tag, which is excessive since
  https://www.altlinux.org/Binary_package_identity_change
  was implemented.

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.3.21-alt8
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 4.3.21-alt7.S1
- rebuilt for ocaml 4.06.1

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 4.3.21-alt6.S1
- added ubt tag
- moved out from site-lib dir

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.3.21-alt6
- rebuild with ocaml 4.04.1

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 4.3.21-alt5
- rebuild with new ocaml

* Mon Dec 26 2011 Alexey Shabalin <shaba@altlinux.ru> 4.3.21-alt4
- rebuild with new ocaml

* Thu Nov 18 2010 Boris Savelev <boris@altlinux.org> 4.3.21-alt3
- rename packages (%name -> %name-runtime ; %name-devel -> %name)

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 4.3.21-alt2
- fix x86_64 build

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 4.3.21-alt1
- initial build for Sisyphus from Mandriva

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-4mdv2008.1
+ Revision: 178361
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-3mdv2008.0
+ Revision: 77595
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Tue Feb 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-2mdv2007.0
+ Revision: 123144
- requires corresponding native devel package

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-1mdv2007.1
+ Revision: 122841
- fix build dependencies

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-1mdv2007.1
- first mdv release

