Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-haw
Summary: Hawaiian hunspell dictionaries
Version: 0.03
Release: alt1_1
Source: https://addons.mozilla.org/firefox/downloads/file/248540/hawaiian_spell_checker-%{version}-tb+fx+fn+sm.xpi
URL: http://borel.slu.edu/crubadan/
License: GPLv2+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Hawaiian hunspell dictionaries.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/haw-US.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/haw.aff
cp -p dictionaries/haw-US.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/haw.dic


%files
%doc dictionaries/README_haw_US.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_9
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- update to new release by fcimport

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_1
- initial fedora import

