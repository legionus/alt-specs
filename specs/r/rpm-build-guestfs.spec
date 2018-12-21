Name: rpm-build-guestfs
Version: 0.4
Release: alt1

Summary: RPM helper post script for build guestfs appliance
License: GPL
Group: Development/Other

BuildArch: noarch
Requires(pre):  make-initrd-guestfs >= 0.4
Requires(pre):  kernel >= 4.3

%description
RPM helper post script for build guestfs appliance

%files

%post

mkdir -p %_libdir/guestfs
VMLINUZ="$(readlink -e -- /boot/vmlinuz-*alt*)"
KVER="${VMLINUZ##*/vmlinuz-}"
echo "VMLINUZ = $VMLINUZ"
echo "KVER = $KVER"
cp $VMLINUZ %_libdir/guestfs/vmlinuz.%_arch
make-initrd --verbose --no-checks --config=/etc/initrd.mk.d/guestfs.mk.example --kernel=$KVER
chmod 644 %_libdir/guestfs/*

%postun
rm -rf %_libdir/guestfs

%changelog
* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- rebuild with libguestfs-1.36.15-alt1
- build with new make-initrd v2
- fix detect kernel version for aarch64 too

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt6
- rebuld with libguestfs-1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt5
- rebuld with libguestfs-1.32.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt4
- rebuild

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- add --verbose to make-initrd

* Fri Feb 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
