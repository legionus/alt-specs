Name: libzio
Version: 1.06
Release: alt1

Summary: A library for accessing compressed text files
License: GPLv2+
Group: System/Libraries
Url: http://libzio.sourceforge.net/

# http://downloads.sourceforge.net/libzio/libzio-%version.tar.bz2
Source: libzio-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: zlib-devel bzlib-devel liblzma-devel xz

%package devel
Summary: Development files for the libzio library
Group: Development/C
Requires: %name = %version-%release

%description
Libzio provides a wrapper function for reading or writing gzip, bzip2
and lzma-compressed files with FILE streams.

%description devel
Libzio provides a wrapper function for reading or writing gzip, bzip2
and lzma-compressed files with FILE streams.

This package contains library and header files needed for
building libzio-aware applications.

%prep
%setup
%patch -p1

%build
%def_enable Werror
%make_build libdir=/%_lib noweak tests testt testx

%install
%make_install install-shared install-data \
	DESTDIR=%buildroot libdir=/%_lib mandir=%_mandir

# Relocate development library from /%_lib/ to %_libdir/.
mkdir -p %buildroot%_libdir
for f in %buildroot/%_lib/*.so; do
	t=$(readlink "$f")
	ln -s ../../%_lib/"$t" "%buildroot%_libdir/${f##*/}"
	rm "$f"
done

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
rm -f sample* out
for s in gz bz2 lzma xz; do
	ln -s sample sample.$s
done
for f in *; do
	[ -f "$f" -a ! -L "$f" ] || continue
	for comp in gzip bzip2 lzma xz; do
		$comp -c < "$f" > sample
		for s in '' .gz .bz2 .lzma .xz; do
			LD_LIBRARY_PATH=%buildroot/%_lib ./testt sample$s > out
				cmp "$f" out
			cat sample$s |
				LD_LIBRARY_PATH=%buildroot/%_lib ./tests ${comp:0:1} > out
				cmp "$f" out
		done
	done
done
rm sample* out
for f in *; do
	[ -f "$f" -a ! -L "$f" ] || continue
	rm -f sample*
	LD_LIBRARY_PATH=%buildroot/%_lib ./testx < "$f" > sample ''
	cmp "$f" sample
	LD_LIBRARY_PATH=%buildroot/%_lib ./testx < "$f" > sample.gz g
	gzip -dc <sample.gz |cmp "$f" -
	LD_LIBRARY_PATH=%buildroot/%_lib ./testx < "$f" > sample.bz2 b
	bzip2 -dc <sample.bz2 |cmp "$f" -
	LD_LIBRARY_PATH=%buildroot/%_lib ./testx < "$f" > sample.xz x
	xz -dc <sample.xz |cmp "$f" -
	LD_LIBRARY_PATH=%buildroot/%_lib ./testx < "$f" > sample.lzma l
	lzma -dc <sample.lzma |cmp "$f" -
done

%files
%doc README
/%_lib/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%changelog
* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 1.06-alt1
- 1.04 -> 1.06.
- Fixed build without libio.h.
- Fixed lzma support broken upstream.

* Fri Mar 17 2017 Dmitry V. Levin <ldv@altlinux.org> 1.04-alt1
- 1.02 -> 1.04.

* Fri Nov 01 2013 Dmitry V. Levin <ldv@altlinux.org> 1.02-alt1
- Updated to 1.02.

* Sat Feb 19 2011 Alexey Tourbin <at@altlinux.ru> 0.99-alt8
- Fixed support for write-mode compression levels.

* Fri Feb 18 2011 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt7
- Rebuilt for debuginfo.

* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt6
- Rebuilt with liblzma.so.5.

* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt5
- Rebuilt for soname set-versions.

* Mon Sep 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt4
- Fixed bzip2 support in write mode (reported by Alexey Tourbin).
- Fixed lzma and xz support in write mode.
- Added write test to the testsuite.

* Thu Sep 24 2009 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt3
- Risen priority for compression method guess made by magic probe.

* Thu Sep 24 2009 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt2
- Moved running tests to %%check section.
- Add xz support: build with liblzma-devel/xz instead of
  liblzmadec-devel/lzma-utils.

* Sat May 16 2009 Dmitry V. Levin <ldv@altlinux.org> 0.99-alt1
- Updated to 0.99.

* Mon Dec 15 2008 Dmitry V. Levin <ldv@altlinux.org> 0.91-alt1
- Updated to 0.91.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Updated to 0.4.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt5
- Uncompressed tarball.

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt4
- Fixed build with --as-needed.

* Mon Aug 15 2005 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt3
- Restricted list of global symbols exported by the library.

* Wed Jun 15 2005 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt2
- Relocated shared library from %_libdir to /%_lib (fixes #7093).

* Thu Nov 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
