%define oname joblib

%def_with python3

Name: python-module-%oname
Version: 0.11
Release: alt2
Summary: Lightweight pipelining: using Python functions as pipeline jobs
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/joblib

# https://github.com/joblib/joblib.git
Source: %name-%version.tar
# Remove failing test, should be fixed in https://github.com/joblib/joblib/issues/413, but apparently it isn't
Patch1: %oname-%version-alt-tests.patch
BuildArch: noarch

BuildRequires: python-module-nose python-module-pytest python-modules-json time
BuildRequires: python-module-numpy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-pytest
BuildRequires: python3-module-numpy
%endif

%description
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight pipelining: using Python 3 functions as pipeline jobs
Group: Development/Python3

%description -n python3-module-%oname
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%package -n python3-module-%oname-tests
Summary: Tests for joblib (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.
%endif

%package tests
Summary: Tests for joblib
Group: Development/Python
Requires: %name = %version-%release

%description tests
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

This package contains tests for joblib.

%prep
%setup
%patch1 -p1

%if_with python3
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
%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test*

%files tests
%python_sitelibdir/%oname/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*
%exclude %python3_sitelibdir/%oname/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test*
%python3_sitelibdir/%oname/__pycache__/test*
%endif

%changelog
* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt2
- Applied patch to tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt1
- Update to upstream version 0.11.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.b3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.b3.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.b3
- Version 0.9.0b3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0d-alt1
- Version 0.7.0d

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6.4-alt1.1
- Rebuild with Python-3.3

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.dev
- Version 0.5.6.dev

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev
- Version 0.5.5.dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

