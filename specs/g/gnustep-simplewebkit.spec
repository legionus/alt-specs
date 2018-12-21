%set_verify_elf_method unresolved=strict

Name: gnustep-simplewebkit
Version: 0.1.0
Release: alt2.svn20140201
Summary: Framework which is meant to be a simple, drop-in replacement for WebKit
License: LGPLv2+
Group: Networking/WWW
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/simplewebkit/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
SimpleWebKit is a framework which is meant to be a simple, drop-in
replacement for WebKit.

%package -n lib%name
Summary: Shared libraries of SimpleWebKit
Group: System/Libraries

%description -n lib%name
SimpleWebKit is a framework which is meant to be a simple, drop-in
replacement for WebKit.

This package contains shared libraries of SimpleWebKit.

%package -n lib%name-devel
Summary: Development files of SimpleWebKit
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
SimpleWebKit is a framework which is meant to be a simple, drop-in
replacement for WebKit.

This package contains development files of SimpleWebKit.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2 -lm'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/$i ./
	for j in *.so.*.*.*; do
		ln -s %_libdir/$j \
			GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/$i
	done
done
rm -f \
	GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/SimpleWebKit
ln -s %_libdir/$j \
	GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/SimpleWebKit
popd

%files
%doc ChangeLog README ToDo
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/SimpleWebKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/Headers

%files -n lib%name
%doc ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/SimpleWebKit.framework/Headers
%_libdir/GNUstep/Frameworks/SimpleWebKit.framework/Versions/0.1/Headers

%changelog
* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.svn20140201
- New snapshot

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.svn20131216
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.svn20131216
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20131216
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20130508
- New snapshot

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20120905
- Initial build for Sisyphus

