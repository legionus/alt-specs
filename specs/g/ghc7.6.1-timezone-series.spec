%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name timezone-series
%define f_pkg_name timezone-series
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://projects.haskell.org/time-ng/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Enhanced timezone handling for Data.Time



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
This package endows Data.Time, from the time package, with several data
types and functions for enhanced processing of timezones. For one way to
create timezone series, see the timezone-olson package.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- Spec created by cabal2rpm 0.20_08
