%define module_name	LiME
%define module_version	1.7.8

%define module_release alt1.k

%define flavour		std-def
%define karch x86_64 i586
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: LiME module for Linux kernel 
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: BSD 3-clause
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>


ExclusiveOS: Linux
Url: http://www.linuxfoundation.org/collaborate/workgroups/networking/alx 
BuildRequires(pre): rpm-build-kernel
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
This driver provide a Linux Memory Extractor


%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar.*
%setup -D -T -n kernel-source-%module_name-%version

%build
make -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules

%install
mkdir -p %buildroot/%module_dir
install lime.ko %buildroot/%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
