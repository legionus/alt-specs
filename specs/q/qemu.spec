# vim: set ft=spec
# vim600: set fdm=marker:

# {{{ macros define

%def_disable edk2_cross

%def_enable user_static

%def_enable sdl
%def_enable curses
%def_enable bluez
%def_enable vnc
%def_enable vnc_sasl
%def_enable vnc_jpeg
%def_enable vnc_png
%def_enable xkbcommon
%def_disable vde
%def_enable alsa
%def_enable pulseaudio
%def_enable oss
%def_enable aio
%def_enable blobs
%def_enable smartcard
%def_enable libusb
%def_enable usb_redir
%def_enable vhost_crypto
%def_enable vhost_net
%def_enable vhost_scsi
%def_enable vhost_vsock
%def_enable opengl
%def_enable guest_agent
%def_enable tools
%def_enable spice
%def_enable libiscsi
%def_enable rbd
%def_enable libnfs
%def_enable seccomp
%def_enable glusterfs
%def_enable gtk
%def_disable gtk_gl
%def_enable gnutls
%def_enable nettle
%def_disable gcrypt
%def_enable virglrenderer
%def_enable tpm
%def_enable libssh2
%def_enable live_block_migration
%ifnarch armh
%def_enable numa
%else
%def_disable numa
%endif
%def_disable tcmalloc
%def_disable jemalloc
%def_enable replication
%def_disable vxhs
%def_enable rdma
%def_enable lzo
%def_enable snappy
%def_enable bzip2
%def_disable xen
%def_enable mpath
%def_enable libxml2
%def_disable libpmem
%def_enable libudev

%define power64 ppc64 ppc64p7 ppc64le
%define mips32 mips mipsel mipsr6 mipsr6el
%define mips64 mips64 mips64el mips64r6 mips64r6el
%define mips_arch %mips32 %mips64

%ifarch %ix86
%global kvm_package system-x86
%def_enable qemu_kvm
%endif
%ifarch x86_64
%global kvm_package system-x86
%def_enable qemu_kvm
%endif
%ifarch %power64
%global kvm_package   system-ppc
%endif
%ifarch s390x
%global kvm_package   system-s390x
%endif
%ifarch armh
%global kvm_package   system-arm
%def_enable qemu_kvm
%endif
%ifarch aarch64
%global kvm_package   system-aarch64
%def_enable qemu_kvm
%endif
%ifarch %mips_arch
%global kvm_package   system-mips
%endif

%def_enable have_kvm

%define audio_drv_list %{?_enable_oss:oss} %{?_enable_alsa:alsa} %{?_enable_sdl:sdl} %{?_enable_pulseaudio:pa}

%global _group vmusers
%global rulenum 90
%global _libexecdir /usr/libexec
%global _localstatedir /var

# }}}

Name: qemu
Version: 3.1.0
Release: alt1

Summary: QEMU CPU Emulator
License: GPL/LGPL/BSD
Group: Emulators
Url: https://www.qemu.org
# git://git.qemu.org/qemu.git
Source0: %name-%version.tar
Source100: keycodemapdb-%name-%version.tar
Source2: qemu-kvm.control.in
Source4: qemu-kvm.rules
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh
# guest agent service
Source8: qemu-guest-agent.rules
Source9: qemu-guest-agent.service
Source10: qemu-guest-agent.init
Source11: qemu-ga.sysconfig
# /etc/qemu/bridge.conf
Source12: bridge.conf
# PR manager service
Source14: qemu-pr-helper.service
Source15: qemu-pr-helper.socket

Patch: qemu-alt.patch

