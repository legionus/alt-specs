%define ver_major 3.30
%define plugins_ver 12
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Software

%def_enable gspell
%def_enable gudev
%def_enable gnome_desktop
%def_enable polkit
%ifarch  %ix86  x86_64
%def_enable fwupd
%else
%def_disable  fwupd
%endif
%def_enable flatpak
%def_disable limba
%def_disable packagekit
%def_enable webapps
%def_enable odrs
%def_enable steam
%def_disable valgrind
%def_disable tests
# dropped since 3.27.90
%def_disable rpm
%def_disable rpm_ostree
%def_disable external_appstream

Name: gnome-software
Version: %ver_major.6
Release: alt1

Summary: Software manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Software

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.46
%define gtk_ver 3.22.4
%define appstream_glib_ver 0.7.14
%define json_glib_ver 1.1.1
%define soup_ver 2.52
%define packagekit_ver 1.1.9
%define gnome_desktop_ver 3.18
%define fwupd_ver 1.0.3
%define flatpak_ver 0.6.12
%define limba_ver 0.5.6
%define ostree_ver 2018.4

%{?_enable_fwupd:Requires: fwupd >= %fwupd_ver}
%{?_enable_packagekit:Requires: appstream-data}

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libappstream-glib-devel >= %appstream_glib_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: gnome-common rpm-build-xdg intltool yelp-tools gtk-doc xsltproc docbook-style-xsl
BuildRequires: libsqlite3-devel libsecret-devel gsettings-desktop-schemas-devel liboauth-devel
BuildRequires: valgrind-tool-devel
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_enable_gspell:BuildRequires: libgspell-devel}
%{?_enable_gnome_desktop:BuildRequires: libgnome-desktop3-devel >= %gnome_desktop_ver}
%{?_enable_polkit:BuildRequires: libpolkit-devel}
%{?_enable_fwupd:BuildRequires: fwupd-devel >= %fwupd_ver}
%{?_enable_flatpak:BuildRequires: libflatpak-devel >= %flatpak_ver}
%{?_enable_limba:BuildRequires: liblimba-devel >= %limba_ver}
%{?_enable_packagekit:BuildRequires: libpackage-glib-devel >= %packagekit_ver}
%{?_enable_valgrind:BuildRequires: valgrind}
%{?_enable_rpm_ostree:BuildRequires: libostree-devel >= %ostree_ver}
%{?_enable_rpm:BuildRequires: librpm-devel}

%description
GNOME Software is a software center for GNOME.

%package devel
Summary: Development files for GNOME Software
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains files necessary to develop plugins for GNOME
Software.

%package devel-doc
Summary: Development documentation for GNOME Software
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains documentation necessary to develop plugins for
GNOME Software.


%prep
%setup

%build
%meson \
	%{?_enable_gspell:-Dgspell=true} \
	%{?_enable_gudev:-Dgudev=true} \
	%{?_enable_gnome_desktop:-Dgnome_desktop=true} \
	%{?_enable_polkit:-Dpolkit=true} \
	%{?_disable_fwupd:-Dfwupd=false} \
	%{?_enable_flatpak:-Dflatpak=true} \
	%{?_enable_ostree:-Dostree=true} \
	%{?_disable_limba:-Dlimba=false} \
	%{?_enable_rpm_ostree:-Drpm_ostree=true} \
	%{?_disable_packagekit:-Dpackagekit=false} \
	%{?_disable_valgrind:-Dvalgrind=false} \
	%{?_disable_tests:-Dtests=false} \
	%{?_enable_external_appstream:-Dexternal_appstream=true}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_xdgconfigdir/autostart/%name-service.desktop
%_bindir/%name
%_bindir/%name-editor
%_libexecdir/%name-cmd
%_libexecdir/%name-restarter
%{?_enable_external_appstream:%_libexecdir/%name-install-appstream}
%_libdir/gs-plugins-%plugins_ver/
%_desktopdir/%name-local-file.desktop
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Editor.desktop
%_datadir/app-info/xmls/%xdg_name.Featured.xml
%_datadir/dbus-1/services/%xdg_name.service
%{?_enable_packagekit:%_datadir/dbus-1/services/org.freedesktop.PackageKit.service}
%{?_enable_external_appstream:%_datadir/polkit-1/actions/org.gnome.software.external-appstream.policy}
%_datadir/%name/
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_iconsdir/hicolor/*x*/*/%xdg_name.png
%_iconsdir/hicolor/scalable/apps/%xdg_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/software-installed-symbolic.svg
%_datadir/glib-2.0/schemas/org.gnome.software.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/metainfo/%xdg_name.Plugin.Epiphany.metainfo.xml
%{?_enable_flatpak:%_datadir/metainfo/%xdg_name.Plugin.Flatpak.metainfo.xml}
%{?_enable_odrs:%_datadir/metainfo/%xdg_name.Plugin.Odrs.metainfo.xml}
%{?_enable_steam:%_datadir/metainfo/%xdg_name.Plugin.Steam.metainfo.xml}
%{?_enable_fwupd:%_datadir/metainfo/%xdg_name.Plugin.Fwupd.metainfo.xml}
%_man1dir/%name.1.*
%_man1dir/%name-editor.1.*
%doc AUTHORS README*

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.6-alt1
- 3.30.6

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.5-alt1
- 3.30.5

* Thu Oct 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- enabled fwupd support

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.7-alt1
- 3.26.7

* Thu Feb 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.6-alt1
- 3.26.6

* Tue Jan 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt1
- 3.26.5

* Tue Dec 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Tue Nov 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Thu Nov 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt2
- new -devel, -devel-doc subpackages

* Mon May 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt0.2
- 3.24.1

* Sun Mar 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt0.2
- 3.24.0

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt0.2
- 3.22.7
- enabled ostree/flatpak support

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt0.1
- 3.22.6

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt0.1
- 3.22.5

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt0.1
- first preview for Sisyphus


