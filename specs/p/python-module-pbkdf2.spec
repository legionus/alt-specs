%define oname pbkdf2

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2.2
Summary: PKCS#5 v2.0 PBKDF2 Module
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/pbkdf2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3 
BuildRequires: python3-devel python3-module-distribute
%endif

%description
This module implements the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%if_with python3
%package -n python3-module-%oname
Summary: PKCS#5 v2.0 PBKDF2 Module (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This module implements the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.
%endif

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 1.3-alt2
- Restoring python3 provides

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-3.3

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

