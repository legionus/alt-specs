%define _unpackaged_files_terminate_build 1

%def_with check

Name: py
Version: 1.7.0
Release: alt1

Summary: Testing and distributed programming library
License: MIT
Group: Development/Tools
# Source-git: https://github.com/pytest-dev/py.git
Url: https://github.com/pytest-dev/py

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: subversion
BuildRequires: subversion-server-common
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-attrs
BuildRequires: python-module-pytest
BuildRequires: python-module-decorator
BuildRequires: python-module-jinja2
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-attrs
BuildRequires: python3-module-pytest
BuildRequires: python3-module-decorator
BuildRequires: python3-module-jinja2
%endif

BuildArch: noarch
Requires: python-module-%name = %EVR

%py_provides py.apipkg py.builtin py.code py.error py.iniconfig py.io py.log py.path py.process py.std py.xmlgen

%description
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

%package -n python3-module-%name
Summary: Python 3 module of testing and distributed programming library
Group: Development/Python3
%add_python3_req_skip compiler
%py3_provides py.apipkg py.builtin py.code py.error py.iniconfig py.io py.log py.path py.process py.std py.xmlgen

%description -n python3-module-%name
The %name lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains python module of %name lib.

%package -n python-module-%name
Summary: Python module of testing and distributed programming library
Group: Development/Python
Conflicts: %name

%description -n python-module-%name
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains python module of %name lib.

%prep
%setup
%patch0 -p1

rm -rf ../python3
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
%python_install

pushd ../python3
%python3_install

popd

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export LC_ALL=en_US.UTF-8
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=`pwd`

# copy necessary exec deps
TOX_TESTENV_PASSENV='LC_ALL SETUPTOOLS_SCM_PRETEND_VERSION PYTHONPATH' tox \
--sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/py.test .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='LC_ALL SETUPTOOLS_SCM_PRETEND_VERSION PYTHONPATH' tox \
--sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH=`pwd`
TOX_TESTENV_PASSENV='LC_ALL SETUPTOOLS_SCM_PRETEND_VERSION PYTHONPATH' tox.py3\
 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/py.test3 .tox/py%{python_version_nodots python3}/bin/py.test

TOX_TESTENV_PASSENV='LC_ALL SETUPTOOLS_SCM_PRETEND_VERSION PYTHONPATH' tox.py3\
 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files -n python-module-%name
%doc AUTHORS CHANGELOG LICENSE *.rst
%python_sitelibdir/py/
%python_sitelibdir/py-*.egg-info/

%files -n python3-module-%name
%doc AUTHORS CHANGELOG LICENSE *.rst
%python3_sitelibdir/py/
%python3_sitelibdir/py-*.egg-info/

%changelog
* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.0 -> 1.7.0.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.3 -> 1.6.0.

* Fri Mar 23 2018 Stanislav Levin <slev@altlinux.org> 1.5.3-alt1
- 1.4.34 -> 1.5.3

* Thu Feb 08 2018 Alexey Appolonov <alexey@altlinux.org> 1.4.34-alt4
- test.py now packed into main package because it isn't actualy a test,
  it's a program that provides ability to use pytest module as py.test.

* Thu Feb 08 2018 Alexey Appolonov <alexey@altlinux.org> 1.4.34-alt3
- All test-files packed into testing subpackages.

* Wed Feb 07 2018 Alexey Appolonov <alexey@altlinux.org> 1.4.34-alt2
- Right way to run tests.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.34-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.34-alt1
- Updated to upstream version 1.4.34.
- Disabled tests.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.32-alt1
- automated PyPI update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.30-alt1.hg20150709.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.30-alt1.hg20150709.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.30-alt1.hg20150709
- Version 1.4.30

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.27.dev1-alt1.dev1.hg20141024
- Version 1.4.27.dev1

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.26-alt1.dev1.hg20141008
- Version 1.4.26.dev1

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt1.dev3.hg20140705
- Version 1.4.21.dev3

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt1.dev1.hg20140602
- Version 1.4.21.dev1

* Mon Nov 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.18.dev2-alt1.hg20131024
- Version 1.4.18.dev2

* Fri Jul 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.16.dev1-alt1.hg20130716
- Version 1.4.16.dev1

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.13-alt1.hg20130301
- Version 1.4.13

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1.4.13-alt1.dev3.hg20130127.1
- Rebuild with Python-3.3

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.13-alt1.dev3.hg20130127
- Version 1.4.13.dev3

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.10.dev1-alt1.hg20120614
- Version 1.4.10.dev1

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt2.hg20120217
- Added module for Python 3

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt1.hg20120217
- Version 1.4.7

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.6-alt1.hg20111120
- Version 1.4.6 (dev1)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1.a1.hg20101007.1
- Rebuild with Python-2.7

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.a1.hg20101007
- Version 1.4.0a1

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.hg20100628.a1
- Version 1.3.2
- Added testing package (ALT #23695)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20090913
- Initial build for Sisyphus

