Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-lt
Summary: Lithuanian hunspell dictionaries
Version: 1.2.1
Release: alt2_18
## Note that upstream is dead and there is no download link available
## so please don't report FTBFS bugs for this package.
Source: ftp://ftp.akl.lt/ispell-lt/lt_LT-%{version}.zip
URL: ftp://ftp.akl.lt/ispell-lt/
License: BSD
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lithuanian hunspell dictionaries.

%prep
%setup -q -n lt_LT-%{version}


%build
chmod -x *
for i in INSTRUKCIJOS.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc README.EN INSTRUKCIJOS.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_6
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6
- import from Fedora by fcimport

