Name: kernel-headers-common
Version: 1.2.7
Release: alt1

Summary: Common header files for the Linux kernel
License: GPL
Group: Development/Kernel
ExclusiveArch: %ix86 x86_64 %arm aarch64 %e2k %mips riscv64 ppc ppcle ppc64 ppc64le

Source0: adjust_kernel_headers
Source1: adjust_kernel_headers.8
Source2: kheaders.init
Source3: kheaders.service
Source4: kheaders.filetrigger

%define base_arch %_target_cpu
%ifarch %ix86 x86_32 x86_64
%define base_arch x86
%endif
%ifarch %arm
%define base_arch arm
%endif
%ifarch ppc ppc64
%define base_arch powerpc
%endif
%ifarch aarch64
%define base_arch arm64
%endif
%ifarch %mips
%define base_arch mips
%endif
%ifarch s390x
%define base_arch s390
%endif
%ifarch riscv64
%define base_arch riscv
%endif
%ifarch ppc ppcle ppc64 ppc64le
%define base_arch powerpc
%endif

%define _unpackaged_files_terminate_build 1

%add_findreq_skiplist %_includedir/*
%add_findreq_skiplist /etc/sysconfig/kernel/include
Requires: glibc-kernheaders
Conflicts: kernel-headers-alsa

%description
This package contains common directories and C header files from
various versions of the linux kernel.

%install
mkdir -p %buildroot{%_sbindir,%_man8dir,%systemd_unitdir}
install -pm755 %_sourcedir/adjust_kernel_headers %buildroot%_sbindir/
sed -i 's/@VERSION@/%version/g' -- \
	%buildroot%_sbindir/adjust_kernel_headers
install -pm644 %_sourcedir/adjust_kernel_headers.8 %buildroot%_man8dir/
install -pm644 %_sourcedir/kheaders.service %buildroot%systemd_unitdir/
install -pD -m755 %_sourcedir/kheaders.init %buildroot%_initdir/kheaders
mkdir -p %buildroot%_rpmlibdir/
install -m755 %_sourcedir/kheaders.filetrigger %buildroot%_rpmlibdir/
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_sysconfdir/sysconfig/kernel
mkdir -p %buildroot%_prefix/lib/kernel
mkdir -p %buildroot/var/run/kernel

ln -s %_sysconfdir/sysconfig/kernel/include/asm{,-generic,-%base_arch} \
	%buildroot%_includedir/

ln -s %_sysconfdir/sysconfig/kernel/include/{drm,linux,mtd,sound,video} \
	%buildroot%_includedir/

[ "%base_arch" = "%_target_cpu" ] ||
	ln -s asm-%base_arch %buildroot%_includedir/asm-%_target_cpu

ln -s %_includedir/linux-default/include \
	%buildroot%_sysconfdir/sysconfig/kernel/

touch %buildroot%_sysconfdir/sysconfig/kernel/include_manual_mode

for f in {autoconf,modversions,version}.{h,ph} _h2ph_pre.ph; do
        touch "%buildroot/var/run/kernel/$f"
done

%pre
for n in asm{,-generic,-%base_arch,-%_target_cpu} drm linux mtd sound video; do
	d="%_includedir/$n"
	[ -d "$d" -a ! -L "$d" ] || continue
	rmdir "$d" 2> /dev/null ||:
done

%post
%post_service kheaders

%preun
%preun_service kheaders

%triggerin -- glibc-kernheaders, kernel-headers-std-up, kernel-headers-std-smp, kernel22-headers, kernel24-headers
%_sbindir/adjust_kernel_headers ||:

%triggerpostun -- glibc-kernheaders, kernel-headers-std-up, kernel-headers-std-smp, kernel22-headers, kernel24-headers, kernel22-up, kernel22-up-secure, kernel22-smp, kernel22-smp-secure, kernel24-up, kernel24-smp
%_sbindir/adjust_kernel_headers ||:

%triggerpostun -- kernel-headers-common < 0:1.1-alt1
/sbin/chkconfig --add kheaders
/sbin/service kheaders start ||:

%files
%systemd_unitdir/kheaders.service
%_rpmlibdir/kheaders.filetrigger
%_initdir/kheaders
%_sbindir/adjust_kernel_headers
%_man8dir/*
%dir %_sysconfdir/sysconfig/kernel
%ghost %_sysconfdir/sysconfig/kernel/include
%ghost %_sysconfdir/sysconfig/kernel/include_manual_mode
%_includedir/asm
%_includedir/asm-generic
%_includedir/asm-%base_arch
%if "%base_arch" != "%_target_cpu"
%_includedir/asm-%_target_cpu
%endif
%_includedir/drm
%_includedir/linux
%_includedir/mtd
%_includedir/sound
%_includedir/video
%dir %_prefix/lib/kernel
%dir /var/run/kernel
%ghost /var/run/kernel/*

%changelog
* Mon Dec 03 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.7-alt1
- Added support of mips*, s390x, riscv64, and power* architectures.

* Sat Jan 16 2016 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- Added e2k architecture support.

* Mon Sep 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.5-alt1
- Added aarch64 architecture support.

* Thu Jun 20 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.4-alt1
- Added kheaders.filetrigger for kernel headers adjustment.

* Thu Feb 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.3-alt1.1
- Rebuilt for newer %%arm macro.

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Added kheaders.service.

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Added a workaround for update problems (closes: #27320).

* Fri May 11 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Packaged %_includedir/asm-%%_target_cpu symlink to make packages
  always different on different architectures.

* Wed Apr 04 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- Added /usr/include/{drm,mtd,sound,video} symlinks.
- On %%ix86 and x86_64, replaced obsolete /usr/include/asm-{i386,x86_64}
  symlinks with /usr/include/asm-x86.

* Fri Apr 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.11-alt1
- adjust_kernel_headers: Added branch kernels support (closes: #19641).

* Mon Mar 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.10-alt1
- Added ARM support (Kirill A. Shutemov).
- Suppressed dependencies autogenerated for dangling
  %_includedir/asm-* symlinks (closes: #18592).

* Sun Nov 26 2006 Sergey Vlasov <vsu@altlinux.ru> 1.1.9-alt1
- Added /usr/include/asm-$ARCH symlinks (required for Linux 2.6.18 headers on
  x86_64, and sometimes used even in older versions).
- Package is no longer noarch (the set of asm-$ARCH symlinks is arch-specific:
  asm-i386 on 32-bit x86, both asm-x86_64 and asm-i386 on x86_64).
- Used explicit list instead of %%_includedir/* in %%files (otherwise rpmbuild
  does not put files which happen to be dangling symlinks into the package).
- Terminate build if unpackaged files were found.

* Sat Nov 25 2006 Sergey Vlasov <vsu@altlinux.ru> 1.1.8-alt1
- adjust_kernel_headers: Decrease linux/version.h size threshold to 90 bytes
  (fixes problems with Linux 2.6.18 headers, where linux/version.h became
  smaller due to UTS_RELEASE removal).
- Removed all %%__* macro abuse from spec.

* Mon Jan 30 2006 Sergey Vlasov <vsu@altlinux.ru> 1.1.7-alt1
- adjust_kernel_headers:
  + always give "default" headers (glibc-kernheaders) lowest priority when
    using --first to enable use of linux-libc-headers with hasher (#8918);
  + fix bashism noted in comment to #8422.

* Fri Dec 02 2005 Sergey Vlasov <vsu@altlinux.ru> 1.1.6-alt1
- adjust_kernel_headers:
  + applied linux-libc-headers support patch from Konstantin A Lepikhov
    <lakostis@altlinux> (#8422).

* Wed May 25 2005 Sergey Vlasov <vsu@altlinux.ru> 1.1.5-alt2
- Spec fixes for x86_64 compatibility from mouse@ (#6538).

* Mon Mar 08 2004 Sergey Vlasov <vsu@altlinux.ru> 1.1.5-alt1
- adjust_kernel_headers:
  + added auto and manual modes;
  + added proper "--help" text;
  + added "--version" option;
  + fixed old-style headers handling (even if usable version.h exists in
    /usr/lib/kernel/$VERSION, do not consider the headers available unless
    something reasonable exists in /usr/lib/kernel/include);
  + cleanup suggested by Dmitry V. Levin <ldv@altlinux>.
- Added man page for adjust_kernel_headers.
- Added triggers for glibc-kernheaders, kernel-headers-std-{up,smp},
  kernel22-headers, kernel24-headers and also %%triggerpostun for old kernel
  packages (which contained part of the kernel headers) to fix headers on
  install/uninstall.
- Added /usr/include/asm-generic symlink (needed by 2.6.x kernel headers).

* Wed Jul 30 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- adjust_kernel_headers:
  + added "--list" option;
  + added "--first" option.

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- init.d/kheaders: fixed $LOCKFILE handling.

* Mon Jun 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- adjust_kernel_headers:
  + fixed KERNEL_VERSION definition;
  + better kernel autodetection.

* Thu May 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- adjust_kernel_headers: better --help support.

* Tue May 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Updated to support new kernel headers scheme.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt2
- rebuild

* Wed Aug 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt1
- Initial revision.
