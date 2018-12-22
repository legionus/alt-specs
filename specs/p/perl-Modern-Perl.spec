Epoch: 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Modern-Perl
Version:        1.20181021
Release:        alt1_1
Summary:        Enable all of the features of Modern Perl with one command
License:        GPL-1.0-or-later or Artistic
URL:            https://metacpan.org/release/Modern-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel >= 5.10.0
BuildRequires:  perl(autodie.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(mro.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(autodie.pm) >= 2.220
Source44: import.info
Provides: perl(Modern/Perl.pm) = 2012.0

%description
Modern Perl often relies on the presence of several core and CPAN pragmas
and modules.  Wouldn't it be nice to use them all with a single command?

%prep
%setup -q -n Modern-Perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/Modern/

%changelog
* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20181021-alt1_1
- update to new release by fcimport

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20181021-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20180928-alt1_1
- update to new release by fcimport

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20180928-alt1
- automated CPAN update

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20180901-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20180701-alt1_2
- update to new release by fcimport

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20180701-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.20170117-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.20170117-alt1_2
- update to new release by fcimport

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.20170117-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.20161229-alt1
- automated CPAN update

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.20161005-alt1_1
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1_3
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.20140107-alt1
- automated CPAN update

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.20121103-alt1_1
- update to new release by fcimport

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.20121103-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.03-alt1_7
- added provides

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121103-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2
- fc import

