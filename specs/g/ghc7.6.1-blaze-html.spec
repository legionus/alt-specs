%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name blaze-html
%define f_pkg_name blaze-html
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.1.3
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://jaspervdj.be/blaze
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A blazingly fast HTML combinator library for Haskell



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-blaze-builder ghc7.6.1-common ghc7.6.1-text libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-blaze-markup ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour

%description
A blazingly fast HTML combinator library for the Haskell programming
language. The Text.Blaze module is a good starting point, as well as this
tutorial: <http://jaspervdj.be/blaze/tutorial.html>.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.1.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.1.3-alt1
- Spec created by cabal2rpm 0.20_08