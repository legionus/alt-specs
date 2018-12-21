%set_verify_elf_method unresolved=strict

Name: gnustep-gscoredata
Version: r33286
Release: alt4.svn20110612
Summary: Free implementation of the Apple Core Data framework
License: LGPLv2.1+, FDLv1.2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gscoredata/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel /proc
BuildPreReq: doxygen graphviz

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
GNUstep Core Data framework, a free implementation of the Apple Core
Data framework as available in the Mac OS X, release 10.4 (Tiger)
operating system.

%package -n lib%name
Summary: Shared libraries of GNUstep Core Data framework
Group: System/Libraries

%description -n lib%name
GNUstep Core Data framework, a free implementation of the Apple Core
Data framework as available in the Mac OS X, release 10.4 (Tiger)
operating system.

This package contains shared libraries of GNUstep Core Data framework.

%package -n lib%name-devel
Summary: Development files of GNUstep Core Data framework
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
GNUstep Core Data framework, a free implementation of the Apple Core
Data framework as available in the Mac OS X, release 10.4 (Tiger)
operating system.

This package contains development files of GNUstep Core Data framework.

%package -n lib%name-devel-doc
Summary: Documentation for GNUstep Core Data framework
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
GNUstep Core Data framework, a free implementation of the Apple Core
Data framework as available in the Mac OS X, release 10.4 (Tiger)
operating system.

This package contains development documentation for GNUstep Core Data
framework.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
doxygen

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in CoreData; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/CoreData.framework/Versions/0/$j ./
		ln -s %_libdir/$lib \
			GNUstep/Frameworks/CoreData.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/CoreData.framework/Versions/0/$i
	ln -s %_libdir/$lib \
		GNUstep/Frameworks/CoreData.framework/Versions/0/$i
done
popd

%files
%doc ChangeLog README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/CoreData.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/CoreData.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/CoreData.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/CoreData.framework/Headers

%files -n lib%name-devel-doc
%doc Documentation/html/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r33286-alt4.svn20110612
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r33286-alt3.svn20110612
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r33286-alt2.svn20110612
- Rebuilt with new gnustep-gui

* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r33286-alt1.svn20110612
- Initial build for Sisyphus

