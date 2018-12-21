%define oname pygsl
Name: python-module-%oname
Version: 2.2.0
Release: alt1
Summary: Python interface for GNU Scientific Library (GSL)
License: GPLv2
Group: Development/Python
Url: http://pygsl.sourceforge.net/

Source: %oname-%version.tar.gz

BuildRequires: libgsl-devel libnumpy-devel swig

%description
This project provides a python interface for the GNU scientific library
(GSL).

%package devel
Summary: Development files of Python interface for GSL
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description devel
This project provides a python interface for the GNU scientific library
(GSL).

This package contains development files of Python interface for GSL.

%package testing
Summary: Tests for Python interface for GSL
Group: Development/Python
Requires: %name = %version-%release

%description testing
This project provides a python interface for the GNU scientific library
(GSL).

This package contains tests for Python interface for GSL.

%package docs
Summary: Documentation for Python interface for GSL
Group: Development/Documentation
BuildArch: noarch

%description docs
This project provides a python interface for the GNU scientific library
(GSL).

This package contains documentation for Python interface for GSL.

%package examples
Summary: Examples for Python interface for GSL
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This project provides a python interface for the GNU scientific library
(GSL).

This package contains examples for Python interface for GSL.

%prep
%setup

rm -f swig_src/*

%build
python setup.py config
%python_build_debug

%install
%python_install

%files
%doc CREDITS ChangeLog README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/testing

%files devel
%_includedir/*/*

%files testing
%python_sitelibdir/%oname/testing

%files docs
%doc doc/*.html

%files examples
%doc examples/*

%changelog
* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt3
- Rebuilt with gsl90 instead of gsl

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

