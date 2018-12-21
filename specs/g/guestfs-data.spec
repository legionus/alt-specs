Name: guestfs-data
Version: 0.4
Release: alt1

Summary: Virtual machine needed for libguestfs
License: GPLv2+
Group: File tools

Provides: lib%name = %version-%release

BuildPreReq: rpm-build-guestfs
BuildRequires: /proc

%description
libguestfs needs for it's run a virtual machine image.
This package provides such an image, an initrd and a kernel.

%install
mkdir -p %buildroot%_libdir/guestfs
cp -a %_libdir/guestfs/* %buildroot%_libdir/guestfs/
chmod 644 %buildroot%_libdir/guestfs/*

%files
%dir %_libdir/guestfs/
%_libdir/guestfs/*

%changelog
* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- rebuild with libguestfs-1.36.15-alt1
- build with new make-initrd v2

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt6
- rebuld with libguestfs-1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt5
- rebuld with libguestfs-1.32.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt4
- rebuld with libguestfs-1.31.17

* Tue Sep 22 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt3
- rebuld with libguestfs-1.31.6

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- rebuild

* Fri Feb 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
