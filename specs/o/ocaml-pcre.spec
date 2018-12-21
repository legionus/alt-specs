# on i586: ERROR: ./usr/lib/ocaml/pcre/pcre.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed

Name: ocaml-pcre
Version: 7.3.4
Release: alt3

Summary: Perl compatibility regular expressions (PCRE) for OCaml
License: LGPL
Group: Development/ML
Url: http://mmottl.github.io/pcre-ocaml/

# https://github.com/mmottl/pcre-ocaml
Source: %name-%version.tar
Provides: pcre-ocaml = %version-%release
Obsoletes: pcre-ocaml
Provides: ocaml-pcre-runtime = %version-%release
Obsoletes: ocaml-pcre-runtime < %version-%release

BuildRequires: libpcre-devel ocaml ocaml-findlib ocaml-ocamlbuild ocaml-ocamldoc jbuilder opam ocaml-base ocaml-configurator ocaml-stdio

%description
This OCaml-library interfaces the PCRE (Perl-compatibility regular
expressions) library which is written in C. it can be used for matching
regular expressions which are written in "PERL"-style.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Requires: libpcre-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md README.md
%_libdir/ocaml/pcre
%exclude %_libdir/ocaml/pcre/*.a
%exclude %_libdir/ocaml/pcre/*.cmxa
%exclude %_libdir/ocaml/pcre/*.cmx
%exclude %_libdir/ocaml/pcre/*.mli
%_libdir/ocaml/stublibs/*.so

%files devel
%doc README.md
%_libdir/ocaml/pcre/*.a
%_libdir/ocaml/pcre/*.cmxa
%_libdir/ocaml/pcre/*.cmx
%_libdir/ocaml/pcre/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 7.3.4-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 7.3.4-alt2
- rebuilt with ocaml 4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 7.3.4-alt1
- 7.3.4

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 7.2.3-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 7.2.3-alt3
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 7.2.3-alt2
- split to devel and main package

* Tue Apr 11 2017 Anton Farygin <rider@altlinux.ru> 7.2.3-alt1
- new version

* Thu Dec 22 2011 Alexey Shabalin <shaba@altlinux.ru> 6.2.4-alt1
- 6.2.4

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 5.14.0-alt2
- recompiled pcre.cma without -custom flag

* Thu Apr 10 2008 Alexey Tourbin <at@altlinux.ru> 5.14.0-alt1
- 5.13.0 -> 5.14.0

* Wed Mar 12 2008 Grigory Batalov <bga@altlinux.ru> 5.13.0-alt1
- New upstream release.

* Wed Dec 20 2006 Grigory Batalov <bga@altlinux.ru> 5.11.2-alt3
- New upstream release.
- Moved on to get_SVR macro.
- Strict packaging.
- Url updated.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.09.0-alt3
- Moved on to get_dep macro.

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.09.0-alt2
- Rebuild with ocaml-3.09.1.

* Wed Dec 28 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.09.0-alt1.1
- Rebuild with ocaml-3.08.1-alt1.1 .

* Tue Oct 26 2004 Vitaly Lugovsky <vsl@altlinux.ru> 5.09.0-alt1
- a new version

* Sat Jul 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.4-alt6
- rebuild

* Wed Jul 07 2004 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.4-alt5
- rebuild

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 5.04.4-alt4.1
- Non-maintainer upload
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Thu Mar 18 2004 Dmitry V. Levin <ldv@altlinux.org> 5.04.4-alt4
- Rebuilt with ocaml-3.07-alt6.

* Fri Mar 12 2004 Dmitry V. Levin <ldv@altlinux.org> 5.04.4-alt3.1
- Fixed package dependencies.
- Specfile cleanup.

* Wed Feb 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.4-alt3
- rebuild

* Tue Jan 27 2004 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.4-alt2
- rebuild

* Tue Dec 16 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.4-alt1
- A new version

* Fri Nov 28 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.04.3-alt1
- a new version

* Fri Oct 10 2003 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt5s
- rebuild (3.07)

* Wed Aug 27 2003 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt4s
- rebuild (3.07bs)

* Thu Mar 06 2003 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt3s
- runtime part separated

* Fri Jan 31 2003 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt2s
- rebuild with 3.06 [Shared]

* Fri Jan 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt2
- rebuild

* Sun Oct 27 2002 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.3-alt1
- new version

* Thu Aug 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 4.28.2-alt1
- new version

* Tue Jul 30 2002 Vitaly Lugovsky <vsl@altlinux.ru> 4.26.3-alt2
- rebuild: ocaml 3.05

* Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 4.26.3-alt1
- First RPM release.
