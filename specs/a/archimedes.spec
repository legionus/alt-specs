# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dvipdf /usr/bin/dvips /usr/bin/latex gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	2D Quantum Monte Carlo simulator for semiconductor devices
Name:		archimedes
Version:	2.0.1
Release:	alt1_11
License:	GPLv3+
Group:		Engineering
URL:		http://www.gnu.org/software/archimedes/
Source0:	ftp://ftp.gnu.org/gnu/archimedes/%{name}-%{version}.tar.gz

BuildRequires:	dos2unix
Source44: import.info

%description
Archimedes is a package for the design and simulation of submicron
semiconductor devices. It is a 2D Fast Monte Carlo simulator which can take
into account all the relevant quantum effects, thank to the implementation of
the Bohm effective potential method.

The physics and geometry of a general device is introduced by typing a simple
script, which makes, in this sense, Archimedes a powerful tool for the
simulation of quite general semiconductor devices.

%prep
%setup -q


# Use tests as user examples
mv tests/ examples/
rm -rf examples/*/.log

# Suppress rpmlint errors
dos2unix COPYING doc/* doc/*/*
# Fix spurious-executable-perm warning
chmod 644 doc/*/*

# gcc-7 compatibility (F26FTBFS)
sed -i -e 's,inline,static inline,' src/random.h


%build
%configure
%make_build


%install
%makeinstall_std


%files
%{_bindir}/%{name}
%doc AUTHORS ChangeLog doc examples NEWS README THANKS
%doc --no-dereference COPYING

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_11
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_7
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2
- initial release by fcimport

