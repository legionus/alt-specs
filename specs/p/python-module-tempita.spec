%define oname tempita

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1.hg20131219.1.2
Summary: A very small text templating language
License: MIT
Group: Development/Python
Url: http://pythonpaste.org/tempita/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone http://bitbucket.org/ianb/tempita
Source: Tempita-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%`` substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.

%if_with python3
%package -n python3-module-%oname
Summary: A very small text templating language (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%`` substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%python3_build
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
%doc docs/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/*
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.3-alt1.hg20131219.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt1.hg20131219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1.hg20131219.1
- NMU: Use buildreq for BR.

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.hg20131219
- Version 0.5.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.1-alt2.hg20110828.1
- Rebuild with Python-3.3

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.hg20110828
- Added module for Python 3

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.hg20110828
- Version 0.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.hg20101221.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.hg20101221
- New snapshot

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.hg20100914
- Version 0.5

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.svn20090420.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.svn20090420
- Initial build for Sisyphus

