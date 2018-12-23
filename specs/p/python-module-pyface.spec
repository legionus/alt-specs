%define _unpackaged_files_terminate_build 1

%define oname pyface

Name: python-module-%oname
Version: 6.0.0
Release: alt1
Summary: Traits-capable windowing framework

Group: Development/Python
License: BSD and EPL and LGPL
URL: http://www.enthought.com/
BuildArch: noarch

# https://github.com/enthought/pyface.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires(pre): python-module-sphinx-devel
BuildRequires: python-module-setuptools python-devel
BuildRequires: python-module-setupdocs

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

%package docs
Summary: Documentation for pyface
Group: Development/Documentation

%description docs
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains documentation for pyface.

%package pickles
Summary: Pickles for pyface
Group: Development/Python

%description pickles
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains pickles for pyface.

%package tests
Summary: Tests for pyface
Group: Development/Python
Requires: %name = %EVR

%description tests
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits
package.  Thus, you can write code in terms of the Traits API (views,
items, editors, etc.), and let pyface and your selected toolkit and
back-end take care of the details of displaying them.

This package contains tests for pyface.

%prep
%setup
%patch1 -p1

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%make -C docs html
%make -C docs pickle

%install
%python_install

# pickles
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/util/tests
%exclude %python_sitelibdir/%oname/ui/qt4/util/test*

%files tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/util/tests
%python_sitelibdir/%oname/ui/qt4/util/test*

%files docs
%doc docs/build/html examples docs/*.txt docs/*.doc docs/*.pdf docs/*.ppt

%files pickles
%python_sitelibdir/%oname/pickle

%changelog
* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt1
- Updated to upstream version 6.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1
- automated PyPI update

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150401
- Version 4.6.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20140923
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20140430
- Version 4.4.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130620
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130620
- New snapshot

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130418
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130128
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20121010
- Version 4.2.1

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2.git20120504
- Extracted tests into separate package

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120120
- Version 4.1.1

* Mon Nov 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111115
- Initial build for Sisyphus

