# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt4.1.1
%define oname z3c.recipe.paster

%def_with python3

Name: python-module-%oname
Version: 0.5.3
#Release: alt4.1
Summary: Zope3 paste deploy setup recipe
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.paster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c.recipe paste paste.deploy paste.script ZConfig
%py_requires zc.recipe.egg zope.app.wsgi zope.app.debug zope.schema
%py_requires zope.interface

%description
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

%package -n python3-module-%oname
Summary: Zope3 paste deploy setup recipe
Group: Development/Python3
%py3_requires z3c.recipe paste paste.deploy paste.script ZConfig
%py3_requires zc.recipe.egg zope.app.wsgi zope.app.debug zope.schema
%py3_requires zope.interface

%description -n python3-module-%oname
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 paste deploy setup recipe
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires transaction ZODB3 pytz zc.lockfile zc.recipe.filestorage
%py3_requires zdaemon zope.annotation zope.app.appsetup
%py3_requires zope.authentication zope.app.publication zope.browser
%py3_requires zope.broken zope.cachedescriptors zope.component
%py3_requires zope.configuration zope.container zope.copy
%py3_requires zope.deferredimport zope.dottedname zope.error zope.event
%py3_requires zope.exceptions zope.filerepresentation zope.i18n
%py3_requires zope.i18nmessageid zope.processlifetime
%py3_requires zope.lifecycleevent zope.location zope.minmax zope.proxy
%py3_requires zope.publisher zope.session zope.site zope.size
%py3_requires zope.testing zc.buildout zope.traversing zope.security

%description -n python3-module-%oname-tests
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

This package contains tests for Zope3 paste deploy setup recipe.

%package tests
Summary: Tests for Zope3 paste deploy setup recipe
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction ZODB3 pytz zc.lockfile zc.recipe.filestorage
%py_requires zdaemon zope.annotation zope.app.appsetup
%py_requires zope.authentication zope.app.publication zope.browser
%py_requires zope.broken zope.cachedescriptors zope.component
%py_requires zope.configuration zope.container zope.copy
%py_requires zope.deferredimport zope.dottedname zope.error zope.event
%py_requires zope.exceptions zope.filerepresentation zope.i18n
%py_requires zope.i18nmessageid zope.processlifetime
%py_requires zope.lifecycleevent zope.location zope.minmax zope.proxy
%py_requires zope.publisher zope.session zope.site zope.size
%py_requires zope.testing zc.buildout zope.traversing zope.security

%description tests
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

This package contains tests for Zope3 paste deploy setup recipe.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt4.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Fixed requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

