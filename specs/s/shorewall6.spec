%define _libexecdir /usr/libexec
%set_compress_method skip

Name: shorewall6
Version: 5.2.1.1
Release: alt1
Summary: Shoreline Firewall 6 is an ip6tables-based firewall for Linux systems.
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source: %name-%version.tar.bz2
Source3: shorewall6-control
Source4: shorewall6-README.ALT.RU.UTF8

BuildArch: noarch
Requires: shorewall-core iptables-ipv6
Requires: shorewall >= 5.2.0

BuildRequires: perl-Digest-SHA

%description
The Shoreline Firewall 6, more commonly known as "Shorewall6", is a Netfilter
(ip6tables) based IPv6 firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.


%prep
%setup -n %name-%version

%build
%install
./configure.pl --host=%_vendor \
               --prefix=%prefix \
               --perllibdir=%perl_vendorlib \
               --libexecdir=%_libexecdir \
               --sbindir=%_sbindir

DESTDIR=%buildroot ./install.sh

install -D -m 0755 %SOURCE3 %buildroot%_controldir/%name
install -m 0644 %SOURCE4 README.ALT.RU.UTF8
touch %buildroot%_sysconfdir/%name/isusable
touch %buildroot%_sysconfdir/%name/notrack

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING INSTALL changelog.txt releasenotes.txt tunnel ipsecvpn ipv6 Samples6
%doc README.ALT.RU.UTF8
%_sbindir/%name
%_initdir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%attr(0600,root,root) %config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%ghost %_sysconfdir/%name/isusable
%_controldir/%name
%dir %_datadir/%name
%_datadir/%name/*
%dir %_localstatedir/%name
%_man5dir/*
%_man8dir/*

%changelog
* Fri Nov 16 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1.1-alt1
- 5.2.1.1

* Sat Jul 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.2.1-alt0.Beta2
- 5.2.1-Beta2

* Fri Apr 27 2018 Grigory Ustinov <grenka@altlinux.org> 4.4.23.3-alt3.1
- Rebuilt for e2k.

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt3
- only root have access to config files

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt2
- drop all %%attr

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 4.4.23.3-alt1
- 4.4.23.3

* Fri Dec 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.15.1-alt1
- 4.4.15.1

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.13.1-alt1
- 4.4.13.1

* Thu Feb 11 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.6-alt1
- 4.4.6

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.4.2-alt1
- 4.4.4.2

* Fri Nov 06 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1
- 4.4.3

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- Initial build for Sisyphus
