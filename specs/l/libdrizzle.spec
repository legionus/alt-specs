# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared

Summary: Drizzle Client & Protocol Library
Name: libdrizzle
Version: 0.8
Release: alt3_10.qa1
# All code is BSD, except libdrizzle/sha1.{c,h} which are Public Domain
License: BSD and Public Domain
Group: System/Libraries
URL: https://launchpad.net/libdrizzle
Source0: http://launchpad.net/%{name}/trunk/0.8/+download/%{name}-%{version}.tar.gz
Source1: README

BuildRequires: doxygen
Source44: import.info

%description
This is the the client and protocol library for the Drizzle project. The
server, drizzled, will use this as for the protocol library, as well as the
client utilities and any new projects that require low-level protocol
communication (like proxies). Other language interfaces (PHP extensions, SWIG,
...) should be built off of this interface.

%package devel
Group: Development/C
Summary: Drizzle Client & Protocol Library - Header files
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the Drizzle Client & Protocol Library

%package doc 
Group: Documentation 
Summary: Drizzle Client & Protocol Library Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc 
Documentation files for the Drizzle Client & Protocol Library

%prep
%setup -q
cp -a %{SOURCE1} .

%configure
%build
make %{_smp_mflags}
make doxygen

%install
make install DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""

# cleanup
rm -f %{buildroot}/%{_libdir}/libdrizzle.la 


%files 
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/libdrizzle.so.*

%files devel
%doc PROTOCOL
%{_includedir}/libdrizzle/
%{_libdir}/pkgconfig/libdrizzle.pc
%{_libdir}/libdrizzle.so

%files doc
%doc docs/api docs/dev

%changelog
* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.8-alt3_10.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libdrizzle-doc

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_10
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt3_9
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_9
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_7
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_7
- initial import by fcimport

