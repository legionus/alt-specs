%define _unpackaged_files_terminate_build 1
%define module Lingua-EN-NameParse

Name: perl-%module
Version: 1.38
Release: alt1

Summary: Routines for manipulating a person's name
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/K/KI/KIMRYAN/%{module}-%{version}.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Tue Jul 06 2010
BuildRequires: perl-Parse-RecDescent perl-Test-Pod perl-Test-Pod-Coverage

%description
This module takes as input a person or persons name in
free format text such as,
    Mr AB & M/s CD MacNay-Smith
    MR J.L. D'ANGELO
    Estate Of The Late Lieutenant Colonel AB Van Der Heiden
and attempts to parse it.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc surname_prefs.txt Changes README examples
%perl_vendor_privlib/Lingua

%changelog
* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.30-alt1
- 1.30

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.29-alt1
- 1.29

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 06 2010 Victor Forsiuk <force@altlinux.org> 1.27-alt1
- 1.27

* Thu Jan 10 2008 Victor Forsyuk <force@altlinux.org> 1.24-alt1
- 1.24

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 1.23-alt1
- 1.23
- Actually this is noarch package.
- Spec cleanups.

* Tue Aug 16 2005 Maxim Tkachenko <tma@altlinux.ru> 1.22-alt1
- Update version to 1.22.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.18-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Jul 28 2004 Maxim Tkachenko <tma@altlinux.ru> 1.18-alt1
- build for AltLinux
