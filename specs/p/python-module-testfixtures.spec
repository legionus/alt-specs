%define  modulename testfixtures
%def_with python3
%def_without docs

Name:    python-module-%modulename
Version: 6.3.0
Release: alt1

Summary: A collection of helpers and mock objects for unit tests and doc tests
License: MIT
Group:   Development/Python
URL:     http://www.simplistix.co.uk/software/python/testfixtures

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python2.7(sybil) python2.7(mock) python2.7(django.db) python2.7(zope.component)
BuildRequires: python2.7(pkginfo)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
BuildRequires: python3(sybil) python3(mock) python3(django.db) python3(zope.component)
%endif
%if_with docs
BuildRequires: python-module-sphinx-devel
%endif

Source:  %modulename-%version.tar
#VCS:    https://github.com/Simplistix/testfixtures

%description
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.

%if_with python3
%package -n python3-module-%modulename
Group: Development/Python3
Summary:        A collection of helpers and mock objects for unit tests and doc tests

%description -n python3-module-%modulename
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.
%endif

%prep
%setup -n %modulename-%version

%if_with python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with docs
PYTHONPATH=$(pwd) %make -C docs html SPHINXBUILD=sphinx-build
mv docs/_build/html ./
rm -rf docs/_build
%endif

%check
rm -rf build
rm -f testfixtures/tests/test_django/test_compare.py
PYTHONPATH=$(pwd) py.test testfixtures/tests

%if_with python3
pushd ../python3
rm -rf build
rm -f testfixtures/tests/test_django/test_compare.py
PYTHONPATH=$(pwd) py.test3 testfixtures/tests
popd
%endif

%files
%doc README.rst docs
%if_with docs
%doc html
%endif
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc README.rst docs
%if_with docs
%doc html
%endif
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.0-alt1
- New version.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 6.2.0-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Wed Apr 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.
- Build without HTML documentation.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Wed Nov 22 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Mon Sep 04 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt2
- Enabled python-3 build.
- Enabled tests.
- Built and packaged docs.

* Fri Jun 09 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.14.3-alt1
- New version

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.13.5-alt1
- New version

* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 4.13.4-alt1
- new version 4.13.4

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 4.13.3-alt1
- new version 4.13.3

* Sat Nov 05 2016 Andrey Cherepanov <cas@altlinux.org> 4.13.1-alt1
- new version 4.13.1

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 4.12.0-alt1
- new version 4.12.0

* Fri Oct 14 2016 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- new version 4.11.0

* Wed Sep 07 2016 Andrey Cherepanov <cas@altlinux.org> 4.10.1-alt1
- new version 4.10.1

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- new version 4.10.0

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Fri Mar 28 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for ALT Linux
