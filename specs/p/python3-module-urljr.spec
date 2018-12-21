%define _unpackaged_files_terminate_build 1
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base
BuildRequires: python3-tools rpm-build-python3 time

#BuildRequires: python3-tools
%define oldname python-module-urljr
Name: python3-module-urljr
Version: 1.0.1
Release: alt2

Summary: URL-related utilites

Group: Development/Python3
License: LGPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

%global modulename urljr
%global packagename python3-module-%{modulename}
BuildRequires(pre): rpm-build-python3

Source: http://openidenabled.com/files/python-openid/files/python-urljr-%version.tar.bz2

%description
URL-related utilites, including a common interface to HTTP fetchers for
PycURL and urllib2.

%prep
%setup -n python-%modulename-%version

%build
python3-2to3 -w -n .
python3-2to3 -w -d -n .
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Fri Apr  8 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2
- Don't depend on the python3's minor version during build
  (2to3-3.3 -> python3-2to3).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1.1
- python3 copycat import

