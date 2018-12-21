# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-ExtUtils-CppGuess
Version:        0.12
Release:        alt1_4
Summary:        Guess C++ compiler and flags
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/ExtUtils-CppGuess
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(Fatal.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(XSLoader.pm)
Source44: import.info

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%setup -q -n ExtUtils-CppGuess-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/ExtUtils*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_4
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3
- update to new release by fcimport

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- update to new release by fcimport

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

