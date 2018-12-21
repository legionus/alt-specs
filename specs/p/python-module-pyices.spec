%define oname pyices

%def_without python3

Name: python-module-%oname
Version: 0.2
Release: alt2.git20140507
Summary: Python bindings for Yices SMT solver
License: Free
Group: Development/Python
Url: https://github.com/cheshire/pyices

# https://github.com/cheshire/pyices.git
Source: %name-%version.tar

BuildRequires: libyices-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-ctypesgen python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%if "%_lib" == "lib64"
Requires: libyices.so.2.3()(64bit)
%else
Requires: libyices.so.2.3
%endif

%description
Python bindings for Yices SMT solver. Works as a layer on top of C API,
on top of the layer generated by ctypesgen.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python bindings for Yices SMT solver. Works as a layer on top of C API,
on top of the layer generated by ctypesgen.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python bindings for Yices SMT solver
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python bindings for Yices SMT solver. Works as a layer on top of C API,
on top of the layer generated by ctypesgen.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python bindings for Yices SMT solver. Works as a layer on top of C API,
on top of the layer generated by ctypesgen.

This package contains tests for %oname.
%endif

%prep
%setup

%if "%_lib" == "lib64"
LIB_SUFF=64
%endif
sed -i "s|@64@|$LIB_SUFF|" setup.py

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%install
export YICES_PATH=%prefix
%python_build_install

%if_with python3
pushd ../python3
python3_build_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
nosetests -v
%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2.git20140507
- Cleaned up spec and fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20140507.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140507
- Initial build for Sisyphus

