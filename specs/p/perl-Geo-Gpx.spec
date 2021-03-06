#
#   - Geo::Gpx -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Geo::Gpx --version 0.26
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Geo-Gpx
%define m_distro Geo-Gpx
%define m_name Geo::Gpx
%define m_author_id unknown
%define _enable_test 1

Name: perl-Geo-Gpx
Version: 0.26
Release: alt1

Summary: Geo-Gpx - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Mykola Grechukh <gns@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Tue Oct 12 2010
BuildRequires: perl-DateTime-Format-ISO8601 perl-HTML-Parser perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-XML-Descent

%description
None.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Geo/*

%changelog
* Tue Oct 12 2010 Mykola Grechukh <gns@altlinux.ru> 0.26-alt1
- initial build for ALT Linux Sisyphus

