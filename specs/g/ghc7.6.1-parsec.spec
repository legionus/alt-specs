%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name parsec
%define f_pkg_name parsec
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 3.1.3
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.cs.uu.nl/~daan/parsec.html
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Monadic parser combinators



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-mtl ghc7.6.1-text

%description
Parsec is designed from scratch as an industrial-strength parser library.
It is simple, safe, well documented (on the package homepage), has
extensive libraries and good error messages, and is also fast. It is
defined as a monad transformer that can be stacked on arbitrary monads, and
it is also parametric in the input stream type.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 3.1.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 3.1.3-alt1
- Spec created by cabal2rpm 0.20_08
