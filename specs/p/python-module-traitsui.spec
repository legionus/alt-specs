%define _unpackaged_files_terminate_build 1

%define oname traitsui

%def_without python3
%def_enable bootstrap

Name: python-module-%oname
Version: 6.0.0
Release: alt1
Summary: A set of user interface tools designed to complement Traits
Group: Development/Python
License: BSD and EPL and LGPL
URL: http://www.enthought.com/
BuildArch: noarch

# https://github.com/enthought/traitsui.git
Source: %oname-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires: python-module-setuptools python-devel
%if_disabled bootstrap
BuildRequires(pre): python-module-sphinx-devel
BuildRequires: python-module-setupdocs
BuildRequires: python-module-traits
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setupdocs
BuildRequires: python-tools-2to3
%endif

%description
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%if_with python3
%package -n python3-module-%oname
Summary: A set of user interface tools designed to complement Traits (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

%package -n python3-module-%oname-tests
Summary: Tests for TraitsUI (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.
%endif

%package tests
Summary: Tests for TraitsUI
Group: Development/Python
Requires: %name = %EVR
Conflicts: %name < %EVR

%description tests
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains tests for TraitsUI.

%package docs
Summary: Documentation for TraitsUI
Group: Development/Documentation

%description docs
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains documentation for TraitsUI.

%package pickles
Summary: Pickles for TraitsUI
Group: Development/Python
AutoReq: nopython

%description pickles
TraitsUI is a set of user interface tools designed to complement Traits.
In the simplest case, it can automatically generate a user interface for
editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a
Model-View-Controller (MVC) design pattern for Traits-based objects.

This package contains pickles for TraitsUI.

%prep
%setup
%patch1 -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_disabled bootstrap
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i ||:
done
%python3_build_debug
popd
%endif

%if_disabled bootstrap
%make -C docs html
%make -C docs pickle
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_disabled bootstrap
# pickles
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%if_disabled bootstrap
%exclude %python_sitelibdir/%oname/pickle
%endif

%if_disabled bootstrap
%files docs
%doc docs/build/html docs/*.txt docs/*.ppt docs/*.pdf

%files pickles
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20150224
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140911
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140110
- Version 4.5.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131022
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20131022
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130413
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20121009
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120408
- New snapshot
- Added module for Python 3

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120122
- Version 4.1.1

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.git20111103
- Moved tests into separate package

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20111103
- Initial build for Sisyphus

