Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-ts
Summary: Tsonga hunspell dictionaries
%global upstreamid 20110323.1
Version: 0.%{upstreamid}
Release: alt1_1
Source:https://addons.mozilla.org/firefox/downloads/file/376225/tsonga_spell_checker-20110323.1-typefix-fn+sm+tb+fx.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/tsonga-spell-checker/
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tsonga hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ts


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ts-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.aff
cp -p dictionaries/ts-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.dic


%files
%doc README-ts-ZA.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.20110323.1-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20091101-alt1_2
- import from Fedora by fcimport

