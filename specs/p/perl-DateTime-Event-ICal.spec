# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Event-ICal
Version:        0.13
Release:        alt1_8
Summary:        Perl DateTime extension for computing rfc2445 recurrences
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/DateTime-Event-ICal
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Event/Recurrence.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(DateTime/Span.pm)
BuildRequires:  perl(DateTime/SpanSet.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(vars.pm)
# Test suite
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info
# Runtime

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for rfc2445 style recurrences.

%prep
%setup -q -n DateTime-Event-ICal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README TODO
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update to new release by fcimport

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1
- update to new release by fcimport

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_10
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_9
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_9
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7
- fc import

