%define oname encore
Name: python-module-%oname
Version: 0.6.1
Release: alt1.dev.git20141208
Summary: A Collection of core-level utility modules for Enthought projects
License: BSD
Group: Development/Python
Url: https://github.com/enthought/encore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/encore.git
Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel graphviz
BuildPreReq: python-module-pydot

%description
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

%package docs
Summary: Documentation for encore
Group: Development/Documentation

%description docs
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains documentation for encore.

%package pickles
Summary: Pickles for encore
Group: Development/Python

%description pickles
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains pickles for encore.

%package tests
Summary: Tests for encore
Group: Development/Python
Requires: %name = %EVR

%description tests
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

This package contains tests for encore.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
%make -C docs pickle

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE.txt README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/testing

%files docs
%doc docs/build/html/*

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/testing

%changelog
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.dev.git20141208
- Version 0.6.1.dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.git20140910
- New snapshot

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.git20140422
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20140422
- Version 0.6.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20131018
- Version 0.4.0

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130405
- Version 0.3

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20130115
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20120822
- Version 0.2.1

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120119
- Initial build for Sisyphus

