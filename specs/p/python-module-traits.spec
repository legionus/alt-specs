%define _unpackaged_files_terminate_build 1

%define oname traits

%def_without python3

Name:           python-module-%oname
Version:        4.6.0
Release:        alt2
Summary:        Explicitly typed attributes for Python

Group:          Development/Python
# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file. Except enthought/traits/ui/editors_gen.py
# which is GPLv2+ all remaining source or image files are in BSD
# 3-clause license. Confirmed from upstream.
License:        BSD and EPL-1.0 and LGPLv2 and GPL-2.0-or-later
URL:            http://code.enthought.com/projects/traits/

# https://github.com/enthought/traits.git
Source: Traits-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires(pre): python-module-sphinx-devel
BuildRequires: python-module-setuptools libnumpy-devel python-devel
BuildRequires: python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildRequires: libnumpy-py3-devel python-tools-2to3
%endif

%description
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object 
attributes, traits also have several additional characteristics: 

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

%if_with python3
%package -n python3-module-%oname
Summary: Explicitly typed attributes for Python 3
Group: Development/Python3

%description -n python3-module-%oname
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object 
attributes, traits also have several additional characteristics: 

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

%package -n python3-module-%oname-tests
Summary: Tests for Traits, explicitly typed attributes for Python 3
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The traits package developed by Enthought provides a special type
definition called a trait. This package contains tests for it.
%endif

%package doc
Summary: Documentation for Traits, explicitly typed attributes for Python
Group: Development/Documentation
BuildArch: noarch

%description doc
The traits package developed by Enthought provides a special type
definition called a trait. This package contains development
documentation for it.

%package pickles
Summary: Pickles for Traits, explicitly typed attributes for Python
Group: Development/Python

%description pickles
The traits package developed by Enthought provides a special type
definition called a trait. This package contains pickles for it.

%package tests
Summary: Tests for Traits, explicitly typed attributes for Python
Group: Development/Python
Requires: %name = %EVR

%description tests
The traits package developed by Enthought provides a special type
definition called a trait. This package contains tests for it.

%prep
%setup -n Traits-%version
%patch1 -p1

# file not utf-8
iconv -f iso8859-1 -t utf-8 image_LICENSE_Eclipse.txt \
 > image_LICENSE_Eclipse.txt.conv && mv -f \
 image_LICENSE_Eclipse.txt.conv image_LICENSE_Eclipse.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .

%build
%add_optflags -fno-strict-aliasing

%python_build_debug

%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
popd
%endif

%install
%python_install

rm -f %buildroot/%python_sitelibdir/traits/protocols/_speedups.c
rm -f %buildroot/%python_sitelibdir/traits/ctraits.c

# Prevents non standard permissions
#chmod 755 %buildroot/%python_sitelibdir/traits/protocols/_speedups.so
chmod 755 %buildroot/%python_sitelibdir/traits/ctraits.so

%if_with python3
pushd ../python3
%python3_install

rm -f %buildroot/%python3_sitelibdir/traits/protocols/_speedups.c
rm -f %buildroot/%python3_sitelibdir/traits/ctraits.c

# Prevents non standard permissions
#chmod 755 %buildroot/%python_sitelibdir/traits/protocols/_speedups.so
#chmod 755 %buildroot/%python_sitelibdir/traits/ctraits.so
popd
%endif

# pickles

install -d %buildroot%python_sitelibdir/%oname
export PYTHONPATH=%buildroot%python_sitelibdir
%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html
cp -fR pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/testing

%files doc
%doc examples html
%doc docs/*.txt

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/testing

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/testing
%endif

%changelog
* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.0-alt2
- Updated to upstream release version 4.6.0.

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150320
- New snapshot

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150224
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20141007
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20140507
- Version 4.6.0

* Mon Oct 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3.git20131024
- Moved all tests into tests subpackage

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131024
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130329
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130329
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130102
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120905
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120331
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20111221.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20111221
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110914
- Version 4.0.1

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Fri Oct 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.svn20110127
- Version 3.6.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.svn20101105
- Version 3.5.1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20100714
- Version 3.4.1

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted tests into separate package
- Added pickles package

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.3
- Rebuilt with new NumPy

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929.1
- Extracted documentation into separate package

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090929
- Version 3.2.1

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus (thnx Valery Pipin)

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-2
- Fixed missing setupdocs BR

* Fri Jun 12 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.1.0-1
- Updated

* Tue Jan 27 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-2
- Fixed permissions for ctraits.so and _speedups.so
- Fixed license after confirming from upstream

* Sun Dec 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.2-1
- Initial package
