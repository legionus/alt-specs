%define dist Net-Pcap-Easy

%ifdef __BTE
%def_without test
%endif

Name: perl-%dist
Version: 1.4210
Release: alt1

Summary: Net::Pcap is awesome, but it's difficult to bootstrap
Group: Development/Perl
License: GPL or Artistic
BuildArch: noarch

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JE/JETTERO/Net-Pcap-Easy-%{version}.tar.gz

BuildRequires: perl-devel perl-Net-Pcap perl-NetPacket perl-Net-Netmask

%description
This module is little more than a collection of macros and convenience functions. Net::Pcap does all the real work (of lifting libpcap into perl anyway).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net*
%doc README

%changelog
* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.4210-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4209-alt1
- automated CPAN update

* Mon Dec 12 2011 Eugene Prokopiev <enp@altlinux.ru> 1.4207-alt1
- First build for Sisyphus
