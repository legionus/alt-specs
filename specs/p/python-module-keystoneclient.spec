%define oname keystoneclient


Name:       python-module-%oname
Version:    3.17.0
Release:    alt1
Summary:    Client library for OpenStack Identity API
License:    Apache-2.0
Group:      Development/Python
Url:        http://docs.openstack.org/developer/python-%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0

# doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-fixtures >= 3.0.0

BuildRequires: python-module-requests-mock >= 1.1


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.1

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-lxml >= 3.4.1
BuildRequires: python3-module-fixtures >= 3.0.0

BuildRequires: python3-module-requests-mock >= 1.1

%description
Client library and command line utility for interacting with Openstack
Identity API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Client library for OpenStack Identity API
Group: Development/Python3

%description -n python3-module-%oname
Client library and command line utility for interacting with Openstack
Identity API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack Identity API Client
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%prepare_sphinx doc/source

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

python3 setup.py build_sphinx
rm -f doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE doc/build/html

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 3.17.0-alt1
- Updated to 3.17.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0
- The `keystone` CLI has been removed, using the `openstack` CLI is recommended

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2
- add python3 package

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- New build for ALT (based on Fedora 0.9.0-2.fc21.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.2-alt1
- Initial release for Sisyphus (based on Fedora)

