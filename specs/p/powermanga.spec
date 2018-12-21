Name: powermanga
Version: 0.93.1
Release: alt1
Summary: Shoot them up with 3d graphics

License: %gpl3plus
Group: Games/Arcade

Url: http://linux.tlk.fr/games/Powermanga/
Source: %name-%version.tgz

Source100: %name.desktop

Source200: %name.16.png
Source201: %name.32.png
Source202: %name.48.png

Requires: %name-data

BuildPreReq: rpm-build-licenses

# Based on configure.ac
BuildRequires: libXxf86dga-devel libXext-devel
BuildRequires: libSDL-devel libSDL_mixer-devel
BuildPreReq: libpng-devel

%description
In this shoot them up with 3d graphics, you'll have to face and destroy
more than 60 different types of opponents. Nice musics, many weapons, and
a ton of surprises.

%package data
Summary: Data files for Powermanga
Group: Games/Arcade
BuildArch: noarch

%description data
This package contains data files for Powermanga (see %name package for
description). To play the game, you should install both %name and %name-data packages.

%prep
%setup

%build
%autoreconf
%add_optflags -DPNG_EXPORT_ENABLE=1
%configure \
	--mandir=%_man6dir \
	--enable-x11 \
	--with-x
%make scoredir=%_localstatedir/games

%install
%makeinstall_std gamesdir=%_bindir scoredir=%_localstatedir/games

install -Dpm 644 %SOURCE100 %buildroot/%_desktopdir/%name.desktop

install -Dpm 644 %SOURCE200 %buildroot/%_miconsdir/%name.png
install -Dpm 644 %SOURCE201 %buildroot/%_niconsdir/%name.png
install -Dpm 644 %SOURCE202 %buildroot/%_liconsdir/%name.png

%files
%doc README
%attr(0660, games, games) %_localstatedir/games/*
%attr(2711, root, games) %_bindir/%name
%_man6dir/*
%_desktopdir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%files data
%_datadir/games/%name

%changelog
* Sat Sep 24 2016 Fr. Br. George <george@altlinux.ru> 0.93.1-alt1
- Autobuild version bump to 0.93.1

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.92-alt1
- Version 0.92

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.90-alt3.1.qa1
- NMU: rebuilt for updated dependencies.

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.90-alt3.1
- Fixed build

* Sun Dec 28 2008 Alexey Rusakov <ktirf@altlinux.org> 0.90-alt3
- Removed deprecated stuff from the .desktop file.
- Removed no more needed post/postun scripts.
- Moved all game data to a separate noarch subpackage.

* Thu Dec 04 2008 Alexey Rusakov <ktirf@altlinux.org> 0.90-alt2
- Updated buildreqs (fixing the build after recent changes in X.org
  packages).
- Fix the license tag (%gpl3plus instead of a vague GPL).
- Removed %%__ macros.

* Wed Sep 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.90-alt1
- 0.90

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.78-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Oct 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.78-alt1
- 0.78

* Tue Apr 29 2003 Stanislav Ievlev <inger@altlinux.ru> 0.76-alt1
- 0.76

* Thu Oct 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.74-alt1
- 0.74

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 0.73-alt1.1
- rebuild with new XFree86
- added buildreq

* Wed Sep 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.73-alt1
- 0.73
- Updated patches
- Updated CFLAGS
- fixed permissions to score files

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.71c-alt2.1
- fixed suid/sgid permissions

* Sat Jun 9 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.71c-alt2
- Fixed permission for /var/lib/games/powermanga.hi

* Fri Jun 8 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.71c-alt1
- New version 0.71c
- Added some Mandrake Cooker patches

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Wed Dec 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.71-2mdk
- ix86 only.

* Tue Nov 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.71-1mdk
- mdk package
