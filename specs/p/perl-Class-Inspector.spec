%define _unpackaged_files_terminate_build 1
%define dist Class-Inspector
Name: perl-%dist
Version: 1.32
Release: alt1

Summary: Get information about a class and its structure
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Pod-Escapes perl-devel

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
aren't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README author.yml
%perl_vendor_privlib/Class

%changelog
* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt1
- 1.25 -> 1.27

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.25-alt2
- disabled build dependency on perl-Module-Install

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 1.25-alt1
- 1.24 -> 1.25

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.23 -> 1.24

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.23-alt1
- new version 1.23 (with rpmrb script)

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- first build for ALT Linux Sisyphus
