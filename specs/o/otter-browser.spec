# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     otter-browser
Version:  0.9.99.3
Release:  alt1

Summary:  Otter Browser aims to recreate the best aspects of the classic Opera (12.x) UI using Qt5
License:  GPL-3.0
Group:    Other
Url:      https://github.com/OtterBrowser/otter-browser

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)
#BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(hunspell)

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%doc CHANGELOG CONTRIBUTING.md COPYING README.md

%changelog
* Thu Sep 13 2018 Anton Midyukov <antohami@altlinux.org> 0.9.99.3-alt1
- new version 0.9.99.3

* Fri Jul 06 2018 Anton Midyukov <antohami@altlinux.org> 0.9.99.1-alt1.S1
- new version 0.9.99.1

* Thu Jun 07 2018 Anton Midyukov <antohami@altlinux.org> 0.9.99-alt1.S1
- new version 0.9.99

* Fri Mar 23 2018 Anton Midyukov <antohami@altlinux.org> 0.9.96-alt1.S1
- new version 0.9.96

* Fri Jan 05 2018 Anton Midyukov <antohami@altlinux.org> 0.9.94-alt1.S1
- Initial build for Sisyphus
