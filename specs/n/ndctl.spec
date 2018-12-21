%def_without bash
# too old kernel in hasher
%def_disable check

Name: ndctl
Version: 63
Release: alt1

Summary: Manage NVDIMM subsystem devices (Non-volatile Memory)
License: GPLv2
Group: System/Base
Url: https://github.com/pmem/ndctl

#Source: https://github.com/pmem/%name/archive/v%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release
Requires: libdaxctl = %version-%release

BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(json-c)
BuildRequires: libsystemd-devel
%{?_with_bash:BuildRequires: bash-completion >= 2.0}
BuildRequires: asciidoctor asciidoc xmlto

%description
Utility library for managing the "libnvdimm" subsystem. The "libnvdimm"
subsystem defines a kernel device model and control message interface for
platform NVDIMM resources like those defined by the ACPI 6+ NFIT (NVDIMM
Firmware Interface Table).

%package -n lib%name
Summary: Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
License: LGPLv2
Group: System/Libraries
Requires: libdaxctl = %version-%release

%description -n lib%name
Libraries for %name.

%package -n lib%name-devel
Summary: Development files for libndctl
License: LGPLv2
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%package -n daxctl
Summary: Manage Device-DAX instances
License: GPLv2
Group: System/Base
Requires: libdaxctl = %version-%release

%description -n daxctl
The daxctl utility provides enumeration and provisioning commands for
the Linux kernel Device-DAX facility. This facility enables DAX mappings
of performance / feature differentiated memory without need of a
filesystem.

%package -n libdaxctl
Summary: Management library for "Device DAX" devices
License: LGPLv2
Group: System/Libraries

%description -n libdaxctl
Device DAX is a facility for establishing DAX mappings of performance
feature-differentiated memory. libdaxctl provides an enumeration
control API for these devices.

%package -n libdaxctl-devel
Summary: Development files for libdaxctl
License: LGPLv2
Group: Development/C
Requires: libdaxctl = %version-%release

%description -n libdaxctl-devel
This package contains libraries and header files for
developing applications that use libdaxctl, a library for enumerating
"Device DAX" devices.  Device DAX is a facility for establishing DAX
mappings of performance / feature-differentiated memory.

%prep
%setup

%build
echo %version > version
./autogen.sh
%configure --disable-static \
	%{subst_with bash}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name
%_man1dir/%{name}*
%_sysconfdir/%name/monitor.conf
%_unitdir/%name-monitor.service
%{?_with_bash:%_datadir/bash-completion/completions/%name}

%files -n lib%name
%_libdir/lib%name.so.*
%doc README.md

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%files -n daxctl
%_bindir/daxctl
%_man1dir/daxctl*

%files -n libdaxctl
%_libdir/libdaxctl.so.*
%doc README.md

%files -n libdaxctl-devel
%_includedir/daxctl/
%_libdir/libdaxctl.so
%_pkgconfigdir/libdaxctl.pc

%changelog
* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 63-alt1
- 63

* Wed Aug 01 2018 Yuri N. Sedunov <aris@altlinux.org> 61.2-alt1
- 61.2

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 60.3-alt1
- 60.3

* Sat May 12 2018 Yuri N. Sedunov <aris@altlinux.org> 60.1-alt1
- first build for Sisyphus

