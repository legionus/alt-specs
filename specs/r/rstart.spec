Name: rstart
Version: 1.0.5
Release: alt1

Summary: a sample implementation of a Remote Start client
License: (MIT or X11)
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Tue May 03 2011
# optimized out: pkg-config
BuildRequires: xorg-xproto-devel

BuildRequires: xorg-util-macros

%description
Rstart  is  a simple implementation of a Remote Start client as defined
in "A Flexible Remote Execution Protocol Based on rsh".  It uses rsh as
its underlying remote execution mechanism.

%prep
%setup

# XXX this fixes error, but doesn't fix bug
sed -i 's/(sysconfdir)/sysconfdir/' configure.ac

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
# XXX move config to /etc/X11/rstart
##_sysconfdir/X11/rstart
%_bindir/*
%_man1dir/*
%_libdir/X11/%name

%changelog
* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4
- Fix patch

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Apr 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- rebuild

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Fri Dec 02 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

