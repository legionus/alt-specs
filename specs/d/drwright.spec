Name: drwright
Version: 3.5
Release: alt1.27.gfa0bade
License: GPL2
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/drwright
Summary: A program that reminds you to take wrist breaks
# git://git.gnome.org/drwright
Source: %name-%version.tar

BuildRequires: gnome-settings-daemon-devel
# Automatically added by buildreq on Mon Oct 02 2017 (-bi)
# optimized out: at-spi2-atk elfutils fontconfig glib2-devel gnu-config gtk-builder-convert libX11-devel libXext-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcanberra-devel libcanberra-gtk-common-devel libcanberra-gtk3 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+3-devel libpango-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server perl perl-Encode perl-XML-Parser pkg-config python-base python-modules python-modules-encodings python-modules-xml python3 python3-base rpm-build-python3 shared-mime-info termutils xml-common xml-utils xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: desktop-file-utils gnome-common intltool libXScrnSaver-devel libcanberra-gtk3-devel libnotify-devel python3-module-yieldfrom time

%description
WARNING: no GUI for settings except dconf-editor! (key
/org/gnome/settings-daemon/plugins/typing-break/)

"typing break" drwright - Typing monitor to force typing breaks

It's a program that forces you to take regular breaks to prevent RSI
(Repetitive Strain Injury). It's similar to workrave. It can be found in GNOME
control center as "typing break".

It used to be part of GNOME 2's main core, but is now packaged separately.

Features
* You can specify the work interval (how much time you want to work between
  breaks) and a break interval (how long your break will be).
* It also allows postponing of breaks.
* There is an option to lock the screen in case you want to step out
  indefinetely (v3.2.3).

%prep
%setup
%__subst 's/^gsd_plugin_LTLIBRARIES/gsd_plugin_LTLIBRARIES_turnoff/' src/Makefile.am
%__subst 's/^ccpanels_LTLIBRARIES/ccpanels_LTLIBRARIES_turnoff/' src/Makefile.am
%__subst 's/^gsd_plugin_DATA/gsd_plugin_DATA_turnoff/' src/Makefile.am

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%find_lang %name --with-gnome
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	%buildroot%_desktopdir/gnome-typing-break-panel.desktop

%files -f %name.lang
%doc AUTHORS NEWS
%_libexecdir/%name/
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%_datadir/locale/sr@Latn/LC_MESSAGES/drwright.mo

%changelog
* Sun Oct 01 2017 Ildar Mulyukov <ildar@altlinux.ru> 3.5-alt1.27.gfa0bade
- new version
- tear off the gnome-settings-daemon and gnome-control-center plugins
- settings/options only through dconf
    key /org/gnome/settings-daemon/plugins/typing-break/

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.5-alt1.1
- Fixed build

* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 3.2.5-alt1
- new version 3.2.5 (with rpmrb script) (ALT bug #27192)

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for drwright
  * altlinux-policy-obsolete-buildreq for drwright

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18-alt6
- fix build

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for drwright
  * obsolete-call-in-post-scrollkeeper-update for drwright
  * postclean-05-filetriggers for spec file

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt5
- cleanup spec, change packager, remove COPYING, enable SMP build

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt4
- build fixes

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt3
- rebuld without D-BUS

* Thu Feb 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt2
- rebuild with GNOME 2.8

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version
- cleanup spec

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt3
- rebuild with new libgnome
- add russian translation

* Mon Feb 16 2004 Vital Khilko <vk@altlinux.ru> 0.17-alt2
- rebuild with gcc-3.3.3

* Thu Dec 11 2003 Vital Khilko <vk@altlinux.ru> 0.17-alt1
- initial build for ALT Linux Sisyphus
- added belarusian translation
