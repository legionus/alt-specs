Name: hspell
Version: 1.3
Release: alt1
Summary: A Hebrew spell checker
License: AGPL-3.0-only
Group: Text tools
Url: http://hspell.ivrix.org.il/
# http://hspell.ivrix.org.il/%name-%version.tar.gz
Source: %name-%version.tar
Patch: hspell-1.3-alt-fixes.patch
Requires: lib%name = %version-%release
BuildRequires: libhunspell-devel hunspell-utils zlib-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: aspell-he}}

%description
Hspell is a Hebrew SPELLer and morphological analyzer.  It provides a
mostly spell-like interface (gives the list of wrong words in the input
text), but can also suggest corrections (-c).  It also provides a true
morphological analyzer (-l), that prints all known meanings of a Hebrew
string.

%package common
Summary: Hspell common files
Group: Text tools
BuildArch: noarch

%description common
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell common files.

%package data
Summary: Hspell data files
Group: Text tools
BuildArch: noarch
Requires: %name-common = %version-%release

%description data
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell data files.

%package -n lib%name
Summary: Hspell shared library
Group: System/Libraries
Requires: %name-common = %version-%release

%description -n lib%name
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains Hspell shared library.

%package -n lib%name-devel
Summary: Development library and include files for Hspell
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Hspell is a Hebrew SPELLer and morphological analyzer.
This package contains development library and include files.

%package -n hunspell-he
Summary: Hebrew hunspell dictionaries
Group: Text tools
BuildArch: noarch
Requires: %name-common = %version-%release
Requires: hunspell

%description -n hunspell-he
Hebrew hunspell dictionaries.

%prep
%setup
%patch -p1
iconv -f hebrew -t utf8 -o WHATSNEW.new WHATSNEW
mv WHATSNEW.new WHATSNEW

%build
autoconf
%configure --enable-fatverb --enable-linginfo --enable-shared
make
make hunspell

%install
%makeinstall_std STRIP=:
mkdir -p %buildroot%_datadir/myspell
cp -p he.dic %buildroot%_datadir/myspell/he_IL.dic
cp -p he.aff %buildroot%_datadir/myspell/he_IL.aff
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 LICENSE README WHATSNEW %buildroot%docdir/

%check
LD_LIBRARY_PATH=%buildroot%_libdir make test &> test.log && rc= || rc=$?
cat test.log
if grep -F FAILED test.log | grep -v '^Test 1/aspell/[89] '; then
	rc=1
fi
[ -z "$rc" ]

%files
%_bindir/*
%_man1dir/*

%files common
%docdir/

%files data
%_datadir/%name/

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib*.so
%_man3dir/*

%files -n hunspell-he
%_datadir/myspell/*

%changelog
* Sun Jan 17 2016 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- 1.2 -> 1.3.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated to 1.2.

* Fri Jul 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Initial release for ALT Linux, based on hspell-1.1-4 from Fedora.
