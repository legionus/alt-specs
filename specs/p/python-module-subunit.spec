%define oname subunit

Name: python-module-%oname
Version: 1.3.0
Release: alt1

Summary: Python implementation of subunit test streaming protocol
License: Apache or BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/python-subunit/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-mimeparse
BuildRequires: python-module-testscenarios
BuildRequires: python2.7(hypothesis) python2.7(fixtures)
BuildRequires: python-module-testtools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-mimeparse
BuildRequires: python3-module-testscenarios
BuildRequires: python3(hypothesis) python3(fixtures)
BuildRequires: python3-module-testtools

Provides: python-module-python-%oname = %EVR
Obsoletes: python-module-python-%oname < %EVR

%add_python3_req_skip gtk.gdk

%description
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%package -n python3-module-%oname
Summary: Python 3 implementation of subunit test streaming protocol
Group: Development/Python3
Provides: python3-module-python-%oname = %EVR
Obsoletes: python3-module-python-%oname < %EVR
%add_python3_req_skip gtk pynotify

%description -n python3-module-%oname
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%package -n python3-module-%oname-tests
Summary: Tests for python-subunit (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Provides: python3-module-python-%oname-tests = %EVR
Obsoletes: python3-module-python-%oname-tests < %EVR

%description -n python3-module-%oname-tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.

%package tests
Summary: Tests for python-subunit
Group: Development/Python
Requires: %name = %version-%release
Provides: python-module-python-%oname-tests = %EVR
Obsoletes: python-module-python-%oname-tests < %EVR

%description tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
#find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py2_$i
done
popd
pushd ../python3
%python3_install
popd


%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc NEWS README.rst
%_bindir/py2_*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc NEWS README.rst
%_bindir/*
%exclude %_bindir/py2_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests


%changelog
* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt4
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt3
- Updated build dependencies.

* Mon Jun 05 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt2
- Fix test_results packaging

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt1
- Version 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt3
- Added necessary obsoletes

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt2
- Renamed python-module-python-subunit -> python-module-subunit

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt1
- Version 0.0.18

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1
- Version 0.0.15

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1
- Version 0.0.10

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.7-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

