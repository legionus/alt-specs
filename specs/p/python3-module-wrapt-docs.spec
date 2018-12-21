%define oname wrapt
%define fname python3-module-%oname
%define descr \
The aim of the wrapt module is to provide a transparent object proxy for \
Python, which can be used as the basis for the construction of function \
wrappers and decorator functions.

Name: %fname-docs
Version: 1.10.11
Release: alt2

%if "-docs"==""
Summary: A Python module for decorators, wrappers and monkey patching
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: BSD
Url: https://pypi.python.org/pypi/wrapt/
# https://github.com/GrahamDumpleton/wrapt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-tox python3-devel python3-module-tox rpm-build-python3 time python3-module-pytest
# optimized out: -=FIXES: python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(sphinx_rtd_theme)


%if "-docs"!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
BuildArch: noarch
%else
%py3_provides %oname
%endif

%description
%descr

%if "-docs"!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for %oname
Group: Development/Python3

%description -n %fname-pickles
%descr

This package contains pickles for %oname.
%endif

%prep
%setup
%if "-docs"!=""
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%if "-docs"==""
%add_optflags -fno-strict-aliasing
%python3_build
%else
%make -C docs pickle
%make -C docs html
%endif

%install
%if "-docs"==""
%python3_install
%else
mkdir -p %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if "-docs"==""
%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%doc README.rst
%python3_sitelibdir/*

%else

%files
%doc docs/_build/html blog

%files -n %fname-pickles
%python3_sitelibdir/*/pickle

%endif

%changelog
* Thu May 10 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.11-alt2
- Fix provides for docs part.

* Thu Apr 26 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.11-alt1
- Build new version.
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt2.git20140822.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt2.git20140822.1.1.1
- Fixed build spec

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20140822.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.git20140822.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.git20140822.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20140822
- Initial build for Sisyphus

