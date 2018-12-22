# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name	 Clone-PP
%define upstream_version 1.07

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Recursively copy Perl datatypes
License:    Artistic or GPL-1.0-only
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Clone/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Benchmark.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README
%{perl_vendor_privlib}/Clone

%changelog
* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_1
- update by mgaimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_5
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_2
- update by mgaimport

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update by mgaimport

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_1
- update by mgaimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_3
- Sisyphus build

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- converted for ALT Linux by srpmconvert tools

