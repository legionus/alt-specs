%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name funcmp
%define f_pkg_name funcmp
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.7
Release: alt2
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://savannah.nongnu.org/projects/funcmp/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Functional MetaPost



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
Functional MetaPost is a Haskell frontend to the MetaPost language by John
Hobby. Users write their graphics as Haskell programs, which then emit
MetaPost code that can be compiled into encapsulated PostScript files and
smoothly included into e.g. LaTeX.

A collection of useful examples how to use Functional MetaPost can be found
in the user's manual at
<http://download.savannah.nongnu.org/releases/funcmp/Manual_eng.ps>. The
document doesn't offer very much detail in terms of explanations, but the
code samples are quite helpful.

Further documentation can be found in the original thesis that describes
the implementation. The text is available in German at
<http://download.savannah.nongnu.org/releases/funcmp/Thesis.ps> and in
English at
<http://download.savannah.nongnu.org/releases/funcmp/Thesis_eng.ps>.

Last but not least, there is a tutorial that offers many helpful examples
available in German at
<http://download.savannah.nongnu.org/releases/funcmp/Tutorial.ps> and in
English at
<http://download.savannah.nongnu.org/releases/funcmp/Tutorial_eng.ps>.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.7-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.7-alt1
- Spec created by cabal2rpm 0.20_08
