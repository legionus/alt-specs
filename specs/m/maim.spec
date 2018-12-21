Name: maim
Version:  5.5.2
Release: alt1

Summary:  maim (make image) takes screenshots of your desktop.
License: GPLv3
Group: Graphics
Url: https://github.com/naelstrof/maim

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libslop-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel libjpeg-devel
BuildRequires: libXrandr-devel libXfixes-devel libXcomposite-devel libglvnd-devel
BuildRequires: libicu-devel libXext-devel libglm-devel

%description
maim (make image) takes screenshots of your desktop. It has options to take only
a region, and relies on slop to query for regions. maim is supposed to be
an improved scrot.

Features:

 * Takes screenshots of your desktop, and saves it in png or jpg format.
 * Takes screenshots predetermined regions or windows, useful for automation.
 * Allows a users to select a region, or window, before taking a screenshot
   on the fly.
 * Blends the system cursor to the screenshot. screenshot with cursor
 * Masks off-screen pixels to be transparent or black.
 * Maim cleanly pipes screenshots directly to standard output (unless otherwise
   specified). Allowing for command chaining.
 * Maim supports anything slop does, even selection shaders!

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc COPYING README.md

%changelog
* Wed Oct 11 2018 Pavel Skrylev <majioa@altlinux.org> 5.5.2-alt1
- Bump to 5.5.2 with slop support.

* Fri Jun 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.41-alt1
- initial build for ALT Linux Sisyphus

* Fri Jun 26 2015 nemysis@gmx.ch
- Update to 3.3.41, no changelog entry
- Change Source0 Web URL, to have right maim-3.3.41.tar.gz
- Add BuildRequires for cmake and gengetopt
- Add BuildRoot
- Use %%{name} instead of maim
- Switch to manual installation, because in Source isn't install command
- Add Documentation
- Add %%changelog
* Mon Oct 20 2014 rneuhauser@suse.cz
- maim-2.3.17
* Fri Oct 17 2014 rneuhauser@suse.cz
- maim-2.2.13
