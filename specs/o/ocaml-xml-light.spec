%set_verify_elf_method textrel=relaxed
Name: ocaml-xml-light
Version: 2.4
Release: alt6
Summary: Minimal XML parser and printer for OCaml

Group: Development/ML
License: LGPLv2+
Url: https://opam.ocaml.org/packages/xml-light/
Source0: %name-%version.tar

BuildRequires: ocaml-ocamldoc ocaml-findlib

%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make all doc
make opt
sed -e 's/@VERSION@/%version/' < META.in > META

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
rm -f test.*
ocamlfind install xml-light META *.mli *.cmi *.cma *.a *.cmxa *.cmx

%files
%doc README
%_libdir/ocaml/xml-light
%exclude %_libdir/ocaml/xml-light/*.a
%exclude %_libdir/ocaml/xml-light/*.cmxa
%exclude %_libdir/ocaml/xml-light/*.cmx
%exclude %_libdir/ocaml/xml-light/*.mli

%files devel
%doc README doc/*
%_libdir/ocaml/xml-light/*.a
%_libdir/ocaml/xml-light/*.cmxa
%_libdir/ocaml/xml-light/*.cmx
%_libdir/ocaml/xml-light/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt6
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt5
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 2.4-alt4
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt2
- rebuild with ocaml 4.04.1

* Wed Apr 12 2017 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version
- build for ocaml-4.04

* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1.1
- rebuild with new ocaml

* Thu Nov 12 2009 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- first build for Sisyphus, based on Fedora specfile
