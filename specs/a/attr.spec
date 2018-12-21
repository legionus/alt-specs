Name: attr
Version: 2.4.48.0.7.14ad
Release: alt1

Summary: Utilities for managing filesystem extended attributes
License: GPLv2+
Group: File tools
Url: http://savannah.nongnu.org/projects/attr
# git://git.altlinux.org/gears/a/attr.git
Source: %name-%version-%release.tar

Requires: lib%name = %version-%release

%define _libexecdir %_libdir
%def_enable static

%description
A set of tools for manipulating extended attributes on filesystem
objects, in particular getfattr(1) and setfattr(1).
An attr(1) command is also provided which is largely compatible
with the SGI IRIX tool of the same name.

%package -n lib%name
Summary: Dynamic library for extended attribute support
License: LGPLv2+
Group: System/Libraries

%package -n lib%name-devel
Summary: Extended attribute development library and headers files
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: Static library for extended attribute support
License: LGPLv2+
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with lib%name.

%description -n lib%name-devel
This package contains the development library and header files
needed to develop programs which make use of extended attributes.
For Linux programs, the documented system call API is the
recommended interface, but an SGI IRIX compatibility interface
is also provided.

Currently only ext2, ext3, JFS and XFS support extended attributes.
The SGI IRIX compatibility API built above the Linux system calls is
used by programs such as xfsdump(8), xfsrestore(8) and xfs_fsr(8).

%description -n lib%name-devel-static
This package contains the static library needed to develop
statically linked programs which make use of extended attributes.

%prep
%setup

%build
./autogen.sh
%configure %{subst_enable static}
%make_build V=1

%install
%makeinstall_std dist_doc_DATA='README doc/CHANGES'

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%find_lang %name
%set_verify_elf_method strict

%check
if ./setfattr -n user.name -v value .; then
	%make_build -k check
else
	echo 'xattrs are probably not supported by the file system'
	stat -f .
fi

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_docdir/%name/

%files -n lib%name
%config(noreplace) %_sysconfdir/xattr.conf
/%_lib/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_man3dir/*
%_includedir/*
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Sun Dec 02 2018 Dmitry V. Levin <ldv@altlinux.org> 2.4.48.0.7.14ad-alt1
- v2.4.48 -> v2.4.48-7-g14adc89.

* Mon Nov 27 2017 Dmitry V. Levin <ldv@altlinux.org> 2.4.48-alt1
- v2.4.47-44-g315af30 -> v2.4.48.
- getfattr: fixed large-file support.

* Wed Nov 08 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.47.0.44.315a-alt2
- Reenabled static subpackage (needed for static qemu-user to support *attr
  syscalls).

* Mon Jul 04 2016 Dmitry V. Levin <ldv@altlinux.org> 2.4.47.0.44.315a-alt1
- v2.4.47-35-gdce9b44 -> v2.4.47-44-g315af30 (closes: #32244).

* Mon Sep 21 2015 Dmitry V. Levin <ldv@altlinux.org> 2.4.47.0.35.dce9-alt2
- attr/xattr.h: Reintroduced more old stuff for backwards compatibility.

* Tue Sep 15 2015 Dmitry V. Levin <ldv@altlinux.org> 2.4.47.0.35.dce9-alt1
- Updated to v2.4.47-35-gdce9b44.

* Sat Sep 21 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.47-alt1
- Updated to v2.4.47-4-gda8435b.

* Sun Apr 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.46-alt2
- attr_copy_{fd,file}: handle empty xattr lists efficiently.

* Tue Sep 20 2011 Dmitry V. Levin <ldv@altlinux.org> 2.4.46-alt1
- Updated to v2.4.46-3-g9bf1321.

* Mon Mar 07 2011 Dmitry V. Levin <ldv@altlinux.org> 2.4.44-alt1
- Updated to v2.4.44-13-g0a2d62b (closes: #25199).
- Applied few fixes from Fedora attr-2.2.44-6.
- Fixed some compilation warnings.
- Cleaned up specfile.
- Disabled build and packaging of the static library.

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.43-alt3
- rebuilt with set-versioned rpm

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.43-alt2
- obsolete by filetriggers macros removed

* Thu Nov  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.43-alt1
- 2.4.43

* Mon Mar 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.41-alt1
- 2.4.41

* Tue Sep 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.39-alt1
- 2.4.39

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.32-alt1.0
- Automated rebuild.

* Thu Sep 14 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.32-alt1
- 2.4.32

* Mon Aug 30 2004 Anton D. Kachalov <mouse@altlinux.org> 2.4.15-alt2
- Multilib support (#5093)

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 2.4.15-alt1
- 2.4.15

* Thu Dec 11 2003 Alexander Bokovoy <ab@altlinux.ru> 2.4.12-alt1
- 2.4.12

* Thu Aug 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt2
- Explicitly use old libtool for build.
- Corrected interpackage dependencies.
- Fixed -devel packaging.

* Tue May 20 2003 Alexander Bokovoy <ab@altlinux.ru> 2.2.0-alt1
- 2.2.0, maintainer change.
- Updated buildrequires
- removed outdated patches

* Fri Dec 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.8-alt1
- 2.0.8
- Added buildrequires

* Wed Apr 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.5-alt0.1cvs
- 2.0.5

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt3
- Rebuilt with libxfs 1.3.13

* Wed Oct 31 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt2
- Rebuilt with libxfs 1.3.7

* Thu Sep 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt1
- First build for Sisyphus

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.3-2mdk
- Fix provides.

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.3-1mdk
- Rework the .spec.
- Make libs in subpackage.
- 1.1.3.

* Wed May  2 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-1mdk
- First attempt.


