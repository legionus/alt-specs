# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.svn20100615.1.1
%define oname swiginac

Name: python-module-%oname
Version: 1.5.1.1
#Release: alt3.svn20100615.1
Summary: Extending Python with Symbolic Mathematics
Group: Development/Python
License: GPL
URL: http://swiginac.berlios.de/
# svn://svn.berlios.de/swiginac/trunk
Source: %oname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: libginac-devel swig gcc-c++ ginac
BuildPreReq: libnumpy-devel
BuildPreReq: python-devel
%setup_python_module %oname

%description
Swiginac is a Python interface to GiNaC, built with SWIG. The aim of swiginac is
to make all the functionality of GiNaC accessible from Python as an extension
module.

Features:

*    Symbols and expressions with arithmetic operations
*    Multivariate polynomials and rational functions
*    Matrices and vectors
*    Linear systems solver
*    Tayler series expansions
*    Differentiation and integration
*    Output C, Python and LaTeX code

%package -n %oname-docs
Summary: Documentation for Swiginac
Group: Development/Documentation
BuildArch: noarch
%py_requires Symbolic

%description -n %oname-docs
Swiginac is a Python interface to GiNaC, built with SWIG. The aim of swiginac is
to make all the functionality of GiNaC accessible from Python as an extension
module.

This package contains development documentation for Swiginac.

%package -n python-module-Symbolic
Summary: Symbolic subpackage of Swiginac
Group: Development/Python
#BuildArch: noarch

%description  -n python-module-Symbolic
Swiginac is a Python interface to GiNaC, built with SWIG. The aim of swiginac is
to make all the functionality of GiNaC accessible from Python as an extension
module.

This package contains Symbolic subpackage of Swiginac.

%prep
%setup

%build
%python_build_debug build_ext build_py

%install
%python_install

install -d %buildroot%_docdir/%oname
cp -fR doc/* %buildroot%_docdir/%oname/
install -p -m644 ChangeLog %buildroot%_docdir/%oname
cp -fR tests %buildroot%_docdir/%oname/

rm -f %buildroot%python_sitelibdir_noarch/Symbolic/*.pyo

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

%files
%doc %dir %_docdir/%oname
%doc %_docdir/%oname/ChangeLog
%python_sitelibdir/*%{oname}*

%files -n python-module-Symbolic
%python_sitelibdir/Symbolic*

%files -n %oname-docs
%doc %dir %_docdir/%oname
%doc %_docdir/%oname/*
%exclude %_docdir/%oname/ChangeLog

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1.1-alt3.svn20100615.1.1
- (AUTO) subst_x86_64.

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.1.1-alt3.svn20100615.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt3.svn20100615
- Rebuilt with new libginac

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt2.svn20100615
- Rebuilt with libginac 1.6.2

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.1.1-alt1.svn20100615.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.1.1-alt1.svn20100615.3.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt1.svn20100615.3
- Rebuilt with libginac 1.6.1

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt1.svn20100615.2
- Rebuilt for debuginfo

* Fri Dec 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt1.svn20100615.1
- Rebuilt for soname set-versions

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.1-alt1.svn20100615
- Version 1.5.1.1

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt4.svn20090924.1
- Added requirement %oname-docs on python-module-Symbolic

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt4.svn20090924
- Built from git-svn
- Rebuilt with reformed NumPy
- Added tests into %oname-docs

* Fri Dec 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt3
- Rebuilt without python-module-Numeric

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt2
- Rebuild with python 2.6

* Mon May 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
