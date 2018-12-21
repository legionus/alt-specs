Name: gnustep-systempreferences
Version: 1.2.0
Release: alt1.svn20140214
Summary: Implementation of the PreferencePanes framework (NSPreferencePane)
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/apps/systempreferences/trunk/
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

Inspiration for some of the panels comes from Jeff Teunissen's original
Preferences application (Backbone project:
http://www.nongnu.org/backbone/ ).

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the implementation of the PreferencePanes framework
(NSPreferencePane) as described in the Apple Documentation.

This package contains development files of %name.

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
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in *.so*; do
	rm -f $i
	mv GNUstep/Frameworks/PreferencePanes.framework/Versions/1/$i ./
	for j in *.so.*.*; do
		ln -s %_libdir/$j \
			GNUstep/Frameworks/PreferencePanes.framework/Versions/1/$i
	done
done
rm -f \
	GNUstep/Frameworks/PreferencePanes.framework/Versions/1/PreferencePanes
ln -s %_libdir/$j \
	GNUstep/Frameworks/PreferencePanes.framework/Versions/1/PreferencePanes
rm -f \
	GNUstep/Frameworks/PreferencePanes.framework/Headers
ln -s Versions/1/Headers \
	GNUstep/Frameworks/PreferencePanes.framework/Headers
popd

install -Dp -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/PreferencePanes.framework/Versions/1/Headers
%exclude %_libdir/GNUstep/Frameworks/PreferencePanes.framework/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/PreferencePanes.framework/Versions/1/Headers
%_libdir/GNUstep/Frameworks/PreferencePanes.framework/Headers

%changelog
* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20140214
- Version 1.2.0

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt7.svn20130916
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt6.svn20130916
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5.git20130916
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5.git20130912
- New snapshot

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5.git20130207
- New snapshot

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5.git20120323
- Added menu file (thnx kostyalamer@)

* Mon Jan 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4.git20120323
- Fixed symlink for Headers

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3.git20120323
- Don't require devel packages for runtime packages

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.git20120323
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20120323
- Initial build for Sisyphus

