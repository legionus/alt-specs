# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname zc.selenium

%def_with python3

Name: python-module-%oname
Version: 1.2.1
#Release: alt3.1
Summary: Selenium integration for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.selenium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zope.interface zope.component zope.publisher
%py_requires z3c.zrtresource

%description
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

%package -n python3-module-%oname
Summary: Selenium integration for Zope 3
Group: Development/Python3
%py3_requires zc zope.interface zope.component zope.publisher
%py3_requires z3c.zrtresource

%description -n python3-module-%oname
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

%package -n python3-module-%oname-tests
Summary: Tests for Selenium integration for Zope 3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

This package contains tests for Selenium integration for Zope 3.

%package tests
Summary: Tests for Selenium integration for Zope 3
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

This package contains tests for Selenium integration for Zope 3.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*test.py*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*test.py*
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test.py
%exclude %python3_sitelibdir/*/*/__pycache__/*test.*
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test.py
%python3_sitelibdir/*/*/__pycache__/*test.*
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

