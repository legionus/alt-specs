%define oname aiogibson

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20150210.1.2
Summary: asyncio (PEP 3156) Gibson cache support
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiogibson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jettify/aiogibson.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-coverage
#BuildPreReq: python-module-flake8 python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-coverage
#BuildPreReq: python3-module-flake8 python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base python3-module-mccabe python3-module-pytest python3-module-setuptools python3-pyflakes python3-tools-pep8
BuildRequires: python3-module-coverage python3-module-flake8 python3-module-nose rpm-build-python3

%description
aiogibson is a library for accessing a gibson cache database from the
asyncio (PEP-3156/tulip) framework.

%package -n python3-module-%oname
Summary: asyncio (PEP 3156) Gibson cache support
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
aiogibson is a library for accessing a gibson cache database from the
asyncio (PEP-3156/tulip) framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|flake8|python3-flake8|' ../python3/Makefile
sed -i 's|nosetests|nosetests3|' ../python3/Makefile
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

rm -f requirements.txt

%check
%if_with python2
python setup.py test
%make test FLAGS=-v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
%make test FLAGS=-v
popd
%endif

%if_with python2
%files
%doc *.txt *.rst docs/*.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt1.git20150210.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20150210.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20150210.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150210
- Version 0.1.3

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150101
- Initial build for Sisyphus

