Name: volk
Version: 1.4
Release: alt1.1
Summary: Vector-Optimized Library of Kernels
License: GPLv3
Group: Development/C++
Url: http://libvolk.org/

Source: %name-%version.tar

%description
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n lib%name
Group: Development/C++
Summary: Vector-Optimized Library of Kernels
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: liborc-devel orc
BuildRequires: boost-filesystem-devel

%description -n lib%name
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n lib%name-devel
Summary: Vector-Optimized Library of Kernels
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
VOLK:
- is the Vector-Optimized Library of Kernels;
- is a free library, currently offered under the GPLv3 license;
- provides an abstraction of optimized math routines targetting several SIMD processors.

%package -n python-module-%name
Summary: The Python bindings for VOLK
Group: Development/Python
BuildRequires: python-module-six
BuildRequires: python-module-mako
Requires: lib%name = %version

%description -n python-module-%name
Python module for VOLK.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%doc COPYING README.md

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/%name

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 22 2018 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- new version 1.4

* Fri Aug 11 2017 Anton Midyukov <antohami@altlinux.org> 1.3-alt1
- New version 1.3

* Tue Mar 25 2016 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- Initial ALT Linux build.
