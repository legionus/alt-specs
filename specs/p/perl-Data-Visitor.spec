#
#   - Data::Visitor -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Data-Visitor
%define m_distro Data-Visitor
%define m_name Data::Visitor
%define m_author_id NUFFIN
%def_enable test

Name: perl-Data-Visitor
Version: 0.30
Release: alt2

Summary: %m_name - Visitor style traversal of Perl data structures

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Data-Visitor/

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DO/DOY/Data-Visitor-%{version}.tar.gz

# Automatically added by buildreq on Wed Apr 21 2010 (-bi)
BuildRequires: perl-Moose perl-Task-Weaken perl-Test-use-ok perl-Tie-ToObject perl-namespace-clean
BuildRequires: perl-Tie-RefHash perl(Test/Requires.pm)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- cleanup of BRs

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.15 -> 0.27

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Fri Jun 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.15-alt1
- 0.15 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

