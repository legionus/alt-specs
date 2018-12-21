%define oname pycerberus

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1.1.2
Summary: Highly flexible, no magic input validation library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pycerberus
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
#BuildPreReq: python-tools-2to3
%endif

%description
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

%if_with python3
%package -n python3-module-%oname
Summary: Highly flexible, no magic input validation library (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

%package -n python3-module-%oname-tests
Summary: Tests for pycerberus (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

This package contains tests for pycerberus.
%endif

%package tests
Summary: Tests for pycerberus
Group: Development/Python
Requires: %name = %version-%release

%description tests
pycerberus is a framework to check user data thoroughly so that you can
protect your application from malicious (or just garbled) input data.

This package contains tests for pycerberus.

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/__pycache__/test*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

