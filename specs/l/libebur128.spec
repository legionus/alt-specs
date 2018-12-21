%define _name ebur128
%def_enable check

Name: lib%_name
Version: 1.2.4
Release: alt1

Summary: A library that implements the EBU R 128 standard for loudness normalization
Group: Sound
License: MIT
Url: https://github.com/jiixyj/%name

Source: https://github.com/jiixyj/%name/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildRequires: cmake gcc-c++

%description
A library that implements the EBU R 128 standard for loudness
normalization.

It implements M, S and I modes, loudness range measurement (EBU - TECH
3342), true peak scanning and all sample-rates by recalculation of the
filter coefficients.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%make -C BUILD test

%files
%_libdir/%name.so.*
%doc README.md COPYING

%files devel
%_includedir/%_name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%exclude %_libdir/%name.a

%changelog
* Sun Jul 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- first build for Sisyphus

