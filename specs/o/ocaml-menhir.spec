%set_verify_elf_method textrel=relaxed
Name: ocaml-menhir
Version: 20181113
Release: alt1
Summary: LR(1) parser generator for the OCaml programming language.

Group: Development/ML
License: QPL
Url: http://gallium.inria.fr/~fpottier/menhir/
Source: menhir-%version.tar

BuildRequires(pre): ocaml
Provides: ocaml4-menhir = %EVR
Obsoletes: ocaml4-menhir

BuildRequires: ocaml-camlp4 ocaml-findlib ocaml-ocamlbuild python-module-google python3-base

%description
Menhir is a LR(1) parser generator for the OCaml programming language.
That is, Menhir compiles LR(1) grammar specifications down to OCaml
code. Menhir is 90 percent compatible with ocamlyacc. Legacy ocamlyacc
grammar specifications are accepted and compiled by Menhir. The
resulting parsers run and produce correct parse trees. However, parsers
that explicitly invoke functions in module Parsing behave slightly
incorrectly. For instance, the functions that provide access
to positions return a dummy position when invoked by a Menhir parser.
Porting a grammar specification from ocamlyacc to Menhir requires
replacing all calls to module Parsing with new Menhir-specific keywords.

%prep
%setup -q -n menhir-%version

%build
make PREFIX=/usr all

%install
mkdir -p %buildroot%_libdir/ocaml
make OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml PREFIX=%buildroot/usr install

mkdir -p %buildroot%_datadir/doc/%name-%version
mv %buildroot%_datadir/doc/menhir/* %buildroot%_datadir/doc/%name-%version/
rm -rf %buildroot%_datadir/doc/menhir
rm -rf %buildroot%_datadir/doc/%name-%version/src/

%files
%doc CHANGES.md
%doc demos
%doc INSTALLATION.md
%doc README.md
%doc LICENSE
%_bindir/*
%_man1dir/*
%dir %_datadir/menhir
%_datadir/menhir/*
%dir %_libdir/ocaml/menhirLib
%dir %_libdir/ocaml/menhirSdk
%_libdir/ocaml/menhirLib/*
%_libdir/ocaml/menhirSdk/*

%changelog
* Mon Nov 19 2018 Anton Farygin <rider@altlinux.ru> 20181113-alt1
- 20181113

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 20181026-alt1
- 20181026

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 20181005-alt2
- rebuilt for ocaml-4.07.1

* Tue Oct 09 2018 Anton Farygin <rider@altlinux.ru> 20181005-alt1
- 20181005

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 20180530-alt2
- rebuilt with ocaml-4.07

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 20180530-alt1
- 20180530 (closes: #34902)

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 20171222-alt1
- 20171222

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt2
- rebuilt for ocaml 4.06

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 20170607-alt1
- updated to 20170607

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt2
- rebuild with ocaml 4.04.1

* Thu Mar 30 2017 Anton Farygin <rider@altlinux.ru> 20170101-alt1
- renamed to ocaml-menhir
- new version

* Mon Jun 27 2016 Andrey Bergman <vkni@altlinux.org> 20160518-alt1
- Initial release for Sisyphus.
