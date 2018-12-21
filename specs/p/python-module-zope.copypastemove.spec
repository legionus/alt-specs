# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname zope.copypastemove

%def_with python3

Name: python-module-%oname
Version: 4.0.0
#Release: alt3.1
Summary: Copy, Paste and Move support for content components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.copypastemove/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.annotation zope.component zope.container
%py_requires zope.copy zope.event zope.exceptions zope.interface
%py_requires zope.lifecycleevent zope.location

%description
This package provides Copy, Paste and Move support for content
components in Zope.

%package -n python3-module-%oname
Summary: Copy, Paste and Move support for content components
Group: Development/Python3
%py3_requires zope zope.annotation zope.component zope.container
%py3_requires zope.copy zope.event zope.exceptions zope.interface
%py3_requires zope.lifecycleevent zope.location

%description -n python3-module-%oname
This package provides Copy, Paste and Move support for content
components in Zope.

%package -n python3-module-%oname-tests
Summary: Tests for zope.copypastemove
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.principalannotation zope.testing zope.traversing
%py3_requires zope.dublincore

%description -n python3-module-%oname-tests
This package provides Copy, Paste and Move support for content
components in Zope.

This package contains tests for zope.copypastemove.

%package tests
Summary: Tests for zope.copypastemove
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.principalannotation zope.testing zope.traversing
%py_requires zope.dublincore

%description tests
This package provides Copy, Paste and Move support for content
components in Zope.

This package contains tests for zope.copypastemove.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Initial build for Sisyphus

