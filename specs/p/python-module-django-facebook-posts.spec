%define oname django-facebook-posts

%def_with python3

Name: python-module-%oname
Version: 0.1.10
Release: alt2
Summary: Django implementation for Facebook Graph API Posts
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-posts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ramusus/django-facebook-posts.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Application for interacting with Facebook Graph API Posts objects using
Django model interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip factories models

%description tests
Application for interacting with Facebook Graph API Posts objects using
Django model interface.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django implementation for Facebook Graph API Posts
Group: Development/Python3

%description -n python3-module-%oname
Application for interacting with Facebook Graph API Posts objects using
Django model interface.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip factories models

%description -n python3-module-%oname-tests
Application for interacting with Facebook Graph API Posts objects using
Django model interface.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.10-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.git20140909.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.10-alt1.git20140909
- Initial build for Sisyphus

