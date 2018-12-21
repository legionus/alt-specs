%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ansi-terminal
%define f_pkg_name ansi-terminal
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.5.1
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://batterseapower.github.com/ansi-terminal
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Simple ANSI terminal support, with Windows compatibility



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
ANSI terminal support for Haskell: allows cursor movement, screen clearing,
color output showing or hiding the cursor, and changing the title.
Compatible with Windows and those Unixes with ANSI terminals, but only GHC
is supported as a compiler.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.5.1-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.5.1-alt1
- Spec created by cabal2rpm 0.20_08
