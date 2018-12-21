Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global pkgname Tie-Function

Name:           perl-Tie-Function
Version:        0.02
Release:        alt1_15
Summary:        Wrap functions in tied hash sugar
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tie-Function
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDNICO/handy_tied_functions/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Test.pm)
Requires:       perl(warnings.pm)
Source44: import.info

%description
Tie::Function simplifies wrapping functions in tied hash syntax so they can
be interpolated in double-quoted literals without messy intermediate
variables.

%prep
%setup -qn %{pkgname}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_15
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_11
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_9
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

