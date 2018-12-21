# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1.1
%define oname z3c.jsonrpc

%def_with python3

Name: python-module-%oname
Version: 0.7.2
#Release: alt2.1
Summary: JSON RPC server and client implementation for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.jsonrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.json zope.app.publication zope.component
%py_requires zope.configuration zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.location zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
This package provides an JSON-RPC server implementation for Zope3.

%package -n python3-module-%oname
Summary: JSON RPC server and client implementation for Zope3
Group: Development/Python3
%py3_requires z3c.json zope.app.publication zope.component
%py3_requires zope.configuration zope.i18n zope.i18nmessageid
%py3_requires zope.interface zope.location zope.publisher zope.schema
%py3_requires zope.security zope.traversing

%description -n python3-module-%oname
This package provides an JSON-RPC server implementation for Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.jsonrpc
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage zope.app.testing zope.security
%py3_requires zope.browserpage zope.principalregistry zope.testbrowser
%py3_requires zope.testing zope.securitypolicy

%description -n python3-module-%oname-tests
This package provides an JSON-RPC server implementation for Zope3.

This package contains tests for z3c.jsonrpc.

%package tests
Summary: Tests for z3c.jsonrpc
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.app.testing zope.security
%py_requires zope.browserpage zope.principalregistry zope.testbrowser
%py_requires zope.testing zope.securitypolicy

%description tests
This package provides an JSON-RPC server implementation for Zope3.

This package contains tests for z3c.jsonrpc.

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
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

