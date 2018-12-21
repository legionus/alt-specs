#
#   - Cache-Simple-TimedExpiry -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Cache::Simple::TimedExpiry
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Cache-Simple-TimedExpiry
%define m_distro Cache-Simple-TimedExpiry
%define m_name Cache-Simple-TimedExpiry
%define m_author_id JESSE
%define _enable_test 1

Name: perl-Cache-Simple-TimedExpiry
Version: 0.27
Release: alt2.1

Summary: Cache-Simple-TimedExpiry - A lightweight cache with timed expiration

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/modules/by-module/Cache/%m_distro-%version.tar.bz2

# Automatically added by buildreq on Thu Sep 01 2005
BuildRequires: perl-devel

%description
A lightweight cache with timed expiration.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Cache/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt2
- fix directory ownership violation

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- new version 0.27 (with rpmrb script)

* Thu Sep 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt1
- first build for ALT Linux Sisyphus