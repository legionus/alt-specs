%define oname mario

%def_disable check
%def_with bootstrap

Name: python3-module-%oname
Version: 0.27.1
Release: alt2
Summary: Mario is a framework to develop projects
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/mario/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-sugarbowl python3-module-clyde
#BuildPreReq: python3-module-runfile python3-module-run-render
#BuildPreReq: python3-module-run-io python3-module-nose

%py3_provides %oname
%py3_requires sugarbowl clyde

%if_with bootstrap
%add_python3_req_skip run.plugins.io run.plugins.render
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-jinja2 python3-module-setuptools
BuildRequires: python3-module-nose python3-module-pytest python3-module-runfile rpm-build-python3

%description
Mario is a framework to develop projects.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.27.1-alt2
- rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.27.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.27.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.1-alt1
- Initial build for Sisyphus

