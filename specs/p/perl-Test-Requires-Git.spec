%define _unpackaged_files_terminate_build 1
%define module_name Test-Requires-Git
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Git/Version/Compare.pm) perl(List/Util.pm) perl(Pod/Coverage/TrustPod.pm) perl(Scalar/Util.pm) perl(Test/Builder/Module.pm) perl(Test/CPAN/Meta.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.008
Release: alt1
Summary: Check your test requirements against the available version of Git
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/B/BO/BOOK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/T*

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.008-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1
- automated CPAN update

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1.1
- to Sisyphus

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- regenerated from template by package builder

* Sun Mar 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- regenerated from template by package builder

* Fri May 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- initial import by package builder

