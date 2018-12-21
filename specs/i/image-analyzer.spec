# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: image-analyzer
Version: 3.2.0
Release: alt1
Summary: Simple Gtk+ application that displays tree structure of disc image
Summary(ru_RU.UTF-8): Простое GTK+ приложение для просмотра структуры образа диска
License: GPLv2+
Group: Emulators
Url: http://cdemu.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: cmake intltool

Buildarch: noarch

%description
Image Analyzer is a simple Gtk+ application that displays tree structure of disc
image created by libMirage.

It is mostly intended as a demonstration of libMirage API use, although it can
be also used to verify that an image is correctly handled by libMirage.

%description -l ru_RU.UTF-8
Image Analyzer представляет собой простое Gtk+ приложениеn для просмотра структуры
образов созданных с помощью libMirage.

Он в основном предназначен для демонстрации того, как использовать API
libMirage, тем не менее он может также использоваться для того, чтобы проверить, 
корректно ли обрабатывается образ libMirage.

%prep
%setup

#fix PATH to python3
sed 's|/usr/bin/env python3|/usr/bin/python3|' -i src/%name

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS COPYING
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*.svg

%changelog
* Mon Jul 30 2018 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1
- new version (3.2.0) with rpmgs script

* Thu Aug 03 2017 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- new version (3.1.0) with rpmgs script

* Fri Oct 14 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- New version.

* Tue Sep 06 2016 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus.
