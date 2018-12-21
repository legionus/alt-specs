%define _unpackaged_files_terminate_build 1

Name: ncmpc
Version: 0.31
Release: alt1
Summary: curses client for mpd
License: GPL
Group: Sound
Url: https://www.musicpd.org/

# https://github.com/MusicPlayerDaemon/ncmpc.git
Source: %name-%version.tar
Source1: %name.desktop

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: glib2-devel libncursesw-devel libtinfo-devel pkg-config
BuildRequires: liblirc-devel
BuildRequires: libmpdclient-devel
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: python3-module-sphinx

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc
connects to a MPD running on a machine on the local network, and
controls this with an interface inspired by cplay. If ncmpc is used
with lirc and irpty it can be used to manage playlists and control MPD
with a remote control.

%prep
%setup
sed -i -e "s,sphinx-build,sphinx-build-3,g" doc/meson.build

%build
%meson \
	-D lirc=true \
	-D lyrics_screen=true \
	-D lyrics_plugin_dir=%_datadir/%name/lyrics

%meson_build

%install
%meson_install

install -m 644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideo \
	--add-category=Player \
	%buildroot%_desktopdir/%name.desktop

rm -f %buildroot%_defaultdocdir/%name/html/.buildinfo

%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_defaultdocdir/%name
%_datadir/%name

%changelog
* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.31-alt1
- Updated to upstream version 0.31.

* Fri Sep 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.27-alt1
- Updated to upstream version 0.27.

* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 0.19-alt1
- NMU
- Updated to 0.19

* Thu May 19 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.18-alt2
- Applied patch from repocop (adds proper categories to .desktop file)

* Sat Dec 04 2010 Slava Semushin <php-coder@altlinux.ru> 0.18-alt1
- NMU
- Updated to 0.18

* Sun Jul 25 2010 Slava Semushin <php-coder@altlinux.ru> 0.17-alt1
- NMU
- Updated to 0.17

* Sun Feb 28 2010 Slava Semushin <php-coder@altlinux.ru> 0.16.1-alt1
- NMU
- Updated to 0.16.1

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 0.16-alt1
- NMU
- Updated to 0.16 (Closes: #20170)
- Updated home page

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt6
- Removed obsolete update_menu macros

* Mon Jun 05 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt5
- Built with libncursesw-devel

* Sun May 21 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt4
- Built with libncursesw
- Fixed .desktop (#9153)

* Wed Jan 18 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt3
- Added patch to allow build with ncursesw (disabled by default)
- Fixed more typos in translation
- Added menu

* Thu Nov 03 2005 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt2
- Corrected russian translation encoding
- Fixed typos in translation

* Sat Oct 29 2005 Damir Shayhutdinov <damir@altlinux.ru> 0.11.1-alt1
- Initial build for Sisyphus

