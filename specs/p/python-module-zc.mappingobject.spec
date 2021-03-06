# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1
%define oname zc.mappingobject

%def_with python3

Name: python-module-%oname
Version: 1.0.0
#Release: alt1.1
Summary: Wrapper for a mapping objects that provides both attribute and item access
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.mappingobject/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires zc

%description
Sometimes, you want to use a mapping object like a regular object.

zc.mappingobject provides a wrapper for a mapping objects that provides
both attribute and item access.

%package -n python3-module-%oname
Summary: Wrapper for a mapping objects that provides both attribute and item access
Group: Development/Python3
%py3_provides %oname
%py3_requires zc

%description -n python3-module-%oname
Sometimes, you want to use a mapping object like a regular object.

zc.mappingobject provides a wrapper for a mapping objects that provides
both attribute and item access.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

