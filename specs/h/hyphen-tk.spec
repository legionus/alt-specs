Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hyphen-tk
Summary: Turkmen hyphenation rules
%global upstreamid 20110620
Version: 0.%{upstreamid}
Release: alt1_11
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex?view=co
Source: hyph-tk.tex
URL: http://tug.org/tex-hyphen
License: Public Domain
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-tk-cleantex.patch
Source44: import.info

%description
Turkmen hyphenation rules.

%prep
%setup -T -q -c -n hyphen-tk
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 15 hyph-tk.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_tk_TM.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/hyph_tk_TM.dic

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_9
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass

