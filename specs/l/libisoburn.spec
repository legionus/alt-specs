Name: libisoburn
Version: 1.5.0
Release: alt1

Summary: ISO9660 filesystem creation library
License: GPLv2
Group: System/Libraries

Url: http://libburnia-project.org
Source: %name-%version.tar

BuildRequires: zlib-devel libacl-devel libattr-devel libreadline-devel
BuildRequires: libburn-devel >= %version, libisofs-devel >= %version
BuildRequires: texinfo
# For tests
BuildRequires: gcc-c++

%description
libisoburn is a frontend for libraries libburn and libisofs
which enables creation and expansion of ISO-9660 filesystems
on all CD/DVD media supported by libburn. This includes media
like DVD+RW, which do not support multi-session management
on media level and even plain disk files or block devices.

The price for that is thorough specialization on data files
in ISO-9660 filesystem images. So libisoburn is not suitable
for audio (CD-DA) or any other CD layout which does not entirely
consist of ISO-9660 sessions.

Currently it is only supported on Linux with kernels >= 2.4.

%package devel
Summary: Development files for libisofs
Group: System/Libraries
Requires: %name = %version

%description devel
libisoburn is a frontend for libraries libburn and libisofs
which enables creation and expansion of ISO-9660 filesystems
on all CD/DVD media supported by libburn. This includes media
like DVD+RW, which do not support multi-session management
on media level and even plain disk files or block devices.

The price for that is thorough specialization on data files
in ISO-9660 filesystem images. So libisoburn is not suitable
for audio (CD-DA) or any other CD layout which does not entirely
consist of ISO-9660 sessions.

Currently it is only supported on Linux with kernels >= 2.4.

This package contains development headers.

%package -n xorriso
Summary: Creates an image of an ISO9660 filesystem
Group: Archiving/Cd burning
Requires: %name = %version
Requires: libburn >= %version

%description -n xorriso
xorriso is a program which maps file objects from POSIX compliant
filesystems into Rock Ridge enhanced ISO 9660 filesystems and
allows session-wise manipulation of such filesystems. It can load
the management information of existing ISO images and it writes
the session results to optical media or to filesystem objects.

Currently it is only supported on Linux with kernels >= 2.4.

A special property of xorriso is that it needs neither an external
ISO 9660 formatter program nor an external burn program for CD
or DVD but rather incorporates the libraries of libburnia-project.org .

%package -n xorriso-x11
Summary: Graphical utility to create ISO9660 image
Group: Archiving/Cd burning
Requires: xorriso = %version
BuildArch: noarch

%description -n xorriso-x11
This package contains GUI for xorriso, a program to create
or extract ISO9660 images common for CD-ROM/DVD media.

%prep
%setup
touch NEWS

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%check
# From Fedora
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%buildroot%_libdir"
export TERM="xterm"
cd releng
if ! ./run_all_auto -x ../xorriso/xorriso; then
	cat releng_generated_data/log.*
	exit 1
fi

%files
%_libdir/%name.so.*

%files devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/%name.so
%_pkgconfigdir/*.pc

%files -n xorriso
%_man1dir/*
%_infodir/*
%_bindir/*
%exclude %_bindir/xorriso-tcltk

%files -n xorriso-x11
%_bindir/xorriso-tcltk

%changelog
* Mon Oct 15 2018 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Dec 10 2015 Michael Shigorin <mike@altlinux.org> 1.3.4-alt3
- x11 subpackage made noarch

* Wed Dec 09 2015 Michael Shigorin <mike@altlinux.org> 1.3.4-alt2
- added explicit BR: texinfo to fix FTBFS

* Fri Dec 20 2013 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated Url:

* Wed Dec 11 2013 Michael Shigorin <mike@altlinux.org> 1.2.6-alt2
- xorriso-tcltk moved to xorriso-x11 subpackage, shame on slow me!

* Sun Feb 24 2013 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- 1.2.6
- minor spec cleanup according to policy recommendations

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt3
- clarified libburn dependency as versioned for xorriso (thx amike@)

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt2
- clarified libburn-devel build dependency as versioned
- minor description readability fixup

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Mar 21 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Oct 31 2011 Mikhail Efremov <sem@altlinux.org> 1.1.6-alt1
- tests: Fix for as_needed.
- Enable tests.
- Add zlib-devel, libacl-devel, libattr-devel, libreadline-devel to BR.
- Remove obsoleted patch.
- sources: tar.gz -> tar.
- Updated to 1.1.6.

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8.pl00-alt1
- new upstream version

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.6.pl00-alt1
- new upstream version

* Thu Sep 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.2.pl00-alt1
- new upstream version

* Thu May 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.6.pl00-alt1
- new upstream version

* Mon Nov 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.2.pl02-alt1
- new upstream version

* Tue Jul 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0.pl00-alt1
- new version
- buffer overflow fixed

* Tue Apr 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.6.pl00-alt1
- new version
- additional binaries in xorriso subpackage

* Thu May 01 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.4-alt1
- new version 

* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.0-alt1
- Initial build

