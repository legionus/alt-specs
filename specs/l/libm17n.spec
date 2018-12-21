%define oname m17n-lib
Name: libm17n
Version: 1.8.0
Release: alt1

Summary: Multilingual text processing library

Group: Text tools
License: LGPL
Url: http://www.nongnu.org/m17n/

# repacked http://download.savannah.gnu.org/releases/m17n/m17n-lib-%version.tar.gz
Source: %oname-%version.tar
Source1: %oname.watch

# $ freetype-config --libs
# -lfreetype -lz
BuildRequires: zlib-devel

# Automatically added by buildreq on Mon Dec 28 2009
BuildRequires: glibc-devel-static imake libXaw-devel libXft-devel libxml2-devel xorg-cf-files
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libm17n-db = %version

%description
The m17n library is a multilingual text processing library for the C
language.

%package -n m17n-utils
Summary: Multilingual text processing utilities
Group: Development/C

%description -n m17n-utils
Multilingual text processing utilities.

%package -n libm17n-gui
Summary: Multilingual text processing library GUI level APIs
Group: Development/C

%description -n libm17n-gui
The m17n library is a multilingual text processing library for the C
language.

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries/include files for development with %name.

%prep
%setup -q -n %oname-%version

%build
%autoreconf
%configure \
	--with-fontconfig \
	--disable-rpath \
	--disable-static
%make

%install
%makeinstall

%files
%doc AUTHORS NEWS
%_libdir/libm17n.so.*
%_libdir/libm17n-core.so.*
%_libdir/libm17n-flt.so.*

%files -n libm17n-gui
%_libdir/m17n
%_libdir/libm17n-gui.so.*

%files -n m17n-utils
%_bindir/*

%files devel
%doc README TODO ChangeLog
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*

%changelog
* Mon Jul 30 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.0-alt1
- 1.8.0
- libm17n-devel: didn't package m17n-config because we have pkg-config

* Thu May 18 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Sep 12 2011 Alexey Gladkov <legion@altlinux.ru> 1.6.2-alt2
- Fix buildrequires (workaround).

* Fri Dec 17 2010 Alexey Gladkov <legion@altlinux.ru> 1.6.2-alt1
- New version (1.6.2).

* Mon Dec 28 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.5-alt1
- new version (1.5.5).

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.2
- build without gui, unresolved=relaxed

* Fri Mar 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.1
- new version (1.3.3)

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1
- initial build for ALT Linux Sisyphus
