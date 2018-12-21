Name: xprop
Version: 1.2.3
Release: alt1
Summary: property displayer for X
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.gz

BuildRequires: libX11-devel xorg-util-macros

%description
The xprop utility is for displaying window and font properties in an  X
server.   One  window  or font is selected using the command line argu-
ments or possibly in the case of a window, by clicking on  the  desired
window.   A  list of properties is then given, possibly with formatting
information.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Autobuild version bump to 1.2.3

* Thu Feb 19 2015 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Mar 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Jan 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

