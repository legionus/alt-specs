%define oname uflacs

Name: python-module-%oname
Version: 1.6.0
Release: alt1.dev.git20150421
Summary: UFL Analyser and Compiler System
Group: Development/Python
License: LGPLv3
URL: https://launchpad.net/uflacs
# https://bitbucket.org/fenics-project/uflacs.git
Source: %name-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-distribute

%description
The UFL Analyser and Compiler System - uflacs - is a utility for
processing UFL code in various fashions.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README* doc/*
#_bindir/*
%python_sitelibdir/*

%changelog
* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev.git20150421
- Version 1.6.0dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20140901
- Version 1.4.0

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20140429
- Version 0.3.0

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.git20130926
- New snapshot

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.git20130322
- New snapshot

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20130130
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20120928
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.bzr20120622
- Added %_bindir/%oname

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20120622
- Initial build for Sisyphus

