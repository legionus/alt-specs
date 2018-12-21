%define origname FIAT

%def_without new_package

Name:           python-module-fiat
Version:        1.6.0
Release:        alt2.dev.git20150429
Summary:        FInite element Automatic Tabulator
Group:          Development/Python
License:        LGPLv3+
URL:           http://fenicsproject.org/
BuildArch: noarch

# https://bitbucket.org/fenics-project/fiat.git
Source:        %origname-%version.tar


BuildRequires(pre): rpm-build-python
BuildRequires: python-devel texlive-latex-recommended
BuildRequires: /usr/bin/pdflatex tex(pdftex.def)

%setup_python_module %origname

%description
FIAT is a FInite element Automatic Tabulator.

%package new
Summary: New experimental FIAT package
Group: Development/Python
BuildArch: noarch
%setup_python_module %{origname}_NEW

%description new
FIAT is a FInite element Automatic Tabulator.

This is a new experimental FIAT package.

%package manual
Summary: Documentation for FIAT
Group: Documentation
BuildArch: noarch

%description manual
FIAT is a FInite element Automatic Tabulator.

This package contains documentation for FIAT.

%prep
%setup

%build
%python_build

pushd doc
pdflatex manual.tex
popd

%install
CFLAGS="%optflags" python setup.py install \
	--root=%buildroot --optimize=2

%if_with new_package
cp -fR %{origname}_NEW %buildroot%python_sitelibdir/
%endif

install -d %buildroot%_docdir/%origname
install -m644 doc/*.pdf %buildroot%_docdir/%origname

%files
%doc AUTHORS COPYING ChangeLog README
%python_sitelibdir/*
%if_with new_package
%exclude %python_sitelibdir/%{origname}_NEW
%endif

%if_with new_package
%files new
%python_sitelibdir/%{origname}_NEW
%endif

%files manual
%_docdir/%origname

%changelog
* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt2.dev.git20150429
- Updated build dependencies.

* Sat May 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev.git20150429
- Version 1.6.0dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20140730
- Version 1.4.0

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140214
- Version 1.3.0

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130411
- New snapshot

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.bzr20130108
- Version 1.1.0

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20121001
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20120610
- New snapshot

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20111207
- Rebuilt with updated NumPy

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20111207
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta.bzr20110811
- Version 1.0-beta

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.bzr20110625.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110625
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110223
- Version 0.9.9

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.bzr20101018
- New snapshot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.bzr20100701
- Version 0.9.2

* Mon Jul 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.bzr20100304.1
- Rebuilt

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.bzr20100304
- Version 0.9.1

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt4.bzr20091124
- New snapshot

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090831
- Snapshot 20090831

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090819
- New snapshot

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Build as noarch package

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
