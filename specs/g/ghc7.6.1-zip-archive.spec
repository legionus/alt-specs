%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name zip-archive
%define f_pkg_name zip-archive
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.3.4
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/jgm/zip-archive
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Library for creating and modifying zip archives.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-digest ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-mtl ghc7.6.1-utf8-string ghc7.6.1-zlib zlib-devel

%description
The zip-archive library provides functions for creating, modifying, and
extracting files from zip archives.

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
* Mon May 06 2013 Denis Smirnov <mithraen@altlinux.ru> 0.1.3.4-alt1
- new version 0.1.3.4

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.2.1-alt1
- Spec created by cabal2rpm 0.20_08
