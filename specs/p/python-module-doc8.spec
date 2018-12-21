%define  modulename doc8

Name:    python-module-%modulename
Version: 0.8.0
Release: alt1

Summary: Style checker for sphinx (or other) rst documentation.
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/openstack/doc8
BuildArch: noarch

Source:  %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-chardet
BuildRequires: python-module-docutils
BuildRequires: python-module-restructuredtext_lint >= 0.7
BuildRequires: python-module-six
BuildRequires: python-module-stevedore

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-chardet
BuildRequires: python3-module-docutils
BuildRequires: python3-module-restructuredtext_lint >= 0.7
BuildRequires: python3-module-six
BuildRequires: python3-module-stevedore


%description
Doc8 is an opinionated style checker for rst_ (with basic support for
plain text) styles of documentation.

%package -n python3-module-%modulename
Summary: Style checker for sphinx (or other) rst documentation.
Group: Development/Python3

%description -n python3-module-%modulename
Doc8 is an opinionated style checker for rst_ (with basic support for
plain text) styles of documentation.

%prep
%setup -n %modulename-%version
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
%python_sitelibdir/*

%files -n python3-module-%modulename
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
