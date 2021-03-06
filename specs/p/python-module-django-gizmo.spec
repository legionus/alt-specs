%define oname django-gizmo

%def_with python3
%def_with bootstrap

Name: python-module-%oname
Version: 0.0.4
Release: alt2
Summary: Django app allowing for configurable targetting of template inclusion tags
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-gizmo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-gizmo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Django app allowing for configurable targetting of template inclusion
tags.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Django app allowing for configurable targetting of template inclusion
tags.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app allowing for configurable targetting of template inclusion tags
Group: Development/Python3

%description -n python3-module-%oname
Django app allowing for configurable targetting of template inclusion
tags.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults
%endif

%description -n python3-module-%oname-tests
Django app allowing for configurable targetting of template inclusion
tags.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20120731.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120731
- Initial build for Sisyphus

