%define oname tulipcore

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt2.a2.git20140503.1.2
Summary: An alternative Gevent core loop implementation with asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tulipcore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/decentfox/tulipcore.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-gevent
#BuildPreReq: python-module-greenlet
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-gevent
#BuildPreReq: python3-module-greenlet
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pycparser python3-module-setuptools
BuildRequires: python3-module-cffi python3-module-greenlet python3-module-pytest rpm-build-python3

#BuildRequires: python3-module-cffi python3-module-greenlet python3-module-pytest
%endif

%py_provides %oname
#%py_requires asyncio gevent greenlet

%description
tulipcore is an alternative gevent core loop. It is based on asyncio
a.k.a. tulip, the async library for Python 3. With tulipcore, you can
run gevent code on top of asyncio.

%package -n python3-module-%oname
Summary: An alternative Gevent core loop implementation with asyncio
Group: Development/Python3
%py3_provides %oname
#%py3_requires asyncio gevent greenlet

%description -n python3-module-%oname
tulipcore is an alternative gevent core loop. It is based on asyncio
a.k.a. tulip, the async library for Python 3. With tulipcore, you can
run gevent code on top of asyncio.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2.a2.git20140503.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt2.a2.git20140503.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2.a2.git20140503.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.1.0-alt2.a2.git20140503
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a2.git20140503
- Initial build for Sisyphus

