# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1.1
%define oname zc.monitor

%def_with python3

Name: python-module-%oname
Version: 0.3.1
#Release: alt2.1
Summary: A network-accessible command-line monitoring interface
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.monitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.ngi zope.component zope.testing

%description
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

%package -n python3-module-%oname
Summary: A network-accessible command-line monitoring interface
Group: Development/Python3
%py3_requires zc.ngi zope.component zope.testing

%description -n python3-module-%oname
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

%package -n python3-module-%oname-tests
Summary: Tests for zc.monitor
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

This package contains tests for zc.monitor.

%package tests
Summary: Tests for zc.monitor
Group: Development/Python
Requires: %name = %version-%release

%description tests
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

This package contains tests for zc.monitor.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

