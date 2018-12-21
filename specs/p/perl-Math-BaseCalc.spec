# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Math-BaseCalc
%define upstream_version 1.019

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    %{upstream_name} perl module
License:    GPL or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Config.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(integer.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl-CPAN perl-Digest-SHA perl-Encode perl-Encode-devel perl-JSON-PP perl-Module-CoreList perl-Pod-Checker perl-Pod-Parser perl-Pod-Usage perl-devel
BuildArch:  noarch
Source44: import.info

%description
This module facilitates the conversion of numbers between various
number bases.  You may define your own digit sets, or use any of
several predefined digit sets.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build

CFLAGS="$RPM_OPT_FLAGS" /usr/bin/perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make
make test

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT 

%files 
%doc Changes LICENSE META.yml README SIGNATURE
%{perl_vendor_privlib}/Math/*

%changelog
* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.019-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.019-alt1_1
- update by mgaimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.019-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.017-alt2_6
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.017-alt2_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.017-alt2_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.017-alt2_3
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.017-alt2_2
- moved to Sisyphus

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.017-alt1_2
- mga update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.017-alt1_1
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.016-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.016-alt1_1
- converted for ALT Linux by srpmconvert tools

