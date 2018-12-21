%define TOOL_CHAIN_TAG GCC49
%define openssl_ver 1.1.0e

%def_disable cross

%ifarch %{ix86} x86_64
%def_enable build_ovmf_ia32
%ifarch x86_64
%def_enable build_ovmf_x64
%endif
%endif

%ifarch aarch64
%def_enable build_aavmf_aarch64
%endif

%ifarch %{arm}
%def_enable build_aavmf_arm
%endif

%if_enabled cross
%def_enable build_ovmf_x64
%def_enable build_ovmf_ia32
%def_enable build_aavmf_aarch64
%def_enable build_aavmf_arm
%endif

# More subpackages to come once licensing issues are fixed
Name: edk2
Version: 20181113
Release: alt1
Summary: EFI Development Kit II

#Vcs-Git: https://github.com/tianocore/edk2.git
Source: %name-%version.tar

Source2: openssl.tar
Source3: Logo.bmp

Patch1: %name-%version.patch

License: BSD
Group: Emulators
Url: http://www.tianocore.org

%if_enabled cross
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
%else
ExclusiveArch:  x86_64 aarch64
%endif

%if_enabled cross
BuildRequires: gcc-c++-x86_64-linux-gnu
%{?_enable_aarch64:BuildRequires: gcc-c++-aarch64-linux-gnu}
%{?_enable_arm:BuildRequires: gcc-c++-arm-linux-gnu}
%endif

BuildRequires: iasl nasm gcc-c++
BuildRequires: python-devel python-modules-sqlite3
BuildRequires: libuuid-devel

%description
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.

%package tools
Summary: EFI Development Kit II Tools
Group: Emulators

%description tools
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package tools-python
Summary: EFI Development Kit II Tools
Group: Development/Python
BuildArch: noarch

%description tools-python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.

%package tools-doc
Summary: Documentation for EFI Development Kit II Tools
Group: Development/Documentation
BuildArch: noarch

%description tools-doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package ovmf
Summary: Open Virtual Machine Firmware
Group: Emulators
Requires: ipxe-roms-qemu
Requires: seavgabios
License: BSD License (no advertising) with restrictions on use and redistribution
%if_enabled cross
BuildArch: noarch
%endif

%description ovmf
EFI Development Kit II
Open Virtual Machine Firmware

%package ovmf-ia32
Summary: Open Virtual Machine Firmware
Group: Emulators
License:        BSD and OpenSSL
%if_enabled cross
BuildArch:      noarch
%endif

%description ovmf-ia32
EFI Development Kit II
Open Virtual Machine Firmware (ia32)

%package aarch64
Summary: AARCH64 Virtual Machine Firmware
Group: Emulators
%if_enabled cross
BuildArch:      noarch
%endif

%description aarch64
EFI Development Kit II
AARCH64 UEFI Firmware

%package arm
Summary: ARM Virtual Machine Firmware
Group: Emulators
%if_enabled cross
BuildArch:      noarch
%endif

%description arm
EFI Development Kit II
armv7 UEFI Firmware

%package efi-shell
Summary: EFI Development Kit II
Group: System/Kernel and hardware
Provides: efi-shell = 2.2
Obsoletes: efi-shell

%description efi-shell
EFI Development Kit II implementation of UEFI Shell 2.0+

%prep
%setup -q
%patch1 -p1

cp -f %SOURCE3 MdeModulePkg/Logo/

