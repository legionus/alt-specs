# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global lang fi
%global langrelease 0
Summary: Finnish dictionaries for Aspell
Name: aspell-%{lang}
Version: 0.7
Release: alt1_9
License: GPLv2
Group: Text tools
URL: http://aspell.net
Source: http://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 0.60
Requires: aspell >= 0.60

%define debug_package %{nil}
Source44: import.info

%description
Provides the word list/dictionaries for the following: Finnish

%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure 
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING Copyright 
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_7
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4
- update to new release by fcimport

* Fri Jun 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- converted for ALT Linux by srpmconvert tools

