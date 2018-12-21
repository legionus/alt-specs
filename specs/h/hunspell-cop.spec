Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-cop
Summary: Coptic hunspell dictionaries
Version: 0.3
Release: alt2_13
Source: http://www.moheb.de/download/dict-cop_EG_v03.oxt
URL: http://www.moheb.de/coptic_oo.html
License: GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Coptic hunspell dictionaries.

%prep
%setup -q -c


%build
for i in README.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p cop_EG-Bohairic/cop_EG.* $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc README.txt
%doc --no-dereference license-gpl.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_9
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_2
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_1
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_1
- import from Fedora by fcimport

