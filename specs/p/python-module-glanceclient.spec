%define oname glanceclient

Name:    python-module-%oname
Version: 2.13.0
Release: alt1
Summary: Python API and CLI for OpenStack Glance

Group:   Development/Python
License: Apache-2.0
Url:     http://docs.openstack.org/developer/python-%oname
Source:  https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

Patch:   workaround-requests.patch

BuildArch: noarch

Requires: python-module-requests >= 2.12.0
%py_requires urllib3

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-keystoneauth1 >= 3.6.2
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-warlock >= 1.2.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-wrapt >= 1.7.0
BuildRequires: python-module-OpenSSL >= 17.1.0

BuildRequires: python-module-mock >= 2.0
BuildRequires: python-module-subunit python-module-subunit-tests
BuildRequires: python-module-os-client-config >= 1.28.0
BuildRequires: python-module-testrepository >= 0.0.18
BuildRequires: python-module-testtools >= 2.2.0
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-requests-mock >= 1.2.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-sphinxcontrib-apidoc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-keystoneauth1 >= 3.6.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-warlock >= 1.0.1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-wrapt >= 1.7.0
BuildRequires: python3-module-OpenSSL >= 17.1.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python API and CLI for OpenStack Glance
Group: Development/Python3
%py3_requires urllib3

%description -n python3-module-%oname
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Glance API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100 percent of the OpenStack Glance API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version
%patch -p1

# Remove bundled egg-info
rm -rf python_glanceclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/glance %buildroot%_bindir/glance.py2

pushd ../python3
%python3_install
popd


sphinx-build -b html doc/source doc/build/html
# generate man page
sphinx-build -b man doc/source man
install -p -D -m 644 man/glance.1 %buildroot%_man1dir/glance.1

%files
%doc README.rst
%doc LICENSE
%_bindir/glance.py2
%python_sitelibdir/*
%_man1dir/glance*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/glance
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.13.0-alt1
- 2.13.0

* Tue Oct 09 2018 Grigory Ustinov <grenka@altlinux.org> 2.12.1-alt1
- Updated to 2.12.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- add test packages

* Tue Feb 21 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- add patch for workaround requests >= 2.12

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- fix work with system urllib3

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 0.12.0-alt1
- First build for ALT (based on Fedora 0.12.0-1.fc20.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)

