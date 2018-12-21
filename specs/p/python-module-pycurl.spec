%define oname pycurl
%define oversion %(echo %version | sed -e "s|\\.|_|g")

%def_with python3

Name: python-module-%oname
Version: 7.43.0.2
Release: alt1

Summary: Python bindings to libcurl

Group: Development/Python
License: LGPL
Url: http://pycurl.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module %oname

# Source-url: https://github.com/pycurl/pycurl/archive/REL_%oversion.tar.gz
Source: %modulename-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils pkg-config python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: libcurl-devel libssl-devel python-devel python3-devel rpm-build-python3

#BuildRequires: libcurl-devel libssh2-devel python-devel

#BuildPreReq: libssl-devel libidn-devel zlib-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
%endif

%description
This module provides the Python bindings to libcurl.

%package -n python3-module-%oname
Summary: Python bindings to libcurl
Group: Development/Python3

%description -n python3-module-%oname
This module provides the Python bindings to libcurl.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing

python setup.py docstrings
%python_build_debug

%if_with python3
pushd ../python3
python3 setup.py docstrings
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%python_sitelibdir/*
%_docdir/%modulename/

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.2-alt1
- new version 7.43.0.2 (with rpmrb script)

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.43.0.1-alt2
- NMU: rebuilt with openssl 1.1.

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 7.43.0.1-alt1
- new version 7.43.0.1 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.43.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 7.43.0-alt1
- new version (7.43.0) with rpmgs script

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.19.5.3-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 7.19.5.3-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 7.19.5.3-alt1
- new version 7.19.5.3 (with rpmrb script)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.5-alt1
- Version 7.19.5
- Added module for Python 3

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 7.19.3.1-alt1
- new version 7.19.3.1 (with rpmrb script)

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0.3-alt1
- Version 7.19.0.3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.2
- Rebuilt for debuginfo

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.1
- Fixed build

* Thu Dec 02 2010 Ivan Fedorov <ns@altlinux.org> 7.19.0-alt1
- 7.19.0

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.4-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 7.16.4-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 7.16.4-alt1
- new version 7.16.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16.1-alt1
- new version 7.16.1 (with rpmrb script)

* Sun Feb 04 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16-alt0.1cvs
- build from CVS 20070204

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 7.15.5.1-alt0.1
- initial build for ALT Linux Sisyphus
