%define dist HTTP-Date
Name: perl-%dist
Version: 6.02
Release: alt1

Summary: Date conversion routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Date-%{version}.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-devel

%description
This module provides functions that deal the date formats used by
the HTTP protocol (and then some more).  Only the first two functions,
time2str() and str2time(), are exported by default.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 6.02-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 6.00 -> 6.01

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
