Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-tpi
Summary: Tok Pisin hunspell dictionaries
Version: 0.07
Release: alt1_10
Source: https://downloads.sourceforge.net/project/aoo-extensions/4824/3/hunspell-tpi-0.07.oxt
URL: http://extensions.services.openoffice.org/en/project/tok-pisin-spell-checker
License: GPLv3+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Tok Pisin hunspell dictionaries.

%prep
%setup -q -c


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/tpi_PG.* $RPM_BUILD_ROOT/%{_datadir}/myspell


%files
%doc dictionaries/README_tpi_PG.txt
%doc --no-dereference LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- initial release by fcimport

