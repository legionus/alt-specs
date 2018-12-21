%define oname positional

Name: python-module-%oname
Version: 1.2.1
Release: alt1

%setup_python_module %oname

Summary: Library to enforce positional or key-word arguments
License: ASL 2.0
Group: Development/Python

Url: https://github.com/morganfainberg/positional
BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-wrapt


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-wrapt

%description
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Library to enforce positional or key-word arguments
Group: Development/Python3

%description -n python3-module-%oname
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1
- add test packages

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build
