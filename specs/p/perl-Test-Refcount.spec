# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(B.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Symbol.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-Refcount
Version:        0.08
Release:        alt1_12
Summary:        Assert reference counts on objects

Group:          Development/Other
License:        GPL-1.0-or-later or Artistic
URL:            https://metacpan.org/release/Test-Refcount
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Refcount-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Devel/Refcount.pm)
# Test suite fails with Perl 5.18 if Devel::FindRef is installed (CPAN RT#85998)
#BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
Source44: import.info

%description
The Perl garbage collector uses simple reference counting during the normal
execution of a program. This means that cycles or unweakened references in
other parts of code can keep an object around for longer than intended. To
help avoid this problem, the reference count of a new object from its class
constructor ought to be 1. This way, the caller can know the object will be
properly DESTROYed when it drops all of its references to it.


%prep
%setup -q -n Test-Refcount-%{version}


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/Test


%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_8
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- update to new release by fcimport

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2_11
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_11
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_5
- fc import

