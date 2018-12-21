# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libmodman
Version:        2.0.1
Release:        alt2_16
Summary:        A simple library for managing C++ modules (plug-ins)

License:        LGPLv2+
URL:            http://code.google.com/p/libmodman/
Source0:        http://libmodman.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++-common
BuildRequires:  ctest cmake
BuildRequires:  zlib-devel
Source44: import.info

%description
libmodman is a simple library for managing C++ modules (plug-ins).

%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{?epoch:%{epoch}}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%{fedora_cmake}
%make_build

%check
make test

%install
%makeinstall_std

%files
%doc COPYING
%doc AUTHORS
%{_libdir}/libmodman.so.*

%files devel
%{_includedir}/libmodman/
%{_libdir}/libmodman.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/Findlibmodman.cmake

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- initial import by fcimport

