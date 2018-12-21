%define binutils_sourcedir /usr/src/binutils-source

Name: binutils
Version: 2.31.1
Release: alt4
Epoch: 1

Summary: GNU Binary Utility Development Utilities
License: GPLv3+
Group: Development/Other
Url: http://sourceware.org/binutils/

# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.xz
Source: %name-%version.tar
Source1: bfd.h
Source2: gcc.sh
Source3: g++.sh
Source4: ld.sh
Source5: output-format.sed

Patch: binutils-2_31-branch.patch

Patch1: 0001-Add-lto-and-none-lto-input-support-for-ld-r.patch
Patch2: 0002-Add-test-for-nm-on-mixed-LTO-non-LTO-object.patch
Patch3: 0003-Don-t-check-the-plugin-target-twice.patch
Patch4: 0004-Handle-ELF-compressed-header-alignment-correctly-by-.patch
Patch5: 0005-Initialize-uncompressed_align_pow_p-to-0.patch
Patch6: 0006-gold-Get-alignment-of-uncompressed-section-from-ch_a.patch
Patch7: 0007-ld-testsuite-ld-ifunc-pr18808b.c-pass-Wno-return-typ.patch
Patch8: 0008-ld-testsuite-ld-elf-pr22269-1.c-pass-Wno-return-type.patch
Patch9: 0009-bfd-export-demangle.h-and-hashtab.h.patch
Patch10: 0010-ld-add-no-warn-shared-textrel-option.patch
Patch11: 0011-ld-enable-optimization-and-warn-shared-textrel-by-de.patch
Patch12: 0012-ld-enable-z-relro-by-default.patch
Patch13: 0013-gold-enable-z-relro-by-default.patch
Patch14: 0014-ld-testsuite-restore-upstream-default-options.patch
Patch15: 0015-gold-testsuite-use-sysv-hash-style-for-two-tests.patch
Patch16: 0016-bfd-elflink.c-bfd_elf_final_link-check-all-objects-f.patch

# List of architectures worthy to care about test results.
%define check_arches x86_64 %ix86
%def_with check

Conflicts: libbfd
# due to c++filt
Conflicts: gcc-common < 0:1.2.1-alt4

BuildRequires: flex makeinfo perl-Pod-Parser zlib-devel
BuildRequires: gcc-c++ libstdc++-devel-static
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu, gcc-c++, glibc-devel-static, zlib-devel-static, bc, /proc, /dev/pts}}

%package devel
Summary: Development files for development with BFD, opcodes and libiberty libraries
Group: Development/C
Requires: zlib-devel-static
Provides: libiberty-devel = %epoch:%version-%release
Provides: libbfd-devel = %epoch:%version-%release
Obsoletes: libiberty-devel
Obsoletes: libbfd-devel

%package source
Summary: Binutils sources
Group: Development/Other
BuildArch: noarch

%description
Binutils is a collection of binary utilities, including:
+ addr2line: converting addresses to file and line;
+ ar: creating modifying and extracting from archives;
+ nm: listing symbols from object files;
+ objcopy: copying and translating object files;
+ objdump: displaying information from object files;
+ ranlib: generating an index for the contents of an archive;
+ size: listing the section sizes of an object or archive file;
+ strings: listing printable strings from files;
+ strip: discarding symbols.

%description devel
This package contains include files, dynamic and static libraries needed
for development software based on Binary File Descriptor library and
libiberty.

%description source
This package contains source code of GNU Binutils.

%prep
%setup

%patch -p1
chmod +x gold/testsuite/plugin_pr22868.sh

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

# Replay libtool commits
# a042d335197ac7afb824ab54c3aab91f3e79a2d0
# 9e68384a4fac10585e54519a3f1925cb99d338e8
sed -i -e '
/^      \*32-bit\*)$/ a \
	libsuff=x32
/^      \*64-bit\*)$/ a \
	libsuff=64
s,sys_lib_search_path_spec="/lib /usr/lib /usr/local/lib",sys_lib_search_path_spec="/lib$libsuff /usr/lib$libsuff /usr/local/lib$libsuff",
s,sys_lib_dlsearch_path_spec="/lib /usr/lib",sys_lib_dlsearch_path_spec="/lib$libsuff /usr/lib$libsuff",
s,sys_lib_dlsearch_path_spec="/lib /usr/lib \$lt_ld_extra",sys_lib_dlsearch_path_spec="$sys_lib_dlsearch_path_spec $lt_ld_extra",
s,x86_64-\*kfreebsd\*-gnu|x86_64-\*linux\*|powerpc\*-\*linux\*|,aarch64*-*linux*|riscv64*-*linux*|mips64*-*linux*|&,
' libtool.m4 */configure

