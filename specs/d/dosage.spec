# SPEC file for dosage package

Name:    dosage
Version: 2.15
Release: alt1

Summary: a commandline webcomic downloader and archiver

License: %mit
Group:   Other
URL:     https://github.com/wummel/dosage

BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Sep 10 2014
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings
BuildRequires: python-module-distribute python-module-google python-module-zope

%description
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip
of webcomic, or catch-up to the last strip downloaded, or
download a strip for a particular date/index (except if the
webcomic's site layout makes this impossible).

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc doc/changelog.txt doc/dosage.txt doc/README.txt
%_bindir/%name
%_man1dir/*
%python_sitelibdir/%{name}lib*
%python_sitelibdir/*egg-info
%python_sitelibdir/_dosage*

%changelog
* Wed Sep 10 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt1
- New version 2.15

* Wed Feb 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.12-alt1
- New version 2.12

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.7-alt1
- New version 2.7

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.5-alt1
- New version 2.5

* Sat Jun 29 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.4-alt1
- New version 2.4

* Sun Jun 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.3-alt1
- New version 2.3

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- New version 2.2

* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- Initial build for ALT Linux Sisyphus

