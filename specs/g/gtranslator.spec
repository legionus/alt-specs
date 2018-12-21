%def_disable snapshot

%define ver_major 3.30
%define api_ver 3.0
%define xdg_name org.gnome.Gtranslator

Name: gtranslator
Version: %ver_major.1
Release: alt1

Summary: A GNOME po file editor with many bells and whistles.
License: GPLv3
Group: Development/Tools
Url: https://wiki.gnome.org/Apps/Gtranslator

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: libgda5-sqlite gettext-tools

%define gtk_ver 3.22.20
%define gspell_ver 1.2.0
%define gtksourceview_ver 4.0.2
%define xml_ver 2.4.12

BuildRequires(pre): meson rpm-build-gir
BuildRequires: yelp-tools gtk-doc libgtk+3-devel >= %gtk_ver
BuildRequires: libgda5-devel libgtksourceview4-devel >= %gtksourceview_ver
BuildRequires: libsoup-devel gsettings-desktop-schemas-devel iso-codes-devel
BuildRequires: libgspell-devel >= %gspell_ver libxml2-devel >= %xml_ver

%description
gtranslator is a quite comfortable gettext po/po.gz/(g)mo files editor
for the GNOME 3.x platform with many features. It's evolving quite fast
and many useful functions are already implemented; gtranslator aims to
be a very complete editing environment for translation issues within the
GNU gettext/GNOME desktop world.

%package devel
Summary: %name header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides header files needed for build %name plugins.

%package devel-doc
Summary: %name development documentation
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation needed to develop %name plugins.

%set_typelibdir %_libdir/%name/girepository-1.0

%prep
%setup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%xdg_name.*
%_iconsdir/hicolor/symbolic/apps/%{xdg_name}*.svg
%_pixmapsdir/*.png
%_man1dir/%name.1*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README* THANKS

%files devel
%_includedir/gtr-marshal.h
%_datadir/gtk-doc/html/%name/

%changelog
* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sat Nov 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Dec 30 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt4
- 2.91.6

* Mon Dec 03 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt3
- rebuild against libgda5

* Sat Dec 01 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt2
- updated to 398ebe3e8

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1.2
- rebuilt against libgdl-3.so.5

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1.1
- used %%set_typelibdir macros

* Thu Jun 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Sat Oct 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.12-alt1
- 1.9.12

* Fri May 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.11-alt1
- 1.9.11

* Wed Apr 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.10-alt1
- 1.9.10

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.9-alt1
- 1.9.9

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.8-alt1
- 1.9.8

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.7-alt1
- 1.9.7

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt2
- rebuild with libgdl 2.28.2

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt1
- 1.9.6

* Fri Jul 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt3
- updated translation

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt2
- updated build dependencies

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt1
- initial relese

