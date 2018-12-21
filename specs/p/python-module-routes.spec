%define oname routes

%def_with python3

Name: python-module-%oname
Version: 2.4.1
Release: alt1
Summary: Routing Recognition and Generation Tools
License: BSD
Group: Development/Python
Url: http://routes.groovie.org/

# git://github.com/bbangert/routes
Source: %oname-%version.tar.gz
BuildArch: noarch

Requires: python-module-repoze.lru

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-sphinx-devel python-module-Pygments
BuildRequires: python-module-repoze.lru python-module-webob
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-six
%endif

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

Routes allows conditional matching based on domain, cookies, HTTP
method, or a custom function. Sub-domain support is built in. Routes
comes with an extensive unit test suite.

%package -n python3-module-%oname
Summary: Routing Recognition and Generation Tools
Group: Development/Python3
Requires: python3-module-repoze.lru

%description -n python3-module-%oname
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

Routes allows conditional matching based on domain, cookies, HTTP
method, or a custom function. Sub-domain support is built in. Routes
comes with an extensive unit test suite.

%package doc
Summary: Documentation for Routing Recognition and Generation Tools
Group: Development/Documentation
BuildArch: noarch

%description doc
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

This package contains documentation for Routes.

%package pickles
Summary: Pickles for Routing Recognition and Generation Tools
Group: Development/Python

%description pickles
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to application actions, and conversely to generate URLs.
Routes makes it easy to create pretty and concise URLs that are RESTful
with little effort.

This package contains pickles for Routes.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs

install -d %buildroot%_docdir/%name
popd

%files
%doc CHANGELOG LICENSE README TODO
%python_sitelibdir/*

%files doc
%_docdir/%name


%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG LICENSE README TODO
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1-alt2.git20150117.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1-alt2.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 2.1-alt2.git20150117
- assembly documentation disabled

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20150117
- Version 2.1

* Wed Jul 30 2014 Lenar Shakirov <snejok@altlinux.ru> 2.0-alt2.git20140108
- python-module-repoze.lru added to Requires

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140108
- New snapshot
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20131120
- Version 2.0

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1.git20030523
- Version 1.13

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.3-alt1.hg20100605.1
- Rebuild with Python-2.7

* Wed Jul 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.3-alt1.hg20100605
- Version 1.12.3

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20090928.1
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20090928
- Initial build for Sisyphus

