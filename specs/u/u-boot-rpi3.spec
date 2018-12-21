Name: u-boot-rpi3
Version: 2018.11
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64

Source: %name-%version-%release.tar

BuildRequires: dtc >= 1.4 flex

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports Raspberry 3 board.

%ifarch armh
%define rpi rpi_3_32b
%define img kernel7.img
%endif
%ifarch aarch64
%define rpi rpi_3
%define img kernel8.img
%endif

%prep
%setup

%build
%make_build %{rpi}_defconfig all

%install
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/%rpi/%img

%files
%doc README
%_datadir/u-boot/*

%changelog
* Mon Dec 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Fri Jun 22 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt2
- use flat directory layout for dtbs

* Thu Jun 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Tue Feb 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- initial

