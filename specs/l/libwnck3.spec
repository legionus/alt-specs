%define _name libwnck
%define ver_major 3.30
%define api_ver 3.0

%def_enable introspection
%def_enable startup_notification
%def_disable static
%def_disable debug

Name: %{_name}3
Version: %ver_major.0
Release: alt1

Summary: libwnck is a Window Navigator Construction Kit
License: %lgpl2plus
Group: System/Libraries
URL: ftp://ftp.gnome.org

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires(pre): rpm-build-gnome rpm-build-licenses
# From configure.ac
BuildRequires: libX11-devel libXres-devel libXext-devel libXt-devel libXi-devel
BuildRequires: libgtk+3-devel >= 3.22.0
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: gtk-doc >= 1.9
%{?_enable_startup_notification:BuildRequires: libstartup-notification-devel >= 0.4}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+3-gir-devel}

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use for
writing pagers and taskslists and stuff.

This library is a part of the GNOME 3 platform.

%package devel
Summary: Header and development libraries for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: %{name}2.22-devel = %version-%release
Provides: %{name}2.20-devel = %version-%release
Obsoletes: %{name}2.22-devel
Obsoletes: %{name}2.20-devel

%description devel
This package contains header and development libraries for %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Window Navigator Construction Kit library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Window Navigator Construction Kit library

%if_enabled static
%package devel-static
Summary: Static libraries and objects for %name
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
This package contains the General Window Manager interfacing static
libraries and objects.
%endif

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{?_disable_startup_notification:--disable-startup-notification} \
    --program-suffix=-3
%make_build

%check
%make check

%install
%makeinstall_std
%find_lang --output=%_name.lang %_name-%api_ver

%files -f %_name.lang
%_bindir/wnck-urgency-monitor-3
%_bindir/wnckprop-3
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Sep 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 3.24.1-alt1.1
- NMU: Rebuilt for e2k.

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Thu Jun 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Jun 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Jun 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Sep 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.4.9-alt1
- 3.4.9

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.7-alt1
- 3.4.7

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.5-alt1
- 3.4.5

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4

* Fri Sep 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt1
- 2.91.92

* Wed Feb 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt1
- first build for Sisyphus

