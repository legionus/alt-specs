
Name: libvcmmd
Version: 7.0.22
Release: alt1
Summary: Library for accessing vcmmd
Group: System/Libraries
License: LGPLv2.1
Source: %name-%version.tar
#Patch: %name-%version.patch
BuildRequires: libdbus-devel

%description
This package contains a library that provides a convenient API for accessing
the vcmmd daemon. It can be used in order to configure memory settings of
Virtuozzo Containers and VMs.

%package devel
Summary: Development files for libvcmmd
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files and libraries needed for developing software
that uses libvcmmd.

%prep
%setup -q
#patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libvcmmd.so.*


%files devel
%_libdir/libvcmmd.so
%dir %_includedir/libvcmmd
%_includedir/libvcmmd/*.h

%changelog
* Thu Feb 08 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.22-alt1
- Initial build
