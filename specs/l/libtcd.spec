%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global		postver	-r2
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		2.2.7

%global		fedorarel	2
%global		rpmrel		%{fedorarel}%{?postver:.%postrpmver}

Name:		libtcd
Version:	%{mainver}
Release:	alt1_%{rpmrel}.4
Summary:	Tide Constituent Database Library

Group:		System/Libraries
License:	Public Domain
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/%{name}-%{version}%{?postver}.tar.bz2
Source44: import.info


%description
libtcd provides a software API for reading and writing Tide
Constituent Database (TCD) files.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure
%make_build -k

%install
make \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	install

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%doc *.html

%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_2.r2.4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_2.r2.2
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_2.r2.1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_2.r2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_1.2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_1.1
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_5.r3.1
- update to new release by fcimport

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_5.r3
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_4.r2.2
- initial fc import

