# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(LWP/Simple.pm) perl(Test/Deep.pm) perl(Test/Pod.pm) perl(Text/Diff.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Filter
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Module-Compile
Version:        0.37
Release:        alt1_2
Summary:        Perl Module Compilation
License:        GPL-1.0-or-later or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Module-Compile
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Compile-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Digest/SHA1.pm)
BuildRequires:  perl(Filter/Util/Call.pm)
# Tests only
BuildRequires:  perl(App/Prove.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Base.pm)
BuildRequires:  perl(Test/Base/Filter.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(YAML.pm)
Requires:       perl(Digest/SHA1.pm) >= 2.130
Requires:       perl(Filter/Util/Call.pm)


Source44: import.info
%filter_from_requires /:__requires_exclude\|}^perl(Digest.SHA1\\)$/d

%description
This module provides a system for writing modules that compile other
Perl modules.

%prep
%setup -q -n Module-Compile-%{version}
rm -rf inc/ && sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_2
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_1
- update to new release by fcimport

* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2
- to Sisyphus as perl-PDL dep

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- regenerated from template by package builder

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
fixed requires

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- initial import by package builder

