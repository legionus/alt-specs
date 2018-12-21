%define _unpackaged_files_terminate_build 1

%define oname openassets

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt3.git20141102
Summary: Reference implementation of the Open Assets Protocol
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/openassets/

# https://github.com/OpenAssets/openassets.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio) python-module-bitcoinlib
BuildRequires: python2.7(enum34)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3-module-bitcoinlib
BuildRequires: python3(enum)
%endif

%py_provides %oname
Requires: python-module-bitcoinlib
%py_requires asyncio enum34

%description
The openassets Python package is the reference implementation of the
colored coins Open Assets Protocol.

Open Assets is a protocol for issuing and transferring custom digital
tokens in a secure way on the Bitcoin blockchain (or any compatible
blockchain).

%if_with python3
%package -n python3-module-%oname
Summary: Reference implementation of the Open Assets Protocol
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-bitcoinlib
%py3_requires asyncio enum

%description -n python3-module-%oname
The openassets Python package is the reference implementation of the
colored coins Open Assets Protocol.

Open Assets is a protocol for issuing and transferring custom digital
tokens in a secure way on the Bitcoin blockchain (or any compatible
blockchain).
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu May 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt3.git20141102
- NMU: rebuilt to regenerate dependencies.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt2.git20141102.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt2.git20141102
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20141102.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20141102.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141102
- Initial build for Sisyphus

