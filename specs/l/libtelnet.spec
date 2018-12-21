%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libtelnet
Version:	0.21
Release:	alt1_12
Summary:	TELNET protocol parsing framework

Group:		System/Libraries
License:	Public Domain
URL:		http://github.com/elanthis/libtelnet
Source0:	http://cloud.github.com/downloads/seanmiddleditch/libtelnet/libtelnet-%{version}.tar.gz

BuildRequires: zlib-devel
BuildRequires: doxygen
Source44: import.info

%description
Small library for parsing the TELNET protocol, responding to TELNET
commands via an event interface, and generating valid TELNET commands.

libtelnet includes support for the non-official MCCP, MCCP2, ZMP, and
MSSP protocols used by MUD servers and clients.

%package devel
Summary: Header files for libtelnet
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Requires: pkg-config

%description devel
Header files for developing applications making use of libtelnet.

%package utils
Summary: TELNET utility programs from libtelnet
Group: Networking/WWW
Requires: %{name} = %{version}-%{release}

%description utils
Provides three utilities based on the libtelnet library.
  * telnet-proxy - a TELNET proxy and debugging daemon
  * telnet-client - simple TELNET client
  * telnet-chatd - no-features chat server for testing TELNET clients.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
rm -rf "$RPM_BUILD_ROOT"
make install INSTALL="install -p" DESTDIR="$RPM_BUILD_ROOT"
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la

%files
%doc README COPYING NEWS
%{_libdir}/*.so.*

%files devel
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files utils 
%{_bindir}/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_9
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_4
- initial import by fcimport

