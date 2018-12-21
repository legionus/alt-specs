# TODO: use external wxsqlite3 (from altautoimports)
Name: myrulib
Version: 0.29.16.git0fe54bf16
Release: alt2

Summary: Tool for maintaining fb2 files collection

Url: http://myrulib.lintest.ru/
Source: %name-%version.tar
License: GPL

# Source-git: https://github.com/lintest/myrulib.git
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Group: Office

# Automatically added by buildreq on Sat Feb 02 2013
# optimized out: fontconfig gnu-config libgdk-pixbuf libstdc++-devel libsystemd-daemon libwayland-client libwayland-server pkg-config
BuildRequires: bzlib-devel gcc-c++ libexpat-devel libsqlite3-devel libwxGTK-devel libxml2-devel

#BuildRequires: libsqlite3-devel >= 3.7.17
BuildRequires: libwxsqlite3-devel >= 3.0.3

BuildRequires: bakefile

%description
Tool for maintaining home library, contaning fb2 files. Supports search,
export and so on.

%prep
%setup
# assure we do not build it
rm -rf 3rdparty/{sqlite3,wxsqlite3}

# hack due search wxcode_gtk2u_wxsqlite3-2.8 but libwxsql3 contains wxcode_gtk2_wxsqlite3-2.8
subst 's|wx_temp="$wx_temp""u"|wx_temp="$wx_temp"|g' ./configure

%build
# note: checking for SQLITE_ENABLE_ICU support in system SQLite... no
# so we can't use --with-icu
%configure --with-expat \
    --without-strip \
    --without-sqlite --without-wxsqlite  --without-bzip2
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%makeinstall_std
mkdir -p %buildroot%_iconsdir/hicolor/32x32/apps/
install sources/MyRuLib/desktop/home-32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/myrulib.png
mkdir -p  %buildroot%_iconsdir/hicolor/64x64/apps/
install sources/MyRuLib/desktop/home-64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/myrulib.png
%find_lang %name

%files -f %name.lang
%_bindir/myrulib
%_desktopdir/myrulib.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/32x32/apps/myrulib.png
%_iconsdir/hicolor/48x48/apps/myrulib.png
%_iconsdir/hicolor/64x64/apps/myrulib.png

%changelog
* Sun Oct 11 2015 Vitaly Lipatov <lav@altlinux.ru> 0.29.16.git0fe54bf16-alt2
- Rebuilt for new gcc5 C++11 ABI

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 0.29.16.git0fe54bf16-alt1
- build from last git

* Sat Sep 28 2013 Vitaly Lipatov <lav@altlinux.ru> 0.29.16-alt1
- version 0.29.16
- fiw MSW database creation error
- fix FbExportDlg error
- update CREngine
- patch for CREngine
- change info.plist
- set default toolbar icon size
- fix settings dialog error

* Mon Mar 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.29.12-alt1
- version 0.29.12
- fix procedure: replace author
- trim title, authors, sequence when import files
- fix SQL error in sequence frame
- modify convert script: add user rate to database
- store <annotation> in FTS table
- read annotation when import books
- menu item: Select All

* Sat Feb 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.29.11-alt1
- build new version
- update buidreqs

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28.7-alt1.1
- Fixed build

* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.28.7-alt1
- new version

* Tue May 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.27.4-alt1
- new version

* Tue Nov 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.24.18-alt1
- new version
- upstream git used

* Mon Apr 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.21-alt1
- new version
- translations

* Mon Feb 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.19-alt1
- new version

* Tue Dec 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.17-alt1
- new version
- compilation flags added

* Wed Dec 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.16-alt1
- initial build

