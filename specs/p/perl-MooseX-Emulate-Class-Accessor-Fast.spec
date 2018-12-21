%define dist MooseX-Emulate-Class-Accessor-Fast
Name: perl-%dist
Version: 0.009032
Release: alt1

Summary: Emulate Class::Accessor::Fast behavior using Moose attributes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-Moose perl-Test-Exception perl-namespace-clean

%description
This module attempts to hijack Class::Accessor::Fast in INC and replace
it with MooseX::Emulate::Class::Accessor::Fast. Make sure it is loaded
before the classes you have that use Class::Accessor::Fast. It is meant
as a tool to help you migrate your project from Class::Accessor::Fast,
to MooseX::Emulate::Class::Accessor::Fast and ultimately, to Moose.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.009032-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.00903-alt1.1
- rebuild to restore role requires

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.00903-alt1
- initial revision, for Catalyst
