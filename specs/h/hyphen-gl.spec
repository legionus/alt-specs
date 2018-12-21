Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-gl
Summary: Galician hyphenation rules
Version: 0.99
Release: alt1_15
Source: https://forxa.mancomun.org/frs/download.php/534/hyph_gl.oxt
URL: https://forxa.mancomun.org/projects/hyphenation-gl
License: GPLv3
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Galician hyphenation rules.

%prep
%setup -q -c -n hyphen-gl


%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_gl_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_gl_ES.dic


%files
%doc LEME-gl_ANY.txt LICENCES-gl.txt LICENSES-en.txt  
%{_datadir}/hyphen/*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_11
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_9
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_3
- import by fcmass

