#
#   - Class::Member -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Class::Member
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-Member
%define m_distro Class-Member
%define m_name Class::Member
%define m_author_id unknown
%define _enable_test 1

Name: perl-Class-Member
Version: 1.6
Release: alt1

Summary: A set of modules to make the module developement easier

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Baranov <baraka@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Thu Mar 10 2011 (-bi)
BuildRequires: perl-devel

%description
none.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/*

%changelog
* Thu Mar 10 2011 Denis Baranov <baraka@altlinux.ru> 1.6-alt1
- initial build for ALT Linux Sisyphus
