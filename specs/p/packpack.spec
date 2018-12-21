Name: packpack
Version: 1.0
Release: alt2

Summary: Simple tool to build RPM and Debian packages from git repository

Url: https://github.com/packpack/packpack
License: BSD
Group: Development/Other

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/packpack/packpack/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: docker-ce

BuildArch: noarch

%description
PackPack is a simple tool to build RPM and Debian packages
from git repository using Docker:

 * Fast reproducible builds using Docker containers
 * Semantic versioning based on annotated git tags
 * Support for all major Linux distributions as targets

%prep
%setup
%__subst "s|echi|echo|" packpack

%build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name
%_datadir/%name/
#_man1dir/%name.*

%changelog
* Mon Nov 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix docker requires

* Mon Jan 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
