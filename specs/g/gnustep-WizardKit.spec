%set_verify_elf_method unresolved=strict

Name: gnustep-WizardKit
Version: 0.1
Release: alt3
Summary: Framework needed by Project Manager
License: MIT or FDL
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/WizardKit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel doxygen
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Framework needed by Project Manager.

%package -n lib%name
Summary: Shared libraries of WizardKit
Group: System/Libraries

%description -n lib%name
Framework needed by Project Manager.

This package contains shared libraries of WizardKit.

%package -n lib%name-devel
Summary: Development files of WizardKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Framework needed by Project Manager.

This package contains development files of WizardKit.

%package docs
Summary: Documentation for WizardKit
Group: Documentation
BuildArch: noarch

%description docs
Framework needed by Project Manager.

This package contains documentation for WizardKit.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2'
 
doxygen

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in WizardKit; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/0/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/0/$i ||:
			rm GNUstep/Frameworks/$j.framework/Versions/0/$j ||:
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/0/$j ||:
		done
	done
done
popd

%files
%doc README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files docs
%doc Documentation/html/*

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

