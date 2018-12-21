# ./usr/lib/ocaml/yojson/yojson.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-yojson
%define libname %(sed -e 's/^ocaml-//' <<< %name)
Version: 1.4.1
Release: alt3
Summary: An optimized parsing and printing library for the JSON format
Group: Development/ML
License: BSD
Url: http://opam.ocaml.org/packages/yojson/
# https://github.com/mjambon/yojson.git
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-easy-format-devel
BuildRequires: opam jbuilder

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make all

%install
mkdir -p %buildroot%_libdir/ocaml
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE
%_libdir/ocaml/%libname/
%_bindir/ydump
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc LICENSE README.md Changes examples
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- first build for ALT, based on RH spec
