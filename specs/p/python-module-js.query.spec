# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.hg20130303.1.1
%define oname js.query

%def_with python3

Name: python-module-%oname
Version: 1.9.2
#Release: alt1.dev0.hg20130303.1
Summary: fanstatic jQuery
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/fanstatic/js.jquery
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js

%description
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

%package -n python3-module-%oname
Summary: fanstatic jQuery
Group: Development/Python3
%py3_provides %oname
%py3_requires js

%description -n python3-module-%oname
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

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

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.dev0.hg20130303.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.dev0.hg20130303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1.dev0.hg20130303
- Initial build for Sisyphus

