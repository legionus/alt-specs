Name: warzone2100
Version: 3.2.3
Release: alt1.1

Summary: Warzone 2100 Resurrection Project (RTS 3D game)
License: GPLv2+ and CC-BY-SA
Group: Games/Strategy

Url: http://wz2100.net/
# https://github.com/Warzone2100/warzone2100.git
Source: %name-%version.tar
#Source1: http://www.deviantart.com/download/92153956/Warzone_2100_Tango_Icon_by_Unit66.zip
Source1: Warzone_2100_Tango_Icon_by_Unit66.tar
# Regenerate it for each version by running following command on release tag:
# ./build_tools/autorevision -t sh -o autorevision.cache > autorevision-$version.cache
Source2: autorevision-%version.cache

BuildRequires: /proc
BuildRequires: qt5-base-devel qt5-3d-devel qt5-script-devel qt5-x11extras-devel openssl-devel
BuildRequires: elfutils fontconfig fontconfig-devel gnu-config libGL-devel libGLU-devel libX11-devel libXrandr-devel libXrender-devel libfreetype-devel libogg-devel libpng-devel libstdc++-devel pkg-config python-base texlive-latex-base xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: asciidoc-a2x flex gcc-c++ imake libSDL2-devel libfribidi-devel libglew-devel libopenal-devel libphysfs-devel libtheora-devel libvorbis-devel unzip xorg-cf-files zip

# 'zip -T' called in build process needs unzip to work...

Requires: %name-gamedata = %version

%description
Warzone 2100 is a real-time strategy game. Although comparable to Earth 2150
in many significant respects, it does contain aspects that are unique. These
include various radar technologies and a greater focus on artillery and
counter-battery technologies.

%package gamedata
Summary: Game data for warzone2100
Group: Games/Strategy
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description gamedata
Game data for warzone2100.

%prep
%setup -a 1
cp %SOURCE2 ./src/autorevision.cache

%build
./autogen.sh
%configure --with-distributor="ALT Linux"
%make_build

%install
%makeinstall_std
install -d %buildroot%_pixmapsdir
install -m644 icons/warzone2100.png %buildroot%_pixmapsdir
install -pD -m644 warzone2100_48x48.png %buildroot%_liconsdir/warzone2100.png
install -pD -m644 warzone2100_32x32.png %buildroot%_niconsdir/warzone2100.png
install -pD -m644 warzone2100_16x16.png %buildroot%_miconsdir/warzone2100.png

%find_lang warzone2100

%files -f warzone2100.lang
%doc COPYING* README.md
%exclude /usr/share/doc
%_bindir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%exclude %_iconsdir/warzone2100.png
%_pixmapsdir/*
%_desktopdir/*
%_man6dir/*

%files gamedata
%_datadir/warzone2100

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.2.3-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.3-alt1
- Updated to upstream version 3.2.3.

* Wed Jan 30 2013 Denis Smirnov <mithraen@altlinux.ru> 3.1.0-alt1
- 3.1.0
- build from git

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 2.3.9-alt1
- 2.3.9

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 2.3.8-alt1
- 2.3.8

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 2.3.7-alt2
- Build with new libphysfs.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 2.3.7-alt1
- 2.3.7

* Tue Nov 30 2010 Victor Forsiuk <force@altlinux.org> 2.3.6-alt1
- 2.3.6

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 2.3.5-alt1
- 2.3.5

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 2.3.4-alt1
- 2.3.4

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 2.3.3-alt1
- 2.3.3

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue May 25 2010 Victor Forsiuk <force@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Nov 14 2009 Victor Forsyuk <force@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Dec 22 2008 Victor Forsyuk <force@altlinux.org> 2.1.0-alt1
- 2.1.0
- Split (huge!) game data to noarch package.

* Tue Jan 22 2008 Victor Forsyuk <force@altlinux.org> 2.0.10-alt1
- 2.0.10

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Thu Apr 05 2007 Victor Forsyuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 2.0.5-alt2
- Fix to build for 64 bit.

* Fri Dec 29 2006 Victor Forsyuk <force@altlinux.org> 2.0.5-alt1
- 2.0.5
- New URL.
- Refresh buildrequires.
- More informative summary and description.

* Wed Nov 16 2005 Anton Farygin <rider@altlinux.ru> 2.0.2.3-alt1
- new version

* Fri Sep 02 2005 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- first build for Sisyphus
