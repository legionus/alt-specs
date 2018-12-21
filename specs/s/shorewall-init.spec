%define _libexecdir /usr/libexec
%filter_from_requires /^\/etc\/default\/shorewall-init/d

Name: shorewall-init
Version: 5.2.1.1
Release: alt1
Summary: Shorewall-init adds functionality to Shoreline Firewall (Shorewall).
License: GPLv2
Group: Security/Networking
Url: http://www.shorewall.net/
Source: %name-%version.tar.bz2

BuildArch: noarch
Requires: shoreline_firewall >= 4.5.0
BuildRequires: perl-Digest-SHA

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

Shorewall Init is a companion product to Shorewall that allows for tigher
control of connections during boot and that integrates Shorewall with
ifup/ifdown and NetworkManager.


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

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING changelog.txt releasenotes.txt
%_sbindir/%name
%_initdir/%name
%_unitdir/*.service
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_datadir/%name
%_datadir/%name/*
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Fri Nov 16 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1.1-alt1
- 5.2.1.1

* Sat Jul 14 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt0.Beta2
- Initial build for 5.2.1-Beta2