# cleanup
find . -name '*.efi' -print0 | xargs -0 rm -f
rm -rf BaseTools/Bin \
	UefiCpuPkg/ResetVector/Vtf0/Bin/*.raw \
	EdkCompatibilityPkg/Other \
	AppPkg \
	DuetPkg/BootSector/bin \
	StdLib/LibC/Main/Ia32/ftol2.obj \
	BeagleBoardPkg/Debugger_scripts/rvi_dummy.axf \
	BaseTools/Source/Python/*/*.pyd \
	BaseTools/Source/Python/UPT/Dll/sqlite3.dll \
	Vlv2TbltDevicePkg/GenBiosId \
	Vlv2TbltDevicePkg/*.exe \
	ArmPkg/Library/GccLto/liblto-*.a

# Ensure old shell and binary packages are not used
rm -rf EdkShellBinPkg
rm -rf EdkShellPkg
rm -rf FatBinPkg
rm -rf ShellBinPkg

# add openssl
mkdir -p CryptoPkg/Library/OpensslLib/openssl
tar -xf %SOURCE2 -C CryptoPkg/Library/OpensslLib/openssl --strip-components 1

%build

source ./edksetup.sh

# compiler
CC_FLAGS="-t %TOOL_CHAIN_TAG"

# common features
#CC_FLAGS="${CC_FLAGS} --cmd-len=65536 -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} -b RELEASE"
#CC_FLAGS="${CC_FLAGS} -b DEBUG --hash"
CC_FLAGS="${CC_FLAGS} --cmd-len=65536"
CC_FLAGS="${CC_FLAGS} -D NETWORK_IP6_ENABLE"
CC_FLAGS="${CC_FLAGS} -D TPM2_ENABLE"

# ovmf features
OVMF_FLAGS="${CC_FLAGS}"
OVMF_FLAGS="${OVMF_FLAGS} -D TLS_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D HTTP_BOOT_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D NETWORK_IP6_ENABLE"
OVMF_FLAGS="${OVMF_FLAGS} -D FD_SIZE_2MB"

# ovmf + secure boot features
OVMF_SB_FLAGS="${OVMF_FLAGS}"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SECURE_BOOT_ENABLE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D SMM_REQUIRE"
OVMF_SB_FLAGS="${OVMF_SB_FLAGS} -D EXCLUDE_SHELL_FROM_FD"

# arm firmware features
#ARM_FLAGS="-t %TOOL_CHAIN_TAG -b DEBUG --cmd-len=65536"
ARM_FLAGS="${CC_FLAGS}"
ARM_FLAGS="${ARM_FLAGS} -D DEBUG_PRINT_ERROR_LEVEL=0x8040004F"


unset MAKEFLAGS

# prepare
#cp /usr/share/seabios/bios-csm.bin OvmfPkg/Csm/Csm16/Csm16.bin
#cp /usr/share/seabios/bios-csm.bin corebootPkg/Csm/Csm16/Csm16.bin
%make \
	 -C BaseTools


#(cd UefiCpuPkg/ResetVector/Vtf0; python Build.py)

#mkdir -p FatBinPkg/EnhancedFatDxe/{X64,Ia32}
#source ./edksetup.sh

# build ovmf
%if_enabled cross
export %{TOOL_CHAIN_TAG}_IA32_PREFIX="x86_64-linux-gnu-"
export %{TOOL_CHAIN_TAG}_X64_PREFIX="x86_64-linux-gnu-"
export %{TOOL_CHAIN_TAG}_AARCH64_PREFIX="aarch64-linux-gnu-"
export %{TOOL_CHAIN_TAG}_ARM_PREFIX="arm-linux-gnu-"
%endif

# build ovmf (x64)
%if_enabled build_ovmf_x64
mkdir -p OVMF
build ${OVMF_FLAGS} -a X64 -p OvmfPkg/OvmfPkgX64.dsc
cp Build/OvmfX64/*/FV/OVMF_*.fd OVMF
rm -rf Build/OvmfX64
# build ovmf with secure boot
build ${OVMF_SB_FLAGS} -a IA32 -a X64 -p OvmfPkg/OvmfPkgIa32X64.dsc
cp Build/Ovmf3264/*/FV/OVMF_CODE.fd OVMF/OVMF_CODE.secboot.fd
%endif

# build shell
%ifarch x86_64
build ${OVMF_FLAGS} -a X64 -p ShellPkg/ShellPkg.dsc
%endif

# build ovmf-ia32
%if_enabled build_ovmf_ia32
mkdir -p ovmf-ia32
build ${OVMF_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/
rm -rf Build/OvmfIa32
# build ovmf-ia32 with secure boot
build ${OVMF_SB_FLAGS} -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc
cp Build/OvmfIa32/*/FV/OVMF_CODE.fd ovmf-ia32/OVMF_CODE.secboot.fd
%endif


