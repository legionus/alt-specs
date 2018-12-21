# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.git20120330.1.1
%define oname repoze.lemonade

%def_with python3

Name: python-module-%oname
Version: 0.8
#Release: alt2.git20120330.1
Summary: Library for content-management applications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.lemonade
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.lemonade.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze zope.component zope.interface zope.configuration
%py_requires zope.testing nose

%description
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

%package -n python3-module-%oname
Summary: Library for content-management applications
Group: Development/Python3
%py3_requires repoze zope.component zope.interface zope.configuration
%py3_requires zope.testing nose

%description -n python3-module-%oname
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.lemonade
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

This package contains tests for repoze.lemonade.

%package tests
Summary: Tests for repoze.lemonade
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.lemonade is a collection of utilties that make it possible to
create Zope CMF-like applications without requiring any particular
persistence mechanism.

This package contains tests for repoze.lemonade.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt2.git20120330.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt2.git20120330.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2.git20120330
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20120330
- Version 0.8

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.git20110225
- Initial build for Sisyphus

