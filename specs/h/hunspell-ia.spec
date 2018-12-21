Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-ia
Summary: Interlingua hunspell dictionaries
%global upstreamid 20050226
Version: 0.%{upstreamid}
Release: alt2_15
Source: http://download.savannah.gnu.org/releases/interlingua/ia_myspell.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Interlingua_.28x-register.29
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Interlingua hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < README_ia.txt > README_ia.txt.new
touch -r README_ia.txt README_ia.txt.new
mv -f README_ia.txt.new README_ia.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ia.* $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc README_ia.txt
%{_datadir}/myspell/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050226-alt1_5
- import from Fedora by fcimport

