%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name uniplate
%define f_pkg_name uniplate
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.6.10
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://community.haskell.org/~ndm/uniplate/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Help writing simple, concise and fast generic operations.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-hashable ghc7.6.1-text libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-syb ghc7.6.1-unordered-containers

%description
Uniplate is library for writing simple and concise generic operations.
Uniplate has similar goals to the original Scrap Your Boilerplate work, but
is substantially simpler and faster. The Uniplate manual is available at
<http://community.haskell.org/~ndm/darcs/uniplate/uniplate.htm>.

To get started with Uniplate you should import one of the three following
modules:

* "Data.Generics.Uniplate.Data" - to quickly start writing generic
functions. Most users should start by importing this module.

* "Data.Generics.Uniplate.Direct" - a replacement for
"Data.Generics.Uniplate.Data" with substantially higher performance (around
5 times), but requires writing instance declarations.

* "Data.Generics.Uniplate.Operations" - definitions of all the operations
defined by Uniplate. Both the above two modules re-export this module.

In addition, some users may want to make use of the following modules:

* "Data.Generics.Uniplate.Zipper" - a zipper built on top of Uniplate
instances.

* "Data.Generics.SYB" - users transitioning from the Scrap Your Boilerplate
library.

* "Data.Generics.Compos" - users transitioning from the Compos library.

* "Data.Generics.Uniplate.DataOnly" - users making use of both @Data@ and
@Direct@ to avoid getting instance conflicts.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.6.10-alt1
- Spec created by cabal2rpm 0.20_08
