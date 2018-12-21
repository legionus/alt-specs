%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Module/Build.pm)
#
#   - MooseX-Types-LoadableClass -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' --no-depchk --url http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MooseX-Types-LoadableClass-0.006.tar.gz http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MooseX-Types-LoadableClass-0.006.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module MooseX-Types-LoadableClass
%define m_distro MooseX-Types-LoadableClass
%define m_name MooseX-Types-LoadableClass
%define m_author_id unknown
%define _disable_test 1

Name: perl-MooseX-Types-LoadableClass
Version: 0.015
Release: alt1

Summary: ClassName type constraint with coercion to load the class

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MooseX-Types-LoadableClass-0.006.tar.gz

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Thu Sep 29 2011
BuildRequires: perl-Class-Load perl-Pod-Escapes perl-devel perl-namespace-clean perl-MooseX-Types perl-Moose


%description
use Moose::Util::TypeConstraints;

    my $tc = subtype as ClassName;
    coerce $tc, from Str, via { Class::MOP::load_class($_); $_ };

I've written those three lines of code quite a lot of times, in quite
a lot of places.

Now I don't have to.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX*

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1.1
- rebuild to restore role requires

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial build for ALT Linux Sisyphus
