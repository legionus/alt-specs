%define _libexecdir %_prefix/libexec
%define _name geocode-glib
%define ver_major 3.26
%define api_ver 1.0
%def_enable gtk_doc
%def_enable introspection
%def_enable installed_tests
%def_disable check

Name: lib%{_name}
Version: %ver_major.0
Release: alt1

Summary: Convenience library for the Yahoo! Place Finder APIs
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.44
%define soup_ver 2.42
%define json_glib_ver 1.0

BuildPreReq: meson libjson-glib-devel >= %json_glib_ver
BuildRequires: libgio-devel >= %glib_ver libsoup-devel >= %soup_ver
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_introspection:BuildRequires: libsoup-gir-devel libjson-glib-gir-devel}

%description
%_name is a helper library for geocoding and reverse-geocoding
services offered by OpenStreetMap and Nominatim.

%package devel
Summary: Development files for %_name library
Group: Development/C
Requires: %name = %version-%release

%description devel
%_name is a helper library for geocoding and reverse-geocoding
services offered by OpenStreetMap and Nominatim.

This package contains files needed to develop with %_name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library

%package tests
Summary: Tests for the %_name
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.


%prep
%setup -n %_name-%version

%build
%meson %{?_enable_gtk_doc:-Denable-gtk-doc=true} \
	%{?_enable_introspection:-Denable-introspection=true} \
	%{?_enable_installed_tests:-Denable-installed-tests=true}
%meson_build

%install
%meson_install

%find_lang %_name

%check
%{?_enable_check:%meson_test}

%files -f %_name.lang
%_libdir/*.so.*
%_iconsdir/gnome/scalable/places/*.svg
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%if_enabled introspection
%files gir
%_typelibdir/GeocodeGlib-%api_ver.typelib

%files gir-devel
%_girdir/GeocodeGlib-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
#%_datadir/installed-tests/%_name-%api_ver/
%endif

%changelog
* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Aug 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.4.1-alt1
- 3.25.4.1

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Feb 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.23.90-alt1
- 3.23.90

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Feb 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sun Jan 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.99.0-alt1
- first build for Sisyphus
