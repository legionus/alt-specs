%define _unpackaged_files_terminate_build 1
%define oname zope.i18nmessageid
%define fname python-module-%oname
%define descr \
This package provides facilities for *declaring* messages within \
program source text;  translation of the messages is the responsiblity \
of the 'zope.i18n' package.

%def_with check

Name: %fname
Version: 4.1.0
Release: alt2

%if ""==""
Summary: Message Identifiers for internationalization
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: ZPLv2.1
# Source-git https://github.com/zopefoundation/zope.i18nmessageid.git
Url: http://pypi.python.org/pypi/zope.i18nmessageid
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx rpm-build-python
BuildRequires: python-dev python-module-sphinx python-module-sphinx-devel python-module-setuptools

%if_with check
BuildRequires: python-module-zope.testing python-module-zope.testrunner
%endif

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
BuildArch: noarch
%endif

%description
%descr

%if ""!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for Zope Configuration Markup Language (ZCML)
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for %oname.

%else

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
%descr

This package contains tests for %oname.

%endif

%prep
%setup
%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%if ""==""
%add_optflags -fno-strict-aliasing
%python_build
%else
%make -C docs pickle
%make -C docs html
%endif

%install
%if ""==""
%python_install
%else
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if ""==""
%check
export PYTHONPATH=src
python setup.py test -v

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/zope/i18nmessageid/tests.*

%files tests
%python_sitelibdir/zope/i18nmessageid/tests.*

%else

%files
%doc docs/_build/html

%files -n %fname-pickles
%python_sitelibdir/*/pickle
%endif

%changelog
* Mon May 14 2018 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.0-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150309.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150309.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150309
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt4
- Added necessary requirements
- Excluded *.pth

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt3
- Added %%py_provides zope.i18nmessageid

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Don't build python-module-zope.arch

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

