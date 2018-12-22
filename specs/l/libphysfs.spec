%define uname physfs
Name: libphysfs
Version: 3.0.1
Release: alt1

Summary: PhysicsFS file abstraction layer for games
License: Zlib
Group: System/Libraries
Url: http://www.icculus.org/physfs/
Provides: %uname = %version
Source0: http://icculus.org/physfs/downloads/physfs-%version.tar.gz
Patch: physfs-3.0.1-dirfix.patch

# Automatically added by buildreq on Sat Oct 24 2009
BuildRequires: doxygen gcc-c++ libncurses-devel libreadline-devel zlib-devel cmake

%description
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat inspired
by Quake 3's file subsystem. The programmer defines a "write directory" on
the physical filesystem. No file writing done through the PhysicsFS API can
leave that write directory, for security. For example, an embedded scripting
language cannot write outside of this path if it uses PhysFS for all of its
I/O, which means that untrusted scripts can run more safely. Symbolic links
can be disabled as well, for added safety. For file reading, the programmer
lists directories and archives that form a "search path". Once the search
path is defined, it becomes a single, transparent hierarchical filesystem.
This makes for easy access to ZIP files in the same way as you access a file
directly on the disk, and it makes it easy to ship a new archive that will
override a previous archive on a per-file basis. Finally, PhysicsFS gives
you platform-abstracted means to determine if CD-ROMs are available, the
user's home directory, where in the real filesystem your program is running,
etc.

%package devel
Summary: Development headers, libraries, and documentation for PhysicsFS
Group: Development/C
Requires: %name = %version-%release
Provides: %uname-devel = %version

%description devel
PhysicsFS is a library to provide abstract access to various archives.
This package contains the development headers, libraries, and documentaion to
build programs using PhysicsFS.

%prep
%setup -n %uname-%version
%patch -p1

%build
%cmake_insource \
	-DPHYSFS_BUILD_STATIC:BOOL=OFF

%make_build

doxygen

%install
%makeinstall_std

%files
%doc docs/CHANGELOG.txt docs/CREDITS.txt docs/INSTALL.txt LICENSE.txt docs/TODO.txt
%_libdir/*so.*[0-9]

%files devel
%_bindir/test_physfs
%doc docs/*
%_libdir/*.so
%_libdir/pkgconfig/physfs.pc
%_includedir/physfs.h

%changelog
* Wed Nov 07 2018 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Build new version.

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.1
- Fixed build

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.0.2-alt1
- Autobuild version bump to 2.0.2

* Thu Sep 30 2010 Fr. Br. George <george@altlinux.ru> 2.0.1-alt1
- Autobuild version bump to 2.0.1
- (Closes: #10289, #19309)

* Thu Sep 30 2010 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Version highly updated

* Sat Oct 24 2009 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2
- remove internal zlib before build

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt1.1
- Rebuilt with libreadline.so.5.

* Mon Oct 10 2005 Sergey Pinaev <dfo@altlinux.ru> 1.0.1-alt1
- 1.0.1
- build with system zlib
- .spec cleanup
- move "test_physfs" binary to -devel package

* Tue Sep 28 2004 Sergey Pinaev <dfo@altlinux.ru> 1.0.0-alt1
- first build for ALT

* Thu Dec 18 2002 Edward Rudd <eddie@omegaware.com>
- added zlib_license_change.txt to documents

* Wed Jul 10 2002 Edward Rudd <eddie@omegaware.com>
- added doxygen to build requirements

* Wed Jul 10 2002 Edward Rudd <eddie@omegaware.com>
- updated to release 0.17

* Tue May 15 2002 Edward Rudd <eddie@omegaware.com>
- updated to latest CVS and modified spec file to use
  the autoconf/automake support in the latest CVS

* Tue Apr 30 2002 Edward Rudd <eddie@omegaware.com>
- Initial spec file
