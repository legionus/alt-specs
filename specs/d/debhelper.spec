Name: debhelper
Version: 9.20151005
Release: alt1

Summary: Tools for Debian Packages

License: GPLv2+
Group: System/Configuration/Packaging
Url: http://packages.debian.org/unstable/devel/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: ftp://ftp.debian.org/debian/pool/main/d/%name/%{name}_%version.tar.xz
Source: %{name}_%version.tar

BuildArch: noarch

# Automatically added by buildreq on Wed Jan 07 2009
BuildRequires: dpkg perl-Test-Pod po4a

%description
The packages contains helper utilities for Debian alien.

%prep
%setup -n %name

%build
make -f debian/rules build

%install
rm -f *{es,fr}.1
rm -f dh_testversion*
%makeinstall_std

#install -d -m 755 %buildroot

# autoscripts
#install -d -m 755 %buildroot%_datadir/debhelper/autoscripts
#install -m 644 autoscripts/* %buildroot%_datadir/debhelper/autoscripts

# perl modules
#install -d -m 755 %buildroot%perl_vendorlib/Debian/Debhelper
#install -m 644 Debian/Debhelper/* %buildroot%perl_vendorlib/Debian/Debhelper

# man pages
install -d -m 755 %buildroot%_man1dir/
install -d -m 755 %buildroot%_man7dir/
install -m 644 *.1 %buildroot%_man1dir/
install -m 644 *.7 %buildroot%_man7dir/

# binaries
install -d -m 755 %buildroot%_bindir
install -m 755 dh_*[^1-9] %buildroot%_bindir

%files
%doc doc debian/{changelog,copyright} examples/
%_bindir/*
%_datadir/%name/
%perl_vendorlib/Debian/
%_man1dir/*
%_man7dir/*

%changelog
* Thu Nov 05 2015 Vitaly Lipatov <lav@altlinux.ru> 9.20151005-alt1
- new version 9.20151005 (with rpmrb script)

* Wed Apr 23 2014 Fr. Br. George <george@altlinux.ru> 9.20140228-alt1
- Updated to 9.20140228 (fix build)

* Wed May 22 2013 Dmitry V. Levin <ldv@altlinux.org> 9.20130518-alt1
- Updated to 9.20130518 (fixes "find -perm" usage).

* Thu Sep 20 2012 Vitaly Lipatov <lav@altlinux.ru> 9.20120830-alt1
- new version 9.20120830 (with rpmrb script)

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 7.1.1-alt1
- new version 7.1.1 (with rpmrb script)
- update buildreq

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 7.0.16-alt1
- new version 7.0.16 (with rpmrb script)

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 6.0.2-alt1
- new version 6.0.2 (with rpmrb script)

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.44-alt1
- new version 5.0.44 (with rpmrb script)

* Sun Oct 08 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.40-alt0.1
- new version 5.0.40 (with rpmrb script)

* Tue Sep 19 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.37.3-alt0.1
- new version (5.0.37.3)
- fix URL
- switch to noarch
- add packager

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0.22-alt0.1
- initial build for ALT Linux Sisyphus

