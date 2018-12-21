%define _unpackaged_files_terminate_build 1
%define oname vine

%def_with python3

Name: python-module-%oname
Version: 1.1.4
Release: alt1
Summary: Python promises
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/celery/vine

# https://github.com/celery/vine.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
Promises, promises, promises.

%if_with python3
%package -n python3-module-%oname
Summary: Python promises
Group: Development/Python3

%description -n python3-module-%oname
Promises, promises, promises.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%endif

%changelog
* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1
- Initial build for ALT.
