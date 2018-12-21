# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Devel/TimeThis.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Math-Prime-XS
Version:        0.27
Release:        alt1.1_7
Summary:        Detect and calculate prime numbers with deterministic tests
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Math-Prime-XS
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
# XXX BuildRequires:  perl(File::HomeDir)
# XXX BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
Math::Prime::XS detects and calculates prime numbers by either applying
Modulo operator division, the Sieve of Eratosthenes, a Summation
calculation or Trial division.

%prep
%setup -q -n Math-Prime-XS-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete

# %{_fixperms} %{buildroot}/*

%check
./Build test


%files
%doc Changes devel META.json README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Math*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1_7
- update to new release by fcimport

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1_5.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1_2
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_15
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_14.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_14
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_12.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_10
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt3_9
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.26-alt2_9
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_7
- initial fc import

