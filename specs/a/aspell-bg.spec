# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lang bg
%define langrelease 0
Summary: Bulgarian dictionaries for Aspell
Name: aspell-%{lang}
#Epoch: 50
Version: 4.1
Release: alt2_18
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source:   http://prdownloads.sourceforge.net/bgoffice/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell libaspell
Requires: aspell libaspell

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Bulgarian

%prep

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure 
%make_build
iconv -f windows-1251 -t utf-8 <bg_phonet.dat >bg_phonet.dat.tmp
mv bg_phonet.dat.tmp bg_phonet.dat


%install
make install DESTDIR=$RPM_BUILD_ROOT
%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_18
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_7
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_5
- update and rebuild with proper aspell datadir

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import

