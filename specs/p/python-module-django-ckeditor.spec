%define oname django-ckeditor

%def_with python3

Name: python-module-%oname
Version: 4.4.6
Release: alt1.git20140923.2
Summary: Django admin CKEditor integration
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-ckeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/shaunsephton/django-ckeditor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing support
included.

This version also includes:

* support to django-storages (works with S3)
* updated ckeditor to version 4.4
* included all ckeditor language files to made everyone happy!

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing support
included.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django admin CKEditor integration
Group: Development/Python3

%description -n python3-module-%oname
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing support
included.

This version also includes:

* support to django-storages (works with S3)
* updated ckeditor to version 4.4
* included all ckeditor language files to made everyone happy!

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Django admin CKEditor integration. Provides a RichTextField and
CKEditorWidget utilizing CKEditor with image upload and browsing support
included.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.4.6-alt1.git20140923.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.6-alt1.git20140923.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1.git20140923
- Initial build for Sisyphus

