%define oname blink

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: REST client interface
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/blink/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-requests python2.7(yaml) python2.7(dateutil.parser)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-requests python3(yaml) python3(dateutil.parser)
%endif

%py_provides %oname

%description
A REST interface from Python.

%if_with python3
%package -n python3-module-%oname
Summary: REST client interface
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A REST interface from Python.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus

