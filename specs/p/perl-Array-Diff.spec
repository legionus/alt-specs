# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Filter/Util/Call.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Test/Deep.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(threads/shared.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Only need manual requires for "use base XXX;" prior to rpm 4.9
%global rpm49 0

Name:           perl-Array-Diff
Version:        0.07
Release:        alt2_28
# Because 0.07 compares newer than 0.05002 in Perl world
# but not in RPM world :-(
Epoch:          1
Summary:        Find the differences between two arrays
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Array-Diff
Source0:        https://cpan.metacpan.org/authors/id/T/TY/TYPESTER/Array-Diff-%{version}.tar.gz
Patch0:         Array-Diff-0.07-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(vars.pm)
# Module Runtime
BuildRequires:  perl(Algorithm/Diff.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(MIME/Base64.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(PerlIO.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Text/Diff.pm)
# Dependencies
%if ! %{rpm49}
Requires:       perl(Class/Accessor/Fast.pm)
%endif
Source44: import.info

%description
This module compares two arrays and returns the added or deleted elements in
two separate arrays. It's a simple wrapper around Algorithm::Diff.

If you need more complex array tools, check Array::Compare.

%prep
%setup -q -n Array-Diff-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%doc --no-dereference LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%dir %{perl_vendor_privlib}/Array/
%{perl_vendor_privlib}/Array/Diff.pm

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_28
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_27
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_26
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_25
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_22
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_21
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_15
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_14
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_13
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_9
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_7
- fc import

