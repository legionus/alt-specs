%define oname ElasticQuery

%def_with python3

Name: python-module-%oname
Version: 3.1
Release: alt1
Summary: A simple query builder for Elasticsearch
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ElasticQuery/
BuildArch: noarch

# https://github.com/Fizzadar/ElasticQuery.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-modules-json
BuildRequires: python-module-pytest
BuildRequires: python2.7(jsontest)
BuildRequires: python2.7(dictdiffer)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
BuildRequires: python3-module-pytest
BuildRequires: python3(jsontest)
BuildRequires: python3(dictdiffer)
%endif

%py_provides elasticquery

%description
A simple query builder for Elasticsearch. Outputs json ready to be sent
to Elasticsearch via your favourite client.

%if_with python3
%package -n python3-module-%oname
Summary: A simple query builder for Elasticsearch
Group: Development/Python3
%py3_provides elasticquery

%description -n python3-module-%oname
A simple query builder for Elasticsearch. Outputs json ready to be sent
to Elasticsearch via your favourite client.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1
- Updated to upstream version 3.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141125
- Version 0.2.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.18-alt1.git20141106
- Version 0.1.18

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1.git20141030
- Initial build for Sisyphus

