%define module_name scapy

Name: scapy
Version: 2.4.0
Release: alt1

Summary: Scapy is a powerful interactive packet manipulation program written in Python

Group: Networking/Other
License: GPL-3.0-only
Url: http://www.secdev.org/projects/scapy/

# Source-url: https://github.com/secdev/scapy/archive/v%version.zip
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch
Requires: python-base >= 2.5
Requires: python-module-scapy = %version-%release

Requires: tcpdump

BuildRequires: python-devel python-module-distribute

Requires: python-dev

%description
Scapy is a powerful interactive packet manipulation program.
It is able to forge or decode packets of a wide number of protocols,
send them on the wire, capture them, match requests and replies, and
much more.
It can easily handle most classical tasks like scanning, tracerouting,
probing, unit tests, attacks or network discovery.

%package -n python-module-%name
Summary: Python module for %name.
Group: Development/Python

%description -n python-module-%name
Powerful interactive packet manipulation python module scapy.

%prep
%setup

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/%name/arch/windows

%files
%_bindir/*scapy
%_man1dir/*

%files -n python-module-scapy
%python_sitelibdir/%name/
%python_sitelibdir/%name-*egg-info

%changelog
* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- cleanup spec, separate python module
- add tcpdump require

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Denis Klimov <zver@altlinux.org> 2.1.0-alt1
- new version
- using python macros in build and install sections
- format description

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0.10-alt1.1
- Rebuilt with python 2.6

* Thu Oct 16 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.0.10-alt1
- Migrating to version 2.0.0.10

* Fri Apr 25 2008 Mikhail Pokidko <pma@altlinux.org> 1.1.1-alt1
- Initial ALT build

