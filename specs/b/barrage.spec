Summary: Kill and destroy as many targets as possible within 3 minutes
Name: barrage
Version: 1.0.4
Release: alt2
License: GPL
Group: Games/Arcade

Source0: %name-%version.tar
Source1: %name.png
Patch0: pach-%name-desktop.patch
##replace alt-DSO path
Patch1: %name-1.0.2-fd-dsolink.patch
Patch2: %name-1.0.2-fd-spelling.patch
URL: http://lgames.sourceforge.net/index.php?project=Barrage

BuildRequires: ImageMagick-tools libSDL_mixer-devel automake

%description
Barrage is a rather violent action game with the objective to kill
and destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%prep
%setup
#%patch0 -p1
%patch1
%patch2

%build
%autoreconf
./configure --prefix=%prefix --bindir=%_gamesbindir
%make_build

%install
%make DESTDIR=%buildroot install
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png

%files
%_gamesdatadir/*
%_gamesbindir/*
%_desktopdir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Oct 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt2
- NMU: fixed build.

* Fri Sep 28 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.0.4-alt1
- Update to 1.0.4
- Import fedora patches:
  + barrage-1.0.2-fd-spelling.patch
  + barrage-1.0.2-fd-dsolink.patch

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.2
- Fixed build

* Tue Jan 05 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 1.0.2-alt1.1
- fix overflow destination buffer

* Tue Jan 05 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 1.0.2-alt1
- new version 1.0.2

* Thu Dec 18 2008 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt3.1
- cleanup spec-file
- run buildreq script

* Sat Dec 13 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.0.1-alt3
- add icons

* Sat Dec 13 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.0.1-alt2
- fixed spec
- relocation to /usr/games
- chang group to Games/Arcade

* Wed Dec 10 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 1.0.1-alt1
- rebuild for ALT Linux
