%define oname httreplay

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150126.1.2
Summary: A HTTP replay library for testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/httreplay/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davepeck/httreplay.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-requests
#BuildPreReq: python-module-urllib3 python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-requests
#BuildPreReq: python3-module-urllib3
%endif

%py_provides %oname
%py_requires six requests urllib3 json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
A Python HTTP replay library for testing. Supports [httplib, requests,
urllib3] and HTTP/S requests.

%package -n python3-module-%oname
Summary: A HTTP replay library for testing
Group: Development/Python3
%py3_provides %oname
%py3_requires six requests urllib3

%description -n python3-module-%oname
A Python HTTP replay library for testing. Supports [httplib, requests,
urllib3] and HTTP/S requests.

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

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1.git20150126.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150126
- Initial build for Sisyphus

