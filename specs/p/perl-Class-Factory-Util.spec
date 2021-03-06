#
#   - Class::Factory::Util -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Class::Factory::Util --version 1.7
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-Factory-Util
%define m_distro Class-Factory-Util
%define m_name Class::Factory::Util
%define m_author_id unknown
%define _enable_test 1

Name: perl-Class-Factory-Util
Version: 1.7
Release: alt2.1

Summary: Class-Factory-Util - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY//%m_distro-%version.tar.bz2

# Automatically added by buildreq on Tue Jun 17 2008
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Base class for dynamic factory classes.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/Class/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- initial build for ALT Linux Sisyphus