# build aarch64 firmware
%if_enabled build_aavmf_aarch64
mkdir -p AAVMF
build ${ARM_FLAGS} -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc
cp Build/ArmVirtQemu-AARCH64/*/FV/*.fd AAVMF
dd of="AAVMF/QEMU_EFI-pflash.raw" if="/dev/zero" bs=1M count=64
dd of="AAVMF/QEMU_EFI-pflash.raw" if="AAVMF/QEMU_EFI.fd" conv=notrunc
dd of="AAVMF/vars-template-pflash.raw" if="/dev/zero" bs=1M count=64
%endif

# build arm firmware
%if_enabled build_aavmf_arm
mkdir -p AVMF
build ${ARM_FLAGS} -a ARM -p ArmVirtPkg/ArmVirtQemu.dsc
cp Build/ArmVirtQemu-ARM/DEBUG_*/FV/*.fd AVMF
dd of="AVMF/QEMU_EFI-pflash.raw" if="/dev/zero" bs=1M count=64
dd of="AVMF/QEMU_EFI-pflash.raw" if="AVMF/QEMU_EFI.fd" conv=notrunc
dd of="AVMF/vars-template-pflash.raw" if="/dev/zero" bs=1M count=64
%endif

%install
# install BaseTools
mkdir -p %buildroot%_bindir \
         %buildroot%_datadir/%name/Conf \
         %buildroot%_datadir/%name/Scripts

pushd BaseTools
install --strip \
	Source/C/bin/* \
	%buildroot%_bindir

ln -f %buildroot%_bindir/GnuGenBootSector \
	%buildroot%_bindir/GenBootSector

install \
	BinWrappers/PosixLike/LzmaF86Compress \
	%buildroot%_bindir

install \
	BuildEnv \
	%buildroot%_datadir/%name

install \
	Conf/*.template \
	%buildroot%_datadir/%name/Conf

install \
	Scripts/GccBase.lds \
	%buildroot%_datadir/%name/Scripts

cp -R Source/Python %buildroot%_datadir/%name/Python

find %buildroot%_datadir/%name/Python -name "*.pyd" | xargs rm -f

for i in BPDG Ecc GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
  echo '#!/bin/sh
PYTHONPATH=%_datadir/%name/Python
export PYTHONPATH
exec python '%_datadir/%name/Python/$i/$i.py' "$@"' > %buildroot%_bindir/$i
  chmod +x %buildroot%_bindir/$i
done

popd

# shell
%ifarch x86_64
install -pm0644 -D Build/Shell/RELEASE_%TOOL_CHAIN_TAG/X64/Shell.efi \
	%buildroot%_libdir/efi/shell.efi
%endif

#install OVMF
mkdir -p %buildroot%_datadir/%name
%if_enabled build_ovmf_x64
cp -a OVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/OVMF %buildroot%_datadir/%name/ovmf
%endif
%if_enabled build_ovmf_ia32
cp -a ovmf-ia32 %buildroot%_datadir/%name
%endif
%if_enabled build_aavmf_aarch64
cp -a AAVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/AAVMF %buildroot%_datadir/%name/aarch64
%endif
%if_enabled build_aavmf_arm
cp -a AVMF %buildroot%_datadir/
ln -r -s %buildroot%_datadir/AVMF %buildroot%_datadir/%name/arm
%endif

%files tools
%_bindir/BootSectImage
%_bindir/EfiLdrImage
%_bindir/EfiRom
%_bindir/GenBootSector
%_bindir/GenCrc32
%_bindir/GenFfs
%_bindir/GenFv
%_bindir/GenFw
%_bindir/GenPage
%_bindir/GenSec
%_bindir/GenVtf
%_bindir/GnuGenBootSector
%_bindir/LzmaCompress
%_bindir/LzmaF86Compress
%_bindir/Split
%_bindir/TianoCompress
%_bindir/VfrCompile
%_bindir/VolInfo
%_datadir/%name/BuildEnv
%_datadir/%name/Conf
%_datadir/%name/Scripts

#%files tools-python
#%_bindir/BPDG
#%_bindir/Ecc
#%_bindir/GenDepex
#%_bindir/GenFds
#%_bindir/GenPatchPcdTable
#%_bindir/PatchPcdValue
#%_bindir/TargetTool
#%_bindir/Trim
#%_bindir/UPT
#%_datadir/%name/Python/

%files tools-doc
%doc BaseTools/UserManuals/*.rtf

%if_enabled build_ovmf_x64
%files ovmf
#%doc FatBinPkg/License.txt
%doc OvmfPkg/License.txt
%_datadir/OVMF
%dir %_datadir/%name
%_datadir/%name/ovmf
%endif

%if_enabled build_ovmf_ia32
%files ovmf-ia32
%doc OvmfPkg/License.txt
%_datadir/%name/ovmf-ia32
%endif

%if_enabled build_aavmf_aarch64
%files aarch64
%_datadir/AAVMF
%_datadir/%name/aarch64
%endif

%if_enabled build_aavmf_arm
%files arm
%_datadir/AVMF
%_datadir/%name/arm
%endif

%ifarch x86_64
%files efi-shell
%_libdir/efi/shell.efi
%endif

%changelog
* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 20181113-alt1
- edk2-stable201811

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt3%ubt
- snapshot of UDK2017 branch

* Mon Sep 18 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170720-alt2%ubt
- added efi-shell subpackage

* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 20170720-alt1%ubt
- snapshot of UDK2017 branch

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 20161227-alt1
- UDK2017 branch

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 20160518-alt1
- master snapshot 855743f7177459bea95798e59b6b18dab867710c

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 20151225-alt1.svn19549
- build from branche UDK2015

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt2
- buils ovmf as noarch

* Wed Jun 17 2015 Alexey Shabalin <shaba@altlinux.ru> 20150616svn17642-alt1
- svn snapshot r17642
- add ovmf package

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 20140722svn2674-alt1
- svn snapshot r2674

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1.svn2594
- initial build
