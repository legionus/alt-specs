%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libfc14audiodecoder
Version: 1.0.3
Release: alt1_12

Summary: C wrapper library for Future Composer audio decoding
Group: System/Libraries
License: GPLv2+
URL: http://xmms-fc.sourceforge.net
Source0: http://downloads.sourceforge.net/xmms-fc/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++
Source44: import.info

%description
This library provides a C API for a Future Composer audio decoder, which
has been used in several plug-ins for versatile audio players like XMMS,
BMP, Audacious and GStreamer.


%package devel
Summary: Files needed for developing with %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the files that are needed when building
software that uses %{name}.


%prep
%setup -q


%build
%configure
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"





%files
%doc --no-dereference COPYING
%doc README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/fc14audiodecoder.h


%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_4
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2
- initial import by fcimport

