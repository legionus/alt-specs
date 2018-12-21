%define oname gantt

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1
Summary: This is a python class to create gantt chart using SVG
License: GPLv3+
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/python-gantt/

Source: %name-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-svgwrite python-module-clize
BuildRequires: python-module-nose python2.7(dateutil)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-svgwrite python3-module-clize
BuildRequires: python3-module-nose python3(dateutil)
BuildRequires: python-tools-2to3
%endif

%py_provides %oname org2gantt
%py_requires svgwrite clize

%description
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: This is a python class to create gantt chart using SVG
Group: Development/Python3
%py3_provides %oname org2gantt
%py3_requires svgwrite clize

%description -n python3-module-%oname
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

This package contains tests for %oname.
%endif

%prep
%setup
%patch1 -p1

touch org2gantt/__init__.py

%if_with python3
cp -fR . ../python3
find ../python3/%oname -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
cp -fR org2gantt %buildroot%python_sitelibdir/
install -d %buildroot%_bindir
sed -i 's|python3|python|' \
	%buildroot%python_sitelibdir/org2gantt/org2gantt.py
ln -s %python_sitelibdir/org2gantt/org2gantt.py \
	%buildroot%_bindir/org2gantt

%if_with python3
pushd ../python3
%python3_install
cp -fR org2gantt %buildroot%python3_sitelibdir/
ln -s %python3_sitelibdir/org2gantt/org2gantt.py \
	%buildroot%_bindir/org2gantt.py3
popd
%endif

%make doc

%check
export PYTHONPATH=$PWD
python setup.py build_ext -i
%make test PYTHON=python NOSETESTS=nosetests
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py build_ext -i
%make test PYTHON=python3 NOSETESTS=nosetests3
popd
%endif

%files
%doc CHANGELOG *.txt org2gantt/*.org *.html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/example.org

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/example.org

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt org2gantt/*.org *.html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/example.org

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/example.org
%endif

%changelog
* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1
- Updated to upstream version 0.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.10-alt1
- Version 0.3.10

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1
- Version 0.3.8

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

