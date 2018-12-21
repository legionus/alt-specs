Name: libaacs
Version: 0.8.1
Release: alt3

Summary: BD AACS library
License: LGPL
Group: System/Libraries
Url: http://bd.videolan.org/

Source: %name-%version-%release.tar

BuildRequires: flex libgcrypt-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libaacs development.

%prep
%setup

%build
%ifarch %e2k
export cc_cv_cflags__Werror_implicit_function_declaration=no
%endif
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/aacs_info
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Fri Jul 06 2018 Michael Shigorin <mike@altlinux.org> 0.8.1-alt3
- worked around ftbfs on e2k

* Tue Oct 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt2
- rebuilt with recent libgcrypt

* Wed Apr 08 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue May 27 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- 0.7.1 released

* Tue Sep 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Fri May 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Tue Oct 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- 0.2 released

* Wed May 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- initial
