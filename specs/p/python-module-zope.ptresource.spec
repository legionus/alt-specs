%define _unpackaged_files_terminate_build 1

%define oname zope.ptresource

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1
Summary: Page template resource plugin for zope.browserresource
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ptresource/

# https://github.com/zopefoundation/zope.ptresource.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-tests.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-tox
BuildRequires: python-module-zope.browserresource
BuildRequires: python-module-zope.pagetemplate
BuildRequires: python-module-zope.publisher python-module-zope.security
BuildRequires: python-module-zope.testing
BuildRequires: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tox
BuildRequires: python3-module-zope.browserresource
BuildRequires: python3-module-zope.pagetemplate
BuildRequires: python3-module-zope.publisher python3-module-zope.security
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
%endif

%py_requires zope.browserresource zope.interface zope.pagetemplate
%py_requires zope.publisher zope.security

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

%if_with python3
%package -n python3-module-%oname
Summary: Page template resource plugin for zope.browserresource
Group: Development/Python3
%py3_requires zope.browserresource zope.interface zope.pagetemplate
%py3_requires zope.publisher zope.security

%description -n python3-module-%oname
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

%package -n python3-module-%oname-tests
Summary: Tests for zope.ptresource
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

This package contains tests for zope.ptresource.
%endif

%package tests
Summary: Tests for zope.ptresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

This package contains tests for zope.ptresource.

%prep
%setup
%patch1 -p1

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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%check
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%python_sitelibdir_noarch:%python_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e py%{python_version_nodots python} -v

pushd ../python3
export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir:src
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e py%{python_version_nodots python3} -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Aug 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1
- Updated to upstream version 4.1.0.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150613
- Version 4.0.1.dev0
- Enabled check

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

