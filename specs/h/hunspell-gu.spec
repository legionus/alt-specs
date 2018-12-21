# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-gu
Summary: Gujarati hunspell dictionaries
Version: 20061015 
Release: alt2_11
Source: http://downloads.sourceforge.net/project/openofficeorg.mirror/contrib/dictionaries/gu_IN.zip
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Gujarati hunspell dictionaries.

%prep
%setup -q -c -n gu-IN

%build
chmod -x *.dic *.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_gu_IN.txt
%{_datadir}/myspell/*

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_10
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_8
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_6
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_5
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt2_4
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20061015-alt1_4
- import from Fedora by fcimport

