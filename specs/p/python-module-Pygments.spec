%define oname Pygments

Name: python-module-Pygments
Version: 2.2.0
Release: alt2

Summary: Pygments is a syntax highlighting package written in Python
License: BSD
Group: Development/Python
Url: http://pygments.org/
BuildArch: noarch

Source: Pygments-%version.tar.gz

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-Pyrex
BuildRequires: python-module-docutils
BuildRequires: python-module-objects.inv
BuildRequires: python-module-alabaster
BuildRequires: python-module-html5lib
BuildRequires: time

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildPreReq: python3-module-docutils
BuildPreReq: python3-module-alabaster
BuildPreReq: python3-module-html5lib
BuildPreReq: python3-module-objects.inv


%description
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

%package -n python3-module-%oname
Summary: Pygments is a syntax highlighting package written in Python 3
Group: Development/Python

%description -n python3-module-%oname
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

%package -n python3-module-%oname-tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains tests for %name.

%package -n python3-module-%oname-doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch
%description -n python3-module-%oname-doc
This package contains documentation for %name.

%package -n python3-module-%oname-pickles
Summary: Pickles for %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname-pickles

This package contains pickles for %name.

%package tests
Summary: Tests for %name
Group: Development/Python
Requires: %name = %version-%release
AutoReq: yes, nopython

%description tests
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains tests for %name.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains documentation for %name.

%package pickles
Summary: Pickles for %name
Group: Development/Python
BuildArch: noarch

%description pickles
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains pickles for %name.

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -a . ../python3

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%make -C doc pickle
%make -C doc html

pushd ../python3
%python3_build
%make SPHINXBUILD='PYTHONPATH=.. py3_sphinx-build' -C doc pickle
%make SPHINXBUILD='PYTHONPATH=.. py3_sphinx-build' -C doc html
popd

%install
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/pygmentize %buildroot%_bindir/pygmentize3

%python_install

install -d %buildroot%_man1dir
install -d %buildroot%_docdir/%name

install -p -m644 AUTHORS CHANGES LICENSE TODO \
	%buildroot%_docdir/%name/
cp -fR doc/_build/html %buildroot%_docdir/%name/

install -p -m644 doc/pygmentize.1 %buildroot%_man1dir
cp -fR tests %buildroot%python_sitelibdir/pygments/
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/pygments/

pushd ../python3
install -d %buildroot%_docdir/python3-module-%oname/
cp -fR tests %buildroot%python3_sitelibdir/pygments/
rm %buildroot%python3_sitelibdir/pygments/tests/examplefiles/unicodedoc.py
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/pygments/
cp -fR doc/_build/html %buildroot%_docdir/python3-module-%oname/
popd

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/*
%exclude %_docdir/%name/html
%_bindir/pygmentize
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/pygments/tests
%_man1dir/*

%files tests
%python_sitelibdir/pygments/tests

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files pickles
%python_sitelibdir/*/pickle

%files -n python3-module-%oname
%_bindir/pygmentize3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/pygments/tests
%exclude %python3_sitelibdir/*/pickle

%files -n python3-module-%oname-tests
%python3_sitelibdir/pygments/tests

%files -n python3-module-%oname-doc
%doc %dir %_docdir/python3-module-%oname
%doc %_docdir/python3-module-%oname/html

%files -n python3-module-%oname-pickles
%python3_sitelibdir/*/pickle


%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- rebuild with python3.6

* Tue Jun 06 2017 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0
- Move "testing" lexer back to main package
- Introduce Python3 doc and pickle

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-3.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- VErsion 1.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Moved %_bindir/pygmentize for Python 3 into python3-module-%oname

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Rebuilt with python-module-sphinx-devel

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Rebuilt with updated macro %%prepare_sphinx

* Wed Feb 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added pickles package

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added documentation and tests

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with python 2.6

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus
