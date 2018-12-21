Summary: Tools for using C-motech hardware with Linux
Name: cmotech-tools
Version: 0.1
Release: alt1.r17.qa2
License: GPLv3
Group: System/Configuration/Networking
Url: http://cmotech-tools.sourceforge.net/
Source0: %name-%version.tar.gz

%description
Tools for using C-motech hardware with Linux. Initially, a program to
switch the CNU-680 USB Modem from CD to modem mode will be
provided. It is typically used in conjunction with udev. The CNU-680
is sold as "D-50" by ice.net.

%prep
%setup -q

%build
./bootstrap
%configure
make

%install
make install DESTDIR=%buildroot rulesdir=%_sysconfdir/udev/rules.d udevdir=/lib/udev
# sysconf/udev policy - /etc is for user
mkdir -p %buildroot%_udevrulesdir/
mv %buildroot%_sysconfdir/udev/rules.d/* %buildroot%_udevrulesdir/

%files
%doc README
%_sbindir/cmotech-cdswitch
%config %_udevrulesdir/cmotech.rules
/lib/udev/cmotech-cdswitch.sh

%changelog
* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt1.r17.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for cmotech-tools

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.r17.qa1
- NMU: rebuilt for debuginfo.

* Fri Sep 19 2008 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt1.r17
- initial build for ALTLinux.
- svn r17 release.

