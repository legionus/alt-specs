# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname z3c.persistentfactory

%def_with python3

Name: python-module-%oname
Version: 0.3
#Release: alt3.1
Summary: Wrap instance methods in persistent factory wrappers for using instance methods as ZCA factories
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.persistentfactory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface zope.component ZODB3

%description
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

%package -n python3-module-%oname
Summary: Wrap instance methods in persistent factory wrappers for using instance methods as ZCA factories
Group: Development/Python3
%py3_requires zope.interface zope.component ZODB3

%description -n python3-module-%oname
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.persistentfactory
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

This package contains tests for z3c.persistentfactory.

%package tests
Summary: Tests for z3c.persistentfactory
Group: Development/Python
Requires: %name = %version-%release

%description tests
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

This package contains tests for z3c.persistentfactory.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

