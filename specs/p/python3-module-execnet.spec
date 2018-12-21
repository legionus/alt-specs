%define _unpackaged_files_terminate_build 1
%define oname execnet
%define fname python3-module-%oname
%define descr \
execnet provides carefully tested means to ad-hoc interact with Python \
interpreters across version, platform and network barriers. It provides \
a minimal and fast API targetting the following uses: \
\
* distribute tasks to local or remote processes \
* write and deploy hybrid multi-process applications \
* write scripts to administer multiple hosts

%if ""!=""
%def_without check
%else
%def_with check
%endif

Name: %fname
Version: 1.5.0
Release: alt1

%if ""==""
Summary: Rapid multi-Python deployment
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: MIT
Url: https://pypi.python.org/pypi/execnet/
Source: %name-%version.tar
Patch0: fix_test_close_initiating_remote_no_error.patch
Patch1: fix-test_popen_nice-test.patch
BuildArch: noarch

%if ""==""
%py3_provides %oname
%add_python3_req_skip win32event win32evtlogutil win32service
%add_python3_req_skip win32serviceutil register
%if "3"=="3"
# hasn't got version for Python3
%add_python3_req_skip rlcompleter2
%endif
%filter_from_provides /^python3(execnet\.script\.shell)/d
# IndexError: list index out of range
%filter_from_provides /^python3(execnet\.script\.socketserverservice)/d
# No module named 'win32serviceutil'
%filter_from_provides /^python3(execnet\.script\.quitserver)/d
# No module named 'execnet.quitserver'
%if "3"=="3"
%filter_from_provides /^python3(execnet\.script\.xx)/d
# depends from rlcompleter2
%endif
%endif

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%endif

BuildRequires(pre): rpm-macros-sphinx rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-apipkg
# one of the python3 tests requires python with 'apipkg' module
BuildRequires: python-module-apipkg

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest-timeout
%endif

%if ""!=""
BuildRequires: python-module-alabaster
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
%endif

%description
%descr
%if ""!=""

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
%patch0 -p1
%patch1 -p2
%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%python3_build

%install
%if ""==""
%python3_install
%else
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html
mkdir -p %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=`pwd`

%if "3"=="3"

# copy necessary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} --notest
cp -T %_bindir/py.test3 .tox/py%{python_version_nodots python3}/bin/py.test

TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages \
-e py%{python_version_nodots python3} -v -- -v

%else

# copy necessary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} --notest
cp -T %_bindir/py.test .tox/py%{python_version_nodots python}/bin/py.test

TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages \
-e py%{python_version_nodots python} -v -- -v

%endif

%if ""==""

%files
%doc CHANGELOG.rst *.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info*

%else

%files
%doc doc/_build/html/*

%files -n %fname-pickles
%python3_sitelibdir/*/pickle
%endif

%changelog
* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.2.0 -> 1.5.0.

* Mon Apr 16 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt4
- fix wrong Provides of pythonX.X(execnet) by docs packages

* Mon Apr 09 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt3
- Fix regular expressions in provides' filters.

* Thu Mar 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Tranfer package to subst-packaging system.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

