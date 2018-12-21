Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libax25
Version:        1.0.5
Release:        alt1_5
Summary:	AX.25 library for hamradio applications

License:	LGPLv2+
URL:		http://www.linux-ax25.org/wiki/Libax25
Source0:	http://www.linux-ax25.org/pub/libax25/%{name}-%{version}.tar.gz

BuildRequires:  autoconf-common automake-common libtool-common
BuildRequires:  zlib-devel
Source44: import.info


%description
libax25 is a library for ham radio applications that use the ax25 protocol. 
Included are routines to do ax25 address parsing, common ax25 application
config file parsing, etc. 


%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# hack; added -lz; report upstream
sed -i -e "s,libax25_la_SOURCES,libax25_la_LIBADD = -lz\nlibax25_la_SOURCES," Makefile.am
sed -i -e "s,libax25io_la_SOURCES,libax25io_la_LIBADD = -lz\nlibax25io_la_SOURCES," Makefile.am



%build
autoreconf -fisv
./autogen.sh
%configure --disable-static
%make_build


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Create /etc/ax25
mkdir -p %{buildroot}%{_sysconfdir}/ax25

# These headers conflict with glibc-headers.
rm -f %{buildroot}%{_includedir}/{netax25/ax25.h,netrom/netrom.h,netrose/rose.h}


%files
%doc AUTHORS ChangeLog README
%doc COPYING
%{_libdir}/*.so.*
%{_mandir}/man?/*
%dir %{_sysconfdir}/ax25

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.9.rc2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.8.rc2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.7.rc2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.6.rc2
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.5.rc2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.4.rc2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.3.rc2
- update to new release by fcimport

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.2.rc2
- fixed build after mass spec cleanup

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_0.2.rc2
- initial release by fcimport

