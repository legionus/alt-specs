%define _unpackaged_files_terminate_build 1
%define dist Net-CIDR
Name: perl-Net-CIDR
Version: 0.19
Release: alt1

Summary: Manipulate IPv4/IPv6 netblocks in CIDR notation
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MR/MRSAM/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-devel

%description
The Net::CIDR package contains functions that manipulate lists of IP
netblocks expressed in CIDR notation.
The Net::CIDR functions handle both IPv4 and IPv6 addresses.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/Net

%changelog
* Tue Jun 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Apr 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13

* Mon Oct 06 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt2
- fixed files list for sisyphus_check

* Thu Aug 18 2005 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt1
- update 0.11

* Mon Jun 27 2005 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus
