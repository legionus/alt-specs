%define oname pyftpdlib
%define fname python-module-%oname
%define descr \
Python FTP server library provides a high-level portable interface to easily \
write asynchronous FTP servers with Python. pyftpdlib is currently the most \
complete RFC-959 FTP server implementation available for Python programming \
language.

Name: %fname
Version: 1.5.4
Release: alt3

%if ""==""
Summary: Python FTP server library
Summary(ru_RU.UTF-8): Модуль Python FTP-сервера
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: MIT
BuildArch: noarch
Url: https://github.com/giampaolo/pyftpdlib
Source: %name-%version.tar
Patch1: %oname-alt-tests.patch

BuildRequires(pre): rpm-macros-branch rpm-build-licenses
BuildRequires: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%else
%py_provides %oname
%if ""==""
%py_requires sendfile
%endif
%endif

%if ""==""
%description -l ru_RU.UTF-8
Модуль Python FTP-сервера беспечивает портативный высокоуровневый интерфейс
для лёгкого написания асинхронного FTP сервера на Python. pyftpdlib сейчас --
наиболее полная реализация RFC-959 FTP-сервера для Python.
%endif

%description
%descr

%if ""!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for %oname
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for %oname.

%else

%package tests
Summary: Documentation for %oname
Group: Development/Python
%py_requires %oname

%description tests
%descr

This package contains tests for %oname.
%endif

%prep
%setup
%if ""==""
%patch1 -p1
%endif

sed -i -e "s|^__ver__ = '[^']*'|__ver__ = '%version'|" pyftpdlib/__init__.py

%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%if ""==""
%python_build
%else
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
%endif

%install
%if ""==""
%python_install
%else
mkdir -p %buildroot%python_sitelibdir/%oname/
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if ""==""
%if ""=="3"
pushd %buildroot%_bindir
for i in $(ls); do
    mv $i $i.py3
done
popd
%endif

%files
%doc CREDITS LICENSE *.rst demo/
%_bindir/*
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/test/README

%else

%files
%doc docs/_build/html/*

%files -n %fname-pickles
%python_sitelibdir/%oname/pickle
%endif

%changelog
* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt3
- Updated runtime dependencies.

* Wed Aug 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt2
- Rebuild with resolving file conflict between modules.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Build new version.

* Fri Mar 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt2
- Transfer package to subst-packaging system.

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1
- Updated to upstream version 1.5.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0
- Added module for Python 3

* Tue Sep 03 2013 Anatoly Kitaykin <cetus@altlinux.org> 1.2.0-alt1
- Release 1.2.0

* Tue Oct 30 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.7.0-alt1
- Release 0.7.0

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.1
- Rebuilt with python 2.6

* Fri Aug 21 2009 Aleksey Avdeev <solo@altlinux.ru> 0.5.1-alt1
- initial build
