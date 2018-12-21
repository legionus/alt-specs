%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name tagsoup
%define f_pkg_name tagsoup
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.8
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://community.haskell.org/~ndm/tagsoup/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Parsing and extracting information from (possibly malformed) HTML/XML documents



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-text

%description
TagSoup is a library for parsing HTML/XML. It supports the HTML 5
specification, and can be used to parse either well-formed XML, or
unstructured and malformed HTML from the web. The library also provides
useful functions to extract information from an HTML document, making it
ideal for screen-scraping.

Users should start from the "Text.HTML.TagSoup" module.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.8-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.8-alt1
- Spec created by cabal2rpm 0.20_08
