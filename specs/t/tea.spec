Name: tea
Version: 46.3.0
Release: alt1

Summary: Powerful text editor with many HTML editing and text processing functions

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Text tools
Url: http://semiletov.org/tea/

#Source: http://semiletov.org/tea/dloads/tea-%version.tar
# Source-url: https://github.com/psemiletov/tea-qt/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ zlib-devel libaspell-devel qt5-base-devel qt5-declarative-devel

%description
Tea is a useful and simple in use Qt-based editor for GNU/Linux and
FreeBSD, released under GPL.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
install -D bin/%name %buildroot%_bindir/%name
mkdir -p %buildroot%_pixmapsdir
cp icons/*.png %buildroot%_pixmapsdir/

mkdir -p %buildroot%_desktopdir
cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Tea
Comment=Tea is a small but powerful text editor
Comment[ru]=Tea - небольшой, но мощный текстовый редактор
Comment[ua]=Tea - малий, але дуже потужний текстовий редактор
TryExec=%name
Exec=%_bindir/%name
Icon=tea_icon_v2.png
Terminal=false
Type=Application
Categories=Application;Office
EOF

%find_lang %name

%files -f %name.lang
%_bindir/*
%doc AUTHORS ChangeLog NEWS README TODO
#%_datadir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop

%changelog
* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 46.3.0-alt1
- new version 46.3.0 (with rpmrb script)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 45.0.2-alt1
- new version (45.0.2) with rpmgs script
- build with Qt5

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 44.1.1-alt1
- new version 44.1.1 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 43.1.0-alt1
- new version 43.1.0 (with rpmrb script)

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 41.0.0-alt1
- new version 41.0.0 (with rpmrb script)

* Sat Apr 05 2014 Vitaly Lipatov <lav@altlinux.ru> 37.2.0-alt1
- new version 37.2.0 (with rpmrb script)

* Sat Mar 30 2013 Vitaly Lipatov <lav@altlinux.ru> 35.0.0-alt1
- new version 35.0.0 (with rpmrb script)

* Mon Jun 11 2012 Vitaly Lipatov <lav@altlinux.ru> 33.1.0-alt1
- new version 33.1.0 (with rpmrb script)

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 26.1.0-alt1
- new version 26.1.0 (with rpmrb script)

* Thu Aug 20 2009 Vitaly Lipatov <lav@altlinux.ru> 25.1.0-alt1
- new version 25.1.0 (with rpmrb script)

* Sun Apr 26 2009 Vitaly Lipatov <lav@altlinux.ru> 23.4.0-alt1
- new version 23.4.0 (with rpmrb script)

* Fri Mar 20 2009 Vitaly Lipatov <lav@altlinux.ru> 23.2.0-alt1
- new version 23.2.0 (build with Qt4)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 17.3.5-alt1
- new version 17.3.5 (with rpmrb script)

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 16.0.5-alt1
- new version 16.0.5 (with rpmrb script)
- change Url, Source

* Mon Nov 21 2005 Vitaly Lipatov <lav@altlinux.ru> 11.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Nov 11 2005 Michael Krylov <m.krylov@mail.ru>
- Update to 11.0.
- Add enable-chai rebuild option.
