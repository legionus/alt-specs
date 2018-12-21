# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1.1
%define oname z3c.pluggabletemplates

%def_with python3

Name: python-module-%oname
Version: 0.2
#Release: alt3.1
Summary: Seperation of view code from skin templates like z3c.viewtemplate
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pluggabletemplates/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.component zope.configuration zope.publisher
%py_requires zope.pagetemplate zope.interface zope.i18nmessageid
%py_requires zope.app.pagetemplate zope.schema zope.contentprovider

%description
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

%package -n python3-module-%oname
Summary: Seperation of view code from skin templates like z3c.viewtemplate
Group: Development/Python3
%py3_requires zope.component zope.configuration zope.publisher
%py3_requires zope.pagetemplate zope.interface zope.i18nmessageid
%py3_requires zope.app.pagetemplate zope.schema zope.contentprovider

%description -n python3-module-%oname
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.pluggabletemplates
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

This package contains tests for z3c.pluggabletemplates.

%package tests
Summary: Tests for z3c.pluggabletemplates
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

This package contains tests for z3c.pluggabletemplates.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

