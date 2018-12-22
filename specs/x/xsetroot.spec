Name: xsetroot
Version: 1.1.2
Release: alt1
Summary: root window parameter setting utility for X
License: (MIT or X11)
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar.gz

BuildRequires: libXcursor-devel libXmu-devel xorg-bitmaps xorg-util-macros

%description
The  setroot  program  allows you to tailor the appearance of the back-
ground ("root") window on a workstation display running  X.   Normally,
you  experiment  with  xsetroot until you find a personalized look that
you like, then put the xsetroot command that produces it  into  your  X
startup  file.   If  no options are specified, or if -def is specified,
the window is reset to its default state.  The -def option can be spec-
ified  along with other options and only the non-specified characteris-
tics will be reset to the default state.

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
* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Aug 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

