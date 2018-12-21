%define _unpackaged_files_terminate_build 1
%define oname tox

%def_with check

Name: python-module-%oname
Version: 3.5.3
Release: alt1

Summary: virtualenv-based automation of test activities
License: MIT
Group: Development/Python
# Source-git: https://github.com/tox-dev/tox.git
Url: https://pypi.python.org/pypi/tox/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: pytest
BuildRequires: python-module-pip
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-mock
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-pytest-timeout
BuildRequires: python-module-pytest-xdist
BuildRequires: python-module-virtualenv
BuildRequires: python-module-six
BuildRequires: python-module-toml
BuildRequires: python-module-filelock
BuildRequires: pytest3
BuildRequires: python3-module-pip
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-six
BuildRequires: python3-module-toml
BuildRequires: python3-module-filelock
%endif

BuildArch: noarch
%py_requires virtualenv

%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%package -n python3-module-%oname
Summary: virtualenv-based automation of test activities
Group: Development/Python3
%py3_requires virtualenv

%description -n python3-module-%oname
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%prep
%setup
%patch -p1
cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
        mv $i $i.py3
done
popd

%python_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%buildroot%python_sitelibdir_noarch
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH RPM_BUILD_DIR' %buildroot%_bindir/tox \
--sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/pytest .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='PYTHONPATH RPM_BUILD_DIR' %buildroot%_bindir/tox \
--sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH RPM_BUILD_DIR' %buildroot%_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/pytest3 .tox/py%{python_version_nodots python3}/bin/pytest

TOX_TESTENV_PASSENV='PYTHONPATH RPM_BUILD_DIR' %buildroot%_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%_bindir/tox
%_bindir/tox-quickstart
%python_sitelibdir/tox/
%python_sitelibdir/tox-*.egg-info/

%files -n python3-module-%oname
%_bindir/tox.py3
%_bindir/tox-quickstart.py3
%python3_sitelibdir/tox/
%python3_sitelibdir/tox-*.egg-info/

%changelog
* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1
- 3.5.2 -> 3.5.3.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.5.2-alt1
- 3.2.1 -> 3.5.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 3.0.0 -> 3.2.1.

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.9.1 -> 3.0.0

* Thu Oct 19 2017 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1
- Version 2.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

