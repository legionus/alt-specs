Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-ast
Summary: Asturian hunspell dictionaries
#Epoch: 1
Version: 0.02
Release: alt1_15
# Following link is dead now, don't report any bugs
Source: http://extensions.services.openoffice.org/e-files/3932/1/asturianu.oxt
URL: http://softastur.org/
License: GPLv3+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Asturian hunspell dictionaries.

%prep
%setup -q -c


%build
chmod -x dictionaries/*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ast.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.aff
cp -p dictionaries/ast.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ast_ES.dic


%files
%doc LICENSES-en.txt LICENCES-ast.txt
%{_datadir}/myspell/*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_14
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update to new release by fcimport

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- import from Fedora by fcimport

