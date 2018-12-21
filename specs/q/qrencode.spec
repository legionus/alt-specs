Name: qrencode
Version: 4.0.2
Release: alt1

Summary: Generate QR 2D barcodes
License: LGPLv2+
Group: File tools

URL: https://fukuchi.org/works/qrencode/index.html.en
Source: %name-%version.tar
#Source: https://fukuchi.org/works/qrencode/qrencode-%version.tar.gz

BuildRequires: glibc-devel libSDL-devel libpng-devel

%description
Qrencode is a utility to encode string data in a QR Code and save as a PNG image.

%package -n libqrencode4
Summary: A C library for encoding data in a QR Code symbol
Group: System/Libraries

%description -n libqrencode4
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

Libqrencode supports QR Code model 2, described in JIS (Japanese Industrial
Standards) X0510:2004 or ISO/IEC 18004.

%package -n libqrencode4-devel
Summary: The development files for the qrencode library
Group: Development/C
Requires: libqrencode4 = %EVR
Provides: libqrencode-devel = %EVR

%description -n libqrencode4-devel
This package contains the development files for the qrencode library.

%prep
%setup
echo -e "#! /bin/sh\n\ntrue" > use/config.rpath
mkdir m4

%build
%autoreconf
%configure \
    --disable-rpath \
    --with-tests \

%make_build

%install
%makeinstall_std

%check
cd ./tests
./test_all.sh

%files
%_bindir/*
%_man1dir/*

%files -n libqrencode4
%_libdir/libqrencode.so.*

%files -n libqrencode4-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Mon Sep 17 2018 Pavel Moseev <mars@altlinux.org> 4.0.2-alt1
- Updated to upstream version 4.0.2

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 3.4.4-alt1
- new version

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 3.4.3-alt0.M70P.1
- built for M70P

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 3.4.3-alt1
- new version

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.1
- Rebuilt with libpng15

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 3.3.1-alt1
- 3.3.1

* Mon Apr 02 2012 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- 3.3.0

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 3.1.1-alt1
- Initial build.
