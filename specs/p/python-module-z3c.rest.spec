# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname z3c.rest

%def_with python3

Name: python-module-%oname
Version: 0.4.0
#Release: alt3.1
Summary: A REST Framework for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires lxml z3c.traverser zope.publisher zope.app.http

%description
This package provides a framework to build REST APIs on top of Zope 3.

%package -n python3-module-%oname
Summary: A REST Framework for Zope 3 Applications
Group: Development/Python3
%py3_requires lxml z3c.traverser zope.publisher zope.app.http

%description -n python3-module-%oname
This package provides a framework to build REST APIs on top of Zope 3.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.rest
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage z3c.etestbrowser zope.app.container
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
This package provides a framework to build REST APIs on top of Zope 3.

This package contains tests for z3c.rest.

%package tests
Summary: Tests for z3c.rest
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage z3c.etestbrowser zope.app.container
%py_requires zope.app.testing

%description tests
This package provides a framework to build REST APIs on top of Zope 3.

This package contains tests for z3c.rest.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

