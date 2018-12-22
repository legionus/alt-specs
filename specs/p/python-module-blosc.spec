%define oname blosc

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt2
Summary: A Python wrapper for the extremely fast Blosc compression library
License: MIT or BSD
Group: Development/Python
Url: http://python-blosc.blosc.org/

# https://github.com/Blosc/python-blosc.git
Source: %name-%version.tar
Patch0: %name-%version-arm.patch
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libblosc-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-numpy-testing python-module-pytest
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-numpy-testing python3-module-pytest
%endif

%py_provides %oname

%description
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains pickles for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A Python wrapper for the extremely fast Blosc compression library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains tests for %oname.
%endif

%prep
%setup
%ifnarch %ix86 x86_64
%patch0 -p1
%endif
%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug \
	--blosc=%prefix

%if_with python3
pushd ../python3
%python3_build_debug \
	--blosc=%prefix
popd
%endif

%install
%python_install \
	--blosc=%prefix

%if_with python3
pushd ../python3
%python3_install \
	--blosc=%prefix
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
cd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v --with-doctest %oname
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v --with-doctest %oname
%endif

%files
%doc *.rst doc/_build/html bench
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/_build/html bench
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Tue May 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt2
- fixed build on non-x86

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1
- Updated to upstream version 1.5.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.6-alt1.dev.git20150415.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1.dev.git20150415.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev.git20150415
- Initial build for Sisyphus

