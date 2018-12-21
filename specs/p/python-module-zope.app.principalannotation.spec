# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1.1
%define oname zope.app.principalannotation

%def_with python3

Name: python-module-%oname
Version: 3.7.1
#Release: alt2.1
Summary: Bootstrap subscriber and browser menu item for zope.principalannotation
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.principalannotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires transaction zope.app.appsetup zope.processlifetime
%py_requires zope.principalannotation zope.app

%description
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

%package -n python3-module-%oname
Summary: Bootstrap subscriber and browser menu item for zope.principalannotation
Group: Development/Python3
%py3_requires transaction zope.app.appsetup zope.processlifetime
%py3_requires zope.principalannotation zope.app

%description -n python3-module-%oname
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.principalannotation
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

This package contains tests for zope.app.principalannotation.

%package tests
Summary: Tests for zope.app.principalannotation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package used to provide implementation of IAnnotations for
zope.security principal objects, but it's now moved to the
zope.principalannotation package. This package only contains a bootstrap
subscriber that sets up the principal annotation utility for the root
site and the browser add menu item for adding the annotation utility
through ZMI.

This package contains tests for zope.app.principalannotation.

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
%exclude %python_sitelibdir/*/*/*/tests.*

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
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.1-alt2.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

