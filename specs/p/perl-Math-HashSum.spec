#
#   - Math::HashSum -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Math::HashSum
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Math-HashSum
%define m_distro Math-HashSum
%define m_name Math::HashSum
%define m_author_id unknown
%define _enable_test 1

Name: perl-Math-HashSum
Version: 0.02
Release: alt2.1

Summary: Sum a list of key-value pairs on a per-key basis

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/S/SP/SPLICE/%m_distro-%version.tar.bz2

# Automatically added by buildreq on Tue Jun 17 2008
BuildRequires: perl-devel

%description
This module allows you to sum a list of key-value pairs on a per-key basis.
It adds up all the values associated with each key in the given list and
returns a hash containing the sum associated with each key.

The example in the synopsis should explain usage of the module effectively.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Math/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for ALT Linux Sisyphus

