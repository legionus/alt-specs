%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskell-src-exts
%define f_pkg_name haskell-src-exts
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.13.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/haskell-src-exts
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Manipulating Haskell source: abstract syntax, lexer, parser, and pretty-printer



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour

%description
Haskell-Source with Extensions (HSE, haskell-src-exts) is an extension of
the standard haskell-src package, and handles most registered syntactic
extensions to Haskell, including:

* Multi-parameter type classes with functional dependencies

* Indexed type families (including associated types)

* Empty data declarations

* GADTs

* Implicit parameters

* Template Haskell

and a few more. All extensions implemented in GHC are supported. Apart from
these standard extensions, it also handles regular patterns as per the HaRP
extension as well as HSX-style embedded XML syntax.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.13.5-alt1
- Spec created by cabal2rpm 0.20_08
