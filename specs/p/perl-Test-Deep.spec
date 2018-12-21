%define _unpackaged_files_terminate_build 1
#
#   - Test::Deep -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Test::Deep
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Test-Deep
%define m_distro Test-Deep
%define m_name Test::Deep
%define m_author_id unknown
%define _enable_test 1

Name: perl-Test-Deep
Version: 1.128
Release: alt1

Summary: Test-Deep - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Mikhail Pokidko <pma@altlinux.org>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Mon Dec 08 2008
BuildRequires: perl-Test-NoWarnings perl-Test-Tester

%description
None.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc README TODO Changes
%perl_vendor_privlib/Test/*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.128-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.127-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.126-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.124-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.123-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.120-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.119-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.115-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.114-alt1
- automated CPAN update

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.112-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.108-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.106-alt1
- automated CPAN update

* Mon Dec 08 2008 Mikhail Pokidko <pma@altlinux.org> 0.103-alt1
- initial build for ALT Linux Sisyphus

