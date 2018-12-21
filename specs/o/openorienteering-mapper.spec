%define _unpackaged_files_terminate_build 1

Name: openorienteering-mapper
Version: 0.8.3
Release: alt1

Summary: OpenOrienteering Mapper program for orienteering mapmaking
License: GPLv3
Group: Graphics

Url: http://www.openorienteering.org/apps/mapper/
#Source: https://github.com/OpenOrienteering/mapper.git
Source: %name-%version.tar

BuildRequires: ccmake
BuildRequires: doxygen
BuildRequires: gdal
BuildRequires: libcups-devel
BuildRequires: libgdal-devel
BuildRequires: libpolyclipping-devel
BuildRequires: libproj-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-sql-sqlite3
BuildRequires: qt5-tools-devel
BuildRequires: sqlite3
# for tests (github #1062)
BuildRequires: libproj-nad
BuildRequires: ctest

#brings gdal libs and licensing information for help menu
Requires: gdal
#provides owner for %%_iconsdir/hicolor subtree
Requires: icon-theme-hicolor
Requires: qt5-assistant

%description
 OpenOrienteering Mapper is an orienteering mapmaking program and provides a
 free alternative to the existing proprietary solution. Its main advantages
 compared to it are:
 Open Source: The program is completely free, every programmer can improve it.
 Cross-platform: The program works on Android, Windows, macOS and Linux.
While it is under continuous development and considered in beta state, it has
been used to produce maps for classical orienteering, MTBO and radio
orienteering races. All required functions for drawing maps are implemented and
the program works very stable. So it  can be considered ready for productive
use, although it is like always a good idea to keep backups of your files. We
are happy about feedback to the program.

%prep
%setup

#provide licensing information search path patterns specific for Altlinux
cp doc/licensing/fedora-licensing.cmake doc/licensing/altlinux-licensing.cmake
sed -i 's|doc/gdal-libs|gdal|g' doc/licensing/altlinux-licensing.cmake

#fix qt assistant search by default paths
sed -i 's|"assistant"|"assistant-qt5"|g' src/gui/util_gui.cpp

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name --with-qt

%check
pushd BUILD/test
make test
popd

%files -f %name.lang
%doc COPYING INSTALL.md README.md
%doc %_docdir/%name/
%_bindir/*
%_man1dir/*
%_datadir/%name/
%_desktopdir/*
%_datadir/mime/packages/*
%_iconsdir/hicolor/*/mimetypes/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Tue Nov 27 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.3-alt1
- New version
- Remove ubt

* Tue Aug 21 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.2-alt1
- New version

* Thu Apr 19 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.1-alt3
- Fix Qt Assistant search by default paths

* Fri Apr 13 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.1-alt2
- Rebuild with ubt

* Thu Mar 22 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.1-alt1
- Update upstream to 0.8.1

* Mon Feb 19 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.8.0-alt1
- Initial build
