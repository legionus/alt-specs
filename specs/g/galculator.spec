Name: galculator
Version: 2.1.4
Release: alt1

Summary: GTK3 based scientific calculator
License: GPL
Group: Sciences/Mathematics

Url: http://galculator.mnim.org
Source: %url/downloads/%name-%version.tar.gz
Source100: galculator.watch
Patch: galculator-1.3.4-alt-desktop.patch

BuildRequires: flex intltool libgtk+3-devel

%description
Galculator is a GTK3 based scientific RPN calculator

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name
install -pD pixmaps/%name.svg \
		%buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -pD pixmaps/%name.png \
		%buildroot%_liconsdir/%name.png
install -pD pixmaps/%name.xpm \
		%buildroot%_liconsdir/%name.xpm
rm -rf %buildroot%_pixmapsdir/

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_liconsdir/%name.png
%_liconsdir/%name.xpm
%_datadir/%name
%_datadir/appdata/*.xml
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README THANKS

# TODO:
# - 32x32 and 16x16? (%%_niconsdir and %%_miconsdir)

%changelog
* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 2.1.4-alt1
- new version (watch file uupdate)
- added appdata file

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Wed May 22 2013 Michael Shigorin <mike@altlinux.org> 2.1.2-alt1
- new version (watch file uupdate)
- gtk3 patch merged upstream

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- added fedora patch to cope with updated gtk3 (thanks aen@)

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- new version (watch file uupdate)

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- new version (watch file uupdate)
  + it wants gtk3, don't believe the README
- buildreq

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.3.4-alt4
- added watch file

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.4-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for galculator

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 1.3.4-alt3
- IconPathsPolicy alignment (repocop)

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 1.3.4-alt2
- fixed desktop file (repocop)
- minor spec cleanup

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- buildreq

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1
- applied repocop patch
- minor spec cleanup

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt2
- buildreq

* Sat Sep 08 2007 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- 1.3

* Tue Mar 20 2007 Michael Shigorin <mike@altlinux.org> 1.2.5.2-alt4
- fixed changelog
- NB: calc.png can be installed with e.g. gnome-icon-theme

* Sun Mar 18 2007 Michael Shigorin <mike@altlinux.org> 1.2.5.2-alt3
- tweaked fd.o menu to use calc.png as an icon
  (#11052; thanks Denis Samsonenko for noticing/advising)

* Sat Mar 17 2007 Michael Shigorin <mike@altlinux.org> 1.2.5.2-alt2
- removed debian menu (converted file was empty, and original
  freedesktop one is already packaged) (fixes: #11052)

* Fri Dec 15 2006 Michael Shigorin <mike@altlinux.org> 1.2.5.2-alt1.1
- rebuild

* Tue Nov 21 2006 Michael Shigorin <mike@altlinux.org> 1.2.5.2-alt1
- 1.2.5.2
- added myself as new Packager:
- spec cleanup

* Tue Apr 19 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Sat May 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Mar 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Mar 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Tue Nov 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sun Aug 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- new version.

* Thu Apr 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt1
- 1.0

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1
- First build for Sisyphus.

