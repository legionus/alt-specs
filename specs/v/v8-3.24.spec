%define MAJOR_VERSION     3
%define MINOR_VERSION     24
%define BUILD_NUMBER      35
%define PATCH_LEVEL       33
%define soversion %MAJOR_VERSION.%MINOR_VERSION
%define libname libv8
%def_without tests

Name:    v8-%MAJOR_VERSION.%MINOR_VERSION
Version: %MAJOR_VERSION.%MINOR_VERSION.%BUILD_NUMBER.%PATCH_LEVEL
Release: alt2

Summary: V8 is Google's open source JavaScript engine.
License: BSD
Group:   System/Libraries
Url:     http://code.google.com/p/v8

Source:  %name-%version.tar
BuildPreReq: gcc4.9-c++ gyp
BuildRequires: python-modules-multiprocessing

Provides: %libname

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used
in Google Chrome, the open source browser from Google. V8 implements ECMAScript
as specified in ECMA-262, 5rd edition.

%package -n lib%name
Summary: Google's JavaScript Engine
License: BSD
Group:   System/Libraries
Provides: %libname = %version
Provides: %libname = %MAJOR_VERSION.%MINOR_VERSION
Obsoletes: %libname = %MAJOR_VERSION.%MINOR_VERSION

%description -n lib%name
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used
in Google Chrome, the open source browser from Google. V8 implements ECMAScript
as specified in ECMA-262, 5rd edition.

%package -n lib%name-devel
Group:   Development/C++
Summary: Development headers and libraries for V8
Requires: lib%name = %version-%release
Provides: %libname-devel = %version
Provides: %libname-devel = %MAJOR_VERSION.%MINOR_VERSION
Conflicts: %libname-devel < %MAJOR_VERSION.%MINOR_VERSION

%description -n lib%name-devel
Development headers and libraries for V8.


%prep
%setup -q
sed -i 's|build/gyp/gyp|gyp|g' Makefile
#sed -i "s|'-Wno-unused-but-set-variable'||g" SConstruct

%build
GYPFLAGS='-Duse_system_icu=0' 
%make_build native \
	    mode=release \
	    library=shared \
	    snapshot=on \
	    i18nsupport=off \
	    soname_version=%{soversion} \
	    V=1 \
%ifarch armh
	    armfloatabi=hard
%endif


