# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define lang nb
%define langrelease 0
Summary: Norwegian dictionaries for Aspell
Name: aspell-no
#Epoch: 50
Version: 0.50.1
Release: alt3_29
License: GPLv2
Group: Text tools
URL: http://aspell.net/
Source: ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell-%{lang}-%{version}-%{langrelease}.tar.bz2
Patch: aspell-nb-0.50.1-0.utf-filename.patch
Buildrequires: aspell libaspell
Requires: aspell libaspell

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Norwegian

%prep
%setup -q -n aspell-%{lang}-%{version}-%{langrelease}
%patch -p1 -b .utf-filename
cp bokmal.alias bokmål.alias

%build
./configure
make

%install
make install  DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_29
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_27
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_25
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_24
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_20
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_19
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_18
- update to new release by fcimport

* Sun Feb 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_17
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt3_16
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt2_16
- update and rebuild with proper aspell datadir

* Wed Apr 30 2008 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt2
- fixed rebuild

* Wed Jan 31 2007 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt1
- first build for Sisyphus
- imported from FC6 by aspell-import

