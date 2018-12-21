%define oname tgming

%def_without bootstrap

Name: python-module-%oname
Version: 0.0.8
Release: alt2.3

Summary: TurboGears2 Support for Ming MongoDB ORM
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/tgming/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3


%description
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%package -n python3-module-%oname
Summary: TurboGears2 Support for Ming MongoDB ORM
Group: Development/Python3
%if_with bootstrap
%add_python3_req_skip ming
%endif

%description -n python3-module-%oname
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc PKG-INFO *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc PKG-INFO *.rst
%python3_sitelibdir/*


%changelog
* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.8-alt2.3
- rebuild with all requires

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.8-alt2.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.8-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Version 0.0.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus
