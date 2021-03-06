#
#   - SQL::Abstract::Limit -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module SQL-Abstract-Limit
%define m_distro SQL-Abstract-Limit
%define m_name SQL::Abstract::Limit
%define m_author_id unknown
%def_enable test

Name: perl-SQL-Abstract-Limit
Version: 0.141
Release: alt2.1

Summary: %m_name - portable LIMIT emulation

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/SQL-Abstract-Limit/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Apr 12 2010 (-bi)
BuildRequires: perl-DBI perl-Module-Build perl-SQL-Abstract perl-Test-Deep perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage

%description
Portability layer for LIMIT emulation.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/SQL*
%doc Changes README

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.141-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.141-alt2
- updated build dependencies

* Sun Nov 08 2009 Michael Bochkaryov <misha@altlinux.ru> 0.141-alt1
- 0.141 version

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.12-alt2
- fix directory ownership violation

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus

