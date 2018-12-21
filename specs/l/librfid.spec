BuildRequires: chrpath
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           librfid
Version:        0.2.0 
Release:        alt3_15
Summary:     The librfid is a Free Software RFID library

Group:          System/Libraries
License:        GPLv2
URL:               http://www.openmrtd.org/projects/librfid/
Source0:        http://openmrtd.org/projects/librfid/files/librfid-%{version}.tar.bz2

BuildRequires:  libusb-compat-devel automake-common libtool-common autoconf-common
Source44: import.info


%description
librfid is a Free Software RFID library. It implements the PCD (reader) 
side protocol stack of ISO 14443 A, ISO 14443 B, ISO 15693, 
Mifare Ultralight and Mifare Classic. Support for iCODE and 
other 13.56MHz based transponders is planned.


%package        devel
Summary:      Development files for %{name}
Group:           Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%files
%doc COPYING README TODO
%{_libdir}/*.so.*
%{_bindir}/librfid-tool
%{_bindir}/mifare-tool
%{_bindir}/librfid-send_script
%{_mandir}/man1/librfid*
%{_mandir}/man1/mifare*

%files devel
%doc README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/librfid.pc


%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_6
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_5
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_4
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_4
- initial import by fcimport