sed -i 's/%%{release}/%release/g' bfd/Makefile{.am,.in}

%build
%define _configure_target --host=%_target_platform --build=%_target_platform
%undefine __libtoolize
ADDITIONAL_TARGETS=
%ifarch %ix86 x86_32
ADDITIONAL_TARGETS="--enable-64-bit-bfd"
%endif
%ifarch ia64 x86_64
ADDITIONAL_TARGETS="--enable-targets=i386-alt-linux"
%endif
%ifarch ppc
ADDITIONAL_TARGETS="--enable-targets=powerpc64-alt-linux --enable-targets=spu --enable-64-bit-bfd"
%endif
%configure \
	--with-system-zlib \
	--enable-shared \
	--with-pic \
	--disable-werror \
	--enable-plugins \
	--with-bugurl=http://bugzilla.altlinux.org/ \
	--enable-gold=yes --enable-ld=default \
	--with-stage1-ldflags=' ' \
	--with-boot-ldflags=' ' \
%ifnarch mipsel mips64el
	--enable-default-hash-style=gnu \
%endif
	$ADDITIONAL_TARGETS

for t in configure-host maybe-all-{libiberty,bfd,opcodes} all; do
	%make_build MAKEINFOFLAGS=--no-split tooldir=%_prefix $t
done

%install
%makeinstall_std tooldir=%_prefix install-info

# Install ld.default and ld wrapper.
ln -snf ld.bfd %buildroot%_bindir/ld.default
install -pm755 %_sourcedir/ld.sh %buildroot%_bindir/ld

# Install PIC version of the libiberty.a
install -pm644 libiberty/pic/libiberty.a %buildroot%_libdir/

# Remove unrelated manpages.
find %buildroot%_man1dir -type f |while read f; do
	n="${f##*/}"
	n="${n%%.1*}"

	[ -f "%buildroot%_bindir/$n" ] || rm -v "$f"
done

%ifarch %ix86 x86_32 ppc
# Sanity check --enable-64-bit-bfd really works.
grep -Fqsx '#define BFD_ARCH_SIZE 64' %buildroot%_prefix/include/bfd.h
%endif

# Generate .so linker scripts for dependencies; imported from glibc/Makerules:

# Remove symlinks
rm -f %buildroot%_libdir/lib{bfd,opcodes}.so

# This fragment of linker script gives the OUTPUT_FORMAT statement
# for the configuration we are building.
OUTPUT_FORMAT="\
/* Ensure this .so library will not be used by a link for a different format
   on a multi-architecture system.  */
$(gcc $CFLAGS $LDFLAGS -shared -x c /dev/null -o /dev/null -Wl,--verbose -v 2>&1 |
	sed -n -f "%_sourcedir/output-format.sed")"

cat >%buildroot%_libdir/libbfd.so <<EOF
/* GNU ld script */

$OUTPUT_FORMAT

/* The -lz and -ldl dependencies are unexpected by legacy build scripts.  */
INPUT ( %_libdir/libbfd.a -liberty -ldl -lz )
EOF

cat >%buildroot%_libdir/libopcodes.so <<EOF
/* GNU ld script */

$OUTPUT_FORMAT

INPUT ( %_libdir/libopcodes.a -lbfd )
EOF

# Relocate include files.
pushd %buildroot%_includedir
	mkdir bfd
	for f in *.h; do
		mv "$f" bfd/
		ln -s bfd/"$f" .
	done
popd

# Cleanup config.h remnants
sed -i '/PR 14072:/,/^#endif/d' %buildroot%_includedir/bfd/bfd.h
sed -i '/HAVE_STDINT_H/,/^#endif/d; /#include <sys\/types.h>/i#include <stdint.h>' \
	%buildroot%_includedir/bfd/plugin-api.h

# Workaround multilib issues
wordsize=$(printf '%%s\n%%s' '#include <bits/wordsize.h>' '__WORDSIZE' | gcc -E -P -)
mv %buildroot%_includedir/bfd/bfd{,-$wordsize}.h
install -pm644 %_sourcedir/bfd.h %buildroot%_includedir/bfd/

