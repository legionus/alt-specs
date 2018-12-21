Name: libmtsupport
Version: 0.0.1
Release: alt3.qa4

Summary: general support library for multitran
License: LGPL
Group: System/Libraries

Source: %name-%{version}alpha2.tar.bz2

# Automatically added by buildreq on Mon Oct 04 2004
BuildRequires: gcc-c++ libstdc++-devel

%description
Library with some usefull functions used in multitran

%package devel
Summary: Development part of %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Contents header files and development libraries for %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
Contents static libraries for %name

%prep
%setup -q -n %name-%{version}alpha2

%build
%make_build

%install
%makeinstall

%files
%doc ChangeLog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Sun Nov 08 2015 Michael Shigorin <mike@altlinux.org> 0.0.1-alt3.qa4
- rebuilt for gcc5 C++ ABI

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.1-alt3.qa3
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt3.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmtsupport
  * postun_ldconfig for libmtsupport
  * postclean-05-filetriggers for spec file

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3
- fixed linkage

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Thu Jan 13 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt2
- alpha2

* Tue Nov 09 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- initial build

