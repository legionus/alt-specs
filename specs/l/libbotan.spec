%define _unpackaged_files_terminate_build 1

Name: libbotan
Version: 2.7.0
Release: alt1

Summary: A C++ Crypto Library
License: BSD
Group: System/Libraries

Url: http://botan.randombit.net

# https://github.com/randombit/botan.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: bzlib-devel gcc-c++ libssl-devel zlib-devel
BuildRequires: python2.7(json)
BuildRequires: liblzma-devel
BuildRequires: boost-complete

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %EVR
Conflicts: libbotan1.11-devel

%description devel
Headers for building software that uses %name

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%package -n python-module-botan
Summary: Python extensions for botan
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-botan
Python extensions for botan

%package -n python3-module-botan
Summary: Python extensions for botan
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-botan
Python extensions for botan

%prep
%setup

%build
./configure.py --prefix=%prefix \
	--libdir=%_libdir \
	--docdir=%_defaultdocdir \
	--includedir=%_includedir \
	--disable-static-library \
	--with-bzip2 \
	--with-lzma \
	--with-zlib \
	--with-boost \
	--with-openssl \
	--with-python-version=%_python_version,%_python3_version

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc readme.rst
%doc %_defaultdocdir/botan-%version

%files -n python-module-botan
%python_sitelibdir/*

%files -n python3-module-botan
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*

%changelog
* Tue Sep 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.0-alt1
- Updated to upstream version 2.7.0.

* Tue Jun 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.17-alt1.1
- Rebuild for aarch64.

* Tue Apr 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.17-alt1
- Updated to upstream version 1.10.17.
- Fixed pkg-config file.

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 1.10.9-alt1
- New version
- Rebuilt for gcc5 C++11 ABI

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.5-alt1
- Version 1.10.5

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.8.10-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt2.1
- Rebuilt with gmp 5.0.5

* Wed Mar 30 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt2
- Add build dependency on zlib-devel for fix building.

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.10-alt1
- Initial build for Sisyphus.

