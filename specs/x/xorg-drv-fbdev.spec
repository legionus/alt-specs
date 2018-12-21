Name: xorg-drv-fbdev
Version: 0.5.0
Release: alt1
Epoch: 1
Summary: video driver for framebuffer device
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Provides: xorg-x11-drv-fbdev = %epoch:%version-%release
Obsoletes: xorg-x11-drv-fbdev

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: xorg-proto-devel

%description
fbdev  is an Xorg driver for framebuffer devices.  This is a
non-accelerated driver, the following framebuffer depths are supported:
8,  15,  16, 24.  All visual types are supported for depth 8, and True-
Color visual is supported for the other depths.  Multi-head  configura-
tions are supported.

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
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Thu May 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5.0-alt1
- 0.5.0

* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt6
- requires XORG_ABI_VIDEODRV = 24.0

* Wed Nov 30 2016 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt5
- requires XORG_ABI_VIDEODRV = 23.0

* Thu Nov 26 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt4
- requires XORG_ABI_VIDEODRV = 20.0

* Wed Feb 04 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt3
- requires XORG_ABI_VIDEODRV = 19.0

* Fri Oct 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt2
- requires XORG_ABI_VIDEODRV = 18.0

* Thu Jan 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.4-alt1
- 0.4.4

* Wed Mar 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.3-alt3
- requires XORG_ABI_VIDEODRV = 14.1

* Fri Jan 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.3-alt2
- requires XORG_ABI_VIDEODRV = 13.1

* Mon Aug 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.3-alt1
- 0.4.3

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.2-alt5
- requires XORG_ABI_VIDEODRV = 12.0

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.2-alt4
- requires XORG_ABI_VIDEODRV = 11.0

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.2-alt3
- requires XORG_ABI_VIDEODRV = 10.0

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.2-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Sat Apr 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.2-alt1
- 0.4.2

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt1
- 0.4.1

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.0-alt4
- requires XORG_ABI_VIDEODRV = 5.0

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.0-alt3
- requires XORG_ABI_VIDEODRV = 4.1

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.0-alt2
- renamed xorg-x11-drv-fbdev to xorg-drv-fbdev
- added requires XORG_ABI_VIDEODRV = 2.0

* Wed Mar 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.0-alt1
- 0.4.0

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.0-alt2
- rebuild with xorg-server-1.4

* Fri May 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.3.0-alt1
- 0.3.0

* Sat May 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:0.2.0-alt1
- 0.2.0

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.0.5-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.0.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.0.2-alt0.1
- initial release

