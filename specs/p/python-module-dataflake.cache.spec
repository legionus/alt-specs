# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1.1
%define oname dataflake.cache

%def_with python3

Name: python-module-%oname
Version: 1.4
#Release: alt1.1.1.1
Summary: Simple caching library
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/dataflake.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires zope.interface dataflake

%description
This package provides a set of simple cache implementations for use in
Python code. Its roots are in the internally-used SimpleCache module
from Products.LDAPUserFolder.

%if_with python3
%package -n python3-module-%oname
Summary: Simple caching library (Python 3)
Group: Development/Python3
%py3_requires zope.interface dataflake

%description -n python3-module-%oname
This package provides a set of simple cache implementations for use in
Python code. Its roots are in the internally-used SimpleCache module
from Products.LDAPUserFolder.

%package -n python3-module-dataflake
Summary: Core package of dataflake (Python 3)
Group: Development/Python3
%py3_provides dataflake

%description -n python3-module-dataflake
Core package of dataflake.
%endif

%package tests
Summary: Tests for dataflake.cache
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a set of simple cache implementations for use in
Python code. Its roots are in the internally-used SimpleCache module
from Products.LDAPUserFolder.

This package contains tests for dataflake.cache.

%package -n python-module-dataflake
Summary: Core package of dataflake
Group: Development/Python
%py_provides dataflake

%description -n python-module-dataflake
Core package of dataflake.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

touch %buildroot%python_sitelibdir/dataflake/__init__.py

%if_with python3
pushd ../python3
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

touch %buildroot%python3_sitelibdir/dataflake/__init__.py
popd
%endif

%files
%doc *.txt docs/*.rst docs/api
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/dataflake/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files -n python-module-dataflake
%python_sitelibdir/dataflake/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst docs/api
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/dataflake/__init__.py*
%exclude %python3_sitelibdir/dataflake/__pycache__/__init__.*

%files -n python3-module-dataflake
%python3_sitelibdir/dataflake/__init__.py*
%python3_sitelibdir/dataflake/__pycache__/__init__.*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4-alt1.1.1
- NMU: Use buildreq for BR.

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-3.3

* Sat May 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

