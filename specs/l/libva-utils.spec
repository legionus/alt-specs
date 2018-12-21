Name: libva-utils
Version: 2.3.0
Release: alt1
Summary: Tools for VAAPI (including vainfo)
License: MIT and BSD
Group: Graphical desktop/Other
Url: https://01.org/linuxmedia
#git https://github.com/01org/libva-utils
Source0: %name-%version.tar

BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libdrm-devel
BuildRequires: libpciaccess-devel
BuildRequires: libva-devel
BuildRequires: libEGL-devel
BuildRequires: libGL-devel
BuildRequires: libGLES-devel
BuildRequires: wayland-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(wayland-client) >= 1
BuildRequires: pkgconfig(wayland-scanner) >= 1
BuildRequires: pkgconfig(wayland-server) >= 1

%description
The libva-utils package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.

%prep
%setup
autoreconf -fisv

%build
%configure --disable-static \
	--enable-glx \

%make_build

%install
%makeinstall

%files
%doc CONTRIBUTING.md README.md COPYING
%_bindir/vainfo
%_bindir/avcstreamoutdemo
%_bindir/vp8enc
%_bindir/vavpp
%_bindir/vp9enc
%_bindir/loadjpeg
%_bindir/jpegenc
%_bindir/avcenc
%_bindir/h264encode
%_bindir/hevcencode
%_bindir/mpeg2vldemo
%_bindir/mpeg2vaenc
%_bindir/putsurface
%_bindir/putsurface_wayland

%changelog
* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Sat Jul 08 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt1
- new version

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- first build for ALT , based on RH spec

