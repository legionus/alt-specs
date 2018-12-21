%define dist Module-Load
Name: perl-%dist
Version: 0.32
Release: alt1

Summary: runtime require of both modules and files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-devel

%description
"load" eliminates the need to know whether you are trying to require
either a file or a module.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Module

%changelog
* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 0.12 -> 0.18

* Tue May 06 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.10 -> 0.12

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus
