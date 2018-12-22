# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		accrete
Version:	1.0
Release:	alt2_17
Summary:	Accrete is a physical simulation of solar system planet formation

License:	ALT-Public-Domain
Group:		Engineering
URL:		http://sourceforge.net/projects/accrete
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		accrete-1.0-savetofile.patch
Source44: import.info


%description
Accrete is a physical simulation of solar system planet formation,
by modelling a dust cloud around a Sun-like star, injecting a series
of masses which collect dust, and form planets. The simulation then
determines what the planetary environments will be like in terms
of temperature, atmospheric composition, and other factors.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p2 -b .filetosave

%build
make 'CFLAGS=%{optflags}' %{_smp_mflags}

%install
install -Dm 755 accrete $RPM_BUILD_ROOT%{_bindir}/accrete

%files
%doc README ChangeLog
%{_bindir}/accrete

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- initial release by fcimport

