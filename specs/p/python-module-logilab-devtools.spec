%define oname logilab-devtools
Name: python-module-%oname
Version: 0.23.0
Release: alt1.1
Summary: Set of development tools used at Logilab
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/logilab-devtools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-logilab-common

%py_provides logilab.devtools
%py_requires logilab.common

%description
Set of tools which aims to help the developpement process, including:

* tools to check and build source and/or Debian packages
* provides integration assistance to work with CubicWeb, Mercurial and
  GuestRepo.

%prep
%setup

%build
%python_build_debug

%install
%python_install

touch %buildroot%python_sitelibdir/hgext/__init__.py

%check
python setup.py test

%files
%doc ChangeLog README
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/logilab/__init__.py*
%exclude %python_sitelibdir/*.pth

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.23.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1
- Initial build for Sisyphus

