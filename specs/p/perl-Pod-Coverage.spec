%define dist Pod-Coverage
Name: perl-%dist
Version: 0.23
Release: alt2

Summary: Checks if the documentation of a module is comprehensive
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RC/RCLAMP/Pod-Coverage-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Devel-Symdump perl-Pod-Parser perl-Test-Pod

%description
This module provides a mechanism for determining if the pod for a
given module is comprehensive.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/pod*
%perl_vendor_privlib/Pod

%changelog
* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- BR: cleanup

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.19 -> 0.21

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt2
- fix directory ownership violation

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- first build for ALT Linux Sisyphus
