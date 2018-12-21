# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/halibut
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global rel 20171202.8a8299e

Name:           agedu
Version:        0
Release:        alt2_15.%{rel}
Summary:        An utility for tracking down wasted disk space
Group:          System/Base
License:        MIT
URL:            http://www.chiark.greenend.org.uk/~sgtatham/agedu/
# Upstream tarball is regenerated nightly, so md5sums will differ.
Source0:        http://www.chiark.greenend.org.uk/~sgtatham/agedu/agedu-%{rel}.tar.gz

BuildRequires:  gcc
Source44: import.info

%description
Agedu is a program that helps you to track down wasted disk space by creating
a graphical representation of last access times and occupied disk space of
files and directories.

%prep
%setup -q -n %{name}-%{rel}


%build
%configure
%make_build


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"



%files
%doc LICENCE TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0-alt2_15.20171202.8a8299e
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt2_13.r9153
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt2_11.r9153
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_10.r9153
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt2_9.r9153
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_8.r9153
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt2_7.r9153
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt2_6.r9153
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt2_5.r9153
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt2_4.r9153
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt2_3.r9153
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_3.r9153
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0-alt1_2.r9153
- initial release by fcimport

