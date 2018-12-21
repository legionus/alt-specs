%define _unpackaged_files_terminate_build 1

%define oname pyScss

%def_with python3

Name: python-module-%oname
Version: 1.3.5
Release: alt3.qa1
Summary: pyScss, a Scss compiler for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyScss/

# https://github.com/Kronuz/pyScss.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libpcre-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Pillow python2.7(enum34) python-module-pathlib python-module-pytest-cov
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-six
BuildRequires: python3-module-Pillow python3(enum) python3-module-pytest-cov
%endif

%py_provides %oname scss
%py_requires six pathlib logging PIL
%py_requires enum34

%description
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

%if_with python3
%package -n python3-module-%oname
Summary: pyScss, a Scss compiler for Python
Group: Development/Python3
%py3_provides %oname scss
%py3_requires six logging PIL

%description -n python3-module-%oname
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%if_with python3
pushd ../python3
%python3_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python3_sitelibdir/scss/grammar/
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python_sitelibdir/scss/grammar/

CFLAGS="%optflags" python setup.py build_ext -i
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test -vv --cov scss
%if_with python3
pushd ../python3
py.test3 -vv --cov scss
popd
%endif

%files
%doc DESCRIPTION *.rst
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
%doc DESCRIPTION *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt3.qa1
- NMU: applied repocop patch

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt3
- Fix build

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt2
- Updated build and runtime dependencies.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1
- Updated to upstream release version 1.3.5.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt1.git20150122.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.4-alt1.git20150122.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150122
- Initial build for Sisyphus

