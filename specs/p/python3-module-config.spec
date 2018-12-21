%define _unpackaged_files_terminate_build 1
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: python3-tools rpm-build-python3 time

#BuildRequires: python3-tools
BuildRequires(pre): rpm-build-python3
%define oldname python-module-config
%define packagename python-module-config

Summary: a module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module.
Name: python3-module-config
Version: 0.3.9
Release: alt2
Source0: config-%version.tar.gz
License: GPL
Group: Development/Python
URL: http://www.red-dove.com/python_config.html
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

#BuildRequires: python3-module-setuptools

%description
A module for configuring Python programs which aims to offer more power and flexibility than the existing ConfigParser module. 
Python programs which are designed as a hierarchy of components can use config to configure their various components in a uniform way.

%prep
%setup  -q -n config-%version

%build
python3-2to3 -w .
python3-2to3 -w -d .
%python3_build

%install
%python3_install

%files
%doc README.txt LICENSE
%python3_sitelibdir/config.*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/config-*.egg-info

%changelog
* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.9-alt2
- Don't depend on the python3's minor version during build
  (2to3-3.3 -> python3-2to3).
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1
- Initial build for Sisyphus

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt2.1.1
- python3 copycat import

