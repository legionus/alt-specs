%define dist Term-Size
Name: perl-%dist
Version: 0.209
Release: alt1

Summary: Perl module for get the size of the terminal
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/F/FE/FERREIRA/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod

%description
Term::Size is a Perl module which provides a straightforward way to get
the size of the terminal (or window) on which a script is running.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README Copyright
%perl_vendor_archlib/Term
%perl_vendor_autolib/Term

%changelog
* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.209-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.207-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.207-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.207-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.207-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.207-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.207-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.207-alt1.2
- rebuilt with perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.207-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.207-alt1
- automated CPAN update

* Wed Mar 02 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt1
- First build for Sisyphus

