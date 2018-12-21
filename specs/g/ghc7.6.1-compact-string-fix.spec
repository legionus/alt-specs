%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name compact-string-fix
%define f_pkg_name compact-string-fix
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://twan.home.fmf.nl/compact-string/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Same as compact-string except with a small fix so it builds on ghc-6.12



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
Fast, packed, strict strings with a list interface. Based on
"Data.ByteString". Multiple encodings are supported. This is the same
package as compact-string-0.3.1 except for a small fix to work with the new
Exception library. Once Twan updates that package, this package will be
deprecated. build-type: Simple

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.2-alt1
- Spec created by cabal2rpm 0.20_08
