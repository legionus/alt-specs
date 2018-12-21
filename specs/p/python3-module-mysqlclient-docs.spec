%define oname mysqlclient
%define fname python3-module-%oname
%define descr \
mysqlclient is a fork of MySQL-python. It add Python 3.3 support and \
merges some pull requests.

%def_disable check

Name: %fname-docs
Version: 1.3.13
Release: alt1

%if "-docs"==""
Summary: Python interface to MySQL
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: GPL
Url: https://pypi.python.org/pypi/mysqlclient/
# https://github.com/PyMySQL/mysqlclient-python.git
Source: %name-%version.tar

Conflicts: python-module-MySQLdb
Conflicts: python-module-MySQLdb2

%if "-docs"!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
BuildArch: noarch
%else
%py3_provides MySQLdb
%endif

BuildRequires(pre): rpm-macros-sphinx rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: libmysqlclient-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest python3-devel python3-module-nose python3-module-pytest rpm-build-python3 time

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
ln -s ../objects.inv doc/
%endif

%build
%if "-docs"==""
%python3_build
%else
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html
%endif


%install
%if "-docs"==""
%python3_install
%else
install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if "-docs"==""
%check
python3 setup.py test

%files
%doc HISTORY* *.md
%python3_sitelibdir/*

%else

%files
%doc doc/_build/html/*

%files -n %fname-pickles
%python3_sitelibdir/*/pickle
%endif

%changelog
* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.13-alt1
- Build new version.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.12-alt1
- Build new version.

* Fri May 11 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1.git20150225.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.6-alt1.git20150225.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.6-alt1.git20150225.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20150225
- Version 1.3.6

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150105
- New snapshot

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20141102
- Initial build for Sisyphus

