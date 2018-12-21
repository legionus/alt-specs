%define _name mx
%define ver_major 1.4
%define api_ver 1.0

%def_enable introspection
%def_enable dbus
%def_disable gtk_doc
%def_disable imcontext
%def_disable gesture
%def_disable gtk

Name: lib%_name
Version: %ver_major.7
Release: alt4

Summary: A clutter widget toolkit
Group: System/Libraries
License: LGPLv2
Url: https://github.com/clutter-project/mx 
Source: %_name-%version.tar

%define clutter_ver 1.8.0

BuildRequires: intltool gtk-doc
BuildRequires: libclutter-devel >= %clutter_ver
BuildRequires: libgdk-pixbuf-devel libstartup-notification-devel libXrandr-devel
%{?_enable_dbus:BuildRequires: libdbus-glib-devel}
%{?_enable_imcontext:BuildRequires: libclutter-imcontext-devel}
%{?_enable_gesture:BuildRequires: libclutter-gesture-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libclutter-gir-devel}

%description
MX is a widget toolkit using Clutter that provides a set of standard
interface elements, including buttons, progress bars, scroll bars and
others. It also implements some standard  managers. One other
interesting feature is the possibility setting style properties from a
CSS format file.

%package devel
Summary: Development package for MX library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files and libraries used for development with MX library

%package docs
Summary: Documentation files for MX library
Group: Development/Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description docs
This package contains developer documentation for MX library

%package gir
Summary: GObject introspection data for the MX library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the MX library

%package gir-devel
Summary: GObject introspection devel data for the MX library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the MX library


%prep
%setup -q -n %_name-%version

%build
autoreconf -fisv
%configure --disable-static \
	--enable-introspection \
	%{?_disable_gtk:--disable-gtk-widgets} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_enable_imcontext:--with-clutter-imcontext} \
	%{?_enable_gesture:--with-clutter-gesture}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
%_bindir/%_name-create-image-cache
%_libdir/*.so.*
%_datadir/%_name
%doc README ChangeLog

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled introspection
%files gir
%_typelibdir/Mx-%api_ver.typelib
#%_typelibdir/MxGtk-%api_ver.typelib

%files gir-devel
%_girdir/Mx-%api_ver.gir
#%_girdir/MxGtk-%api_ver.gir
%endif

%changelog
* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt4
- rebuilt against libcogl.so.20

* Fri Sep 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt3
- updated to 24efb0c
- built against libcogl.so.15

* Fri Mar 29 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt2
- rebuilt against libcogl.so.12

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.7-alt1
- 1.4.7
- moved to upstream git

* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Jan 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Apr 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.11-alt1
- first build for Sisyphus

