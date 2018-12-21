%define oname dobbin

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.1.1.2
Summary: Pure-Python object database
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/dobbin
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%description
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

Key features:

* MVCC concurrency model
* Implemented all in Python
* Multi-thread, multi-process with no configuration
* Zero object access overhead in general case
* Optimal memory sharing between threads
* Efficient storing and serving of binary streams
* Architecture open to alternative storages

%if_with python3
%package -n python3-module-%oname
Summary: Pure-Python 3 object database
Group: Development/Python3

%description -n python3-module-%oname
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

Key features:

* MVCC concurrency model
* Implemented all in Python
* Multi-thread, multi-process with no configuration
* Zero object access overhead in general case
* Optimal memory sharing between threads
* Efficient storing and serving of binary streams
* Architecture open to alternative storages

%package -n python3-module-%oname-tests
Summary: Tests for Dobbin (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

This package contains tests for Dobbin.
%endif

%package tests
Summary: Tests for Dobbin
Group: Development/Python
Requires: %name = %version-%release

%description tests
Dobbin is a transactional object database for Python (2.6+). It's a fast
and convenient way to persist Python objects on disk.

This package contains tests for Dobbin.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-3.3

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

