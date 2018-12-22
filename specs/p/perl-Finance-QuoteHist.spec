%define _unpackaged_files_terminate_build 1
%define dist Finance-QuoteHist
Name: perl-%dist
Version: 1.27
Release: alt1

Summary: Perl module for fetching historical stock quotes
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Finance-QuoteHist/
Source0: http://www.cpan.org/authors/id/M/MS/MSISK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-Date-Manip perl-HTML-TableExtract perl-Regexp-Common perl-Text-CSV perl-Text-CSV_XS perl-devel perl-libwww

%description
Finance::QuoteHist is a top level interface for fetching historical
stock quotes from the web.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Finance

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.12 -> 1.16

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.10 -> 1.12
- hopefully fixed ::Yahoo::splits() parser

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt2
- fix directory ownership violation

* Sun Apr 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- new version 1.10 (with rpmrb script)

* Fri Jan 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.09-alt0.1
- new version 1.09 (with rpmrb script)

* Sun Feb 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt1
- initial build for ALT Linux Sisyphus
