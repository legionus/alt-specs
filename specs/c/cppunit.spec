# vim: set ft=spec: -*- rpm-spec -*-

%def_disable docs

Name: cppunit
Version: 1.14.0
Release: alt1

Summary: C++ port of the famous JUnit framework for unit testing
License: LGPL
Group: Development/C++
Url: https://www.freedesktop.org/wiki/Software/cppunit/

Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Oct 05 2006
BuildRequires: doxygen gcc-c++ graphviz

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%package devel
Summary: C++ port of the famous JUnit framework for unit testing
Group: Development/C++
Requires: %name = %version-%release
Obsoletes: %name-gcc2-devel, %name-gcc3-devel, %name-common-devel
Provides: %name-gcc2 = %version-%release, %name-gcc3 = %version-%release, %name-common-devel = %version-%release

%description devel
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%package devel-docs
Summary: Documentation for CppUnit
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-docs
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

This package contains development documentation for CppUnit.

%prep
%setup

%build
%autoreconf
#./autogen.sh
%configure \
	--disable-static \
	--docdir=%_docdir/%name-%version
%make_build

%install
%makeinstall_std

%check
make check

%files
%_libdir/lib*.so.*

%files devel
%doc %_docdir/%name-%version/*
%_bindir/*
%_includedir/cppunit/
%_libdir/lib*.so
#_datadir/aclocal/*
#_man1dir/*
%_pkgconfigdir/%name.pc

%if_enabled docs
%files devel-docs
%_datadir/%name
%endif

%changelog
* Thu Jul 20 2017 Fr. Br. George <george@altlinux.ru> 1.14.0-alt1
- Upstream switch to LO/FD
- Autobuild version bump to 1.14.0
- Resurrect docs package

* Mon Jun 01 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.12.1-alt2.svn20130422.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.1-alt2.svn20130422
- New snapshot

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.1-alt2.svn20120901
- New snapshot
- Extracted docs into separate package

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.1-alt2
- Rebuilt for debuginfo

* Mon Nov 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.12.1-alt1
- [1.12.1]
- spec cleanup

* Mon Jan 21 2008 Sir Raorn <raorn@altlinux.ru> 1.12.0-alt2
- Fix build with new autoconf

* Thu Oct 05 2006 Sir Raorn <raorn@altlinux.ru> 1.12.0-alt1
- [1.12.0]
- Updated BuildRequires

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.10.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Sep 06 2004 Alexey Voinov <voins@altlinux.ru> 1.10.2-alt1
- new version (1.10.2)

* Sat May 08 2004 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt6
- remove requirements on gcc3.2
- buildreqs fixed

* Mon Mar 15 2004 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt5
- build fixed (*.la removed)
- multiply g++ support completely removed
- little spec clean up

* Tue Jul 08 2003 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt4.2
- fixed version number for gcc3.2

* Tue Sep 10 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt4.1
- fixed version number for gcc3.2
(this is temporary release)

* Mon Aug 19 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt4
- added macros to control compilers version for which to build library
- spec rewrite: subpackages rearranged, files rearranged
- use gcc-version specific directories instead of update-alternatives
- buildreqs fixed

* Mon Jun 10 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt3
- buildreqs fixed

* Thu Jun 06 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt2
- fixed names of .so in update-alternatives
- fixed permissions on cppunit-config*
- added cppunit/ui include directory

* Sun May 26 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt1
- new version (1.8.0)

* Mon May 20 2002 Alexey Voinov <voins@voins.program.ru> 1.6.2-alt0.2
- support for gcc-3.x.x/gcc-2.x.x
- support for alternatives

* Thu Dec 13 2001 Alexey Voinov <voins@voins.program.ru> 1.6.2-alt0.1
- initial build

