%define dist CatalystX-Component-Traits
Name: perl-%dist
Version: 0.19
Release: alt1

Summary: Automatic Trait Loading and Resolution for Catalyst Components
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/CatalystX-Component-Traits-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Jan 22 2011
BuildRequires: perl-Catalyst-Devel perl-MooseX-Traits-Pluggable perl-Test-Pod

%description
Adds a Catalyst::Component/COMPONENT method to your Catalyst component
base class that reads the optional traits parameter from app and component
config and instantiates the component subclass with those traits using
MooseX::Traits/new_with_traits from MooseX::Traits::Pluggable.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CatalystX*

%changelog
* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sat Jan 22 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- 0.14 -> 0.16

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- initial revision
