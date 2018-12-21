%define oname django-export

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20110909.2
Summary: Django app allowing for filtered exporting of model data
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-export/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-export.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app allowing for filtered exporting of model data
Group: Development/Python3

%description -n python3-module-%oname
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

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
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt1.git20110909.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20110909.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20110909
- Initial build for Sisyphus

