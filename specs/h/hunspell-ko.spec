Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.7.0
Release: alt1_5
Source: https://github.com/spellcheck-ko/hunspell-dict-ko/archive/%{version}.tar.gz
URL: https://github.com/spellcheck-ko/hunspell-dict-ko
License: MPLv1.1 or GPLv2 or LGPLv2
BuildArch: noarch
BuildRequires: python3
BuildRequires: hunspell
Requires: hunspell
Source44: import.info

%description
Korean hunspell dictionaries.

%prep
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.dic

%check
make test

%files
%doc README.md
%doc --no-dereference LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/myspell/*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- update to new release by fcimport

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1_2
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1_1
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.5-alt1_1
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_1
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_1
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- import from Fedora by fcimport

