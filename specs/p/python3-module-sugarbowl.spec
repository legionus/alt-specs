%define oname sugarbowl
Name: python3-module-%oname
Version: 0.52.1
Release: alt1.git20141130.1.1
Summary: Sugarbowl provides cachedproperty, import_object and more
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sugarbowl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sugarbowl/sugarbowl.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-coverage

%description
Sugarbowl provides cachedproperty, import_object and more.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.52.1-alt1.git20141130.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.52.1-alt1.git20141130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52.1-alt1.git20141130
- Initial build for Sisyphus

