%def_without qt4

Name: gimagereader
Version: 3.3.0
Release: alt1

Summary: A graphical GTK frontend to tesseract-ocr

License: GPLv3+
Group: Office
Url: https://github.com/manisandro/gImageReader

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO: https://github.com/manisandro/gImageReader/archive/v%version.tar.gz
Source: http://sourceforge.net/projects/gimagereader/files/%version/%name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake intltool gcc-c++
BuildRequires: libgomp-devel libjson-glib-devel libsane-devel libxml++2-devel libleptonica-devel libpcre-devel libexpat-devel libdrm-devel libpodofo-devel libdjvu-devel libzip-devel libuuid-devel tesseract-devel

BuildRequires: python3 python3-module-pygobject3

# something wrong
# Package 'xrandr', required by 'GDK', not found
#BuildPreReq: libdrm-devel libXdmcp-devel libXdamage-devel libXxf86vm-devel libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel libXcomposite-devel wayland-protocols libxkbcommon-devel

# need pkgconfig from 3.04 and above
BuildRequires: tesseract-devel >= 3.04.01

# gtk
BuildRequires: libgtksourceviewmm3-devel libpoppler-glib-devel
BuildRequires: libgtkspellmm3-devel >= 3.0.5

%if_with qt4
BuildRequires: libqt4-devel libqtspell-qt4-devel libpoppler-qt4-devel
%endif

# qt5
BuildRequires: libqtspell-qt5-devel libpoppler-qt5-devel qt5-base-devel libquazip-qt5-devel libquazip-qt5-devel qt5-imageformats

# for compatibility
Requires: %name-gtk

%description
gImageReader is a simple Gtk front-end to tesseract. Features include:
 - Automatic page layout detection
 - User can manually define and adjust recognition regions
 - Import images from disk, scanning devices, clipboard and screenshots
 - Supports multipage PDF documents
 - Recognized text displayed directly next to the image
 - Editing of output text, including search/replace and removing line breaks
 - Spellchecking for output text (if corresponding dictionary installed)

%package gtk
Group: Office
Summary: A Gtk+ front-end to tesseract-ocr
Requires: %name-common = %version-%release
Obsoletes: %name < 2.94

%description gtk
gImageReader is a simple front-end to tesseract. Features include:
 - Automatic page layout detection
 - User can manually define and adjust recognition regions
 - Import images from disk, scanning devices, clipboard and screenshots
 - Supports multipage PDF documents
 - Recognized text displayed directly next to the image
 - Editing of output text, including search/replace and removing line breaks
 - Spellchecking for output text (if corresponding dictionary installed)
This package contains the Gtk+ front-end.

%package qt5
Group: Office
Summary: A Qt 5 front-end to tesseract-ocr
Requires: %name-common = %version-%release

%description qt5
gImageReader is a simple front-end to tesseract. Features include:
 - Automatic page layout detection
 - User can manually define and adjust recognition regions
 - Import images from disk, scanning devices, clipboard and screenshots
 - Supports multipage PDF documents
 - Recognized text displayed directly next to the image
 - Editing of output text, including search/replace and removing line breaks
 - Spellchecking for output text (if corresponding dictionary installed)
This package contains the Qt front-end.

%if_with qt4
%package qt4
Group: Office
Summary: A Qt4 front-end to tesseract-ocr
Requires: %name-common = %version-%release

%description qt4
gImageReader is a simple front-end to tesseract. Features include:
 - Automatic page layout detection
 - User can manually define and adjust recognition regions
 - Import images from disk, scanning devices, clipboard and screenshots
 - Supports multipage PDF documents
 - Recognized text displayed directly next to the image
 - Editing of output text, including search/replace and removing line breaks
 - Spellchecking for output text (if corresponding dictionary installed)
This package contains the Qt front-end.
%endif

%package common
Group: Office
Summary: Common files for %name
BuildArch: noarch
Conflicts: %name < 3.1.2
Requires: iso-codes


%description common
Common files for %name.

%prep
%setup

%build
%cmake -DINTERFACE_TYPE=gtk -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%_docdir/%name-common"
%cmake_build
mv BUILD build-gtk

%if_with qt4
%cmake -DINTERFACE_TYPE=qt4 -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%_docdir/%name-common"
%cmake_build
mv BUILD build-qt4
%endif

%cmake -DINTERFACE_TYPE=qt5 -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%_docdir/%name-common"
%cmake_build
mv BUILD build-qt5

%install
rm -rf BUILD
cp -al build-gtk BUILD
%cmakeinstall_std

%if_with qt4
rm -rf BUILD
cp -al build-qt4 BUILD
%cmakeinstall_std
%endif

rm -rf BUILD
cp -al build-qt5 BUILD
%cmakeinstall_std

%find_lang %name
rm -rfv %_datadir/locale/sr_Cyrl/ %_datadir/locale/sr_Latn/

# make link to old base command
ln -s %name-gtk %buildroot%_bindir/%name


%files common -f %name.lang
%doc COPYING
%doc AUTHORS README.md
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%doc %_docdir/%name-common/manual*.html

%files gtk
%_bindir/%name-gtk
%_datadir/metainfo/%name-gtk.appdata.xml
%_desktopdir/%name-gtk.desktop
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml

%if_with qt4
%files qt4
%_bindir/%name-qt4
#_datadir/appdata/%name-qt4.appdata.xml
%_desktopdir/%name-qt4.desktop
%endif

%files qt5
%_bindir/%name-qt5
%_datadir/metainfo/%name-qt5.appdata.xml
%_desktopdir/%name-qt5.desktop

%files
%_bindir/%name

%changelog
* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- new version 3.3.0 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2.99-alt3
- rebuild with podofo 0.9.6

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2.99-alt2
- drop ccmake and git-core buildreqs

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2.99-alt1
- new version 3.2.99 (with rpmrb script)

* Thu Nov 02 2017 Andrew Savchenko <bircoph@altlinux.org> 3.2.3-alt2
- Fix OpenMP detection: use native cmake's find_package
- C++11 exceptions are not yet implemented in lcc.

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.3-alt1
- new version 3.2.3 (with rpmrb script)

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt2
- rebuild with podofo 0.9.5

* Sat Feb 18 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)

* Mon Jan 02 2017 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- new version 3.2.0 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.1.91-alt1
- new version 3.1.91 (with rpmrb script)

* Mon Aug 17 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt3
- fix inter package requires

* Sun Aug 16 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt2
- build with tesseract 3.04

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)
- split into -gtk, -qt4, -qt5 package

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.93-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 2.93-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Sandro Mani <manisandro@gmail.com> - 2.93-4
- Rebuild (tesseract)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Sandro Mani <manisandro@gmail.com> - 2.93-2
- Workaround rhbz #1065695

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 2.93-1
- Update to 2.93

* Wed Mar 19 2014 Sandro Mani <manisandro@gmail.com> - 2.92-1
- Update to 2.92

* Thu Feb 20 2014 Sandro Mani <manisandro@gmail.com> - 2.91-1
- Update to 2.91

* Sat Feb 15 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.2git20140216
- Update to newer 2.91 pre, work around crash at exit

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.1
- Update to 2.91 pre

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.90-3
- Require hicolor-icon-theme
- Add missing icon theme scriptlets

* Wed Feb 12 2014 Sandro Mani <manisandro@gmail.com> - 2.90-2
- Add appdata file

* Tue Feb 11 2014 Sandro Mani <manisandro@gmail.com> - 2.90-1
- Initial package.
