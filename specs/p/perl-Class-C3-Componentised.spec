%define _unpackaged_files_terminate_build 1
%define dist Class-C3-Componentised
Name: perl-%dist
Version: 1.001002
Release: alt2

Summary: Load mix-ins or components to your C3-based class.

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{dist}-%{version}.tar.gz

BuildRequires: perl-Class-C3 perl-Class-C3-XS perl-Class-Inspector perl-MRO-Compat perl-Module-Install perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage

%description
Load mix-ins or components to your C3-based class.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class/C3/Componentised.pm
%dir %perl_vendor_privlib/Class/C3/Componentised
%perl_vendor_privlib/Class/C3/Componentised/ApplyHooks.pm

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt2
- unpackaged files fixed

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.001000-alt1
- automated CPAN update

* Tue Dec 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0006-alt2
- Added perl-Class-C3 to buildrequires to fix build
- Spec cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.0006-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 1.0006-alt1
- 1.0003 -> 1.0006

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 1.0003-alt2
- fix directory ownership violation

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 1.0003-alt1
- first build for ALT Linux Sisyphus

