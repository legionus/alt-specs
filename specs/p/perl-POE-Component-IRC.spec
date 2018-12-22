%define _unpackaged_files_terminate_build 1
%define dist POE-Component-IRC
Name: perl-%dist
Version: 6.90
Release: alt1

Summary: A fully event-driven IRC client dist
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-IRC-Utils perl-Net-DNS-SEC perl-POE-Component-Client-DNS perl-POE-Component-SSLify perl-POE-Component-Syndicator perl-POE-Filter-IRCD perl-POE-Filter-Zlib perl-devel
BuildRequires: perl-List-MoreUtils  perl-Test-Differences

%description
POE::Component::IRC is a POE (Perl Object Environment) component
which provides a convenient way for POE applications to create a tiny
IRC client session and send and receive IRC events through it.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes docs examples
%perl_vendor_privlib/POE

%changelog
* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 6.90-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 6.88-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 6.87-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 6.83-alt1
- automated CPAN update

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 6.81-alt1
- 6.81

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 6.80-alt1
- 6.75 -> 6.80
- update BR:

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 6.75-alt1
- 6.52 -> 6.75

* Mon Nov 22 2010 Alexey Shabalin <shaba@altlinux.ru> 6.52-alt1
- 6.52
- drop %%perl_vendor_man3dir

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 6.35-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 6.16-alt1
- 6.16

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 5.88-alt1
- initial build for ALT Linux Sisyphus
