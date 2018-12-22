%define _unpackaged_files_terminate_build 1
%define dist ExtUtils-Depends
Name: perl-%dist
Version: 0.405
Release: alt1

Summary: Perl module for building XS extensions easily
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/X/XA/XAOC/ExtUtils-Depends-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-devel

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/ExtUtils

%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.405-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.404-alt1
- automated CPAN update

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.403-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.402-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.401-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.400-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.309-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.308-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.307-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.306-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.305-alt1
- automated CPAN update

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.304-alt2
- rebuilt as plain src.rpm

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1
- automated CPAN update

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.302-alt1
- 0.301 -> 0.302

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.301-alt1
- 0.205 -> 0.301

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.205-alt2
- removed manual pages

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.205-alt1
- 0.204 -> 0.205

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.204-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 0.204-alt1
- 0.202 -> 0.204

* Sat May 15 2004 Alexey Tourbin <at@altlinux.ru> 0.202-alt1
- 0.201 -> 0.202

* Wed Feb 18 2004 Alexey Tourbin <at@altlinux.ru> 0.201-alt1
- 0.201

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 0.104-alt1
- 0.104

* Thu Aug 28 2003 Alexey Tourbin <at@altlinux.ru> 0.103-alt1
- initial revision
