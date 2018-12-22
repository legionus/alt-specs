# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-Reporter
Version:        1.62
Release:        alt1_10
Summary:        Sends test results to cpan-testers@perl.org
License:        GPL-1.0-or-later or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Test-Reporter
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Reporter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(FileHandle.pm)
# Mail::Send is optional
# Net::DNS is optional
# Net::Domain is optional
# Net::SMTP is optional
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(Time/Local.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Optional tests:
# CPAN::Meta not useful

%description
Test::Reporter reports the test results of any given distribution to the
CPAN Testers project. Test::Reporter has wide support for various perl5's
and platforms.

%prep
%setup -q -n Test-Reporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_10
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_6
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1_3
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.60-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.60-alt2_2
- update to new release by fcimport

* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 1.60-alt2_1
- moved to Sisyphus as dependency

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.58-alt2_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.58-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.58-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1_1
- fc import

