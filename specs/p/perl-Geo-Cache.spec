#
#   - Geo::Cache -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Geo::Cache
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Geo-Cache
%define m_distro Geo-Cache
%define m_name Geo::Cache
%define m_author_id unknown
%define _enable_test 1

Name: perl-Geo-Cache
Version: 0.11
Release: alt1

Summary: Classes for dealing with GeoCaches and the related data files

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Mykola Grechukh <gns@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Thu Oct 14 2010
BuildRequires: perl-Time-modules perl-XML-Simple perl-devel

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
* Thu Oct 14 2010 Mykola Grechukh <gns@altlinux.ru> 0.11-alt1
- initial build for ALT Linux Sisyphus
