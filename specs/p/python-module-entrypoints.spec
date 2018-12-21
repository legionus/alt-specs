%define _unpackaged_files_terminate_build 1
%define oname entrypoints

%def_with python3

Name: python-module-%oname
Version: 0.2.3
Release: alt2
Summary: Discover and load entry points from installed packages
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/entrypoints

# https://github.com/takluyver/entrypoints.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_requires configparser

%description
Discover and load entry points from installed packages.

%if_with python3
%package -n python3-module-%oname
Summary: Discover and load entry points from installed packages
Group: Development/Python3
%py3_requires configparser

%description -n python3-module-%oname
Discover and load entry points from installed packages.
%endif

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
pushd ../python3
%python3_install
popd

%python_install

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2.3-alt2
- Added egg-info

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.3-alt1
- Initial build for ALT.
