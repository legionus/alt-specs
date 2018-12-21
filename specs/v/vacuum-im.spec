# -*- coding: latin-1; mode: rpm-spec -*-

%define sname vacuum

Name: %sname-im
Version: 1.2.5
Release: alt1

Summary: Crossplatform Jabber/XMPP client
License: GPL3
Group: Networking/Instant messaging
Url: http://www.vacuum-im.org
Source: %name-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Sun May 23 2010 (-bi)
BuildRequires: gcc-c++ libX11-devel phonon-devel libXScrnSaver-devel

%description
Crossplatform Jabber/XMPP client

%prep
%setup -n %name-%version

%build
qmake-qt4  INSTALL_PREFIX=%_prefix INSTALL_APP_DIR=%name INSTALL_LIB_DIR=%_lib -recursive vacuum.pro
make

%install
make install INSTALL_ROOT=%buildroot
sed  "s/Exec=%sname/Exec=%name/;s/Icon=%sname/Icon=%name/" %buildroot%_desktopdir/%sname.desktop > %buildroot%_desktopdir/%name.desktop
mv %buildroot%_pixmapsdir/%sname.png %buildroot%_pixmapsdir/%name.png
mv %buildroot%_bindir/%sname %buildroot%_bindir/%name
# Copyright.txt say "You may not repackage them and redistribute them with other smiles without my permission." and another smiles pack (tasha) included in distribution.
rm -rf %buildroot%_datadir/%name/resources/emoticons/kolobok*

%files
%doc AUTHORS CHANGELOG COPYING README TRANSLATORS
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_libdir/%name
%_libdir/lib*.so.*
%_libdir/libvacuumutils.so
%_pixmapsdir/%name.png

%doc README CHANGELOG AUTHORS TRANSLATORS

%changelog
* Fri Jun 26 2015 Ilya Mashkin <oddity@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon Mar 31 2014 Ilya Mashkin <oddity@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Aug  3 2012 Terechkov Evgenii <evg@altlinux.org> 1.2.0-alt1
- 1.2.0 (ALT#27591)

* Sat Jan 28 2012 Terechkov Evgenii <evg@altlinux.org> 1.1.2-alt1
- 1.1.2 (ALT#26867)

* Mon Sep  5 2011 Terechkov Evgenii <evg@altlinux.org> 1.1.1-alt1
- 1.1.1 (ALT#26234)

* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2
- fix build

* Sat Mar 19 2011 Terechkov Evgenii <evg@altlinux.org> 1.1.0-alt1
- 1.1.0

* Mon Jul 26 2010 Terechkov Evgenii <evg@altlinux.ru> 1.0.2-alt3
- Fix build with qt4.7

* Sun May 23 2010 Terechkov Evgenii <evg@altlinux.ru> 1.0.2-alt2
- Fix build with new phonon-devel

* Tue May  4 2010 Terechkov Evgenii <evg@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Mar 20 2010 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus
