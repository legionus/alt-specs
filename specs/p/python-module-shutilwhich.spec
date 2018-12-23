%define _unpackaged_files_terminate_build 1
%define oname shutilwhich

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2
Summary: shutil.which for those not using Python 3.3 yet
License: Python-2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/shutilwhich/
BuildArch: noarch

# https://github.com/mbr/shutilwhich.git
Source: %oname-%version.tar.gz

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
A copy & paste backport of Python 3.3's shutil.which function.

%package -n python3-module-%oname
Summary: shutil.which for those not using Python 3.3 yet
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A copy & paste backport of Python 3.3's shutil.which function.

%prep
%setup -q -n %oname-%version

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

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt2
- Rebuilt to fix file permissions.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.git20130302.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20130302
- Added provides %oname

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20130302
- Initial build for Sisyphus

