%define oname pykwalify

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.6.1
Release: alt1
Epoch: 1
Summary: Python lib/cli for JSON/YAML schema validation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pykwalify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Grokzen/pykwalify.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-nose python-module-pbr python-module-tox python-module-unittest2 python-module-z4r-coveralls

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-docopt python-module-yaml
#BuildPreReq: python-module-testfixtures python-module-tox
#BuildPreReq: python-module-coveralls
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docopt python3-module-yaml
#BuildPreReq: python3-module-testfixtures python3-module-tox
#BuildPreReq: python3-module-coveralls
BuildRequires: python3-module-html5lib python3-module-nose python3-module-pbr python3-module-tox python3-module-unittest2 python3-module-z4r-coveralls python3-module-zope.component
%endif

%py_provides %oname
#%py_requires json docopt yaml

%description
YAML/JSON validation library.

This framework is a port with alot added functionality of the java
version of the framework kwalify that can be found at:
http://www.kuwata-lab.com/kwalify/

%package -n python3-module-%oname
Summary: Python lib/cli for JSON/YAML schema validation
Group: Development/Python3
%py3_provides %oname
#%py3_requires json docopt yaml

%description -n python3-module-%oname
YAML/JSON validation library.

This framework is a port with alot added functionality of the java
version of the framework kwalify that can be found at:
http://www.kuwata-lab.com/kwalify/

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1:1.6.1-alt1
- The version is synchronized with upstream (used Epoch)

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 18.03-alt1.git20180314
- build new version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 15.01-alt2.git20150117.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.01-alt2.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 15.01-alt2.git20150117
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.01-alt1.git20150117
- Initial build for Sisyphus
