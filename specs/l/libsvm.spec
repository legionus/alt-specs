%define sover 2

%def_with python3

Name: libsvm
Version: 3.18
Release: alt2.1
Summary: A Library for Support Vector Machines
Group: Sciences/Mathematics
License: BSD
URL: http://www.csie.ntu.edu.tw/~cjlin/libsvm/
Source: %name-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package devel
Summary: Development files of LIBSVM
Group: Development/C++
Requires: %name = %version-%release

%description devel
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains development files of LIBSVM.

%package tools
Summary: Tools for LIBSVM
Group: Sciences/Mathematics
Requires: %name = %version-%release

%description tools
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains tools for LIBSVM.

%package -n python-module-svm
Summary: Python interface for LIBSVM
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description -n python-module-svm
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains Python interface for LIBSVM.

%package -n python3-module-svm
Summary: Python interface for LIBSVM
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release

%description -n python3-module-svm
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains Python interface for LIBSVM.

%prep
%setup

%build
%make_build lib all

%install

install -d %buildroot%_libdir
install -m644 libsvm.so.%sover %buildroot%_libdir
ln -s libsvm.so.%sover %buildroot%_libdir/libsvm.so

install -d %buildroot%_includedir
install -m644 *.h %buildroot%_includedir

install -d %buildroot%_bindir
install -m755 svm-predict svm-scale svm-train \
	%buildroot%_bindir
for i in checkdata easy grid subset; do
	install -m755 tools/$i.py %buildroot%_bindir/svm-$i
done

# python

install -d %buildroot%python_sitelibdir_noarch
install -m644 python/*.py %buildroot%python_sitelibdir_noarch

%if_with python3
install -d %buildroot%python3_sitelibdir_noarch
install -m644 python/*.py %buildroot%python3_sitelibdir_noarch
%endif

%files
%doc COPYRIGHT README *.html
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files tools
%doc tools/README
%_bindir/*

%files -n python-module-svm
%doc python/README
%python_sitelibdir_noarch/*

%if_with python3
%files -n python3-module-svm
%doc python/README
%python3_sitelibdir_noarch/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.18-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18-alt2
- Added module for Python 3

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18-alt1
- Version 3.18

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.17-alt1
- Version 3.17

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt1
- Version 3.16

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt2
- Fixed build

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt1
- Version 3.12

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1
- Version 3.11

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1-alt1.1
- Rebuild with Python-2.7

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.91-alt1
- Initial build for Sisyphus

