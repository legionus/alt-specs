Name: df_shm
Version: r16567
Release: alt1.svn20131216
Summary: %name package for EVpath
License: BSD
Group: Development/Other
Url: http://www.cc.gatech.edu/systems/projects/EVPath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.research.cc.gatech.edu/kaos/df_shm/trunk/
# login: anon
# password: anon
Source: %name-%version.tar

BuildPreReq: cmake ctest gcc-c++

%description
%name package for EVpat.

%package -n lib%name
Summary: %name package for EVpath
Group: System/Libraries

%description -n lib%name
%name package for EVpat.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
%name package for EVpat.

This package contains development files of %name.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r16567-alt1.svn20131216
- Initial build for Sisyphus

