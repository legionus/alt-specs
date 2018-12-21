%def_disable snapshot
# hardcoded lib/geary path
#%%define _libexecdir %_prefix/libexec
%define ver_major 0.12
%define xdg_name org.gnome.Geary
%def_enable contractor

Name: geary
Version: %ver_major.4
Release: alt1

Summary: Email client
License: LGPLv2.1+
Group: Networking/Mail
Url: https://wiki.gnome.org/Apps/Geary

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define vala_ver 0.26
%define gtk_ver 3.14.0
%define sqlite_ver 3.12.0
%define gcr_ver 3.10.1
%define webkit_ver 2.10

BuildRequires: vala-tools >= %vala_ver libvala-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libsqlite3-devel >= %sqlite_ver
BuildRequires: cmake intltool desktop-file-utils gnome-doc-utils
BuildRequires: iso-codes-devel
BuildRequires: libnotify-devel libcanberra-devel libgee0.8-devel
BuildRequires: libgmime-devel libgnome-keyring-devel libexpat-devel
BuildRequires: libpixman-devel libharfbuzz-devel libwebkit2gtk-devel >= %webkit_ver
BuildRequires: libenchant-devel libpng-devel libsecret-devel at-spi2-atk-devel libxml2-devel
BuildRequires: libXdmcp-devel libXdamage-devel libxshmfence-devel
BuildRequires: libXxf86vm-devel libXinerama-devel libXrandr-devel libXi-devel
BuildRequires: libXcursor-devel libXcomposite-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsoup-gir-devel libwebkit2gtk-gir-devel libcanberra-vala
BuildRequires: gcr-libs-devel >= %gcr_ver gcr-libs-vala

%description
Geary is an email client built for the GNOME desktop environment.  It
allows you to read and send email with a simple, modern interface.

Visit http://www.yorba.org to read about the current state of.
Geary's development.

%prep
%setup

%build
%cmake -DGSETTINGS_COMPILE:BOOL=OFF \
	-DICON_UPDATE:BOOL=OFF \
	-DDESKTOP_UPDATE:BOOL=OFF
%cmake_build VERBOSE=1

%install
%cmakeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%{?_enable_contractor:%_bindir/%name-attach}
%_libexecdir/%name/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%name-autostart.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/*/*/apps/*
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/appdata/%xdg_name.appdata.xml
%{?_enable_contractor:%_datadir/contractor/geary-attach.contract}
%doc AUTHORS NEWS README THANKS

%changelog
* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Sat Jul 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt2
- updated to 0.11.0-761-g2f145ac from master branch
- build against gnome-3.23.x libraries

* Sun Dec 25 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3

* Mon Dec 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt2
- updated to geary-0.11.2-14-gd02629c

* Sun Aug 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Mon Jun 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sun May 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- updated to 0.10.0-75-g2d9e9b2 (also fixed BGO #763203 and ALT #32058)

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Tue Feb 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sat Sep 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Sep 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Jul 19 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Jul 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt1
- 0.4.1 trunk (r1119)

* Mon Aug 26 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt3
- Cleanup build requires

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt2
- Fix desktop file

* Sat Apr 13 2013 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Fri Mar 29 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

