%define oname pyFltk
%define mname pyfltk
%define _python_egg_info %python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%define oversion 1.3.3.1

Name: python3-module-%mname
Version: 1.3.3.1
Release: alt1.1.qa1.1

Summary: Python 3 bindings for FLTK library

Group: Development/Python3
License: LGPL
Url: http://pyfltk.sourceforge.net

Source: http://prdownloads.sf.net/pyfltk/%oname-%oversion.tar.bz2
#Patch10: pyfltk-1.3.1rc1-alt-fix-platform.patch

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gcc-c++ libGL-devel libXext-devel libXft-devel
BuildRequires: libfltk-devel libjpeg-devel libpng-devel python3-devel
BuildRequires: libX11-devel libGLU-devel swig

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel
BuildPreReq: libXfixes-devel libXcursor-devel

%description
pyFLTK: Python Wrapper for the FLTK library.

GOALS:
o To wrap FLTK in Python
o To develop a parser to read Fluid's FL files and generate
  Python code.
o To port all programs in test/ to Python using pyFLTK

%prep
%setup -q -n %oname-%oversion
#patch10 -p2
rm -f python/fltk_wrap.*

%build
pushd python
python3 MakeSwig.py
popd
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/fltk
%python3_sitelibdir/pyFltk-*.egg-info
%doc CHANGES README TODO

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3.1-alt1.1.qa1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Apr 27 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.3.3.1-alt1.1.qa1
- Rebuilt with libfltk13-1.3.3-alt1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.3.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 24 2016 Denis Medvedev <nbr@altlinux.org> 1.3.3.1-alt1
- Imported new sources 1.3.3.1_py3

* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2rc1-alt2
- Fixed build

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2rc1-alt1
- Version 1.3.2rc1

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1rc1-alt2.1
- Fixed build

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1rc1-alt2
- Rebuilt with new libfltk

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3.1rc1-alt1.1
- Rebuild with Python-3.3

* Tue May 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1rc1-alt1
- Built for Python 3

* Tue May 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1rc1-alt1
- Version 1.3.1rc1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0rc1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0rc1-alt2.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0rc1-alt2
- Rebuilt with FLTK 1.3.0.r8575

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0rc1-alt1
- Version 1.3.0rc1

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2rel-alt3.3
- Added libGLU-devel into build requirements

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2rel-alt3.2
- Fixed build

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2rel-alt3.1
- Rebuilt with python 2.6

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2rel-alt3
- update buildreqs

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2rel-alt2
- cleanup spec, update buildreqs
- fix build on x86_64

* Tue Feb 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.2rel-alt1
- new version (1.1.2)

* Mon Aug 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.2rc2-alt1
- new version (1.1.2rc2)
- update buildreq

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- new version (1.1)

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1b3-alt2
- rebuild with python 2.4

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.1b3-alt1
- first build for ALT Linux Sisyphus
