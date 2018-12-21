%define _unpackaged_files_terminate_build 1
%define oname dnslib

%def_with python3

Name: python-module-%oname
Version: 0.9.7
Release: alt2
Summary: Simple library to encode/decode DNS wire-format packets
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/dnslib

Source: %{oname}-%{version}.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Simple library to encode/decode DNS wire-format packets
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

This package contains tests for %oname.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
VERSIONS=python ./run_tests.sh -v
%if_with python3
pushd ../python3
VERSIONS=python3 ./run_tests.sh -v
popd
%endif

%files
%doc README* PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc README* PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7-alt2
- Fixed build.

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

