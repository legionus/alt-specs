%def_with klibc
%def_without debug

Name: v86d
Version: 0.1.10
Release: alt9
Summary: A x86 Emulation Daemon
License: GPLv2
Group: System/Kernel and hardware
URL: http://dev.gentoo.org/~spock/projects/uvesafb/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
ExclusiveArch: i586 x86_64

BuildRequires: kernel-headers >= 2.6.25
%{?_with_klibc:BuildRequires: klibc-devel >= 1.5-alt1.2}

%description
%name provides a backend for kernel drivers that need to execute ?86 BIOS code.
The code is executed in a controlled environment and the results are passed back
to the kernel via the netlink interface.


%if_with klibc
%package initramfs
Summary: A x86 Emulation Daemon (initramfs variant)
Group: System/Kernel and hardware

%description initramfs
%name provides a backend for kernel drivers that need to execute ?86 BIOS code.
The code is executed in a controlled environment and the results are passed back
to the kernel via the netlink interface.

This package contains initramfs variant of %name linked with klibc.
%endif


%prep
%setup
%patch -p1
sed -i '/^[[:blank:]]*LDFLAGS/s/ -static .*$//' Makefile


%build
%define _optlevel s

%ifarch %ix86
%def_without x86emu
%else
%def_with x86emu
%endif

%if_with klibc
export CFLAGS="%optflags -fno-asynchronous-unwind-tables"
export LDFLAGS="-shared"
./configure \
	--without-debug \
	%{subst_with x86emu} \
	--with-klibc
%make_build KDIR=%_includedir/linux-default
mv %name{,.initramfs}
make clean
%endif

export CFLAGS="%optflags"
export LDFLAGS=
./configure \
	%{subst_with debug} \
	%{subst_with x86emu} \
	--default
%make_build KDIR=%_includedir/linux-default


%install
install -pD -m 0755 {,%buildroot/sbin/}%name
%{?_with_klibc:install -pD -m 0755 %name.initramfs %buildroot/lib/mkinitrd/%name}


%files
%doc AUTHORS ChangeLog README TODO
/sbin/*


%if_with klibc
%files initramfs
/lib/mkinitrd/*
%endif


%changelog
* Thu Nov 29 2018 Nikita Ermakov <arei@altlinux.org> 0.1.10-alt9
- Added ExclusiveArch to point that this package only works with i586 and x86_64.
- Rebuild with klibc-2.0.4-alt1.

* Thu Apr 24 2014 Led <led@altlinux.ru> 0.1.10-alt8
- rebuild with klibc-2.0.3-alt3

* Fri Apr 11 2014 Led <led@altlinux.ru> 0.1.10-alt7
- rebuild with klibc-2.0.3-alt2

* Mon Nov 18 2013 Led <led@altlinux.ru> 0.1.10-alt6
- rebuild with klibc-2.0.2-alt4

* Sat Dec 15 2012 Led <led@altlinux.ru> 0.1.10-alt5
- rebuild with klibc-2.0.2-alt2

* Fri Nov 23 2012 Led <led@altlinux.ru> 0.1.10-alt4
- rebuild with klibc-2.0.2-alt1

* Wed Nov 21 2012 Led <led@altlinux.ru> 0.1.10-alt3
- rebuild with klibc-1.5.25-alt1

* Sun Nov 18 2012 Led <led@altlinux.ru> 0.1.10-alt2
- rebuild with klibc-1.5.18-alt3

* Thu Oct 18 2012 Led <led@altlinux.ru> 0.1.10-alt1
- rebuild with klibc-1.5.18-alt2
- cleaned up spec

* Thu Feb 02 2012 Led <led@massivesolutions.co.uk> 0.1.10-cx2
- cleaned up spec
- fixed build warnings

* Mon Mar 21 2011 Led <led@altlinux.ru> 0.1.10-cx1
- added -initramfs subpackage
- build with shared klibc

* Sun Mar 13 2011 Led <led@altlinux.ru> 0.1.10-cx0
- 0.1.10

* Tue Oct 07 2008 Led <led@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Wed Sep 24 2008 Led <led@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Sat Aug 02 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.1.5.2-alt1
- 0.1.5.2

* Mon Jun 16 2008 Led <led@altlinux.ru> 0.1.5-alt3
- build with system klibc

* Sat May 31 2008 Led <led@altlinux.ru> 0.1.5-alt2
- fixed Summary and Group

* Fri May 30 2008 Led <led@altlinux.ru> 0.1.5-alt1
- added:
  + %name-0.1.5-format.patch
  + %name-0.1.5-makefile.patch
- build with system libc

* Wed May 07 2008 Led <led@altlinux.ru> 0.1.5-alt0.1
- 0.1.5

* Wed Dec 26 2007 Led <led@altlinux.ru> 0.1.3-alt0.1
- 0.1.3

* Sat Nov 17 2007 Led <led@altlinux.ru> 0.1.2-alt0.1
- 0.1.2

* Sun Oct 28 2007 Led <led@altlinux.ru> 0.1.1-alt0.1
- 0.1.1

* Fri Oct 19 2007 Led <led@altlinux.ru> 0.1-alt0.2
- fixed License

* Wed Aug 22 2007 Led <led@altlinux.ru> 0.1-alt0.1
- initial build
