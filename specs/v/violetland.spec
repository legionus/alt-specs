Name: violetland
Version: 0.5
Release: alt2.1
Summary: An open source cross-platform game similar to Crimsonland
Group: Games/Arcade
License: GPLv3
Url: http://violetland.github.io/
Source: %version.tar.gz
Source1: GettextTranslate.cmake
Source2: FindLibintl.cmake
Patch: violetland-v0.4.3-boost1.51.patch

Requires: %name-data

# Automatically added by buildreq on Tue May 04 2010
BuildRequires: cmake dos2unix gcc-c++ libGL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libxkbfile-devel unzip ImageMagick-tools boost-devel boost-filesystem-devel

%description
Violetland is an open source cross-platform game similar to Crimsonland.

In this game the player should help a girl by name of Violet to struggle
with hordes of monsters. For this purpose the various weapon, and also the
special abilities of the heroine which are opening with experience can be
used. In game there are elements of RPG in the form of strength-agility-vitality
and derivatives. Also there is an unique feature: dynamic change of day and
night.

%package data
Summary: Data files for Violetland game
Group: Games/Arcade
License: CC-BY-SA
BuildArch: noarch

%description data
Violetland is an open source cross-platform game similar to Crimsonland.

In this game the player should help a girl by name of Violet to struggle
with hordes of monsters. For this purpose the various weapon, and also the
special abilities of the heroine which are opening with experience can be
used. In game there are elements of RPG in the form of strength-agility-vitality
and derivatives. Also there is an unique feature: dynamic change of day and
night.

This package contanis data files required for the game

%prep
%setup
#patch -p1
cp %SOURCE1 lib/CMake-Gettext/
install -D %SOURCE2 lib/fcitx/cmake/FindLibintl.cmake

%build
%define warns -Wall -Wno-delete-non-virtual-dtor -Wno-narrowing
install -dm 755 build
pushd build
	#cmake \
	#	-DCMAKE_INSTALL_PREFIX=%buildroot%prefix \
	#	-DDATA_INSTALL_DIR=%_datadir/games/%name \
	#	..
        cmake .. \
            -DCMAKE_SKIP_RPATH:BOOL=yes \
            -DCMAKE_BUILD_TYPE=MinSizeRel \
            -DCMAKE_C_FLAGS:STRING='-pipe %warns -O2' \
            -DCMAKE_CXX_FLAGS:STRING='-pipe %warns -O2' \
            -DCMAKE_INSTALL_PREFIX=%prefix \
            -DDATA_INSTALL_DIR=%_gamesdatadir/%name \
	    -DLOCALE_INSTALL_DIR=%_datadir/locale \
            -DLIB_DESTINATION=%_lib \
            %if "%_lib" == "lib64"
            -DLIB_SUFFIX="64" \
            %else
            -DLIB_SUFFIX="" \
            %endif

	%make_build
popd

cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Name=Violetland
GenericName=Violetland
Categories=Game;ActionGame;
Comment=An open source cross-platform game similar to Crimsonland
Exec=%name
Icon=%name
EOF
#suse_update_desktop_file %name Game ActionGame

for s in 16 24 32 48; do
  convert icon-light.png -resize ${s}x${s} ${s}.png
done

%install
pushd build
	%makeinstall DESTDIR=%buildroot
popd

# icon
install -D icon-light.png %buildroot%_datadir/pixmaps/%name.png
for s in 16 24 32 48; do
  install -D ${s}.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc *.TXT *.md
%_bindir/%name
%_datadir/pixmaps/%name.png
%_desktopdir/%{name}*.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files data
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt2.1
- NMU: rebuilt with boost-1.67.0

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 0.5-alt2
- Rebuild with boost 1.65

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Upstream switched to github
- Autobuild version bump to 0.5
- Fix build

* Mon May 30 2016 Fr. Br. George <george@altlinux.ru> 0.4.99-alt1
- Version up to 0.5-rc1

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.3-alt2.qa4
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.4.3-alt2.1.qa1.1
- rebuild with boost 1.57.0

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.3-alt2.1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt2.1
- Rebuilt with Boost 1.52.0

* Thu Oct 25 2012 Fr. Br. George <george@altlinux.ru> 0.4.3-alt2
- Fix to build with boot filesystem v3

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.1
- Rebuilt with Boost 1.49.0

* Wed Jan 11 2012 Fr. Br. George <george@altlinux.ru> 0.4.3-alt1
- Autobuild version bump to 0.4.3

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.1
- Rebuilt with Boost 1.47.0

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Autobuild version bump to 0.4.2

* Mon Apr 11 2011 Fr. Br. George <george@altlinux.ru> 0.3.2-alt1
- Autobuild version bump to 0.3.2

* Sat Sep 25 2010 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt3
- Really fix repocop warning

* Sun May 09 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt2
- Fix repocop warning

* Tue May 04 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Version up

* Tue May 04 2010 Fr. Br. George <george@altlinux.ru> 0.2.10-alt1
- Initial build from SuSE

* Sat May 01 2010 Toni Graffy <toni@links2linux.de> - 0.2.10-0.pm.1
- update to 0.2.10
- new perk "night vision"
- new bonus "nuke"
- new bonus "strength boost"
- new bonus "agility boost"
- new bonus "vitality boost"
- new bonus "teleport" and a possibility to switch action mode (fire/teleport)
- possibility to change some input binding (now in test mode, see comment for the commit r198)
- new HUD (Head-Up Display)
- fixed issue 32 (pressing C when the player is dead will crash the game)
- fixed issues 29 and 33 (problems with adding of new weapons)
* Sat Feb 27 2010 Toni Graffy <toni@links2linux.de> - 0.2.9-0.pm.1
- update to 0.2.9
- new bonus "penetration bullets"
- death animations of player
- explantation of perks on char stats screen
- loading screen between pressing "new survival" and starting the game
- view of flashlight
- last entry of high scores table was always zero
- death animations of monsters were played above player
- rendering of main menu on wide resolutions
* Thu Jan 28 2010 Toni Graffy <toni@links2linux.de> - 0.2.8-0.pm.1
- update to 0.2.8
- ability to change video settings from options screen
- new graphic - image of weapon in arms will change, animation of shells
- weapons structure
- monsters can have any number of sounds of pain
- fixed sound issues by explicit sound mixing
- issues of loading resources in *nix systems
* Sat Jan 16 2010 Toni Graffy <toni@links2linux.de> - 0.2.7-0.pm.1
- update to 0.2.7
- improved animation of monsters
- corrected error on updating highscores
- new monster animation (spider)
- in-game information line about monster which cursor points to
- parameters of monsters are loaded from files
- names of monsters directories are names of monsters
- redesign of some game images
- sound issues are fixed by temporary turning off music fading
* Fri Jan 08 2010 Toni Graffy <toni@links2linux.de> - 0.2.5-0.pm.1
- update to 0.2.5
* Thu Dec 17 2009 Toni Graffy <toni@links2linux.de> - 0.2.4-0.pm.1
- Initial build