%install
mkdir -p %buildroot{%_libdir,%_bindir,%_includedir}
install -p -m755 out/native/d8 %buildroot%_bindir/
install -p -m644 out/native/lib.target/libv8.so.%soversion %buildroot%_libdir/
ln -s libv8.so.%soversion %buildroot%_libdir/libv8.so
install -p -m644 include/*.h %buildroot%_includedir/

%check
%if_with tests
# TODO: need depot_tools in PATH
LD_LIBRARY_PATH=out/Release/lib.target tools/run-tests.py \
		--no-presubmit \
		--outdir=out \
		--buildbot \
		--arch=native \
		--mode=Release \
		--progress=dots
%endif

%files -n lib%name
%doc AUTHORS ChangeLog LICENSE LICENSE.*
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_bindir/*

%changelog
* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 3.24.35.33-alt2
- Build with gcc 4.9

* Wed Apr 30 2014 Andrey Cherepanov <cas@altlinux.org> 3.24.35.33-alt1
- new version
- security fixes:
  + High CVE-2014-1736: Integer overflow in V8.

* Fri Apr 11 2014 Andrey Cherepanov <cas@altlinux.org> 3.24.35.32-alt1
- new version in 3.24 series (ALT #29866)

* Thu Mar 13 2014 Andrey Cherepanov <cas@altlinux.org> 3.23.17.22-alt1
- new version
- security fixes:
  + CVE-2014-1704: Multiple vulnerabilities in V8

* Fri Feb 21 2014 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.23.17.14-alt1
- new version (Closes: #29837)

* Tue Jan 28 2014 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.22.24.18-alt1
- new version (Closes: #29762)
  + High CVE-2013-6650: Memory corruption in V8.

* Sun Dec 01 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.22.24.8-alt1
- new version (Closes: #29628)
  + Medium CVE-2013-6638: Buffer overflow in v8.
  + High CVE-2013-6639: Out of bounds write in v8.
  + Medium CVE-2013-6640: Out of bounds read in v8.

* Sun Dec 01 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.18.9-alt1
- new version

* Tue Oct 01 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.18.2-alt1.1
- fix arm build (sbolshakov@altlinux.ru)

* Sun Sep 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.18.2-alt1
- new version

* Tue Sep 17 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.16.2-alt1
- new version

* Tue Sep 17 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.20.17.7-alt1
- new version

* Mon Sep 02 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.20.17.4-alt1
- new version

* Tue Aug 06 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.20.12.1-alt1
- new version

* Thu Aug 01 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.20.11.2-alt1
- new version

* Sun Jul 28 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.20.9.1-alt1
- new version

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.18.5.9-alt2
- versioned package

* Wed Jul 24 2013 Andrey Cherepanov <cas@altlinux.org> 3.18.5.9-alt1
- New version

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 3.17.6.14-alt1
- new version (Closes: #29004)

* Fri Mar 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.16.14.10-alt1
- new version (Closes: #28759)
- change soname

* Fri Mar 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.15.11.10-alt2
- built for arm

* Sat Jan 19 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.15.11.10-alt1
- 3.15.11.10 (Closes: #28346)
  + High CVE-2012-5153: Out-of-bounds stack access in v8.
  + High CVE-2013-0836: Crash in v8 garbage collection.

* Thu Nov 08 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.13.7.5-alt1
- 3.13.7.5 (Closes: #27940)
  + CVE-2012-5128

* Mon Sep 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.13.7.1-alt1
- 3.13.7.1

* Mon Sep 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.11.10.22-alt1
- 3.11.10.22

* Sat Jun 16 2012 Dmitry Kulik <lnkvisitor@altlinux.org> 3.11.10.5-alt1
- 3.11.10.5
  + Added ECMAScript 5 support
  
* Thu Mar 15 2012 Vladimir Lettiev <crux@altlinux.ru> 3.9.19-alt1
- 3.9.19

* Tue Jan 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.6.4-alt1
- 2.0.6.4

* Sat Jan 23 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.6.1-alt1
- 2.0.6.1

* Fri Jan 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.6-alt1
- 2.0.6
- bump the soname

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.5.5-alt1
- 2.0.5.5

* Mon Jan 04 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.5.4-alt1
- 2.0.5.4

* Mon Dec 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.5.1-alt1
- 2.0.5.1

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Thu Dec 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Sat Dec 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.3-alt1
- 2.0.3
- bump the soname (some symbols were removed)

* Tue Nov 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.18.9-alt1
- 1.3.18.9

* Fri Nov 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.18.8-alt2
- fix installation on x86_64

* Fri Nov 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.18.8-alt1
- initial build for ALT Linux, based on Fedora spec and Debian package

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.16-1.20091027svn3152
- update to 1.3.16, svn3152

* Tue Oct 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.15-1.20091013svn3058
- update to svn3058

* Thu Oct  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.15-1.20091008svn3036
- update to 1.3.15, svn3036

* Tue Sep 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.13-1.20090929svn2985
- update to svn2985
- drop unused parameter patch, figured out how to work around it with optflag mangling
- have I mentioned lately that scons is garbage?

* Mon Sep 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.13-1.20090928svn2980
- update to 1.3.13, svn2980

* Wed Sep 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.11-1.20090916svn2903
- update to 1.3.11, svn2903

* Wed Sep  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.9-1.20090909svn2862
- update to 1.3.9, svn2862

* Thu Aug 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.8-1.20090827svn2777
- update to 1.3.8, svn2777

* Mon Aug 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.6-1.20090824svn2747
- update to 1.3.6, svn2747

* Tue Aug 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.4-1.20090818svn2708
- update to svn2708, build and package d8

* Fri Aug 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.4-1.20090814svn2692
- update to 1.3.4, svn2692

* Wed Aug 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.3-1.20090812svn2669
- update to 1.3.3, svn2669

* Mon Aug 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090810svn2658
- update to svn2658

* Fri Aug  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090807svn2653
- update to svn2653

* Wed Aug  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090805svn2628
- update to 1.3.2, svn2628

* Mon Aug  3 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090803svn2607
- update to svn2607

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090731svn2602
- update to svn2602

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090730svn2592
- update to 1.3.1, svn 2592

* Mon Jul 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.0-1.20090727svn2543
- update to 1.3.0, svn 2543

* Fri Jul 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090724svn2534
- update to svn2534

* Mon Jul 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090720svn2510
- update to svn2510

* Thu Jul 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090716svn2488
- update to svn2488

* Wed Jul 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090715svn2477
- update to 1.2.14, svn2477

* Mon Jul 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.13-1.20090713svn2434
- update to svn2434

* Sat Jul 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.13-1.20090711svn2430
- update to 1.2.13, svn2430

* Wed Jul  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.12-1.20090708svn2391
- update to 1.2.12, svn2391

* Sat Jul  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.11-1.20090704svn2356
- update to 1.2.11, svn2356

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.9-1.20090626svn2284
- update to svn2284

* Wed Jun 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.9-1.20090624svn2262
- update to 1.2.9, svn2262

* Thu Jun 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-2.20090618svn2219
- fix unused-parameter patch

* Thu Jun 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-1.20090618svn2219
- update to 1.2.8, svn2219

* Mon Jun 8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-2.20090608svn2123
- fix gcc44 compile for Fedora 11

* Mon Jun  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-1.20090608svn2123
- update to 1.2.7, svn2123

* Thu May 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.5-1.20090528svn2072
- update to newer svn checkout

* Sun Feb 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-1.20090222svn1332
- update to newer svn checkout

* Sun Sep 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-2.20080914svn300
- make a versioned shared library properly

* Sun Sep 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-1.20080914svn300
- Initial package for Fedora

