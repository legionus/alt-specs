%def_without python3

Version: 1.1.0
Release: alt1

%setup_python_module cjson

Summary: Fast JSON encoder/decoder for Python
Name: %packagename
License: LGPL
Group: Development/Python

Source0: python-%modulename-%version.tar

URL: http://pypi.python.org/pypi/python-cjson/
Packager: Dmitry M. Maslennikov <rlz at altlinux.org>

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif


%description
This module implements a very fast JSON encoder/decoder for Python.
JSON stands for JavaScript Object Notation and is a text based
lightweight data exchange format which is easy for humans to read/write
and for machines to parse/generate. JSON is completely language
independent and has multiple implementations in most of the programming
languages, making it ideal for data exchange and storage.

The module is written in C and it is up to 250 times faster when
compared to the other python JSON implementations which are written
directly in python. This speed gain varies with the complexity of the
data and the operation and is the the range of 10-200 times for encoding
operations and in the range of 100-250 times for decoding operations.

%package -n python3-module-%modulename
Summary: Fast JSON encoder/decoder for Python
Group: Development/Python3

%description -n python3-module-%modulename
This module implements a very fast JSON encoder/decoder for Python.
JSON stands for JavaScript Object Notation and is a text based
lightweight data exchange format which is easy for humans to read/write
and for machines to parse/generate. JSON is completely language
independent and has multiple implementations in most of the programming
languages, making it ideal for data exchange and storage.

The module is written in C and it is up to 250 times faster when
compared to the other python JSON implementations which are written
directly in python. This speed gain varies with the complexity of the
data and the operation and is the the range of 10-200 times for encoding
operations and in the range of 100-250 times for decoding operations.

%prep
%setup -n python-%modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc ChangeLog README
%python3_sitelibdir/*
%endif

%changelog
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2
- Rebuilt with python 2.6

* Fri Jul 04 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 1.0.5-alt1
- initial build

