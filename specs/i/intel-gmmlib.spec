%define _unpackaged_files_terminate_build 1
%define soversion 1
ExclusiveArch: %ix86 x86_64
Name:     intel-gmmlib
Version:  18.3.0
Release:  alt1
Summary:  Intel(R) Graphics Memory Management Library
License:  MIT
Group:    System/Libraries
Url:      https://github.com/intel/gmmlib
Source:   %name-%version.tar
BuildRequires: cmake rpm-macros-cmake gcc-c++
%description
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and 
the Intel(R) Media Driver for VAAPI.

%package -n libigdgmm%soversion
Summary:  Intel(R) Graphics Memory Management Library
Group:    System/Libraries
%description -n libigdgmm%soversion
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and
the Intel(R) Media Driver for VAAPI.

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
This package provides the development environment for %name

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot/%_libdir/*.a

%files -n libigdgmm%soversion
%_libdir/*.so.%{soversion}*

%files devel
%doc README.rst
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

