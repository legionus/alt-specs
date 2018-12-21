Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-nds
Summary: Lowlands Saxon hunspell dictionaries
Version: 0.1
Release: alt2_14
Source: http://downloads.sourceforge.net/aspell-nds/hunspell-nds-0.1.zip
URL: http://aspell-nds.sourceforge.net/
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Lowlands Saxon hunspell dictionaries.

%prep
%setup -q -n hunspell-nds

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p nds.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.aff
cp -p nds.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
nds_DE_aliases="nds_NL"
for lang in $nds_DE_aliases; do
        ln -s nds_DE.aff $lang.aff
        ln -s nds_DE.dic $lang.dic
done
popd


%files
%doc README_nds.txt Copyright COPYING
%{_datadir}/myspell/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_6
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_4
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_4
- import from Fedora by fcimport