# Add more include files.
install -pm644 include/libiberty.h %buildroot%_includedir/
install -pm644 bfd/{elf-bfd,lib*}.h %buildroot%_includedir/bfd/
cp -a include/{coff,elf} %buildroot%_includedir/bfd/
rm %buildroot%_includedir/bfd/{*in.h,*/ChangeLog*}

# Install NEWS.
for n in binutils gas ld; do
	install -pm644 $n/NEWS NEWS-$n
done

mkdir -p %buildroot%binutils_sourcedir
cp %SOURCE0 %buildroot%binutils_sourcedir/
cp %PATCH0 %buildroot%binutils_sourcedir/

%find_lang binutils bfd gas gold gprof ld opcodes --append --output files.lst

%set_verify_elf_method strict

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
# testsuite requires gcc to be able to print path to liblto_plugin.so
GCC_PFN_LTO=$(gcc -print-file-name=liblto_plugin.so)
GCC_PPN_LTO=$(gcc -print-prog-name=liblto_plugin.so)
[ "$GCC_PFN_LTO" != 'liblto_plugin.so' -o "$GCC_PPN_LTO" != 'liblto_plugin.so' ] || exit
RUNTESTFLAGS=
XFAIL_TESTS=
%ifarch %ix86
# See https://sourceware.org/bugzilla/show_bug.cgi?id=21128
XFAIL_TESTS="$XFAIL_TESTS icf_safe_so_test.sh"
%endif

%make_build -k check CC="%_sourcedir/gcc.sh" CXX="%_sourcedir/g++.sh" \
	XFAIL_TESTS="$XFAIL_TESTS" RUNTESTFLAGS="$RUNTESTFLAGS" \
%ifnarch %check_arches
    || : \
%endif
    #


