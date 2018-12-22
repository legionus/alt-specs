%define dist Text-Iconv
Name: perl-%dist
Version: 1.7
Release: alt4.1.1.1.1

Summary: Perl interface to iconv(3) codeset conversion function
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Requires: iconv

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module provides a Perl interface to the iconv(3) codeset
conversion function, as defined by the Single UNIX Specification.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.7-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.7-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.7-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.7-alt2.2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.7-alt2.1
- rebuilt with perl 5.12

* Tue Aug 12 2008 Alexey Tourbin <at@altlinux.ru> 1.7-alt2
- added dependency on iconv (#15162)

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.7-alt1
- 1.4 -> 1.7

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.4-alt1.1.0
- Automated rebuild.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.4-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- 1.3 -> 1.4

* Wed Jun 30 2004 Alexey Tourbin <at@altlinux.ru> 1.3-alt1
- 1.2 -> 1.3

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt1
- Initial release for ALT
