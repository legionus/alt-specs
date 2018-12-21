%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libgtextutils
Version:	0.7
Release:	alt1_22
Summary:	Assaf Gordon text utilities    

Group:		System/Libraries
License:	AGPLv3+
URL:		http://hannonlab.cshl.edu/fastx_toolkit/
Source0:	https://github.com/agordon/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:		libgtextutils-GCC6-iostream.patch

BuildRequires:  gcc-c++
Source44: import.info

%description
Text utilities library used by the fastx_toolkit, from the Hannon Lab

%package       devel
Summary:       Development files for %{name}
Group:	       Development/Other
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%patch0 -p1

%build
%configure --disable-static
#fix for unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%files
%doc AUTHORS COPYING README THANKS NEWS
%{_libdir}/libgtextutils-*.so.*


%files devel
%{_includedir}/gtextutils
%{_libdir}/libgtextutils*.so
%{_libdir}/pkgconfig/gtextutils.pc

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_17
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_8
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_7
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_5
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5
- initial import by fcimport

