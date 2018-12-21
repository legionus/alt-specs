%define oname apptools

%def_without python3

Name:           python-module-%oname
Version:        4.4.0
Release:        alt2
Summary:        Enthough Tool Suite Application Tools

Group:          Development/Python
License:        BSD and LGPLv2+
URL:            http://www.enthought.com/
# https://github.com/enthought/apptools.git
Source:        AppTools-%version.tar.gz
Source1:        README.fedora.python-AppTools
Patch1: %oname-%version-alt-build.patch

BuildArch:      noarch
BuildRequires:  python-module-setuptools, python-devel
BuildRequires: unzip python-module-setupdocs python-module-sphinx-devel
BuildRequires: python-module-traits-tests python-module-wx python-module-tables-tests xvfb-run
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setupdocs python-tools-2to3
%endif

%py_requires %oname.help.help_plugin.examples_preferences
%add_python_req_skip examples_preferences

%description
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.

%if_with python3
%package -n python3-module-%oname
Summary: Enthough Tool Suite Application Tools (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications. They implement
functionality that is commonly needed by many applications

    * enthought.appscripting: Framework for scripting applications.

    * enthought.help: Provides a plugin for displaying documents and
      examples and running demos in Envisage Workbench applications.

    * enthought.io: Provides an abstraction for files and folders in a
      file system.

    * enthought.naming: Manages naming contexts, supporting non-string
      data types and scoped preferences

    * enthought.permissions: Supports limiting access to parts of an
      application unless the user is appropriately authorised (not
      full-blown security).

and many more.
%endif

%package docs
Summary: Documentation for AppTools
Group: Development/Documentation
BuildArch: noarch

%description docs
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications.

This package contains documentation for AppTools.

%package pickles
Summary: Pickles for AppTools
Group: Development/Python

%description pickles
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications.

This package contains pickles for AppTools.

%package tests
Summary: Tests for AppTools
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip util

%description tests
The AppTools project includes a set of packages that Enthought has
found useful in creating a number of applications.

This package contains tests for AppTools.

%prep
%setup -n AppTools-%version
%patch1 -p1
#rm -rf AppTools.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs/source

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install -O1
install -p -m644 %SOURCE1 README.fedora
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# pickles

install -d %buildroot%python_sitelibdir/%oname
cp -fR pickle %buildroot%python_sitelibdir/%oname/

%check
# remove buggy test
rm examples/permissions/server/test_client.py
xvfb-run py.test

%files
%doc *.txt README.fedora
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
#_bindir/*
%exclude %python_sitelibdir/%oname/*/test*
%exclude %python_sitelibdir/%oname/*/*/*/example*
%exclude %python_sitelibdir/%oname/*/*/example*
%exclude %python_sitelibdir/%oname/*/*/test*

%files tests
%python_sitelibdir/%oname/*/test*
%python_sitelibdir/%oname/*/*/*/example*
%python_sitelibdir/%oname/*/*/example*
%python_sitelibdir/%oname/*/*/test*

%files docs
%doc examples html

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt README.fedora
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Updated to upstream release version 4.4.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150430
- Version 4.4.0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20150211
- Version 4.3.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20140919
- New snapshot

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2.git20140408
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20140408
- Version 4.2.1

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.git20130328
- Version 4.2.0

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20121012
- Version 4.1.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20120329
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111221
- Version 4.0.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111110
- Version 4.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.2-alt1.svn20110127.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1.svn20110127
- Version 3.4.2

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101102.1
- Rebuilt with python-module-sphinx-devel

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20101102
- Version 3.4.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20100706
- Version 3.3.3

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100225
- Version 3.3.2
- Extracted docs into separate package
- Added pickles package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090928.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20090928
- Version 3.3.1

* Fri Oct 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Fixed versions of requirements

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.2.0-1
- Updated

* Thu Jun 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-4
- Added README.fedora

* Fri Apr 24 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-3
- Removed AppTools.egg-info directory

* Fri Mar 06 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Included examples in %%doc, added python-TraitsGUI & python-EnthoughtBase
- as Requires. Added html folder.

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Initial package
