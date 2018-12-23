# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libsavitar
Version: 3.4.1
Release: alt1
Summary: C++ implementation of 3mf loading with SIP Python bindings
License: LGPLv3+
Group: Development/Other
Url: https://github.com/Ultimaker/libSavitar
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: %name-no-pugixml.patch

Buildrequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake dos2unix gcc-c++ libpugixml-devel python3-devel python3-module-sip-devel %_bindir/sip

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package devel
Summary: Development files for libsavitar
# The cmake scripts are BSD
License: AGPL-3.0-or-later and BSD
Group: Development/Other
Requires: %name = %version-%release

%description devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n python3-module-savitar
Summary: Python 3 libSavitar bindings
Group: Development/Python3
Requires: %name = %version-%release
%py3_provides Savitar

%description -n python3-module-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%setup
%patch -p1

# Wrong end of line encoding
dos2unix README.md

# Bundling
rm pugixml -rf
%__subst 's|"../pugixml/src/pugixml.hpp"|<pugixml.hpp>|g' src/*.cpp src/*.h

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md LICENSE
%_libdir/libSavitar.so.*

%files devel
%doc README.md LICENSE
%_libdir/libSavitar.so
%_includedir/Savitar
# Own the dir not to depend on cmake:
%_libdir/cmake

%files -n python3-module-savitar
%doc README.md LICENSE
%python3_sitelibdir/Savitar.so

%changelog
* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1.S1
- new version 3.3.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1.S1
- new version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1.S1
- Initial build for ALT Sisyphus.
