Name: pyside-qt4
Version: 1.2.2
Release: alt3.git20140501
Summary: Python bindings for the Qt cross-platform application and UI framework
License: LGPLv2.1
Group: Development/Tools
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libqt4-devel gcc-c++ cmake
BuildPreReq: python-module-sphinx-devel shiboken libshiboken-devel
BuildPreReq: libgeneratorrunner-devel graphviz xvfb-run
BuildPreReq: generatorrunner phonon-devel qt4-designer xml-utils
BuildPreReq: xsltproc libxml2-devel libxslt-devel
BuildPreReq: libqt4-assistant-devel

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

%package -n lib%name
Summary: Shared libraries of PySide
Group: System/Libraries

%description -n lib%name
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains shared libraries of PySide.

%package -n lib%name-devel
Summary: Development files of PySide
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains development files of PySide.

%package -n lib%name-devel-doc
Summary: Documentation for PySide
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains development documentation for PySide.

%package -n python-module-PySide
Summary: Python module of PySide
Group: Development/Python

%description -n python-module-PySide
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains python module of PySide.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc

%build
export PATH=$PATH:%_qt4dir/bin
%add_optflags -I%_includedir/shiboken
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DENABLE_GCC_OPTIMIZATION:BOOL=ON \
	-DENABLE_VERSION_SUFFIX:BOOL=OFF \
	-DQT_SRC_DIR:PATH=%_datadir/graphviz \
	-DUSE_XVFB:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DQT_PHONON_INCLUDE_DIR:PATH="%_includedir/kde4" \
	.

%make_build VERBOSE=1

%install
%makeinstall_std

pushd doc
export PATH=$PATH:%_qt4dir/bin
cmake -DCMAKE_INSTALL_PREFIX:PATH=%buildroot%prefix .
%make apidocinstall
mv %buildroot%_docdir/PySide- %buildroot%_docdir/PySide
popd

%files -n lib%name
%doc COPYING
%_libdir/*.so.*
%_datadir/PySide*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/PySide

%files -n python-module-PySide
%python_sitelibdir/*

%changelog
* Fri Apr 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt3.git20140501
- fix packaging on 64bit arches other than x86_64

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt2.git20140501
- Exclude ENABLE_VERSION_SUFFIX to prevent difference between
  /usr/include/PySide-1.2/QtGui and /usr/include/PySide/QtGui

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20140501
- New snapshot

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20140422
- Version 1.2.2

* Fri Nov 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20130724
- Version 1.2.1

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20130522
- New snapshot

* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1
- Initial build for Sisyphus

