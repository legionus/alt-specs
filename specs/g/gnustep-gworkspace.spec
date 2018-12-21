Name: gnustep-gworkspace
Version: 0.9.2
Release: alt4.svn20131218
Summary: The GNUstep Workspace Manager of which the most visible part is the filebrowser
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gworkspace.git
Source: %name-%version.tar
Source1: %name.menu
Source2: %name.sh

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel /proc
BuildPreReq: libgnustep-objc2-devel libgnustep-pdfkit-devel
BuildPreReq: gnustep-systempreferences-devel libsqlite3-devel unzip
BuildPreReq: gnustep-gui-devel gnustep-gui inotify-tools-devel

Requires: lib%name = %version-%release
Requires: gnustep-systempreferences
Requires: gnustep-back

%description
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

%package -n lib%name
Summary: Shared libraries of GWorkspace
Group: System/Libraries

%description -n lib%name
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains shared libraries of GWorkspace.

%package -n lib%name-devel
Summary: Development files of GWorkspace
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains development files of GWorkspace.

%package doc
Summary: Documentation for GWorkspace
Group: Documentation
BuildArch: noarch

%description doc
GWorkspace is a clone of the NeXT workspace manager with some added
features as spatial viewing, an advanced database based search system,
etc.

This package contains documentation for GWorkspace.

%prep
%setup

%build
#export GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
#export CC=gcc
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-gwmetadata \
	--with-inotify \
	--with-installation-domain=SYSTEM

%define incs -I%_libdir/GNUstep/Frameworks/PreferencePanes.framework/Headers
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='%incs' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lgnustep-gui -lobjc2 -lm'
 
libFSNode="$PWD/FSNode/FSNode.framework/libFSNode.so"
pushd Inspector
%make clean
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='%incs' \
	CONFIG_SYSTEM_LIBS="$libFSNode -lgnustep-base -lgnustep-gui -lobjc2"
popd

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in MDKit Operation Inspector FSNode; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/?/$i ./
		for k in lib$j.so.*.*; do
			for l in 0 1; do
				ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/$l/$i ||:
				rm GNUstep/Frameworks/$j.framework/Versions/$l/$j ||:
				ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/$l/$j ||:
			done
		done
	done
done
popd

install -Dp -m644 %SOURCE1 %buildroot%_menudir/%name

rm %buildroot%_bindir/GWorkspace
install -Dp -m755 %SOURCE2 %buildroot%_bindir/GWorkspace
sed -i 's,@PATH@,%_libdir/GNUstep/Applications/GWorkspace.app,' %buildroot%_bindir/GWorkspace

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/?/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Versions/?/Headers
%_libdir/GNUstep/Frameworks/*.framework/Headers

%files doc
%doc Documentation/*

%changelog
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt4.svn20131218
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3.svn20131218
- Added Requires: gnustep-systempreferences and Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3.git20131218
- New snapshot

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt3.git20130911
- New snapshot

* Wed Mar 06 2013 Michael Shigorin <mike@altlinux.org> 0.9.2-alt3.git20130304
- NMU: added a shell wrapper to start filemanager by default (thx aen@)

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2.git20130304
- New snapshot

* Wed Feb 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2.git20130127
- Added menu file (thinx kostyalamer@)

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20130127
- Version 0.9.2

* Mon Jan 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt3.git20121017
- Fixed build

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.git20121017
- Rebuilt with libobjc2 instead of libobjc
- Don't require development packages for runtime packages

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20121017
- Initial build for Sisyphus

