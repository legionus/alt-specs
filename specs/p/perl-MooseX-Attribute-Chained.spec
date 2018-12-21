# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/CPAN/Changes.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Warnings.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-Attribute-Chained
Version:        1.0.3
Release:        alt1_6
Summary:        Attribute that returns the instance to allow for chaining
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/MooseX-Attribute-Chained
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOMHUKINS/MooseX-Attribute-Chained-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Script.pm)
BuildRequires:  perl(Try/Tiny.pm)
# for release testing, but they mostly fail
#BuildRequires:  perl(Pod::Coverage::TrustPod)
#BuildRequires:  perl(Test::HasVersion)
#BuildRequires:  perl(Test::Kwalitee)
#BuildRequires:  perl(Test::MinimumVersion)
#BuildRequires:  perl(Test::Pod)
#BuildRequires:  perl(Test::Pod::Coverage)
#BuildRequires:  perl(Test::Portability::Files)

# renamed from perl-MooseX-ChainedAccessors in January 2012
# no explicit provides necessary as this package still contains the old classes
# and rpm automatically detects them
Obsoletes:      perl-MooseX-ChainedAccessors <= 0.02-3.fc17


Source44: import.info

%description
MooseX::Attribute::Chained is a Moose Trait which allows for method
chaining on accessors by returning $self on write/set operations.

%prep
%setup -q -n MooseX-Attribute-Chained-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- update to new release by fcimport

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1.1
- rebuild to restore role requires

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_4
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- fc import

