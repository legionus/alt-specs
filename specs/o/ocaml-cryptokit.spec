# on i586: /usr/lib/ocaml/site-lib/cryptokit/cryptokit.cmxs
%set_verify_elf_method textrel=relaxed

%global pkgname cryptokit
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 1.13
Release: alt3
Group: Development/ML
Summary: OCaml library of cryptographic and hash functions
License: LGPLv2 with exceptions
Url: http://forge.ocamlcore.org/projects/cryptokit/
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-ocamldoc ocaml-ocamlbuild ocaml-zarith-devel ocaml-findlib zlib-devel chrpath
Provides: ocaml-cryptokit-runtime = %version-%release
Obsoletes: ocaml-cryptokit-runtime

%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include:

* Symmetric-key cryptography: AES, DES, Triple-DES, ARCfour, in ECB,
  CBC, CFB and OFB modes.
* Public-key cryptography: RSA encryption and signature; Diffie-Hellman
  key agreement.
* Hash functions and MACs: SHA-1, SHA-256, RIPEMD-160, MD5, and MACs
  based on AES and DES.
* Random number generation.
* Encodings and compression: base 64, hexadecimal, Zlib compression.

Additional ciphers and hashes can easily be used in conjunction with
the library. In particular, basic mechanisms such as chaining modes,
output buffering, and padding are provided by generic classes that can
easily be composed with user-provided ciphers. More generally, the
library promotes a "Lego"-like style of constructing and composing
transformations over character streams.

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
./configure --destdir %buildroot
# Some sort of circular dependency, so sometimes the first make fails.
# Just run make twice.
make ||:
make

chrpath --delete _build/src/dllcryptokit_stubs.so

%install
mkdir -p %buildroot%ocamlstublib
export OCAMLFIND_DESTDIR=%buildroot%ocamlsitelib
make install

%files
%doc LICENSE.txt
%pkgsitelib
%exclude %pkgsitelib/*.mli
%ocamlstublib/*.so*

%files devel
%doc README.txt Changes
%pkgsitelib/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt2
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.13-alt1
- 1.13

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt2
- rebuild with ocaml 4.04.1

* Tue Feb 14 2017 Anton Farygin <rider@altlinux.ru> 1.11-alt1
- updated to new version

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Thu Oct 02 2008 Boris Savelev <boris@altlinux.org> 1.3-alt5
- remove "directory" from META

* Tue Sep 30 2008 Boris Savelev <boris@altlinux.org> 1.3-alt4
- add requires to META (fix #170011)

* Thu Sep 04 2008 Boris Savelev <boris@altlinux.org> 1.3-alt3
- rename to ocaml-cryptokit
- move files to site-lib/cryptokit
- add META
- split runtime and devel package

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 1.3-alt2
- add make allopt (to build cryptokit.cmxa)

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 1.3-alt1
- initial build

