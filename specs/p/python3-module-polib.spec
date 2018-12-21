%define oname polib

Name:		python3-module-%oname
Version:	1.0.5
Release:	alt1.1.2
Summary:	Manipulate, create, and modify gettext files
Group:		Development/Python
License:	BSD-like
Source:		%oname-%version.tar.gz
URL:		https://bitbucket.org/izi/polib
BuildArch:	noarch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools xz
BuildRequires: python3-module-coverage rpm-build-python3 time

#BuildRequires: ctags time
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-coverage

%py3_provides %oname

%description
polib is a library to manipulate, create, modify gettext files (pot, po
and mo files). You can load existing files, iterate through it's
entries, add, modify entries, comments or metadata, etc... or create new
po files from scratch.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
./runtests.sh

%files
%doc CHANGELOG *.rst
%python3_sitelibdir/*

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt1.1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus

