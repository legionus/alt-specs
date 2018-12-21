#
#   - Best -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 0.11 Best
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Best
%define m_distro Best
%define m_name Best
%define m_author_id GAAL
%define _enable_test 1

Name: perl-Best
Version: 0.15
Release: alt1

Summary: Best - Fallbackable module loader

License: MIT
Group: Development/Perl
Url: http://search.cpan.org/dist/Best/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/G/GA/GAAL/Best-%{version}.tar.gz

# Automatically added by buildreq on Fri Sep 05 2008 (-bi)
BuildRequires: perl-Module-Install perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage

%description
Often there are several possible providers of some functionality your program needs, but you don't know which is available at the run site. For example, one of the modules may be implemented with XS, or not in the core Perl distribution and thus not necessarily installed.

Best attempts to load modules from a list, stopping at the first successful load and failing only if no alternative was found.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Best*
%doc Changes README

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 0.11-alt2
- fix directory ownership violation

* Mon Jul 14 2008 Michael Bochkaryov <misha@altlinux.ru> 0.11-alt1
- first build for ALT Linux Sisyphus

