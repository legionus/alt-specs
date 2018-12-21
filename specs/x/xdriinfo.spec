Name: xdriinfo
Version: 1.0.6
Release: alt1
Summary: query configuration information of DRI drivers
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar.gz

BuildRequires: libGL-devel xorg-glproto-devel xorg-util-macros

%description
xdriinfo  can be used to query configuration information of direct ren-
dering drivers. If no command argument is specified it lists the  names
of the direct rendering drivers for all screens

%prep
%setup

%build
%autoreconf
%configure

%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Aug 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

