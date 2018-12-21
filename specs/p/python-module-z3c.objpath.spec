# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1.1
%define oname z3c.objpath

%def_with python3

Name: python-module-%oname
Version: 1.1
#Release: alt2.1
Summary: Generate and resolve paths to to objects
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.objpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.interface zc.buildout

%description
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

%package -n python3-module-%oname
Summary: Generate and resolve paths to to objects
Group: Development/Python3
%py3_requires zope.interface zc.buildout

%description -n python3-module-%oname
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.objpath
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

This package contains tests for z3c.objpath.

%package tests
Summary: Tests for z3c.objpath
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

This package contains tests for z3c.objpath.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

