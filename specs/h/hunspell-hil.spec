Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-hil
Summary: Hiligaynon hunspell dictionaries
#Epoch: 1
Version: 0.14
Release: alt2_15
Source: https://addons.mozilla.org/firefox/downloads/file/108895/litreoir_hiligaynon-%{version}-tb+fx+sm.xpi
URL: http://extensions.services.openoffice.org/project/hunspell-hil
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Hiligaynon hunspell dictionaries.

%prep
%setup -q -c


%build
for i in dictionaries/README_hil_PH.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/hil.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/hil_PH.dic
cp -p dictionaries/hil.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/hil_PH.aff


%files
%doc dictionaries/README_hil_PH.txt
%{_datadir}/myspell/*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_14
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- import from Fedora by fcimport

