%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hint
%define f_pkg_name hint
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.3.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://darcsden.com/jcpetruzza/hint
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Runtime Haskell interpreter (GHC API wrapper)



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-extensible-exceptions ghc7.6.1-monadcatchio-mtl ghc7.6.1-mtl ghc7.6.1-syb ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-ghc-mtl ghc7.6.1-ghc-paths ghc7.6.1-haskell-src ghc7.6.1-hscolour ghc7.6.1-random ghc7.6.1-utf8-string

%description
This library defines an @Interpreter@ monad. It allows to load Haskell
modules, browse them, type-check and evaluate strings with Haskell
expressions and even coerce them into values. The library is thread-safe
and type-safe (even the coercion of expressions to values).

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.3.5-alt1
- Spec created by cabal2rpm 0.20_08
