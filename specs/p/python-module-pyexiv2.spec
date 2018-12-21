%define oname pyexiv2

Name: python-module-%oname
Version: 0.3.2
Release: alt3.bzr20120921.1

Summary: A python binding to exiv2, the C++ library for manipulation of EXIF and IPTC image metadata
License: GPLv2+
Group: Development/Python

%setup_python_module %oname

Url: http://tilloy.net/dev/pyexiv2/
Source0: http://launchpad.net/pyexiv2/0.3.x/0.3/+download/pyexiv2-%version.tar.bz2
Patch1: %oname-0.1.3-overridecxx.patch
Packager: Victor Forsiuk <force@altlinux.org>

# Automatically added by buildreq on Tue Jun 08 2010
BuildRequires: boost-python-devel flex gcc-c++ python-modules-email scons
BuildRequires: libexiv2-devel >= 0.19

%description
Pyexiv2 is a python binding to exiv2, the C++ library for manipulation of EXIF
and IPTC image metadata. It is a python module that allows your python scripts
to read and write metadata (EXIF, IPTC, thumbnail) embedded in image files
(JPEG, TIFF, ...).

It is designed as a high level interface to the functionalities offered by exiv2
(and is built on top of it). Using python's built-in data types and standard
modules, it provides easy manipulation of image metadata.

%prep
%setup -n %modulename-%version
%patch1 -p1

%build
scons -j %__nprocs CXXFLAGS="%optflags"

%install
# Why CXXFLAGS here?? scons will try to recompile sources when CXXFLAGS value
# differ from used for compilation...
scons install DESTDIR=%buildroot CXXFLAGS="%optflags"

%files
%python_sitelibdir/*
%doc doc/*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt3.bzr20120921.1
- NMU: rebuilt with boost-1.67.0

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 0.3.2-alt3.bzr20120921.0
- Rebuild with boost 1.65

* Thu Jul 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt3.bzr20120921
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.2-alt2.bzr20120921.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2.bzr20120921
- Snapshot from bzr

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.8
- Rebuilt with new exiv2

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.7
- Rebuilt with Boost 1.53.0

* Sun Jan 27 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1.6
- rebuilt against libexiv2.so.12

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.5
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.4
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.3
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.2
- Rebuilt with Boost 1.48.0

* Fri Nov 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1.1
- Rebuild with Python-2.7

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2
- built against libexiv2.so.11

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.2
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.1
- Rebuilt with Boost 1.46.1 and for debuginfo

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.1
- Rebuilt with Boost 1.45.0

* Tue Jun 08 2010 Victor Forsiuk <force@altlinux.org> 0.2.2-alt1
- 0.2.2

* Tue Jan 05 2010 Victor Forsyuk <force@altlinux.org> 0.1.3-alt1.2
- Rebuild with libexiv2.so.6.

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.1
- Rebuilt with python 2.6

* Sat Jul 25 2009 Victor Forsyuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3 (for libexiv2 0.18.x).

* Sat Nov 01 2008 Fr. Br. George <george@altlinux.ru> 0.1.2-alt1
- Initial build from scratch

