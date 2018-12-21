%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: A library for accessing deltacloud
Name: libdeltacloud
Version: 0.9
Release: alt2_17
License: LGPLv2+
Group: System/Libraries
URL: https://git.fedorahosted.org/git/deltacloud/libdeltacloud.git
Source0: https://git.fedorahosted.org/cgit/deltacloud.git/libdeltacloud.git/snapshot/%{name}-%{version}.tar.gz
Patch0: libdeltacloud-configure-ac-update.patch
Patch1: libdeltacloud-update-fsf-address.patch
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libtool-common
Source44: import.info

%description
Libdeltacloud is a library for accessing deltacloud via a
convenient C API.

%package devel
Summary: Header files for libdeltacloud library
License: LGPLv2+
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
The libdeltacloud-devel package contains the files needed for developing
applications that need to use the libdeltacloud library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# to support aarch64
libtoolize --force
aclocal
autoheader
autoconf
automake --add-missing
%configure --libdir=/%{_lib}
%make_build

%install
make DESTDIR="${RPM_BUILD_ROOT}" install

# Move the symlink
rm -f $RPM_BUILD_ROOT/%{_lib}/%{name}.so
mkdir -p $RPM_BUILD_ROOT%{_libdir}
VLIBNAME=$(ls $RPM_BUILD_ROOT/%{_lib}/%{name}.so.*.*.*)
LIBNAME=$(basename $VLIBNAME)
ln -s ../../%{_lib}/$LIBNAME $RPM_BUILD_ROOT%{_libdir}/%{name}.so

# Move the pkgconfig file
mv $RPM_BUILD_ROOT/%{_lib}/pkgconfig $RPM_BUILD_ROOT%{_libdir}

# Remove a couple things so they don't get picked up
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.la
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.a

%files
%doc COPYING
%attr(0755,root,root) /%{_lib}/libdeltacloud.so.*

%files devel
%attr(0644,root,root) %{_includedir}/libdeltacloud/action.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/address.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/bucket.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/driver.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/hardware_profile.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/image.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance_state.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/key.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/libdeltacloud.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/link.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/loadbalancer.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/realm.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_snapshot.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_volume.h
%attr(0755,root,root) %{_libdir}/libdeltacloud.so
%{_libdir}/pkgconfig/libdeltacloud.pc

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_8
- update to new release by fcimport

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_7
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- initial import by fcimport

