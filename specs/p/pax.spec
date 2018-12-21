Name: pax
Version: 3.4
Release: alt7

Summary: POSIX File System Archiver
License: BSD
Group: Archiving/Backup
URL: http://ftp.suse.com/pub/people/kukuk/pax
Source: %url/pax-%version.tar.bz2
Patch1: pax-3.4-rdtruncate.patch
Patch2: pax-3.4-abs100.patch
Patch3: pax-3.4-PATHMAX.patch
Patch4: pax-3.4-rh-gcc46.patch
Patch5: %name-%version-alt-includes.patch
Patch6: %name-%version-alt-gcc8.patch

%description
'pax' is the POSIX standard archive tool. It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p2

%build
%add_optflags -Wno-error=implicit-fallthrough
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4-alt7
- Fixed build with gcc-8.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4-alt6
- Fixed build with new toolchain.

* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4-alt5
- Fixed build with current toolchain.

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 3.4-alt4
- Reverted previous change.

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt3.1
- Removed -Werror from compiler flags

* Thu Jul 12 2012 Dmitry V. Levin <ldv@altlinux.org> 3.4-alt3
- Fixed build with new gcc.

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 3.4-alt2
- Add patches from Fedora.

* Thu Oct 27 2005 Victor Forsyuk <force@altlinux.ru> 3.4-alt1
- 3.4 (LFS supported in this version).

* Tue Oct 05 2004 Stanislav Ievlev <inger@altlinux.org> 3.2-alt1
- 3.2

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1-alt1
- Inital release
