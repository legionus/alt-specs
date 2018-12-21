%define oname django-simple-autocomplete

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20140226.2
Summary: Django app adding painless autocomplete to admin
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-simple-autocomplete/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-simple-autocomplete.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app adding painless autocomplete to admin
Group: Development/Python3

%description -n python3-module-%oname
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

This package contains tests for %oname.

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt1.git20140226.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20140226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140226
- Initial build for Sisyphus

