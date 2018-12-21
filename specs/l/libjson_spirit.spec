
%define xx_name json_spirit

Name: lib%xx_name
Version: 4.08
Release: alt1

Summary: JSON parser for C++ written with Boost.Spirit
License: The Code Project Open License (CPOL) 1.02
Group: System/Libraries

Url: http://www.codeproject.com/KB/recipes/JSON_Spirit.aspx
Source: %xx_name-v%version.tar
Source1: CMakeLists.txt-%xx_name
#Patch: json_spirit-2.06-alt-boost-1.52.0.patch

# Automatically added by buildreq on Fri Jul 18 2008
BuildRequires: boost-devel gcc-c++ cmake

%description
JSON (www.json.org) is a text file format similar to XML, but less verbose.
This package includes JSON Spirit, a C++ library that reads and writes JSON
files or streams. It is written using the Boost Spirit parser generator.

%package devel
Group: Development/C++
Summary: JSON Spirit development files
Requires: %name = %version

%description devel
JSON Spirit development files.

%prep
%setup -n %xx_name-v%version
#patch -p2
install -pm644 %_sourcedir/CMakeLists.txt-%xx_name json_spirit/CMakeLists.txt
mkdir build
cd build
cmake ../%xx_name/ \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
         -DCMAKE_C_FLAGS:STRING="%optflags" \
         -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_BUILD_TYPE="Release" \
       -DCMAKE_SKIP_RPATH=YES

%build
pushd build
%make_build VERBOSE=1
popd

%install
pushd build
%makeinstall_std
popd

%files
%_libdir/*.so.*

%files devel
%_includedir/%xx_name
%_libdir/*.so

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.08-alt1
- Version 4.08

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.06-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.06-alt2.1
- Fixed build with Boost 1.52.0

* Tue Nov 18 2008 Ivan A. Melnikov <iv@altlinux.org> 2.06-alt2
- switched to using cmake

* Fri Oct 17 2008 Ivan A. Melnikov <iv@altlinux.org> 2.06-alt1
- inital build for ALT

