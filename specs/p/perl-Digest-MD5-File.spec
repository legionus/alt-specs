#
#   - Digest::MD5::File -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Digest::MD5::File
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Digest-MD5-File
%define m_distro Digest-MD5-File
%define m_name Digest::MD5::File
%define m_author_id unknown
%define _enable_test 1

Name: perl-Digest-MD5-File
Version: 0.08
Release: alt1

Summary: Perl extension for getting MD5 sums for files and urls

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DM/DMUEY/Digest-MD5-File-%{version}.tar.gz

# Automatically added by buildreq on Sat Sep 04 2010
BuildRequires: perl-devel perl-libwww

%description
Get MD5 sums for files of a given path or content of a given url.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Digest/*

%changelog
* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

