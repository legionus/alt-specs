# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname zc.vault

%def_with python3

Name: python-module-%oname
Version: 0.11
#Release: alt3.1
Summary: Low-level versioning support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.vault/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc rwproperty zc.copy zc.freeze zc.objectlog
%py_requires zc.relationship zc.shortcut ZODB3 zope.app.container
%py_requires zope.app.intid zope.app.keyreference zope.cachedescriptors
%py_requires zope.component zope.copypastemove zope.event zope.i18n
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.location zope.proxy zope.publisher zope.schema
%py_requires zope.traversing

%description
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

%package -n python3-module-%oname
Summary: Low-level versioning support
Group: Development/Python3
%py3_requires zc rwproperty zc.copy zc.freeze zc.objectlog
%py3_requires zc.relationship zc.shortcut ZODB3 zope.app.container
%py3_requires zope.app.intid zope.app.keyreference zope.cachedescriptors
%py3_requires zope.component zope.copypastemove zope.event zope.i18n
%py3_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py3_requires zope.location zope.proxy zope.publisher zope.schema
%py3_requires zope.traversing

%description -n python3-module-%oname
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

%package -n python3-module-%oname-tests
Summary: Tests for Low-level versioning support
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires transaction zope.annotation zope.app.component
%py3_requires zope.app.folder zope.app.testing zope.testing

%description -n python3-module-%oname-tests
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

This package contains tests for Low-level versioning support.

%package tests
Summary: Tests for Low-level versioning support
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction zope.annotation zope.app.component
%py_requires zope.app.folder zope.app.testing zope.testing

%description tests
The zc.vault package provides a low-level versioning support similar to
revision control systems, with an example usage and several example
add-ons. It's ZODB-friendly.

This package contains tests for Low-level versioning support.

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
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

