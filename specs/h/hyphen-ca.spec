Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-ca
Summary: Catalan hyphenation rules
#Epoch: 1
Version: 0.9.3
Release: alt1_15
Source: https://downloads.sourceforge.net/project/aoo-extensions/2010/7/hyph-ca.oxt
URL: http://extensions.services.openoffice.org/project/ca_hyph
License: GPLv3
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Catalan hyphenation rules.

%prep
%setup -q -c


%build
for i in release-note_en.txt release-note_ca.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ca_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ca_ES.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s hyph_ca_ES.dic hyph_$lang.dic
done
popd


%files
%doc release-note_en.txt release-note_ca.txt LICENSES-en.txt LLICENCIES-ca.txt
%{_datadir}/hyphen/*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_14
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_2
- import by fcmass

