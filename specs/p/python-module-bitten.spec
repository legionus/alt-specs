%def_without M24

%if_with M24
%define release alt0.M24.1
%else
%define release alt2
%endif

%define version 0.5.3
%setup_python_module bitten

Name: %packagename
Version: %version
Release: %release.1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Distributed continuous integration system
License: BSD
Group: Development/Python
Url: http://bitten.cmlenz.net/

Source: http://heanet.dl.sourceforge.net/sourceforge/%modulename/Bitten-%version.tar.bz2
Patch0: bitten-0.5-alt-unzip.patch

BuildArch: noarch
BuildPreReq: rpm-build-python >= 0.27
BuildRequires: python-module-setuptools

Requires: trac >= 0.9.3
Requires: python-module-setuptools
Requires: python%__python_version(bz2)

%description
Bitten is a simple distributed continuous integration system that not only
coordinates builds across multiple machines, but also collects software
metrics generated by builds, to enable feedback and reporting about
the progress of a software project.
It builds on Trac to provide an integrated web-based user interface.

%prep
%setup -q -n Bitten-%version
%patch0 -p0

%build
%__python setup.py build

%install
mkdir -p %buildroot%python_sitelibdir
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES
echo Bitten-%version-py%__python_version.egg > %buildroot%python_sitelibdir/%modulename.pth

# workaround for failed test install
install -d -m755 $RPM_BUILD_ROOT%python_sitelibdir/Bitten-%version-py%__python_version.egg/bitten/trac_ext/tests
install -m 644 -D bitten/trac_ext/tests/* \
	$RPM_BUILD_ROOT%python_sitelibdir/Bitten-%version-py%__python_version.egg/bitten/trac_ext/tests/

find %buildroot%python_sitelibdir/Bitten-%version-py%__python_version.egg -type d | \
	sed -e "s,^%buildroot,%dir ,g" >> INSTALLED_FILES
	
%files -f INSTALLED_FILES
%doc COPYING ChangeLog README.txt
%python_sitelibdir/%modulename.pth
%python_sitelibdir/Bitten-%version-py%__python_version.egg/bitten/trac_ext/tests/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.5.3-alt1.1
- Rebuilt with python-2.5.

* Mon Jun 19 2006 Grigory Batalov <bga@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Tue Feb 28 2006 Grigory Batalov <bga@altlinux.ru> 0.5.2-alt0.M24.1
- 0.5.2
- Call python as %%__python
- Backport to Master 2.4

* Thu Dec 29 2005 Grigory Batalov <bga@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux
