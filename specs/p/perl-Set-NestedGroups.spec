#
#   - Set::NestedGroups -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' http://search.cpan.org/CPAN/authors/id/A/AB/ABARCLAY/Set-NestedGroups-0.01.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Set-NestedGroups
%define m_distro Set-NestedGroups
%define m_name Set::NestedGroups
%define m_author_id ABARCLAY
%define _enable_test 1

Name: perl-Set-NestedGroups
Version: 0.01
Release: alt1

Summary: grouped data eg ACL's, city/state/country etc

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABARCLAY/%m_distro-%version.tar.gz

# Automatically added by buildreq on Tue Oct 12 2010
BuildRequires: perl-devel

%description
Set::NestedGroups gives an implementation of nested groups,
access control lists (ACLs) would be one example of
nested groups.

For example, if Joe is a Manager, and Managers have access to payroll,
you can create an ACL which implements these rules, then ask the ACL
if Joe has access to payroll.

Another example, you may wish to track which city, state and country
people are in, by adding people to cities, cities to states, and states
to countries.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Set/*

%changelog
* Tue Oct 12 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
