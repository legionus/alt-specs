%set_verify_elf_method textrel=relaxed
Name: ocaml-ssl
Version: 0.5.6
Release: alt1
Summary: OCaml bindings for the OpenSSL library
License: LGPLv2.1 with exemptions
Group: Development/ML
Url: https://github.com/savonet/ocaml-ssl
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: ocaml-findlib libssl-devel

BuildRequires(pre): ocaml dune opam

%description
This package contains OCaml bindings for libssl.

Install it if you intend to develop
SSL-enabled applications in OCaml.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Requires: libssl-devel
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
%build
%make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%_libdir/ocaml/ssl
%exclude %_libdir/ocaml/ssl/*.a
%exclude %_libdir/ocaml/ssl/*.cmxa
%exclude %_libdir/ocaml/ssl/*.mli
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/ssl/*.a
%_libdir/ocaml/ssl/*.cmxa
%_libdir/ocaml/ssl/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.5.5-alt2
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- rebuild with ocaml 4.04.1

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- move module outside site-lib dir
- split to runtime and devel packages

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jan 06 2008 Alex V. Myltsev <avm@altlinux.ru> 0.4.2-alt1
- Initial build for Sisyphus
