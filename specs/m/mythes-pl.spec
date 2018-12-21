Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-pl
Summary: Polish thesaurus
Version: 1.5
Release: alt1_20
Source: httip://downloads.sourceforge.net/synonimy/OOo2-Thesaurus-%{version}.zip
# URL is dead now, please don't file bugs to fix it
URL: http://synonimy.ux.pl/
License: LGPLv2
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Polish thesaurus.

%prep
%setup -q -c


%build
for i in README_th_pl_PL_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_pl_PL_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README_th_pl_PL_v2.txt
%{_datadir}/mythes/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_20
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_19
- update to new release by fcimport

* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_10
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6
- import by fcmass

