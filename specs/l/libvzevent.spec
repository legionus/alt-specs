
%define _libver_major 1
%define _libver_minor 0
%define _libver %_libver_major.%_libver_minor

Name: libvzevent
Summary: Virtuozzo event library
Version: 7.0.7
Release: alt1
License: LGPLv2.1
Group: System/Libraries
Source: %name-%version.tar
Source2: vzevent.tmpfiles
Patch: %name-%version.patch

%description
libvzevent is an event library. It is a component of OpenVZ.

%package devel
Summary: Virtuozzo event development library
Group: Development/C
Requires: %name = %version-%release

%description devel
Virtuozzo event development library

%prep
%setup -q
%patch -p1

%build
%add_optflags %optflags_shared
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std -C src LIBDIR=%_libdir LIBVER=%_libver_major LIBVER_MINOR=%_libver_minor
install -pD -m644 %SOURCE2 %buildroot%_tmpfilesdir/vzevents.conf

%files
%_libdir/libvzevent.so.*
%_tmpfilesdir/vzevents.conf

%files devel
%_libdir/libvzevent.so
%dir %_includedir/vz
%_includedir/vz/*.h

%changelog
* Thu Feb 08 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.7-alt1
- Inital build
