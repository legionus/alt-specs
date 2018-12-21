%define _unpackaged_files_terminate_build 1
%define modulename pymysql

%def_with python3

Name: python-module-%modulename
Version: 0.7.9
Release: alt1

%setup_python_module %modulename

Summary: This pure Python MySQL client provides a DB-API to a MySQL database.
License: MIT
Group: Development/Python

Url: http://code.google.com/p/pymysql/
BuildArch: noarch

# https://github.com/PyMySQL/PyMySQL.git
Source0: https://pypi.python.org/packages/a4/c4/c15457f261fda9839637de044eca9b6da8f55503183fe887523801b85701/PyMySQL-%{version}.tar.gz

#BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
This pure Python MySQL client provides a DB-API to a MySQL database by
talking directly to the server via the binary client/server protocol.

%package tests
Summary: Tests for %modulename
Group: Development/Python
Requires: %name = %EVR

%description tests
This pure Python MySQL client provides a DB-API to a MySQL database by
talking directly to the server via the binary client/server protocol.

This package contains tests for %modulename.

%package -n python3-module-%modulename
Summary: This pure Python MySQL client provides a DB-API to a MySQL database
Group: Development/Python3

%description -n python3-module-%modulename
This pure Python MySQL client provides a DB-API to a MySQL database by
talking directly to the server via the binary client/server protocol.

%package -n python3-module-%modulename-tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: python3-module-%modulename = %EVR

%description -n python3-module-%modulename-tests
This pure Python MySQL client provides a DB-API to a MySQL database by
talking directly to the server via the binary client/server protocol.

This package contains tests for %modulename.

%prep
%setup -q -n PyMySQL-%{version}

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc CHANGELOG example.py *.rst
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%modulename/tests

%files tests
%python_sitelibdir/%modulename/tests

%if_with python3
%files -n python3-module-%modulename
%doc CHANGELOG example.py *.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%modulename/tests

%files -n python3-module-%modulename-tests
%python3_sitelibdir/%modulename/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.6-alt1.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.6-alt1.git20150727.1
- NMU: Use buildreq for BR.

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150727
- Version 0.6.6

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.git20150114
- Version 0.6.3

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20140901
- Version 0.6.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.svn35.1
- Rebuild with Python-2.7

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 0.3-alt1.svn35
- new version

* Tue Mar 16 2010 Alexey Morsov <swi@altlinux.ru> 0.2-alt1.svn4
- initial build

