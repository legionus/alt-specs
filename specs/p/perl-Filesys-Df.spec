%define dist Filesys-Df
Name: perl-%dist
Version: 0.92
Release: alt3.1.1.1.1

Summary: Perl extension for filesystem disk space information
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This module provides a way to obtain filesystem disk space
information.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Filesys
%perl_vendor_autolib/Filesys

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.92-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.92-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.92-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.92-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.92-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1.1
- rebuilt with perl 5.12

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.92-alt1
- initial build for ALT Linux Sisyphus
