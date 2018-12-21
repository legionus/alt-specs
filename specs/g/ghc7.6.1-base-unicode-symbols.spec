%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name base-unicode-symbols
%define f_pkg_name base-unicode-symbols
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.2.4
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://haskell.org/haskellwiki/Unicode-symbols
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Unicode alternatives for common functions and operators



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
This package defines new symbols for a number of functions, operators and
types in the base package.

All symbols are documented with their actual definition and information
regarding their Unicode code point. They should be completely
interchangeable with their definitions.

For further Unicode goodness you can enable the @UnicodeSyntax@ language
extension \[1\]. This extension enables Unicode characters to be used to
stand for certain ASCII character sequences, i.e. &#x2192; instead of @->@,
&#x2200; instead of @forall@ and many others.

Original idea by P&#xE9;ter Divi&#xE1;nszky.

\[1\]
<http://www.haskell.org/ghc/docs/latest/html/users_guide/syntax-extns.html#
unicode-syntax>

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.2.2.4-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.2.2.4-alt1
- Spec created by cabal2rpm 0.20_08
