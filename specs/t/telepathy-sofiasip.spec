%define _name sofiasip

Name: telepathy-sofiasip
Version: 0.6.8
Release: alt1

Summary: SIP connection manager for the Telepathy framework
License: LGPL-2.1-or-later
Group: Networking/Instant messaging
Url: http://sourceforge.net/projects/tp-sofiasip

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

BuildRequires: libdbus-devel libdbus-glib-devel libsofia-sip-glib-devel >= 1.12.11 libgio-devel
BuildRequires: libtelepathy-glib-devel >= 0.8.0 xsltproc
# for check:
BuildRequires: python-module-twisted-words python-module-twisted-core-gui dbus-tools-gui python-module-dbus

%description
telepathy-sofiasip is a SIP connection manager for the Telepathy framework
(http://telepathy.freedesktop.org) based on the SofiaSIP-stack.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files and documentation for telepathy-sofiasip
(SIP connection manager for the Telepathy framework)

%prep
%setup -q

%build
%configure
%make_build

%check
%make check

%install
%make_install DESTDIR=%buildroot install

%files
%_libexecdir/telepathy-sofiasip
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sofiasip.service
%_datadir/telepathy/managers/sofiasip.manager
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/*
%_man8dir/*

%changelog
* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.8-alt1
- 0.6.8

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt2
- python-module-twisted-core-gui added to buldreqs

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3
- %%check section

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.17-alt1
- 0.5.17
- new devel package

* Wed Jun 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.15-alt1
- 0.5.15 development release

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.4.5-alt4
- fix rebuild

* Thu May 01 2008 Igor Zubkov <icesik@altlinux.org> 0.4.5-alt3
- fix rebuild
- buildreq

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 0.4.5-alt2
- add Url

* Thu Dec 06 2007 Igor Zubkov <icesik@altlinux.org> 0.4.5-alt1
- build for Sisyphus


