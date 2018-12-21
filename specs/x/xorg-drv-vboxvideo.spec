%define git %nil

Name: xorg-drv-vboxvideo
Version: 1.0.0
Release: alt1
Epoch: 1
Summary: VirtualBox video driver
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: L.A. Kostis <lakostis@altlinux.org>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: xorg-resourceproto-devel xorg-scrnsaverproto-devel

# there's no virtulabox other than %%x86/x86_64 exists
ExclusiveArch: %ix86 x86_64

%description
xf86-video-vboxvideo - VirtualBox video driver for the Xorg X server

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/*_drv.so
%_man4dir/*

%changelog
* Tue Jul 17 2018 Evgeny Sinelnikov <sin@altlinux.org> 1:1.0.0-alt1
- Build for Sisyphus

* Mon Jun 25 2018 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.0-alt0.2
- Set ExclusiveArch to x86/x86_64 only.

* Fri May 18 2018 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.0-alt0.1
- initial build for ALTLinux.
