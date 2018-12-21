#
#   - Text::vFile::asData -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Text::vFile::asData --version 0.05
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-vFile-asData
%define m_distro Text-vFile-asData
%define m_name Text::vFile::asData
%define m_author_id RCLAMP
%define _enable_test 1

Name: perl-Text-vFile-asData
Version: 0.08
Release: alt1

Summary: Text-vFile-asData - Perl module

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://www.cpan.org/authors/id/R/RC/RCLAMP/Text-vFile-asData-%{version}.tar.gz

# Automatically added by buildreq on Sun Jun 22 2008
BuildRequires: perl-Class-Accessor-Chained perl-Module-Build perl-Test-Pod

%description
Text::vFile::asData reads vFile format files,
such as vCard (RFC 2426) and vCalendar (RFC 2445).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Text/vFile/*

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Dec 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt2
- cleanup spec
- fix directory ownership violation
- disable man packaging
- change packager

* Sun Jun 22 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus
