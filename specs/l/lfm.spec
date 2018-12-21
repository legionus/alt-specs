Summary: Powerful file manager for the console
Name: lfm
Version: 3.1
Release: alt1%ubt
License: GPL
Group: Development/Python
URL: https://inigo.katxi.org/devel/lfm/
BuildArch: noarch

Source: %name-%version.tar
Patch1: %name-%version-alt-prefs.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: python3-devel

%description
Last File Manager is a simple but powerful file manager for the UNIX console.

%prep
%setup -q
%patch1 -p2

%build
export LC_ALL=en_US.UTF-8
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name-%version-*.egg-info
%python3_sitelibdir/%name
%_man1dir/%name.1*

%changelog
* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1%ubt
- Updated to upstream version 3.1.
- Added %%ubt macro to release.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.1
- Rebuilt with python 2.6

* Mon Mar 31 2008 Mikhail Pokidko <pma@altlinux.org> 2.0-alt1
- initial ALT build

