%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name temporary
%define f_pkg_name temporary
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.1.2.4
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.github.com/batterseapower/temporary
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Portable temporary file and directory support for Windows and Unix, based on code from Cabal



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
The functions for creating temporary files and directories in the base
library are quite limited. The unixutils package contains some good ones,
but they aren't portable to Windows. This library just repackages the Cabal
implementations of its own temporary file and folder functions so that you
can use them without linking against Cabal or depending on it being
installed.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1.2.4-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1.2.4-alt1
- Spec created by cabal2rpm 0.20_08
