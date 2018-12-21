%define _unpackaged_files_terminate_build 1
#
#   - Class::Gomor -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Class::Gomor
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-Gomor
%define m_distro Class-Gomor
%define m_name Class::Gomor
%define m_author_id unknown
%define _enable_test 1

Name: perl-Class-Gomor
Version: 1.03
Release: alt1

Summary: another class and object builder

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/G/GO/GOMOR/Class-Gomor-%{version}.tar.gz

# Automatically added by buildreq on Sat Nov 07 2009
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl(Module/Build.pm)

%description
This module is yet another class builder. This one adds parameter checking in new constructor, that is to check for attributes existence, and definedness.

In order to validate parameters, the module needs to find attributes, and that is the reason for declaring attributes in global variables named @AS, @AA, @AO. They respectively state for Attributes Scalar, Attributes Array and Attributes Other. The last one is used to avoid autocreation of accessors, that is to let you declare your own ones.

Attribute validation is performed by looking at classes hierarchy, by following @ISA tree inheritance.

The loss in speed by validating all attributes is quite negligeable on a decent machine (Pentium IV, 2.4 GHz) with Perl 5.8.x. But if you want to avoid checking, you can do it, see below.

This class is the base class for Class::Gomor::Array and Class::Gomor::Hash, so they will inherite the following methods.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Class/*

%changelog
* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Nov 07 2009 Denis Smirnov <mithraen@altlinux.ru> 1.02-alt1
- initial build for ALT Linux Sisyphus
