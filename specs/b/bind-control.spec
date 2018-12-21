Name: bind-control
Version: 1.2
Release: alt1

Summary: ISC BIND facilities control
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: bind-debug.control
Source1: bind-slave.control
Source2: bind-chroot.control

%description
This package contains control rules for ISC BIND - DNS server.
See control(8) for details.

%install
install -pD -m755 %SOURCE0 %buildroot%_controldir/bind-debug
install -pD -m755 %SOURCE1 %buildroot%_controldir/bind-slave
install -pD -m755 %SOURCE2 %buildroot%_controldir/bind-chroot

%files
%config %_controldir/*

%changelog
* Thu Jan 12 2017 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Added bind-chroot facility (by Sergey Bolshakov and me).

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added summary to control files.

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
