%define sover 0
Name: algencan
Version: 3.0.0
Release: alt1.beta
Summary: Solving extremely large problems with moderate computer time
License: GPL v2 or later
Group: Sciences/Mathematics
Url: http://www.ime.usp.br/~egbirgin/tango/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

#BuildPreReq: libatlas-devel liblapack-devel
BuildPreReq: gcc-c++ gcc-fortran R-devel python-devel
BuildPreReq: libparmetis-devel libopenblas-devel libnumpy-devel

%description
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

%package -n python-module-pywrapper
Summary: Python wrapper for ALGENCAN
Group: Development/Python
%setup_python_module pywrapper

%description -n python-module-pywrapper
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

This package contains Python wrapper for ALGENCAN.

%package -n python-module-%name
Summary: Python interface for ALGENCAN
Group: Development/Python
%setup_python_module %name
Requires: python-module-pywrapper = %version-%release

%description -n python-module-%name
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

This package contains Python interface for ALGENCAN.

%package -n R-%name
Summary: R interface for ALGENCAN
Group: Sciences/Mathematics

%description -n R-%name
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

This package contains R interface for ALGENCAN.

%package -n lib%name
Summary: Shared library of ALGENCAN
Group: System/Libraries

%description -n lib%name
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

This package contains shared library of ALGENCAN.

%package -n lib%name-devel
Summary: Headers of ALGENCAN
Group: Development/Other
Provides: %name-devel = %EVR
Requires: lib%name = %EVR
#Requires: python-module-%name = %version-%release
#Requires: R-%name = %version-%release

%description -n lib%name-devel
Fortran code for general nonlinear programming that does not use matrix
manipulations at all and, so, is able to solve extremely large problems
with moderate computer time. The general algorithm is of Augmented
Lagrangian type and the subproblems are solved using GENCAN. GENCAN
(included in ALGENCAN) is a Fortran code for minimizing a smooth
function with a potentially large number of variables and
box-constraints.

This package contains development headers for ALGENCAN.

%prep
%setup
#if "%_python_version" != "2.5"
#sed -i 's|2\.5|%_python_version|g' \
#	Makefile sources/interfaces/py/Makefile
#endif
#sed -i 's|2\.6|%_python_version|g' Makefile
mkdir lib

%install
%make PROBNAME=toyprob
#make algencan-c PROBNAME=toyprob
#make algencan-py
#make algencan-r

install -d %buildroot%_libdir
install -d %buildroot%_bindir
install -d %buildroot%python_sitelibdir/%name
install -d %buildroot%_includedir/%name
RLIBDIR=$(pkg-config libR --variable=rlibdir)
install -d %buildroot$RLIBDIR

#install -m755 bin/fortran/* %buildroot%_bindir
#install -m755 bin/c/* %buildroot%_bindir/%{name}c

#install -m644 bin/py/*.so %buildroot%python_sitelibdir
#touch bin/py/__init__.py
#install -m644 bin/py/*.py \
#	sources/interfaces/py/runalgencan.py \
#	sources/interfaces/py/toyprob.py \
#	%buildroot%python_sitelibdir/%name

#install -m644 bin/r/* %buildroot$RLIBDIR
#INSTALL_R=$PWD/INSTALL_R
#pushd %buildroot
#for i in $(ls ./$RLIBDIR/); do
#	echo $RLIBDIR/$i >>$INSTALL_R
#done
#popd

#for i in c r py; do
#	install -p -m644 sources/interfaces/$i/*.h \
#		%buildroot%_includedir/%name
#done

gfortran -shared -Wl,--whole-archive lib/lib%name.a \
	-Wl,--no-whole-archive \
	-Wl,-soname=lib%name.so.%sover \
	-o %buildroot%_libdir/lib%name.so.%sover
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

#files
#doc license.txt README WHATSNEW
#_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
#_includedir/*
%_libdir/*.so

#files -n python-module-pywrapper
#python_sitelibdir/pywrapper.so

#files -n python-module-%name
#python_sitelibdir/%name

#files -n R-%name -f INSTALL_R

%changelog
* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.beta
- Version 3.0.0-beta

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt3
- Built with OpenBLAS instead of GotoBLAS2

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt2
- Rebuilt

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.7-alt1.1
- Rebuild with Python-2.7

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt1
- Version 2.3.7

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt4
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt3
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt2
- Rebuilt for soname set-versions

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt2
- Fixed underlinking

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3

* Fri Jun 11 2010 Alexey Tourbin <at@altlinux.ru> 2.2.1-alt3.1
- Rebuilt with libR-2.11.so

* Fri Feb 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt3
- Rebuilt with reformed NumPy

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2
- Rebuilt with python 2.6

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus

