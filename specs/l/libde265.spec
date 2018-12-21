Name: libde265
Version: 1.0.3
Release: alt1
Summary: Open H.265 video codec implementation
License: LGPLv3
Group: System/Libraries
Url: https://github.com/strukturag/libde265
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++

%description
libde265 is an open source implementation of the H.265 video codec.
It is written from scratch in plain C for simplicity and efficiency.
Its simple API makes it easy to integrate it into other software.

%package devel
Group: Development/C++
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-dec265 \
	--disable-sherlock265 \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/%name.so.*

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- initial release

