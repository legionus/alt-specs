%define dist Math-Base36
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: Encoding and decoding of base36 strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BR/BRICAS/Math-Base36-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Math-BigInt perl-Test-Pod perl-Test-Pod-Coverage perl(Test/Exception.pm)

%description
This module converts to and from Base36 numbers (0..9 - A..Z)

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Math

%changelog
* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt2
- disabled build dependency on perl-Math-Base36

* Tue Dec 28 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.07 -> 0.09

* Sun Aug 22 2010 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- initial revisoin, for DBIx-Class-0.08123
