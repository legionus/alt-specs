# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Imager.pm) perl(Math/Complex.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Math-Symbolic
Version:        0.612
Release:        alt2_14
Summary:        Symbolic calculations
License:        GPL-1.0-or-later or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Math-Symbolic
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Math-Symbolic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Memoize.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Parse/RecDescent.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(Memoize.pm) >= 1.010

# RPM 4.9 style:

Source44: import.info
%filter_from_requires /perl(Memoize\\)$/d

%description
Math::Symbolic is intended to offer symbolic calculation capabilities to
the Perl programmer without using external (and commercial) libraries
and/or applications.

%prep
%setup -q -n Math-Symbolic-%{version}
for file in Changes README `find lib -name '*.pm'`; do
  iconv -flatin1 -tutf8 < $file > $file.utf8
  touch -r $file $file.utf8
  mv $file.utf8 $file
done
chmod -c a-x examples/*

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README TODO Yapp.yp examples
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_14
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_10
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_9
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_4
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.612-alt2_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.612-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.612-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.612-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.609-alt1_1
- update to new release by fcimport

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.606-alt1_8
- update from fc import

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.606-alt1_7
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.606-alt1_5
- fc import

