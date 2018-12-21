%define oname nfftpy
Name: python-module-%oname
Version: 0.1
Release: alt5.git20110420
Summary: Cython wrapper for NFFT library
License: BSD
Group: Development/Python
Url: https://github.com/enthought/nfftpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/nfftpy.git
Source: %name-%version.tar

BuildPreReq: python-module-distribute libfftw3-devel libnfft-devel
BuildPreReq: python-module-Cython libnumpy-devel

%description
NFFT is a C subroutine library for computing the nonequispaced discrete
Fourier transform (NDFT) and its generalisations in one or more
dimensions, of arbitrary input size, and of complex data.

NFFTPY wraps NFFT using Cython, to make it usable from Python.

%prep
%setup

%build
%python_build_debug build_ext

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5.git20110420
- Rebuilt with updated NumPy

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.git20110420
- Rebuilt with updated NumPy

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.git20110420
- Rebuilt with updated NumPy

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.git20110420
- Rebuilt with nfft 3.2.1-alt1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.git20110420.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20110420
- Initial build for Sisyphus

