%define oname attest

%def_without python3

Name: python-module-%oname
Version: 0.6
Release: alt4.git20130330
Summary: Modern, Pythonic unit testing
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Attest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dag/attest.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-progressbar python-module-Pygments
#BuildPreReq: python-module-six
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-progressbar python3-module-Pygments
#BuildPreReq: python3-module-six
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-progressbar
%py_requires pygments six

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-lxml python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-progressbar python-module-pytest time
%if_with python3
BuildPreReq: python3-module-html5lib python3-module-progressbar python3-module-pytest python3-module-sphinx rpm-build-python3
%endif

%description
Attest is a unit testing framework built from the ground up with
idiomatic Python in mind. Unlike others, it is not built on top of
unittest though it provides compatibility by creating TestSuites from
Attest collections.

%if_with python3
%package -n python3-module-%oname
Summary: Modern, Pythonic unit testing
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-progressbar
%py3_requires pygments six

%description -n python3-module-%oname
Attest is a unit testing framework built from the ground up with
idiomatic Python in mind. Unlike others, it is not built on top of
unittest though it provides compatibility by creating TestSuites from
Attest collections.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Attest is a unit testing framework built from the ground up with
idiomatic Python in mind. Unlike others, it is not built on top of
unittest though it provides compatibility by creating TestSuites from
Attest collections.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Attest is a unit testing framework built from the ground up with
idiomatic Python in mind. Unlike others, it is not built on top of
unittest though it provides compatibility by creating TestSuites from
Attest collections.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -R . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=$PWD
%make test
%if_with python3
pushd ../python3
sed -i 's|attest|attest.py3|' Makefile
export PYTHONPATH=$PWD
%make test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt4.git20130330
- (.spec) Put %%if_with python3 guards around all python3-related code. (Otherwise the build from .src.rpm fails.)

* Fri Apr  8 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt3.git20130330
- Hidden the python3 BuildReqs (because it is turned off now).

* Fri Apr  8 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.git20130330
- %%def_without python3 (because it FTBFS with python3-3.5).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt1.git20130330.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt1.git20130330.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20130330
- Initial build for Sisyphus

