Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-bg
Summary: Bulgarian hyphenation rules
Version: 4.3
Release: alt1_12
Source: http://downloads.sourceforge.net/bgoffice/OOo-hyph-bg-%{version}.zip
URL: http://bgoffice.sourceforge.net/
License: GPL-2.0-or-later or LGPLv2+ or MPL-1.1
BuildArch: noarch

Requires: libhyphen
Source44: import.info

%description
Bulgarian hyphenation rules.

%prep
%setup -q -n OOo-hyph-bg-%{version}

%build
for i in ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
echo "UTF-8" > hyph_bg_BG.dic.new
tail -n +2 hyph_bg_BG.dic | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> hyph_bg_BG.dic.new
mv hyph_bg_BG.dic.new hyph_bg_BG.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/hyphen/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_2
- import by fcmass

