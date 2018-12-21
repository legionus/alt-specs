%define _unpackaged_files_terminate_build 1
%define oname releases

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: A Sphinx extension for changelog manipulation
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/releases/

# https://github.com/bitprophet/releases.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

%package -n python3-module-%oname
Summary: A Sphinx extension for changelog manipulation
Group: Development/Python3

%description -n python3-module-%oname
Releases is a Sphinx extension designed to help you keep a source
control friendly, merge friendly changelog file & turn it into useful,
human readable HTML output.

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
* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Updated to upstream version 1.4.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20150323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150323
- Version 0.7.0

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

