%define oname packaging

%def_with python3

Name: python-module-%oname
Version: 16.8
Release: alt1.qa1%ubt
Summary: Core utilities for Python packages
License: ASLv2.0 or BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/packaging
BuildArch: noarch

# https://github.com/pypa/packaging.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-devel python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib
BuildRequires: python-module-invoke python-module-objects.inv python-module-tox
BuildPreReq: python-module-sphinx-devel
BuildRequires: python-module-pytest python2.7(pretend) python2.7(pyparsing) python2.7(six)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-coverage python3-module-invoke python3-module-tox
BuildRequires: python3-module-pytest python3(pretend) python3(pyparsing) python3(six)
%endif

%description
Core utilities for Python packages.

%if_with python3
%package -n python3-module-%oname
Summary: Core utilities for Python packages
Group: Development/Python3

%description -n python3-module-%oname
Core utilities for Python packages.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Core utilities for Python packages.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test -v
%if_with python3
pushd ../python3
py.test3 -v
popd
%endif

%files
%doc *.rst LICENSE* docs/_build/html tasks
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst LICENSE* docs/_build/html tasks
%python3_sitelibdir/*
%endif

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 16.8-alt1.qa1%ubt
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.8-alt1%ubt
- Updated to upstream version 16.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.4-alt2.dev0.git20150801.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 15.4-alt2.dev0.git20150801
- rebuild with clean buildreq
- disable tests 

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

