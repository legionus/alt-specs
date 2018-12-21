# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname zope.app.pagetemplate

%def_with python3

Name: python-module-%oname
Version: 3.11.2
#Release: alt3.1
Summary: PageTemplate integration for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.pagetemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.browserpage zope.component zope.configuration
%py_requires zope.dublincore zope.i18nmessageid zope.interface
%py_requires zope.pagetemplate zope.schema zope.security zope.size
%py_requires zope.tales zope.traversing

%description
The zope.app.pagetemplate package integrates the Page Template
templating system (zope.pagetemplate) into the Zope 3 application
server.

%package -n python3-module-%oname
Summary: PageTemplate integration for Zope 3
Group: Development/Python3
%py3_requires zope.app zope.browserpage zope.component zope.configuration
%py3_requires zope.dublincore zope.i18nmessageid zope.interface
%py3_requires zope.pagetemplate zope.schema zope.security zope.size
%py3_requires zope.tales zope.traversing

%description -n python3-module-%oname
The zope.app.pagetemplate package integrates the Page Template
templating system (zope.pagetemplate) into the Zope 3 application
server.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.pagetemplate
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component zope.container zope.publisher

%description -n python3-module-%oname-tests
The zope.app.pagetemplate package integrates the Page Template
templating system (zope.pagetemplate) into the Zope 3 application
server.

This package contains tests for zope.app.pagetemplate.

%package tests
Summary: Tests for zope.app.pagetemplate
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component zope.container zope.publisher

%description tests
The zope.app.pagetemplate package integrates the Page Template
templating system (zope.pagetemplate) into the Zope 3 application
server.

This package contains tests for zope.app.pagetemplate.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.11.2-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.11.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.11.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11.2-alt1
- Initial build for Sisyphus