%set_verify_elf_method fhs=relaxed
%add_verify_elf_skiplist %_datadir/%name/*
%add_findreq_skiplist %_datadir/%name/*

Requires: %name-system = %EVR
Requires: %name-user = %EVR

BuildRequires: glibc-devel-static zlib-devel-static glib2-devel-static
BuildRequires: glib2-devel >= 2.40
BuildRequires: texinfo perl-podlators libattr-devel-static libcap-devel libcap-ng-devel
BuildRequires: libxfs-devel
BuildRequires: zlib-devel libcurl-devel libpci-devel glibc-kernheaders
BuildRequires: ipxe-roms-qemu >= 1:20161208-alt1.git26050fd seavgabios seabios >= 1.7.4-alt2 libfdt-devel >= 1.4.2
BuildRequires: libpixman-devel >= 0.21.8
BuildRequires: python3
# Upstream disables iasl for big endian and QEMU checks for this.
%ifnarch s390 s390x ppc ppc64
BuildRequires: iasl
%endif
BuildRequires: libpcre-devel-static
%{?_enable_sdl:BuildRequires: libSDL2-devel}
%{?_enable_curses:BuildRequires: libncursesw-devel}
%{?_enable_bluez:BuildRequires: libbluez-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_vnc_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vnc_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_vnc_png:BuildRequires: libpng-devel}
%{?_enable_xkbcommon:BuildRequires: libxkbcommon-devel}
%{?_enable_vde:BuildRequires: libvde-devel}
%{?_enable_aio:BuildRequires: libaio-devel}
%{?_enable_spice:BuildRequires: libspice-server-devel >= 0.12.0 spice-protocol >= 0.12.3}
BuildRequires: libuuid-devel
%{?_enable_smartcard:BuildRequires: libcacard-devel >= 2.5.1}
%{?_enable_usb_redir:BuildRequires: libusbredir-devel >= 0.5}
%{?_enable_opengl:BuildRequires: libepoxy-devel libgbm-devel}
%{?_enable_guest_agent:BuildRequires: glib2-devel >= 2.38}
%{?_enable_rbd:BuildRequires: ceph-devel}
%{?_enable_libiscsi:BuildRequires: libiscsi-devel >= 1.9.0}
%{?_enable_libnfs:BuildRequires: libnfs-devel >= 1.9.3}
%{?_enable_seccomp:BuildRequires: libseccomp-devel >= 2.2.3}
%{?_enable_glusterfs:BuildRequires: pkgconfig(glusterfs-api)}
%{?_enable_gtk:BuildRequires: libgtk+3-devel >= 3.14.0 libvte3-devel >= 0.32.0}
%{?_enable_gnutls:BuildRequires: libgnutls-devel >= 3.1.18}
%{?_enable_nettle:BuildRequires: libnettle-devel >= 2.7.1}
%{?_enable_gcrypt:BuildRequires: libgcrypt-devel >= 1.5.0}
BuildRequires: libtasn1-devel
%{?_enable_virglrenderer:BuildRequires: pkgconfig(virglrenderer)}
%{?_enable_libssh2:BuildRequires: libssh2-devel >= 1.2.8}
%{?_enable_libusb:BuildRequires: libusb-devel >= 1.0.13}
%{?_enable_rdma:BuildRequires: rdma-core-devel}
%{?_enable_numa:BuildRequires: libnuma-devel}
%{?_enable_tcmalloc:BuildRequires: libgperftools-devel}
%{?_enable_jemalloc:BuildRequires: libjemalloc-devel}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_snappy:BuildRequires: libsnappy-devel}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_xen:BuildRequires: libxen-devel}
%{?_enable_vxhs:BuildRequires: libvxhs-devel}
%{?_enable_mpath:BuildRequires: libudev-devel libmultipath-devel}
%{?_enable_libxml2:BuildRequires: libxml2-devel}
%{?_enable_libpmem:BuildRequires: libpmem-devel}
%{?_enable_libudev:BuildRequires: libudev-devel}

%global requires_all_modules         \
Requires: %name-block-curl = %EVR    \
Requires: %name-block-dmg = %EVR     \
Requires: %name-block-gluster = %EVR \
Requires: %name-block-iscsi = %EVR   \
Requires: %name-block-nfs = %EVR     \
Requires: %name-block-rbd = %EVR     \
Requires: %name-audio-alsa = %EVR    \
Requires: %name-audio-oss = %EVR     \
Requires: %name-audio-pa = %EVR      \
Requires: %name-audio-sdl = %EVR     \
Requires: %name-ui-curses = %EVR     \
Requires: %name-ui-gtk = %EVR        \
Requires: %name-ui-sdl = %EVR 

%description
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.  QEMU has two operating modes:

* Full system emulation.  In this mode, QEMU emulates a full system
  (for example a PC), including a processor and various peripherials.
  It can be used to launch different Operating Systems without rebooting
  the PC or to debug system code.

* User mode emulation.  In this mode, QEMU can launch Linux processes
  compiled for one CPU on another CPU.  It can be used to launch the
  Wine Windows API emulator or to ease cross-compilation and
  cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy
to use.

%package common
Summary: QEMU CPU Emulator - common files
Group: Emulators
BuildArch: noarch
Requires(pre): control >= 0.7.2
Requires(pre): shadow-utils sysvinit-utils
Requires: %name-img = %EVR

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
BuildArch: noarch
Requires: %name-common = %EVR
Requires: %name-tools = %EVR
Conflicts: %name-img < %EVR

Requires: %name-system-aarch64 = %EVR
Requires: %name-system-alpha = %EVR
Requires: %name-system-arm = %EVR
Requires: %name-system-cris = %EVR
Requires: %name-system-lm32 = %EVR
Requires: %name-system-m68k = %EVR
Requires: %name-system-microblaze = %EVR
Requires: %name-system-mips = %EVR
Requires: %name-system-moxie = %EVR
Requires: %name-system-nios2 = %EVR
Requires: %name-system-or1k = %EVR
Requires: %name-system-ppc = %EVR
Requires: %name-system-riscv = %EVR
Requires: %name-system-s390x = %EVR
Requires: %name-system-sh4 = %EVR
Requires: %name-system-sparc = %EVR
Requires: %name-system-tricore = %EVR
Requires: %name-system-unicore32 = %EVR
Requires: %name-system-x86 = %EVR
Requires: %name-system-xtensa = %EVR

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%if_enabled have_kvm
%package kvm
Summary: QEMU metapackage for KVM support
Group: Emulators
Requires: qemu-%kvm_package = %EVR

%description kvm
This is a meta-package that provides a qemu-system-<arch> package for native
architectures where kvm can be enabled. For example, in an x86 system, this
will install qemu-system-x86

%package kvm-core
Summary: QEMU metapackage for KVM support
Group: Emulators
Requires: qemu-%kvm_package-core = %EVR

%description kvm-core
This is a meta-package that provides a qemu-system-<arch>-core package
for native architectures where kvm can be enabled. For example, in an
x86 system, this will install qemu-system-x86-core
%endif

%package user
Summary: QEMU CPU Emulator - user mode emulation
Group: Emulators
Requires: %name-common = %EVR

%description user
User mode emulation.  In this mode, QEMU can launch Linux processes
compiled for one CPU on another CPU.  It can be used to launch the
Wine Windows API emulator or to ease cross-compilation and
cross-debugging.

%package user-binfmt
Summary: QEMU user mode emulation of qemu targets
Group: Emulators
Requires: %name-user = %EVR
# qemu-user-binfmt + qemu-user-static both provide binfmt rules
Conflicts: %name-user-static-binfmt
Conflicts: %name-user < 2.10.1-alt1

%description user-binfmt
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets

%package user-static
Summary: QEMU user mode emulation of qemu targets static build
Group: Emulators
Requires: %name-aux = %EVR

%description user-static
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets built as
static binaries

%package user-static-binfmt
Summary: QEMU user mode emulation of qemu targets static build
Group: Emulators
Requires: %name-user-static
Conflicts: %name-user-binfmt
Conflicts: %name-user < 2.10.1-alt1
Provides: %name-user-binfmt_misc = %EVR
Obsoletes: %name-user-binfmt_misc < %EVR

%description user-static-binfmt
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the user mode emulation of qemu targets

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Provides: qemu-kvm-img
Obsoletes: qemu-kvm-img < %EVR
Requires: %name-aux = %EVR

%description img
This package provides a command line tool for manipulating disk images

%package tools
Summary: Tools for QEMU
Group: Emulators
Requires: %name-img = %EVR
Requires: %name-aux = %EVR
Conflicts: %name-system < 2.11.0-alt2

%description tools
This package contains various QEMU related tools, including a bridge helper,
a virtfs helper.

%package  block-curl
Summary: QEMU CURL block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-curl
This package provides the additional CURL block driver for QEMU.

Install this package if you want to access remote disks over
http, https, ftp and other transports provided by the CURL library.

%package  block-dmg
Summary: QEMU block driver for DMG disk images
Group: Emulators
Requires: %name-common = %EVR
%description block-dmg
This package provides the additional DMG block driver for QEMU.

Install this package if you want to open '.dmg' files.

%package  block-gluster
Summary: QEMU Gluster block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-gluster
This package provides the additional Gluster block driver for QEMU.

Install this package if you want to access remote Gluster storage.

%package  block-iscsi
Summary: QEMU iSCSI block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-iscsi
This package provides the additional iSCSI block driver for QEMU.

Install this package if you want to access iSCSI volumes.

%package  block-nfs
Summary: QEMU NFS block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-nfs
This package provides the additional NFS block driver for QEMU.

Install this package if you want to access remote NFS storage.

%package  block-rbd
Summary: QEMU Ceph/RBD block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-rbd
This package provides the additional Ceph/RBD block driver for QEMU.

Install this package if you want to access remote Ceph volumes
using the rbd protocol.

%package  block-ssh
Summary: QEMU SSH block driver
Group: Emulators
Requires: %name-common = %EVR
%description block-ssh
This package provides the additional SSH block driver for QEMU.

Install this package if you want to access remote disks using
the Secure Shell (SSH) protocol.

%package  audio-alsa
Summary: QEMU ALSA audio driver
Group: Emulators
Requires: %name-common = %EVR
%description audio-alsa
This package provides the additional ALSA audio driver for QEMU.

%package  audio-oss
Summary: QEMU OSS audio driver
Group: Emulators
Requires: %name-common = %EVR
%description audio-oss
This package provides the additional OSS audio driver for QEMU.

%package  audio-pa
Summary: QEMU PulseAudio audio driver
Group: Emulators
Requires: %name-common = %EVR
%description audio-pa
This package provides the additional PulseAudi audio driver for QEMU.

%package  audio-sdl
Summary: QEMU SDL audio driver
Group: Emulators
Requires: %name-common = %EVR
%description audio-sdl
This package provides the additional SDL audio driver for QEMU.

%package  ui-curses
Summary: QEMU curses UI driver
Group: Emulators
Requires: %name-common = %EVR
%description ui-curses
This package provides the additional curses UI for QEMU.

%package  ui-gtk
Summary: QEMU GTK UI driver
Group: Emulators
Requires: %name-common = %EVR
%description ui-gtk
This package provides the additional GTK UI for QEMU.

%package  ui-sdl
Summary: QEMU SDL UI driver
Group: Emulators
Requires: %name-common = %EVR
%description ui-sdl
This package provides the additional SDL UI for QEMU.

%package guest-agent
Summary: QEMU guest agent
Group: Emulators
Requires: %name-aux = %EVR

%description guest-agent
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides an agent to run inside guests, which communicates
with the host over a virtio-serial channel named "org.qemu.guest_agent.0"

This package does not need to be installed on the host OS.

%package doc
Summary: User documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name-aux = %EVR

%description doc
User documentation for %name

%package aux
Summary: QEMU auxiliary package
Group: Emulators
BuildArch: noarch

%description aux
QEMU is a generic and open source processor emulator which achieves
good emulation speed by using dynamic translation.

This is an auxiliary package.

%package -n ivshmem-tools
Summary: Client and server for QEMU ivshmem device
Group: Emulators

%description -n ivshmem-tools
This package provides client and server tools for QEMU's ivshmem device.

%package system-x86
Summary: QEMU system emulator for x86
Group: Emulators
BuildArch: noarch
Requires: %name-system-x86-core = %EVR
%requires_all_modules

%description system-x86
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for x86. When being run in a x86
machine that supports it, this package also provides the KVM virtualization
platform.

%package system-x86-core
Summary: QEMU system emulator for x86
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
Requires: seavgabios
Requires: seabios >= 1.7.4-alt2
Requires: ipxe-roms-qemu >= 1:20161208-alt1.git26050fd
%if_enabled edk2_cross
Requires: edk2-ovmf
%else
%ifarch x86_64
Requires: edk2-ovmf
%endif
%endif
%if_enabled seccomp
Requires: libseccomp >= 2.2.3
%endif

%description system-x86-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for x86. When being run in a x86
machine that supports it, this package also provides the KVM virtualization
platform.

%package system-alpha
Summary: QEMU system emulator for Alpha
Group: Emulators
BuildArch: noarch
Requires: %name-system-alpha-core = %EVR
%requires_all_modules
%description system-alpha
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Alpha systems.

%package system-alpha-core
Summary: QEMU system emulator for Alpha
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-alpha-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Alpha systems.

%package system-arm
Summary: QEMU system emulator for ARM
Group: Emulators
BuildArch: noarch
Requires: %name-system-arm-core = %EVR
%requires_all_modules
%description system-arm
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for ARM systems.

%package system-arm-core
Summary: QEMU system emulator for ARM
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-arm-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for ARM boards.

%package system-mips
Summary: QEMU system emulator for MIPS
Group: Emulators
BuildArch: noarch
Requires: %name-system-mips-core = %EVR
%requires_all_modules
%description system-mips
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for MIPS systems.

%package system-mips-core
Summary: QEMU system emulator for MIPS
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-mips-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for MIPS boards.

%package system-cris
Summary: QEMU system emulator for CRIS
Group: Emulators
BuildArch: noarch
Requires: %name-system-cris-core = %EVR
%requires_all_modules
%description system-cris
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for CRIS systems.

%package system-cris-core
Summary: QEMU system emulator for CRIS
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-cris-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for CRIS boards.

%package system-hppa
Summary: QEMU system emulator for HPPA
Group: Emulators
BuildArch: noarch
Requires: %name-system-cris-core = %EVR
%requires_all_modules
%description system-hppa
This package provides the QEMU system emulator for HPPA.

%package system-hppa-core
Summary: QEMU system emulator for hppa
Group: Emulators
Requires: %name-common = %EVR
%description system-hppa-core
This package provides the QEMU system emulator for HPPA.

%package system-lm32
Summary: QEMU system emulator for LatticeMico32
Group: Emulators
BuildArch: noarch
Requires: %name-system-lm32-core = %EVR
%requires_all_modules
%description system-lm32
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for LatticeMico32 systems.

%package system-lm32-core
Summary: QEMU system emulator for LatticeMico32
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-lm32-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for LatticeMico32 boards.

%package system-m68k
Summary: QEMU system emulator for ColdFire (m68k)
Group: Emulators
BuildArch: noarch
Requires: %name-system-m68k-core = %EVR
%requires_all_modules
%description system-m68k
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for ColdFire boards.

%package system-m68k-core
Summary: QEMU system emulator for ColdFire (m68k)
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-m68k-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for ColdFire boards.

%package system-microblaze
Summary: QEMU system emulator for Microblaze
Group: Emulators
BuildArch: noarch
Requires: %name-system-microblaze-core = %EVR
%requires_all_modules
%description system-microblaze
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Microblaze boards.

%package system-microblaze-core
Summary: QEMU system emulator for Microblaze
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-microblaze-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Microblaze boards.

%package system-or1k
Summary: QEMU system emulator for OpenRisc32
Group: Emulators
BuildArch: noarch
Requires: %name-system-or1k-core = %EVR
%requires_all_modules
%description system-or1k
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for OpenRisc32 boards.

%package system-or1k-core
Summary: QEMU system emulator for OpenRisc32
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-or1k-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for OpenRisc32 boards.

%package system-s390x
Summary: QEMU system emulator for S390
Group: Emulators
BuildArch: noarch
Requires: %name-system-s390x-core = %EVR
%requires_all_modules
%description system-s390x
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for S390 systems.

%package system-s390x-core
Summary: QEMU system emulator for S390
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-s390x-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for S390 systems.

%package system-sh4
Summary: QEMU system emulator for SH4
Group: Emulators
BuildArch: noarch
Requires: %name-system-sh4-core = %EVR
%requires_all_modules
%description system-sh4
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for SH4 boards.

%package system-sh4-core
Summary: QEMU system emulator for SH4
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-sh4-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for SH4 boards.

%package system-sparc
Summary: QEMU system emulator for SPARC
Group: Emulators
BuildArch: noarch
Requires: %name-system-sparc-core = %EVR
%requires_all_modules
%description system-sparc
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for SPARC and SPARC64 systems.

%package system-sparc-core
Summary: QEMU system emulator for SPARC
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
# todo: build new openbios
#Requires: openbios
%description system-sparc-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for SPARC and SPARC64 systems.

%package system-ppc
Summary: QEMU system emulator for PPC
Group: Emulators
BuildArch: noarch
Requires: %name-system-ppc-core = %EVR
%requires_all_modules
%description system-ppc
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for PPC and PPC64 systems.

%package system-ppc-core
Summary: QEMU system emulator for PPC
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
# todo: build new openbios and SLOF
#Requires: openbios
#Requires: SLOF
Requires: seavgabios
%description system-ppc-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for PPC and PPC64 systems.

%package system-riscv
Summary: QEMU system emulator for RISC-V
Group: Emulators
BuildArch: noarch
Requires: %name-system-riscv-core = %EVR
%description system-riscv
This package provides the QEMU system emulator for RISC-V systems.
%package system-riscv-core

Summary: QEMU system emulator for RISC-V
Group: Emulators
Requires: %name-common = %EVR
%description system-riscv-core
This package provides the QEMU system emulator for RISC-V systems.

%package system-xtensa
Summary: QEMU system emulator for Xtensa
Group: Emulators
BuildArch: noarch
Requires: %name-system-xtensa-core = %EVR
%requires_all_modules
%description system-xtensa
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Xtensa boards.

%package system-xtensa-core
Summary: QEMU system emulator for Xtensa
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-xtensa-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Xtensa boards.

%package system-unicore32
Summary: QEMU system emulator for Unicore32
Group: Emulators
BuildArch: noarch
Requires: %name-system-unicore32-core = %EVR
%requires_all_modules
%description system-unicore32
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Unicore32 boards.

%package system-unicore32-core
Summary: QEMU system emulator for Unicore32
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-unicore32-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Unicore32 boards.

%package system-moxie
Summary: QEMU system emulator for Moxie
Group: Emulators
BuildArch: noarch
Requires: %name-system-moxie-core = %EVR
%requires_all_modules
%description system-moxie
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Moxie boards.

%package system-moxie-core
Summary: QEMU system emulator for Moxie
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-moxie-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Moxie boards.

%package system-aarch64
Summary: QEMU system emulator for AArch64
Group: Emulators
BuildArch: noarch
Requires: %name-system-aarch64-core = %EVR
%requires_all_modules
%description system-aarch64
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for AArch64.

%package system-aarch64-core
Summary: QEMU system emulator for AArch64
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%if_enabled edk2_cross
Requires: edk2-aarch64
%else
%ifarch aarch64
Requires: edk2-aarch64
%endif
%endif

%description system-aarch64-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for AArch64.

%package system-tricore
Summary: QEMU system emulator for tricore
Group: Emulators
BuildArch: noarch
Requires: %name-system-tricore-core = %EVR
%requires_all_modules
%description system-tricore
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Tricore.

%package system-tricore-core
Summary: QEMU system emulator for tricore
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-tricore-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for Tricore.

%package system-nios2
Summary: QEMU system emulator for nios2
Group: Emulators
BuildArch: noarch
Requires: %name-system-nios2-core = %EVR
%requires_all_modules
%description system-nios2
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for NIOS2.

%package system-nios2-core
Summary: QEMU system emulator for nios2
Group: Emulators
Requires: %name-common = %EVR
Conflicts: %name-system < 2.10.1-alt1
%description system-nios2-core
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation.

This package provides the system emulator for NIOS2.

%prep
%setup

mkdir -p ui/keycodemapdb
tar -xf %SOURCE100 -C ui/keycodemapdb --strip-components 1

%patch -p1
cp -f %SOURCE2 qemu-kvm.control.in
%ifarch armh aarch64
sed -i 's,/usr/bin/qemu-system-x86_64,/usr/bin/qemu-%kvm_package,' %SOURCE5
%endif

%build
export CFLAGS="%optflags"
# --build-id option is used for giving info to the debug packages.
export extraldflags="-Wl,--build-id"
export buildldflags="VL_LDFLAGS=-Wl,--build-id"

run_configure() {
# non-GNU configure
./configure \
	--disable-git-update \
	--prefix=%prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--with-pkgversion=%name-%version-%release \
%ifarch s390 %mips64
	--enable-tcg-interpreter \
%endif
	--extra-ldflags="$extraldflags -Wl,-z,relro -Wl,-z,now" \
	--extra-cflags="%optflags" \
	--disable-werror \
	--disable-debug-tcg \
	--disable-sparse \
	--disable-strip \
	--enable-kvm \
	--python=/usr/bin/python3 \
	 "$@"
}

%if_enabled user_static
# non-GNU configure
run_configure \
	--disable-pie \
	--static \
	--disable-system \
	--enable-linux-user \
	--disable-xfsctl \
	--disable-smartcard \
	--disable-usb-redir \
	--disable-libusb \
	--disable-rdma \
	--disable-libiscsi \
	--disable-rbd \
	--disable-libnfs \
	--disable-glusterfs \
	--disable-libxml2 \
	--disable-libssh2 \
	--disable-gnutls \
	--disable-nettle \
	--disable-gcrypt \
	--disable-cap-ng \
	--disable-curl \
	--disable-virglrenderer \
	--disable-lzo \
	--disable-numa \
	--disable-tcmalloc \
	--disable-jemalloc \
	--disable-replication \
	--disable-tools \
	--disable-guest-agent \
	--disable-guest-agent-msi \
	--disable-curses \
	--disable-spice \
	--disable-sdl \
	--disable-gtk

# Please do not touch this
sed -i "/TARGET_ARM/ {
N
/cpu_model/ s,any,cortex-a8,
}" linux-user/main.c

%make_build V=1 $buildldflags

%if_with arm
mv arm-linux-user/qemu-arm arm-linux-user/qemu-armh

sed -i '/cpu_model =/ s,cortex-a8,cortex-a53,' linux-user/main.c
%make_build V=1 $buildldflags
mv arm-linux-user/qemu-arm arm-linux-user/qemu-aarch64

sed -i '/cpu_model =/ s,cortex-a53,any,' linux-user/main.c
%make_build V=1 $buildldflags
%endif

find -regex '.*linux-user/qemu.*' -perm 755 -exec mv '{}' '{}'.static ';'
%make_build clean
%endif

# non-GNU configure
run_configure \
	--enable-system \
	--enable-linux-user \
	--enable-pie \
	--enable-modules \
	%{?_enable_sdl:--enable-sdl --with-sdlabi=2.0} \
	%{?_disable_curses:--disable-curses} \
	%{subst_enable bluez} \
	%{subst_enable vnc} \
	%{?_enable_gtk:--enable-gtk --enable-vte} \
	%{?_disable_vnc_tls:--disable-vnc-tls} \
	%{?_disable_vnc_sasl:--disable-vnc-sasl} \
	%{?_disable_vnc_jpeg:--disable-vnc-jpeg} \
	%{?_disable_vnc_png:--disable-vnc-png} \
	%{?_disable_xkbcommon:--disable-xkbcommon} \
	%{?_disable_vde:--disable-vde} \
	%{?_disable_aio:--disable-linux-aio} \
	%{?_disable_blobs: --disable-blobs} \
	%{subst_enable spice} \
	--audio-drv-list="%audio_drv_list" \
	--disable-brlapi \
	--enable-curl \
	--enable-fdt \
	%{subst_enable virglrenderer} \
	%{subst_enable tpm} \
	%{subst_enable xen} \
	%{?_enable_vhost_crypto:--enable-vhost-crypto} \
	%{?_enable_vhost_net:--enable-vhost-net} \
	%{?_enable_vhost_scsi:--enable-vhost-scsi } \
	%{?_enable_vhost_vsock:--enable-vhost-vsock} \
	%{subst_enable smartcard} \
	%{subst_enable libusb} \
	%{?_enable_usb_redir:--enable-usb-redir} \
	%{subst_enable opengl} \
	%{subst_enable seccomp} \
	%{subst_enable libiscsi} \
	%{subst_enable rbd} \
	%{subst_enable libnfs} \
	%{subst_enable glusterfs} \
	%{subst_enable libxml2} \
	%{subst_enable libssh2} \
	%{?_enable_live_block_migration:--enable-live-block-migration} \
	%{subst_enable rdma} \
	%{subst_enable gnutls} \
	%{subst_enable nettle} \
	%{subst_enable gcrypt} \
	%{subst_enable numa} \
	%{subst_enable tcmalloc} \
	%{subst_enable jemalloc} \
	%{subst_enable replication} \
	%{subst_enable vxhs} \
	%{subst_enable lzo} \
	%{subst_enable snappy} \
	%{subst_enable bzip2} \
	%{?_disable_guest_agent:--disable-guest-agent} \
	%{subst_enable tools} \
	%{subst_enable libpmem} \
	--disable-xen

%make_build V=1 $buildldflags

sed -i 's/@GROUP@/%_group/g' qemu-kvm.control.in

%install
%makeinstall_std

%define docdir %_docdir/%name-%version
mv %buildroot%_docdir/qemu %buildroot%docdir
install -m644 LICENSE MAINTAINERS %buildroot%docdir/
for emu in %buildroot%_bindir/qemu-system-*; do
    ln -sf qemu.1.xz %buildroot%_man1dir/$(basename $emu).1.xz
done
%if_enabled user_static
find -regex '.*linux-user/qemu.*\.static' -exec install -m755 '{}' %buildroot%_bindir ';'
%endif

%if_enabled qemu_kvm
install -m 0755 %SOURCE5 %buildroot%_bindir/qemu-kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/qemu
ln -sf qemu.1.xz %buildroot%_man1dir/qemu-kvm.1.xz
%endif

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_sysconfdir/udev/rules.d/*

install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/udev/rules.d/%rulenum-%name-kvm.rules
install -D -m 0755 %name-kvm.control.in %buildroot%_controldir/kvm

# Install qemu-guest-agent service and udev rules
install -D -m 0644 %SOURCE8 %buildroot%_udevrulesdir/%rulenum-%name-guest-agent.rules
install -D -m 0644 %SOURCE9 %buildroot%_unitdir/%name-guest-agent.service
install -D -m 0755 %SOURCE10 %buildroot%_initdir/%name-guest-agent
install -D -m 0644 %SOURCE11 %buildroot%_sysconfdir/sysconfig/qemu-ga
mkdir -p %buildroot%_sysconfdir/%name/fsfreeze-hook.d
install -D -m 0755 scripts/qemu-guest-agent/fsfreeze-hook %buildroot%_sysconfdir/%name/
install -D -m 0644 scripts/qemu-guest-agent/fsfreeze-hook.d/*.sample %buildroot%_sysconfdir/%name/fsfreeze-hook.d/
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/qga-fsfreeze-hook.log

# Install qemu-pr-helper service
install -m 0644 %SOURCE14 %buildroot%_unitdir/qemu-pr-helper.service
install -m 0644 %SOURCE15 %buildroot%_unitdir/qemu-pr-helper.socket
# Install rules to use the bridge helper with libvirt's virbr0
install -m 0644 %SOURCE12 %buildroot%_sysconfdir/%name

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%name.conf
%endif

%find_lang %name

# todo: build new openbios and SLOF
# Provided by package openbios
#rm -f %buildroot%_datadir/%name/openbios*
# Provided by package SLOF
#rm -f %buildroot%_datadir/%name/slof.bin
# Provided by package ipxe
rm -f %buildroot%_datadir/%name/pxe*rom
rm -f %buildroot%_datadir/%name/efi*rom
# Provided by package seavgabios
rm -f %buildroot%_datadir/%name/vgabios*bin
# Provided by package seabios
rm -f %buildroot%_datadir/%name/bios.bin
rm -f %buildroot%_datadir/%name/bios-256k.bin
# Provided by package sgabios
#rm -f %buildroot%_datadir/%name/sgabios.bin

# the pxe ipxe images will be symlinks to the images on
# /usr/share/ipxe, as QEMU doesn't know how to look
# for other paths, yet.

for rom in e1000 ne2k_pci pcnet rtl8139 virtio eepro100 e1000e vmxnet3 ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%name/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%name/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%name/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k}.bin %buildroot%_datadir/%name/

mkdir -p %buildroot%_binfmtdir
./scripts/qemu-binfmt-conf.sh --systemd ALL --exportdir %buildroot%_binfmtdir --qemu-path %_bindir
for i in %buildroot%_binfmtdir/*; do
    mv $i $(echo $i | sed 's/.conf/-dynamic.conf/')
done

%if user_static
for regularfmt in %buildroot%_binfmtdir/*; do
    staticfmt="$(echo $regularfmt | sed 's/-dynamic/-static/g')"
    cat $regularfmt | tr -d '\n' | sed "s/:$/-static:F/" > $staticfmt
done
%endif

%check
# Disabled on aarch64 where it fails with several errors.  Will
# investigate and fix when we have access to real hardware

%define archs_skip_tests aarch64
%def_enable archs_ignore_test_failures

%ifnarch %archs_skip_tests

%if_enabled archs_ignore_test_failures
%make V=1 check ||:
%else
%make V=1 check
%endif # archs_ignore_test_failures

%endif # archs_skip_tests

%pre common
%_sbindir/groupadd -r -f %_group
if [ -f %_controldir/qemu-kvm ];then
%pre_control qemu-kvm
mv -f /var/run/control/qemu-kvm /var/run/control/kvm
else
%pre_control kvm
fi

%post common
%post_control -s vmusers kvm

%files
%files common
%dir %_datadir/%name
%_datadir/%name/keymaps
%_datadir/%name/trace-events-all
%_datadir/%name/*.rom
%_datadir/%name/vgabios*.bin
%_datadir/%name/*.bmp
%_datadir/%name/*.svg
%_man1dir/%name.1*
%_sysconfdir/udev/rules.d/%rulenum-%name-kvm.rules
%_controldir/*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%name.conf
%endif
%_man7dir/qemu-block-drivers.*
%_man7dir/qemu-ga-ref.*
%_man7dir/qemu-qmp-ref.*

%files system -f %name.lang

%if_enabled have_kvm
%files kvm
%files kvm-core
%endif

%files user
%_bindir/qemu-*
%exclude %_bindir/qemu*system*
%exclude %_bindir/qemu-kvm
%if_enabled mpath
%exclude %_bindir/qemu-pr-helper
%endif
%if_enabled user_static
%exclude %_bindir/qemu-*.static
%endif
%exclude %_bindir/qemu-img
%exclude %_bindir/qemu-io
%exclude %_bindir/qemu-nbd
%exclude %_bindir/qemu-ga
%exclude %_bindir/qemu-keymap

%files user-binfmt
%_binfmtdir/qemu-*-dynamic.conf

%if_enabled user_static
%files user-static
%_bindir/qemu-*.static

%files user-static-binfmt
%_binfmtdir/qemu-*-static.conf
%endif

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_man1dir/qemu-img.1*
%_man8dir/qemu-nbd.8*

%files tools
%_bindir/virtfs-proxy-helper
%_man1dir/virtfs-proxy-helper.*
%attr(4710,root,vmusers) %_libexecdir/qemu-bridge-helper
%if_enabled mpath
%_bindir/qemu-pr-helper
%_unitdir/qemu-pr-helper.service
%_unitdir/qemu-pr-helper.socket
%endif
%_bindir/qemu-keymap
%config(noreplace) %_sysconfdir/%name/bridge.conf

%files block-curl
%_libdir/qemu/block-curl.so
%files block-dmg
%_libdir/qemu/block-dmg-bz2.so
%files block-gluster
%_libdir/qemu/block-gluster.so
%files block-iscsi
%_libdir/qemu/block-iscsi.so
%files block-nfs
%_libdir/qemu/block-nfs.so
%if_enabled rbd
%files block-rbd
%_libdir/qemu/block-rbd.so
%endif
%files block-ssh
%_libdir/qemu/block-ssh.so

%if_enabled alsa
%files audio-alsa
%_libdir/qemu/audio-alsa.so
%endif
%if_enabled oss
%files audio-oss
%_libdir/qemu/audio-oss.so
%endif
%if_enabled pulseaudio
%files audio-pa
%_libdir/qemu/audio-pa.so
%endif
%if_enabled sdl
%files audio-sdl
%_libdir/qemu/audio-sdl.so
%endif

%if_enabled curses
%files ui-curses
%_libdir/qemu/ui-curses.so
%endif
%if_enabled gtk
%files ui-gtk
%_libdir/qemu/ui-gtk.so
%endif
%if_enabled sdl
%files ui-sdl
%_libdir/qemu/ui-sdl.so
%endif

%files guest-agent
%_bindir/qemu-ga
%_man8dir/qemu-ga.8*
%_udevrulesdir/%rulenum-%name-guest-agent.rules
%_unitdir/%name-guest-agent.service
%_initdir/%name-guest-agent
%config(noreplace) %_sysconfdir/sysconfig/qemu-ga
%_sysconfdir/%name/fsfreeze-hook
%dir %_sysconfdir/%name/fsfreeze-hook.d
%config(noreplace) %_sysconfdir/%name/fsfreeze-hook.d/*
%ghost %_logdir/qga-fsfreeze-hook.log

%files doc
%docdir/
%exclude %docdir/LICENSE

%files aux
%dir %_sysconfdir/%name
%dir %docdir/
%docdir/LICENSE

%files -n ivshmem-tools
%_bindir/ivshmem-client
%_bindir/ivshmem-server

%files system-x86
%files system-x86-core
%if_enabled qemu_kvm
%_bindir/qemu
%_bindir/qemu-kvm
%_bindir/kvm
%endif
%_bindir/qemu-system-i386
%_bindir/qemu-system-x86_64
%_man1dir/qemu-system-i386.1*
%_man1dir/qemu-system-x86_64.1*

%_man1dir/qemu-kvm.1*

%_datadir/%name/bios.bin
%_datadir/%name/bios-256k.bin
%_datadir/%name/sgabios.bin
%_datadir/%name/linuxboot.bin
%_datadir/%name/linuxboot_dma.bin
%_datadir/%name/multiboot.bin
%_datadir/%name/kvmvapic.bin

%files system-alpha
%files system-alpha-core
%_bindir/qemu-system-alpha
%_man1dir/qemu-system-alpha.1*
%_datadir/%name/palcode-clipper

%files system-arm
%files system-arm-core
%_bindir/qemu-system-arm
%_man1dir/qemu-system-arm.1*

%files system-mips
%files system-mips-core
%_bindir/qemu-system-mips*
%_man1dir/qemu-system-mips*

%files system-cris
%files system-cris-core
%_bindir/qemu-system-cris
%_man1dir/qemu-system-cris.1*

%files system-hppa
%files system-hppa-core
%_bindir/qemu-system-hppa
%_man1dir/qemu-system-hppa.1*
%_datadir/%name/hppa-firmware.img

%files system-lm32
%files system-lm32-core
%_bindir/qemu-system-lm32
%_man1dir/qemu-system-lm32.1*

%files system-m68k
%files system-m68k-core
%_bindir/qemu-system-m68k
%_man1dir/qemu-system-m68k.1*

%files system-microblaze
%files system-microblaze-core
%_bindir/qemu-system-microblaze*
%_man1dir/qemu-system-microblaze*
%_datadir/%name/petalogix*.dtb

%files system-or1k
%files system-or1k-core
%_bindir/qemu-system-or1k
%_man1dir/qemu-system-or1k.1*

%files system-s390x
%files system-s390x-core
%_bindir/qemu-system-s390x
%_man1dir/qemu-system-s390x.1*
%_datadir/%name/s390-ccw.img
%_datadir/%name/s390-netboot.img
%ifarch s390x
%_sysconfdir/sysctl.d/50-kvm-s390x.conf
%endif

%files system-sh4
%files system-sh4-core
%_bindir/qemu-system-sh4*
%_man1dir/qemu-system-sh*

%files system-sparc
%files system-sparc-core
%_bindir/qemu-system-sparc*
%_man1dir/qemu-system-sparc*
%_datadir/%name/QEMU,tcx.bin
%_datadir/%name/QEMU,cgthree.bin
%_datadir/%name/openbios-sparc*

%files system-ppc
%files system-ppc-core
%_bindir/qemu-system-ppc*
%_man1dir/qemu-system-ppc*
%_datadir/%name/bamboo.dtb
%_datadir/%name/canyonlands.dtb
%_datadir/%name/ppc_rom.bin
%_datadir/%name/qemu_vga.ndrv
%_datadir/%name/skiboot.lid
%_datadir/%name/spapr-rtas.bin
%_datadir/%name/u-boot.e500
%_datadir/%name/u-boot-sam460-20100605.bin
%_datadir/%name/openbios-ppc
%_datadir/%name/slof.bin
%ifarch %power64
%_sysconfdir/security/limits.d/95-kvm-ppc64-memlock.conf
%endif

%files system-riscv
%files system-riscv-core
%_bindir/qemu-system-riscv32
%_bindir/qemu-system-riscv64
%_man1dir/qemu-system-riscv*

%files system-unicore32
%files system-unicore32-core
%_bindir/qemu-system-unicore32
%_man1dir/qemu-system-unicore32.1*

%files system-xtensa
%files system-xtensa-core
%_bindir/qemu-system-xtensa*
%_man1dir/qemu-system-xtensa*

%files system-moxie
%files system-moxie-core
%_bindir/qemu-system-moxie
%_man1dir/qemu-system-moxie.1*

%files system-aarch64
%files system-aarch64-core
%_bindir/qemu-system-aarch64
%_man1dir/qemu-system-aarch64.1*

%files system-tricore
%files system-tricore-core
%_bindir/qemu-system-tricore
%_man1dir/qemu-system-tricore.1*

%files system-nios2
%files system-nios2-core
%_bindir/qemu-system-nios2
%_man1dir/qemu-system-nios2.1*

%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt1
- 3.1.0

* Tue Dec 11 2018 Ilfat Aminov <aminov@altlinux.org> 3.0.0-alt4
- Enable OpenGL support

* Tue Nov 20 2018 Lenar Shakirov <snejok@altlinux.ru> 3.0.0-alt3
- qemu-kvm.sh fixed on i?86 systems

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- disable vde support

* Wed Aug 15 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt2
- rebuilt against libnfs.so.12
- set arch for qemu-kvm,qemu-user-binfmt,qemu-user-static-binfmt packages

* Fri Apr 27 2018 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- 2.12.0
- use python3 for build
- generate binfmt configs with qemu-binfmt-conf.sh
- build all supported arch targets (riscv too)
- new packages:
  + qemu-audio-alsa
  + qemu-audio-oss
  + qemu-audio-pa
  + qemu-audio-sdl
  + qemu-ui-curses
  + qemu-ui-gtk
  + qemu-ui-sdl

* Fri Feb 16 2018 Alexey Shabalin <shaba@altlinux.ru> 2.11.1-alt1
- 2.11.1
- This update contains new functionality needed to enable mitigations
  for Spectre/Meltdown (CVE-2017-5715)
- fixes for potential host DoS attacks via VGA devices (CVE-2018-5683)
  and VNC clients (CVE-2017-15124)
- revert define MAX_RESERVED_VA for arm

* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 2.11.0-alt2
- backport patch for fix configure test memfd
- add support fsfreeze-hook for qemu guest agent
- move helpers from system to tools package

* Wed Dec 20 2017 Alexey Shabalin <shaba@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Thu Nov 02 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.10.1-alt3
- Enabled support of *attr syscalls in qemu-user static binaries.

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt2
- fixed qemu-kvm for armh and aarch64 (sbolshakov@)
- disable numa for armh (sbolshakov@)

* Tue Oct 10 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.1-alt1
- 2.10.1
- package arm flavour, with defaults to aarch64
- build without tcmalloc
- split system package to arch subpackages
- build block transports as modules and package to separated packages
- build with OpenRisc32,NIOS2,Xtensa emulator
- rename package qemu-user-binfmt_misc to qemu-user-static
- add qemu-user-binfmt and qemu-user-static-binfmt packages with configs in /lib/binfmt.d

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.10.0-alt1
- 2.10.0
- build with SDL2

* Wed Jun 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.0-alt1.1
- rebuild against libnfs.so.11

* Fri Apr 21 2017 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Wed Dec 21 2016 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0
- enable xen support

* Sat Oct 01 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Tue Sep 06 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fixed CVE-2016-4439,CVE-2016-4441,CVE-2016-4952

* Fri May 13 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- fixed CVE-2015-8558,CVE-2015-8619,CVE-2016-1981,CVE-2016-3710,CVE-2016-3712
- move virtfs-proxy-helper and qemu-bridge-helper to from qemu-img to qemu-system
- ignore test failures for check
- add vhost-net manage to control
- disable xen support

* Tue Apr 12 2016 Denis Medvedev <nbr@altlinux.org> 2.5.0-alt2
- Fixed linking.

* Fri Dec 18 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add tilegx arch
- build with jemalloc support
- libcacard is now a standalone project
- build with virgl support
- build with seccomp support
- add ivshmem-tools package
- add qemu-guest-agent sysv script

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0.1-alt1
- 2.4.0.1
- build without gtk3 ui

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt5
- Fixes a crash during image compression (RH#1214855)

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt4
- add requires edk2-ovmf

* Mon Jun 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt3
- add aarch64-softmmu to target_list_system
- fixed CVE-2015-4037, CVE-2015-3209

* Thu May 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2
- fixed CVE-2015-3456

* Tue Apr 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- build with ceph, xfsctl, libnfs, glusterfs support

* Tue Dec 16 2014 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Aug 04 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt2
- fixed migration from older versions (ALT#30033)
- fixed build on arm

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0
- build aarch64-linux-user
- enable support libusb (ALT#29981)
- add condition for libnfs, but disable (need libnfs package)
- enable quorum support
- enable xen support
- enable lzo and snappy support
- enable build with cris,microblaze,sh4 build
- add binfmt config

* Tue Dec 10 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt3
- rebuild with new libiscsi

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt2
- fixed %%post and %%preun common package

* Thu Nov 28 2013 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Oct 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1 (fixed CVE-2013-4344)
- drop qemu-kvm service

* Fri Aug 16 2013 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0
- build with rdma support

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt2
- switch from vgabios to seavgabios

* Mon Jul 29 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2
- fixed CVE-2013-2231

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue May 21 2013 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- build with libssh2
- build with tpm
- build with gtk3 ui

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Apr 16 2013 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1.1
- Fix test (FC patch)

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Dec 24 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.2.0-alt3
- Rebuild with Flattened Device Tree support.

* Fri Nov 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt2
- Introduced -aux subpackage, updated interpackage dependencies.

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Rebuilt with libpng15

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Aug 30 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt5
- Use upstreamed version of the getdents emulation fix,
  to ease further merges.

* Fri Aug 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt4
- Fixed emulation of getdents.

* Thu Aug 09 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt3
- binfmt_misc: package two arm flavours, with defaults to armv5 and armv7

* Wed Jul 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- reverted make check

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- git snapshot of stable-1.1 branch (b7093f294c330c4db789c077dac9d8611e4f8ee0)
- add systemd unit files
- split qemu-guest agent package

* Mon Mar 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.1-alt2
- change arm defaults to convenient values

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1
- enable libiscsi support

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0
- add usb-redir support
- enable spice for i686
- enable compile alpha

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1
- 0.15.0
- disable compile alpha
- enable compile s390x, lm32, unicore32
- enable smartcard support
- enable compile guest agent

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt4
- enable pulseaudio support

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt3
- enable SDL support
- disable pulseaudio support

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt2
- add udev rules,control rules, init script for load kvm kernel module (import from qemu-kvm package)
- drop alternatives for qemu-img
- add doc subpackage
- move man and locales to common subpackage
- use roms and bioses from another packages: vgabios,seabios,gpxe-roms-qemu
- disable SDL support

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0 release

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt0.rc0
- 0.14.0-rc0

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.13.50-alt1
- snapshot 5677903453
- add alternatives for qemu-system-%ix86
- add img subpackage, add alternatives for qemu-img and other
- cleanup attr
- add spice support for x86_64 only
- add libalsa-devel to buildreq for alsa support
- add vnc-jpeg and vnc-png support
- add adlib and hda soundcards
- build without esound support
- add libpci-devel to buildreq
- fix bluez buildreq
- drop non devel library from buildreq
- install config for sasl
- fix install /etc/qemu/*.conf
- qemu-common package as noarch

* Thu Jan 14 2010 Kirill A. Shutemov <kas@altlinux.org> 0.12.1-alt1
- v0.12.1-31-g49a3aaa
- Fix NULL pointer dereference on handling -chardev socket

* Mon Dec 14 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.92-alt1
- v0.12.0-rc2-3-g910628f
- UUID support enabled

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt6
- Fix building binfmt_misc binaries

* Sat Sep 19 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt5
- v0.11.0-rc0-867-gdbf9580
- Do not set uname for linux-user targets
- Use %%check section for tests

* Tue Sep 08 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt4
- v0.11.0-rc0-799-g2637c75
- Compile alpha, m68k, mips and sparc support by default
- Enable Linux AIO
- Enalbe unit tests
- Review configure options
- Update URL
- Update PIE patches

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt3
- Disable IO thread to fix KVM support

* Tue Sep 01 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt2
- fix building on x86_64

* Fri Aug 21 2009 Kirill A. Shutemov <kas@altlinux.org> 0.11.50-alt1
- updated to v0.11.0-rc0-564-g757506d
  + no KQEMU support any more
  + fixes CVE-2008-0928 (ALT #20010)
  + keyboard works fine without -k (ALT #15774)
  + framebuffer works fine with -kernel (ALT #11324)
- build linux-user targets as PIE and drop link hack
- enable KVM support
- enable curl support
- enable IO thread
- enable VNC SASL support
- enable bluez support

* Thu Feb 19 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt11
- svn 20090219
- add hack to implement CLONE_CHILD_CLEARTID
- enable more audio drivers and cards
- enable curses support
- enable vde support
- enable VNC TLS support

* Sun Dec 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt10
- svn 20081214
  + no need in gcc3 any more
- fixes for mmap() related code

* Mon Oct 13 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt9
- svn 20081013
- fix mmap(), mremap() and shmat() syscalls on 64-bit host with
  32-bit targets

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt8
- rename binaries in package qemu-user-binfmt_misc back to *.static
  to make them compatible with hasher

* Fri Oct 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt7
- svn 20081010
  + some changes merged to upstream
- enable/disable binfmt_misc support at compile time
- fix and cleanup system v ipc syscalls
- fix getdents* syscalls
- fix fstatat64()/newfstatat() syscalls
- implement readahead() syscall
- revert some legacy changes

* Sun Sep 14 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt6
- Fix building with glibc-kernheaders-2.6.27-alt1

* Mon Sep 08 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt5
- svn 20080908
- Implement futimesat() syscall
- binfmt-misc-friendly:
  + Use auxv to find out binary file descriptor
- ioctl:
  + Implement ioctls MTIOCTOP, MTIOCGET and MTIOCPOS

* Sun Aug 31 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt4
- 0.9.1 + svn 20080831
- Add option -binfmt-misc-friendly to user emulators

* Fri Aug 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt3
- fix building on i586
- implement fstatat64() syscall

* Sat Aug 23 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt2
- 0.9.1 + svn 20080829
  + CVE-2008-2004
  + Brand new "Tiny Code Generator" by Fabrice Bellard
  + A lot of changes
- Review all changes and patches cleanup
- fix vfork(2) implementation
- Build only x86, arm and ppc architectures by default

* Tue Jan 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.9.1-alt1.cvs20080127
- 0.9.1 + cvs 20080127
- fix-syscalls--iovec
  + do not stop iovec conversion on iov_base == NULL if iov_len is 0
- fix-signals
  + do not show message on uncaught target signal

* Sun Nov 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071124-alt15
- cvs 20071124
- fix-syscalls--getgroups:
  + getgroups: return total number of supplementary group IDs for the
    process if size == 0

* Sat Nov 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071123-alt14
- cvs 20071123
- fix-cpu-copy:
  + Handle cpu_model in copy_cpu()

* Mon Nov 19 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20071119-alt13
- cvs 20071119
- Branch based git repo
- Fix execve syscall
- Build all targets
- adlib: include missed header
- Cleanup configure options
- Drop obsoleted/unsupported patches:
  + qemu-0.6.2-alt-hdtrans.patch
  + qemu-0.7.0-sigaltstackhack.patch
  + qemu-0.9.0-alt-alpha_syscall_nr.patch
  + qemu-0.9.0-alt-arm_syscall_nr.patch
  + qemu-0.9.0-alt-i386_syscall_nr.patch
  + qemu-0.9.0-alt-m68k_syscall_nr.patch
  + qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + qemu-0.9.0-alt-ppc_syscall_nr.patch
  + qemu-0.9.0-alt-qvm86.patch
  + qemu-0.9.0-alt-sh4_syscall_nr.patch
  + qemu-0.9.0-alt-sparc64_syscall_nr.patch
  + qemu-0.9.0-alt-sparc_syscall_nr.patch
  + qemu-0.9.0-alt-syscall_cleanup.patch
  + qemu-0.9.0-disk-scsi.patch
  + qemu-0.9.0-vmware_vga-fix.patch

* Thu Oct 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070917-alt12
- cvs 20070917
- Added qemu-0.9.0-alt-shm.patch
  + Add shm* syscalls
- Sync patches with new version
- Update qemu-0.9.0-security.patch
  + part of fix is in the upsteam
- qemu-0.9.0-alt-alpha_syscall_nr.patch, qemu-0.9.0-alt-ppc64_syscall_nr.patch
  + sync syscall numbers with kernel
- Drop qemu-0.9.0-alt-statfs.patch
  + fixed in upstream

* Fri Aug 24 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt11
- qemu-arm: uname -m => armv4l/armv4b
- fix path(): return NULL if NULL passed

* Fri Jun 08 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070607-alt10
- cvs 20070607
- qemu-0.8.2-nptl.patch -> qemu-0.9.0-nptl.patch, qemu-0.9.0-disk-scsi.patch:
  + rejection fix
- Drop qemu-0.9.0-alt-mips_syscall_nr.patch
  + in the upstream now
- Update qemu-0.9.0-alt-sem.patch and qemu-0.9.0-alt-sem.patch
  + part of this patches is in the upstream now

* Mon May 21 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt9
- Added qemu-0.9.0-alt-getgroups.patch
  + trivial fix
- Moved qemu-0.9.0-sem.patch -> qemu-0.9.0-alt-sem.patch:
  + Fix do_semctl
  + Added standalone syscalls semget, semop, semctl
- Moved qemu-0.9.0-msgop.patch -> qemu-0.9.0-alt-sem.patch
  + Added standalone syscalls msg*
- Dropped qemu-0.9.0-efault.patch

* Tue Apr 03 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070420-alt8
- cvs 20070420
- Added qemu-0.9.0-security.patch:
  + CVE-2007-1320, CVE-2007-1321, CVE-2007-1322, CVE-2007-1323, CVE-2007-1366
- Added qemu-0.9.0-sb16-fix.patch:
  + Fix infinite loop in the SB16 driver
- Disable building alpha emulation due build error
- Update qemu-0.8.2-nptl.patch
  + Fix cpu_env list corruption by disabling CLONE_VM when doing CLONE_VFORK.
    This is a hack to avoid segfault on vfork.
- Added qemu-0.9.0-nptl-update.patch:
  + implemented/fixed several nptl-related syscalls
  + Fix build on i586
- Added qemu-0.9.0-vmware_vga-fix.patch:
  + Disable -vmwarevga acceleration code for now (missing range checks)
- Fix bug #11363
  + rename qemu to qemu-system-i386
  + add symlink qemu to qemu-system-%%_target_os
- Added qemu-0.8.2-deb-tls-ld.patch
  + Fix segfault of user mode qemu on ix86
- Updated qemu-0.9.0-alt-path.patch
  + content of emulation dir can change
  + some refactoring
- Added qemu-0.9.0-alt-arm-eabi-pread-pwrite.patch:
  + pread and pwrite syscall fix for ARM EABI guest
- Added qemu-0.9.0-alt-statfs.patch
  + fix statfs syscall bug
- Updated qemu-0.9.0-alt-i386-user-fix.patch
  + fix qemu-i386 on x86 host
- Update qemu-0.8.2-alt-qvm86.patch -> qemu-0.9.0-alt-qvm86.patch:
  + rejection fexed
- Updated qemu-0.9.0-disk-scsi.patch
  + rejection fixed
- Update qemu-0.9.0-alt-syscall_cleanup.patch:
  + rejection fixed

* Sun Mar 25 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070324-alt7
- cvs 20070324
- Sync syscall numbers with linux-2.6.21-rc4
- Update linux-user/syscall.c:
  + build fix
  + cleaup
- Dropped Debian's patches
- Added qemu-0.9.0-alt-i386-user-fix.patch:
  + fix SIGSEGV in qemu-i386 (by Sergey Vlasov aka vsu@)
- Added qemu-0.9.0-efault.patch:
  + fix returning EFAULT from syscalls
- Added qemu-0.9.0-msgop.patch:
  + fix msg* syscalls
- Added qemu-0.9.0-sem.patch:
  + fix sem* syscalls
- Dropped qemu-0.9.0-alt-fcntl64-fix.patch:
  + in upstream now

* Tue Mar 20 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070320-alt6
- cvs 20070320
- Dropped 43_arm_cpustate.patch,
  qemu-0.9.0-alt-syscall-getsockname-fix.patch,
  qemu-0.9.0-alt-syscalls-clock.patch,
  qemu-0.9.0-alt-syscalls-recv-and-recvfrom-fix.patch:
  + fixed in upstream now
- Updated qemu-0.9.0-alt-makefile.patch, qemu-0.9.0-disk-scsi.patch:
  + fix rejections
- Updated qemu-0.9.0-alt-fcntl64-fix.patch:
  + pass host flag to fcntl instead target flag
- Renamed qemu-0.8.2-alt-path.patch -> qemu-0.9.0-alt-path.patch
- Updated qemu-0.9.0-alt-path.patch:
  + fix memory leak by caching
- Spec cleap

* Fri Mar 09 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt5
- fix fcntl64 syscal: used TARGET_F_*64 instead F_*64
- cdrom name fixed
- option -disk scsi,type=cdrom fixed (bug #11010)

* Sun Mar 04 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0.cvs20070304-alt4
- cvs snapshot
- fix order of ide devices(bug #11004)
- drop mdk patches
- user gcc 3.4 for building(bug #11006)
- fix sigfault
- spec cleanup

* Thu Mar 01 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt3
- cdrom option fixed(bug #10971)
- syscall clock_gettime rewritten
- syscall clock_getres added
- syscalls getsockname, recv and recvfrom fixed

* Wed Feb 28 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt2
- scsi disk support added

* Thu Feb 15 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt1
- lock_user_string used for mount syscall

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.3
- requires fixed
- docs is in package qemu-common now
- description and summary fixed
- alsa enabled
- spec cleanup

* Wed Feb 07 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.2
- mandriva patches updated
- fix realpath() crash again (by vsu@)

* Tue Feb 06 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.9.0-alt0.1
- 0.9.0
- separate into four packages: qemu, softmmu, user, user-static
- spec cleanup
- patches updated

* Mon Feb 05 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.2
- fix crash with -fstack-protector due to wrong realpath() usage
- patches reorganized, debian patches added
- qemu-0.8.2-alt-path.patch fixed
- qemu-arm: uname -m => armv5l/armv5b
- qemu-0.8.2-alt-mmap.patch added
- support msg* and sem* syscalls
- name for static version: qemu-<arch>.static

* Thu Dec 14 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.2-alt1.1
- build static version of qemu-arm
- patches for qemu-arm and other linux mode emulators

* Wed Aug 23 2006 Alexey Tourbin <at@altlinux.ru> 0.8.2-alt1
- 0.8.0 -> 0.8.2
- sync madriva patches 0.8.2-1mdv2007.0
- removed kernel-source-kqemu from here, which should be packaged
  separately because of its non-free status
- added support for /dev/qvm86

* Wed Dec 21 2005 Kachalov Anton <mouse@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Sep 20 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.2-alt1
- 0.7.2
- Updated Kqemu to 0.7.2

* Thu Aug 04 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.1-alt1
- 0.7.1
- Updated:
  * Kqemu to 0.7.1-1
  * GTK support

* Thu Jun 23 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt2
- Added:
  * GTK support (-use-gtk option)
  * Distribution permission from Fabrice Bellard to Kqemu

* Fri Apr 29 2005 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Kqemu support

* Mon Nov 29 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.2-alt1
- Snapshot of 23-28 Nov 2004
- LARGE disk fix (actual for NT4, win2k, winXP)

* Fri Nov 26 2004 Kachalov Anton <mouse@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun Oct 17 2004 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt1
- initial revision
