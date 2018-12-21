# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.a1.1.1
%define oname z3c.layer.ready2go

%def_with python3

Name: python-module-%oname
Version: 1.0.0
#Release: alt2.a1.1
Summary: A ready to go layer for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.ready2go/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.interface python-module-zope.testrunner
BuildPreReq: python-module-eggtestinfo
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.interface python3-module-zope.testrunner
BuildPreReq: python3-module-eggtestinfo
%endif

%py_requires z3c.form z3c.formui z3c.layer.pagelet zope.viewlet

%description
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

%package -n python3-module-%oname
Summary: A ready to go layer for Zope3
Group: Development/Python3
%py3_requires z3c.form z3c.formui z3c.layer.pagelet zope.viewlet

%description -n python3-module-%oname
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.layer.ready2go
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testbrowser zope.app.authentication zope.app.testing
%py3_requires zope.browserresource zope.principalregistry zope.publisher
%py3_requires zope.security zope.securitypolicy zope.testing

%description -n python3-module-%oname-tests
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

This package contains tests for z3c.layer.ready2go.

%package tests
Summary: Tests for z3c.layer.ready2go
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.authentication zope.app.testing
%py_requires zope.browserresource zope.principalregistry zope.publisher
%py_requires zope.security zope.securitypolicy zope.testing

%description tests
This package provides a layer based on z3c.form and z3c.pagelet. This
layer can be used in custom skins.

This package contains tests for z3c.layer.ready2go.

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
rm -f %buildroot%python3_sitelibdir/*/*/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/*/*/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.a1
- Added module for Python 3

* Sat Apr 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a1
- Version 1.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

