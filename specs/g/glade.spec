%define _unpackaged_files_terminate_build 1

%define ver_major 3.22
%define api_ver 2.0
%def_enable python
%def_enable gladeui
%def_enable webkit2gtk

Name: glade
Version: %ver_major.1
Release: alt2

Summary: A user interface designer for Gtk+ and GNOME
Group: Development/GNOME and GTK+
License: %gpl2plus, %lgpl2plus
Url: http://glade.gnome.org/

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: libgladeui%api_ver = %version-%release

%define gtk_ver 3.20

BuildRequires: rpm-build-licenses rpm-build-gnome
BuildRequires: gnome-common gtk-doc yelp-tools intltool libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libxml2-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
# use python3
#AutoReqProv: nopython
#%%define __python %nil
#BuildRequires: rpm-build-python3 python3-module-pygobject3-devel
%{?_enable_python:BuildRequires: python-devel python-module-pygobject3-devel}
%{?_enable_webkit2gtk:BuildRequires: libwebkit2gtk-devel}

%description
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with GladeUI library.

%package -n libgladeui%api_ver
Summary: GTK+/GNOME3 widget builder library
Group:   Development/GNOME and GTK+

%description -n libgladeui%api_ver
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.
This is library that can be used for embed builder into other
applications.

%package -n libgladeui%api_ver-devel
Summary: GTK+3/GNOME3 widget builder library
Group:   Development/GNOME and GTK+
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-devel
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.

This package contains development files for GladeUI library.

%package -n libgladeui%api_ver-devel-doc
Summary: GladeUI development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: libgladeui%api_ver-devel < %version

%description -n libgladeui%api_ver-devel-doc
This package contains documentation needed to develop applications using
GladeUI library.

%package -n libgladeui%api_ver-gir
Summary: GObject introspection data for the GladeUI
Group: System/Libraries
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-gir
GObject introspection data for the GladeUI library.

%package -n libgladeui%api_ver-gir-devel
Summary: GObject introspection devel data for the GladeUI
Group: Development/Other
BuildArch: noarch
Requires: libgladeui%api_ver-gir = %version-%release
Requires: libgladeui%api_ver-devel = %version-%release

%description -n libgladeui%api_ver-gir-devel
GObject introspection devel data for the GladeUI library.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	--enable-gtk-doc \
	%{subst_enable python} \
	%{subst_enable gladeui} \
	%{subst_enable webkit2gtk}
#	PYTHON=%__python3 \
#	PYTHON_LIBS="$(python3-config --ldflags)"
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-previewer
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%_man1dir/glade-previewer.1.*
%_man1dir/glade.1.*
%doc AUTHORS COPYING NEWS README TODO

%files -n libgladeui%api_ver
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/libgladegtk.so
%{?_enable_python:%_libdir/%name/modules/libgladepython.so}
%{?_enable_gladeui:%_libdir/%name/modules/libgladeglade.so}
%{?_enable_webkit2gtk:%_libdir/%name/modules/libgladewebkit2gtk.so}
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/catalogs
%_datadir/%name/catalogs/*.xml
%_datadir/%name/catalogs/glade-catalog.dtd
%_iconsdir/hicolor/scalable/apps/glade-brand-symbolic.svg
%_datadir/%name/pixmaps
%_datadir/metainfo/%name.appdata.xml

%exclude %_libdir/%name/modules/*.la

%files -n libgladeui%api_ver-devel
%_includedir/libgladeui-%api_ver/
%_libdir/*.so
%_pkgconfigdir/gladeui-%api_ver.pc

%files -n libgladeui%api_ver-devel-doc
%_datadir/gtk-doc/html/*

%files -n libgladeui%api_ver-gir
%_typelibdir/Gladeui-%api_ver.typelib

%files -n libgladeui%api_ver-gir-devel
%_girdir/Gladeui-%api_ver.gir

%changelog
* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt2
- updated buildreqs

* Tue Apr 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Sun Feb 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon Nov 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2
- removed upstreamed patch from previous release

* Fri Oct 13 2017 Paul Wolneykien <manowar@altlinux.org> 3.20.1-alt2
- Apply fix-xorg-100-percent patch (thx arnaud-preevio@).

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Apr 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.15.1-alt1
- 3.15.1

* Thu Mar 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.15.0-alt1
- 3.15.0

* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- first build for Sisyphus