%files devel
%_libdir/*.a
%_libdir/libbfd.so
%_libdir/libopcodes.so
%_includedir/bfd/
%_includedir/*.h
%_infodir/bfd.info*

%files -f files.lst
%_bindir/*
%_prefix/lib/ldscripts/
%_mandir/man?/*
%_libdir/*-*.so
%_infodir/*.info*
%exclude %_infodir/bfd.info*
%doc NEWS*

%files source
%binutils_sourcedir

%changelog
* Sun Dec 02 2018 Dmitry V. Levin <ldv@altlinux.org> 1:2.31.1-alt4
- Updated to 2.31.1 20181202.
- gold: applied upstream fix for ELF compressed data alignment (sw#23919).
- Built with system zlib.

* Fri Nov 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1:2.31.1-alt3
- Updated to 2.31.1 20181130.
- gold: applied a fix for ELF compressed data alignment
  (sw#23919; patch by H.J. Lu).

* Thu Nov 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.31.1-alt2
- Fixed ELF compressed data alignment (sw#23919; patch by Mark Wielaard).
- Disabled gold debug_msg.sh test for x86_64.
- Applied mips-related spec changes from Ivan A. Melnikov (iv@; ALT#35638):
  + Do not force gnu-style hash on mips* architectures (it is
    not currently supported);
  + Run testsuite on non-worthy architectures, but ignore results.

* Thu Nov 08 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.31.1-alt1
- Updated to 2.31.1 20181107.

* Wed Aug 08 2018 Dmitry V. Levin <ldv@altlinux.org> 1:2.30.0-alt2
- Dropped ld.bfd/ld.gold alternatives in favour of ld wrapper setup:
  use LD_FLAVOUR=bfd/gold to control the flavour of ld.

* Mon May 28 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.30.0-alt1
- Updated to 2.30.0 20180528.
- Packaged binutils sources as separate package.

* Thu Nov 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.27.0-alt1
- Updated to 2.27.0 20161101.

* Fri Jul 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.26.1-alt1
- Updated to 2.26.1 20160701.

* Fri Apr 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.26.0-alt1.1
- Applied upstream fix for sw#19886.

* Thu Mar 24 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.26.0-alt1
- Updated to 2.26.0 20160318.

* Tue Dec 22 2015 Dmitry V. Levin <ldv@altlinux.org> 1:2.24.0-alt5
- %%check: xfailed failing gold tests.

* Mon Dec 21 2015 Dmitry V. Levin <ldv@altlinux.org> 1:2.24.0-alt4
- Applied backports prepared by Nick Clifton that fix
  CVE-2014-848[45], CVE-2014-850[1234], and CVE-2014-873[78].
- strings: enabled --all option by default, added --data option
  (by Nick Clifton; addresses past and future CVEs wrt strings(1)).

* Fri Nov 28 2014 Dmitry V. Levin <ldv@altlinux.org> 1:2.24.0-alt3
- Applied upstream fix for sw#16457.

* Fri Oct 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.24.0-alt2
- Fixed ld and gold tests (gcc4.9).

* Mon Jan 13 2014 Dmitry V. Levin <ldv@altlinux.org> 1:2.24.0-alt1
- Updated to 2.24.0 20140113.
- ld, gold: changed defaults:
  + enabled -z relro by default;
  + changed default hash style to gnu.

* Wed Oct 31 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.23.51.0.1-alt2
- Fixed build.

* Wed Aug 29 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.23.51.0.1-alt1
- Updated to 2.23.51.0.1.

* Mon Jul 16 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.22.52.0.4-alt2
- %_includedir/bfd/bfd.h: removed unsuitable checks.

* Mon Jul 16 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.22.52.0.4-alt1
- Updated to 2.22.52.0.4.

* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.22.52.0.3-alt2
- Added -ldl to libbfd.so.

* Tue May 15 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.22.52.0.3-alt1
- Updated to 2.22.52.0.3.

* Tue Jan 25 2011 Kirill A. Shutemov <kas@altlinux.org> 1:2.21.51.0.6-alt1
- 2.21.51.0.6

* Mon Jan 24 2011 Kirill A. Shutemov <kas@altlinux.org> 1:2.21.51.0.5-alt1
- Sync with Fedora 2.21.51.0.5-1

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.20.51.0.12-alt3
- binutils-devel: added Provides/Obsoletes for libbfd-devel, for
  backwards compatibility, because some packages need only header files
  from former libbfd-devel.

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.12-alt2
- Merge all -devel packages into binutils-devel:
  + replace libbfd.so and libopcodes.so with linker script to use static
    libraries for linking external programs;
  + merge with libiberty-devel to avoid cyclical dependences;
  + no Provides/Obsoletes for libbfd-devel-static: no users in Sisyphus;
  + no Provides/Obsoletes for libbfd-devel: have to rebuild users
    anyway;
- Fix alignment for common symbols in BFD linker plugin (closes: 24754)

* Sun Nov 14 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.12-alt1
- Sync with Fedora 2.20.51.0.12-1

* Sun Nov 14 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.20.51.0.11-alt2
- Updated build dependencies to fix build with new perl.

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.11-alt1
- Sync with Fedora 2.20.51.0.11-1

* Mon Jun 21 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.9-alt1
- 2.20.51.0.9
- Sync patches with Fedora 2.20.51.0.7-4

* Wed Mar 31 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.7-alt3
- Package ld manpage (closes: 23259)

* Sat Mar 27 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.7-alt2
- Do not package %_bindir/ld to avoid conflict with alternatives

* Wed Mar 24 2010 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.7-alt1
- 2.20.51.0.7
- Sync patches with Fedora 2.20.51.0.2-17
- Package gold linker as %_bindir/ld.gold
- Alternativies for %_bindir/ld. Use GNU ld (ld.bfd) by default

* Mon Dec 28 2009 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.4-alt1
- 2.20.51.0.4 (closes: 22582)
- Sync patches with 2.20.51.0.2-11 and rebase RH patches to 2.20.51.0.4
  + Apply patches for PR 11088

* Tue Oct 20 2009 Kirill A. Shutemov <kas@altlinux.org> 1:2.20.51.0.2-alt1
- Synced with FC 2.20.51.0.2-1
- Fix tests to pass on ARM

* Thu Oct 01 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.19.51.0.14-alt4
- Make tests pass on ARM (by Kirill A. Shutemov).

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.19.51.0.14-alt3
- Moved "make check" to %%check section.

* Thu Aug 27 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.19.51.0.14-alt2
- Built for Sisyphus.

* Sat Aug 22 2009 Kirill A. Shutemov <kas@altlinux.org> 1:2.19.51.0.14-alt1
- Synced with FC 2.19.51.0.14-31.
- Rebased patches.
- Backported upstream fixes for -pie issues with TLS relocations.

* Tue Jun 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.19.51.0.2-alt2
- Synced with FC 2.19.51.0.2-19.
- Fixed testsuite to make it build with fresh glibc.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Fri May 01 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.19.51.0.2-alt1
- Updated upstream source to 2.19.51.0.2.
- Synced with FC 2.19.51.0.2-18.
- Reenabled translations packaging.

* Fri Mar 20 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.18.50.0.9-alt5
- Synced with FC 2.18.50.0.9-8.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.18.50.0.9-alt4
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Fri Nov 07 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.18.50.0.9-alt3
- Synced with FC 2.18.50.0.9-7.
- Removed -%%release from soname.

* Tue Oct 07 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.18.50.0.9-alt2
- Synced with FC 2.18.50.0.9-5.
- Updated alt-defaults.patch and testsuite.
- Configure with more additional targets.
- Build with zlib to enable compressed sections support.
- Fixed multilib conflicts in bfd.h
- Disabled relax of bfd/elflink symbols checking.
- Packaged NEWS files.
- Fixed libopcodes build on some arches (e.g. arm).

* Sat Sep 13 2008 Wartan Hachaturow <wart@altlinux.org> 1:2.18.50.0.9-alt1
- Synced with FC10 2.18.50.0.9-1.

* Thu Sep 04 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.6-alt5
- Synced with RH 2.17.50.0.6-6.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.6-alt4
- Fixed build with fresh makeinfo.

* Mon Jan 07 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.6-alt3
- Fixed libopcodes build to link with PIC libiberty.

* Sun Sep 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.6-alt2
- Synced with RH 2.17.50.0.6-5.

* Mon Jan 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.6-alt1
- Synced with RH 2.17.50.0.6-3.

* Fri Aug 18 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.3-alt1
- Synced with RH 2.17.50.0.3-2.
- Updated testsuite for defaults changed in 2.16.91.0.5-alt2.

* Thu Jun 29 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.2-alt4
- Synced with RH 2.17.50.0.2-4.

* Tue Jun 27 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.2-alt3
- Synced with RH 2.17.50.0.2-3.

* Sat Jun 03 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.2-alt2
- Updated from CVS to 20060601.
- Synced with RH 2.17.50.0.2-1.

* Mon May 29 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.2-alt1
- Updated to 2.17.50.0.2.

* Tue May 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.17.50.0.1-alt1
- Updated to 2.17.50.0.1, Synced with RH 2.17.50.0.1-1.

* Wed Mar 15 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.6-alt2
- Synced with RH 2.16.91.0.6-4.
- Applied upstream fix for ld --as-needed problem (#9247).

* Thu Feb 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.6-alt1
- Updated to 2.16.91.0.6, synced with RH 2.16.91.0.6-1.

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.5-alt3
- Link libopcodes with libbfd.
- Set %%_verify_elf_method to strict, better safe than sorry.

* Mon Jan 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.5-alt2
- ld: enabled -O1 by default,
  enabled --warn-shared-textrel by default,
  implemented --no-warn-shared-textrel option.

* Thu Jan 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.5-alt1
- Updated to 2.16.91.0.5, synced with RH 2.16.91.0.5-1.

* Sat Dec 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.3-alt2
- Synced with RH binutils-2.16.91.0.3-2.

* Sun Dec 04 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.16.91.0.3-alt1
- Updated to 2.16.91.0.3, synced with RH 2.16.91.0.3.
- Removed merged upstream alt-strings-mem patch.
- Reverted to upstream soname scheme.

* Sun May 29 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2.2-alt3
- Removed obsolete bfd_elf_local_sym_name patch.
- Enhanced alt-strings-mem patch.

* Fri May 27 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2.2-alt2
- Applied upstream fix for unsanitized input issues in the BFD library
  (CAN-2005-1704) and readlink utility.

* Wed Apr 06 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2.2-alt1
- Updated to 2.15.94.0.2.2, synced with RH 2.15.94.0.2.2-1.

* Thu Mar 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2-alt3
- strings: fixed OOM handling (closes #5871).

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2-alt2
- readelf: fixed potential buffer overflows, patch from Jakub Jelinek.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.94.0.2-alt1
- Updated to 2.15.94.0.2, synced with RH 2.15.94.0.2-1.

* Fri Dec 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.92.0.2-alt4
- Synced with RH binutils-2.15.92.0.2-11.

* Tue Nov 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.92.0.2-alt3
- Synced with RH binutils-2.15.92.0.2-6.

* Wed Nov 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.92.0.2-alt2
- Applied bfd_elf_local_sym_name patch from SuSE.

* Tue Nov 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.92.0.2-alt1
- Updated to 2.15.92.0.2, synced with RH binutils-2.15.92.0.2-5.

* Thu Jun 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.90.0.3-alt3
- Synced with RH 2.15.90.0.3-7.

* Sat May 15 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.90.0.3-alt2
- Synced with RH 2.15.90.0.3-5.

* Mon Apr 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.90.0.3-alt1
- Updated to 2.15.90.0.3, synced with RH 2.15.90.0.3-2.

* Mon Apr 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.15.90.0.1.1-alt1
- Updated to 2.15.90.0.1.1, synced with RH 2.15.90.0.1.1-2.

* Thu Jan 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.8-alt1
- Updated to 2.14.90.0.8.
- Synced with RH 2.14.90.0.8-3:
  * Fri Jan 16 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-2
  - fix testcases on AMD64
  - fix .got's sh_entsize on IA32/AMD64
  - set COMMONPAGESIZE on s390/s390x
  - set COMMONPAGESIZE on ppc32 (Alan Modra)
  * Tue Jan 13 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-4
  - fix -z relro on 64-bit arches
  * Mon Jan 12 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-3
  - fix some bugs in -z relro support
  * Fri Jan  9 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-2
  - -z relro support, reordering of RW sections
- Dropped ugly Russian translation introduced in bintutils snapshot 2004-01-02.

* Sun Jan 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.7-alt1
- Updated to 2.14.90.0.7.

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.6-alt3
- Synced with RH 2.14.90.0.6-4:
  * Mon Nov 24 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-4
  - fix assembly parsing of foo=(.-bar)/4 (Alan Modra)
  - fix IA-64 assembly parsing of (p7) hint @pause
  * Tue Sep 30 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-3
  - don't abort on some linker warnings/errors on IA-64

* Tue Dec 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.6-alt2
- Do not package .la files.

* Wed Sep 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.6-alt1
- Synced with RH 2.14.90.0.6-2:
  * Sat Sep 20 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-2
  - fix up merge2.s to use .p2align instead of .align
  * Sat Sep 20 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-1
  - update to 2.14.90.0.6
  - speed up string merging (Lars Knoll, Michael Matz, Alan Modra)
  - speed up IA-64 local symbol handling during linking
  * Fri Aug 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-6
  - SPARC .cfi* support

* Tue Aug 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.5-alt2
- Fixed rh-place-orphan patch (added in previous release).

* Thu Aug 07 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.5-alt1
- Updated to 2.14.90.0.5.
- Synced with RH 2.14.90.0.5-5.

* Sun Jul 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.4-alt3
- Synced with RH 2.14.90.0.4-19:
  * Thu Jul  3 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-17
  - require no undefined non-weak symbols in PIEs like required for
    normal binaries
  * Wed Jul  2 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-16
  - build libiberty.a with -fPIC, so that it can be lined into shared
    libraries
  * Wed Jun 25 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-14
  - added support for Intel Prescott instructions
  * Wed Jun 18 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-13
  - update CFI stuff to 2003-06-18
  - make sure .eh_frame is aligned to 8 bytes on 64-bit arches,
    remove padding within one .eh_frame section
- bfd/elflink.h: relaxed symbols checking for a while,
  to fix ocaml-shared issue.

* Tue Jun 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.4-alt2
- Synced with RH 2.14.90.0.4-7:
  * Fri Jun  6 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-7
  - some CFI updates/fixes
  - don't create dynamic relocations against symbols defined in PIE
    exported from its .dynsym
  * Wed Jun  4 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-6
  - update gas to 20030604
  - PT_GNU_STACK support

* Mon Jun 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.14.90.0.4-alt1
- Updated to 2.14.90.0.4, updated patches.
- Added patches from RH 2.14.90.0.4-2:
  + eh-frame-ro;
  + cfi (gas CFI updates);
  + pie (dynamic executables support).
- Dropped obsolete patches:
  + rh-alt-glibc21
  + rh-oformat
- Ship with c++filt here.
- Disabled build of additional unneeded targets.
- Deal with info dir entries such that the menu looks pretty.

* Mon Oct 07 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.13.90.0.4-alt2
- Fixed build with new rpm-build.
- Rebuilt to fix config files in devel subpackages.

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.13.90.0.4-alt1
- 2.13.90.0.4 (fixes from rh binutils-2.13.90.0.2-2 merged upstream).

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.12.90.0.14-alt1
- 2.12.90.0.14

* Wed Jun 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.12.90.0.12-alt1
- 2.12.90.0.12

* Tue Jun 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.12.90.0.11-alt2
- Added more headers to libbfd-devel and libiberty-devel subpackages.

* Fri Jun 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.12.90.0.11-alt1
- 2.12.90.0.11

* Thu May 30 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.12.90.0.9-alt1
- Updated code to 2.12.90.0.9

* Wed Apr 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.12.90.0.7-alt1
- Updated code to 2.12.90.0.7

* Thu Apr 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.12.90.0.4-alt1
- Updated code to 2.12.90.0.4
- Megred upstream patch 22:
  + binutils-2.11.93.0.2-rh-dataseg-align3.patch

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.12.90.0.3-alt1
- Updated code to 2.12.90.0.3
- Added translations.
- Regenerated patches (aen):
  + binutils-2.12.90.0.3-alt-texinfo.patch
  + binutils-2.12.90.0.3-rh-alt-glibc21.patch
- Megred upstream patches (12..21):
  + binutils-2.11.93.0.2-rh-combreloc-default.patch
  + binutils-2.11.93.0.2-rh-dataseg-align.patch
  + binutils-2.11.93.0.2-rh-dataseg-align2.patch
  + binutils-2.11.93.0.2-eh_frame.patch
  + binutils-2.11.93.0.2-c++-symver.patch
  + binutils-2.11.93.0.2-merge-gc.patch
  + binutils-2.11.93.0.2-alpha-.text.patch
  + binutils-2.11.93.0.2-alias-visibility.patch
  + binutils-2.11.93.0.2-sparc.patch
  + binutils-2.11.93.0.2-SHN_UNDEF.patch

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.11.93.0.2-alt3
- Merged with rh-2.11.93.0.2-9:
  * Mon Mar 11 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-9
  - fix DATA_SEGMENT_ALIGN on ia64/alpha/sparc/sparc64
  * Fri Mar  8 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-8
  - don't crash on SHN_UNDEF local dynsyms (Andrew MacLeod)
  * Thu Mar  7 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-7
  - fix bfd configury bug (Alan Modra)
  * Tue Mar  5 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-6
  - don't copy visibility when equating symbols
  - fix alpha .text/.data with .previous directive bug
  * Tue Mar  5 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-5
  - fix SHF_MERGE crash with --gc-sections (#60369)
  - C++ symbol versioning patch
  * Fri Feb 22 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-4
  - add DW_EH_PE_absptr -> DW_EH_PE_pcrel optimization for shared libs,
    if DW_EH_PE_absptr cannot be converted that way, don't build the
    .eh_frame_hdr search table

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.11.93.0.2-alt2
- Fixed ld -N broken by last rh patch (jj).

* Mon Feb 18 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.11.93.0.2-alt1
- 2.11.93.0.2
- Merged with rh-2.11.93.0.2-2:
  * Tue Feb 12 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-2
  - trade one saved runtime page for data segment (=almost always not shared)
    for up to one page of disk space where possible

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:2.11.92.0.12.3-alt3
- Try 2.11.92.0.12.3 again.
- Merged with rh-2.11.92.0.12-10:
  * Thu Jan 31 2002 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-10
  - don't create SHN_UNDEF STB_WEAK symbols unless there are any relocations
    against them
  * Fri Dec 28 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-8
  - two further .eh_frame patch fixes
  * Wed Dec 19 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-7
  - as ld is currently not able to shrink input sections to zero size
    during discard_info, build a fake minimal CIE in that case
  - update elf-strtab patch to what was commited
  * Mon Dec 17 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-6
  - one more .eh_frame patch fix
  - fix alpha .eh_frame handling
  - optimize elf-strtab finalize
  * Sat Dec 15 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-5
  - yet another fix for the .eh_frame patch

* Wed Dec 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:2.11.90.0.31-alt2
- Back to stable version: 2.11.90.0.31.

* Wed Dec 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.11.92.0.12.3-alt2
- Merged with rh-2.11.92.0.12-4.

* Thu Nov 29 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.11.92.0.12.3-alt1
- 2.11.92.0.12.3
- Merged with rh-2.11.92.0.12-2.

* Wed Nov 21 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.11.92.0.10-alt1
- 2.11.92.0.10
- Merged with rh-2.11.92.0.7-2.

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.31-alt1
- 2.11.90.0.31

* Fri Aug 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.29-alt1
- 2.11.90.0.29
- Moved libiberty development stuff to separate subpackage.
- Moved bfd info pages to libbfd-devel subpackage.

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.25-alt1
- 2.11.90.0.25

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.24-alt1
- 2.11.90.0.24

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.23-alt1
- 2.11.90.0.23
- Added SHF_MERGE support (jj).

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.19-alt1
- 2.11.90.0.19

* Thu Jun 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.15-alt2
- Merged in RH paches (jj):
  - hack - add elf_i386_glibc21 emulation;
  - back out the -oformat, -omagic and -output change for now.

* Wed Jun 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.15-alt1
- 2.11.90.0.15

* Mon May 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.8-alt1
- 2.11.90.0.8

* Sun May 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.7-alt2
- Updated vendor information.

* Thu May 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.7-alt1
- 2.11.90.0.7

* Fri Apr 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.6-alt1
- 2.11.90.0.6

* Mon Apr 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.5-alt1
- 2.11.90.0.5

* Tue Apr 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.4-alt1
- 2.11.90.0.4
- Moved static libraries to devel-static subpackage.

* Tue Mar 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.11.90.0.1-ipl1mdk
- 2.11.90.0.1

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 2.10.91.0.4-ipl1mdk
- 2.10.91.0.4

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.10.91.0.2-ipl1mdk
- 2.10.91.0.2

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.10.1.0.7-ipl1mdk
- 2.10.1.0.7
- Libification.

* Sat Dec 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.1.0.4-ipl1mdk
- 2.10.1.0.4

* Tue Nov 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.1.0.2-ipl1mdk
- 2.10.1.0.2
- Fixed texinfo documentation.

* Wed Nov 08 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.1-ipl1mdk
- 2.10.1

* Sun Oct 22 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.33-ipl1mdk
- 2.10.0.33

* Thu Oct 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.31-ipl1mdk
- 2.10.0.31

* Wed Oct 11 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.29-ipl1mdk
- 2.10.0.29

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.24-ipl2mdk
- Removed c++filt since it's provided by new gcc-c++ package.
- Automatically added BuildRequires.

* Tue Aug 29 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.24-ipl1mdk
- 2.10.0.24

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.18-ipl1mdk
- 2.10.0.18

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.12-ipl1mdk
- 2.10.0.12

* Tue Jun 27 2000 Dmitry V. Levin <ldv@fandra.org> 2.10.0.9-ipl1mdk
- 2.10.0.9
- Use FHS-compatible macros.

* Wed Jun 21 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.10

* Sat Jun 10 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.9.5.0.46

* Sat Apr 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.9.5.0.37

* Sat Apr 15 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.9.5.0.35

* Tue Apr 11 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.9.5.0.31

* Fri Mar 10 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed Mar  8 2000 Pixel <pixel@mandrakesoft.com> 2.9.5.0.22-2mdk
- add prereq /sbin/install-info

* Wed Jan 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.9.5.0.22-1mdk
- 2.9.5.0.22
- applied debian patch.

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Wed Oct 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.9.5.0.16

* Sun Sep 19 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 2.9.5.0.12

* Wed Aug 25 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.9.5.0.8

* Wed Aug 11 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 2.9.5.0.6
- handle RPM_OPT_FLAGS

* Mon Jul 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.9.5.0.3.

* Fri Jul 16 1999 <bero@mandrakesoft.de>
- 2.9.4.0.8

* Mon Jun 28 1999 <bero@mandrakesoft.de>
- Mandrake adaptions

* Sat Jun 26 1999 <hjl@gnu.org>
- updated to 2.9.4.0.7.

* Sun Jun 20 1999 <hjl@gnu.org>
- updated to 2.9.4.0.6.

* Sat Jun 12 1999 <hjl@gnu.org>
- updated to 2.9.4.0.5.

* Fri Jun 11 1999 <hjl@gnu.org>
- updated to 2.9.4.0.4.

* Mon Jun  7 1999 <hjl@gnu.org>
- updated to 2.9.4.0.3.

* Sun Jun  6 1999 <hjl@gnu.org>
- updated to 2.9.4.0.2.

* Sat Jun  5 1999 <hjl@gnu.org>
- updated to 2.9.4.0.1.

* Sat May 22 1999 <hjl@gnu.org>
- updated to 2.9.1.0.25.

* Wed Apr 21 1999 <hjl@gnu.org>
- updated to 2.9.1.0.24.

* Wed Mar 31 1999 hjl <hjl@gnu.org>
- updated to 2.9.1.0.23.

* Wed Feb 26 1999 hjl <hjl@gnu.org>
- updated to 2.9.1.0.22b.
