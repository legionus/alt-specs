
Name: libvirt-glib
Version: 2.0.0
Release: alt1
Summary: libvirt glib integration for events
Group: System/Libraries
License: LGPLv2+
URL: http://libvirt.org/
Source: %name-%version.tar

# From configure.ac
%define libvirt_ver 1.2.5
%define glib_ver 2.38.0
%define libxml2_ver 2.0.0

BuildRequires: intltool
BuildRequires: libvirt-devel >= %libvirt_ver
BuildRequires: glib2-devel >= %glib_ver libgio-devel
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: gobject-introspection-devel >= 1.36.0
BuildRequires: vala-tools gtk-doc

%description
This package provides integration between libvirt and the glib
event loop.

%package devel
Group: Development/C
Summary: libvirt glib integration for events development files
Requires: %name = %version-%release

%description devel
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library


%package -n libvirt-gconfig
Group: System/Libraries
Summary: libvirt object APIs for processing object configuration

%description -n libvirt-gconfig
This package provides APIs for processing the object configuration
data

%package -n libvirt-gconfig-devel
Group: Development/C
Summary: libvirt object APIs for processing object configuration development files
Requires: libvirt-gconfig = %version-%release

%description -n libvirt-gconfig-devel
This package provides development header files and libraries for
the object configuration APIs.

%package -n libvirt-gconfig-gir
Summary: GObject introspection data for the libvirt-gconfig library
Group: System/Libraries
Requires: libvirt-gconfig = %version-%release

%description -n libvirt-gconfig-gir
GObject introspection data for the libvirt-gconfig library

%package -n libvirt-gconfig-gir-devel
Summary: GObject introspection devel data for the libvirt-gconfig library
Group: Development/Other
BuildArch: noarch
Requires: libvirt-gconfig-gir = %version-%release libvirt-gconfig-devel = %version-%release

%description -n libvirt-gconfig-gir-devel
GObject introspection devel data for the libvirt-gconfig library

%package -n libvirt-gobject
Group: System/Libraries
Summary: libvirt object APIs for managing virtualization hosts
Requires: %name = %version-%release libvirt-gconfig  = %version-%release

%description -n libvirt-gobject
This package provides APIs for managing virtualization host
objects

%package -n libvirt-gobject-devel
Group: Development/C
Summary: libvirt object APIs for managing virtualization hosts development files
Requires: libvirt-gobject = %version-%release libvirt-gconfig-devel = %version-%release

%description -n libvirt-gobject-devel
This package provides development header files and libraries for
managing virtualization host objects

%package -n libvirt-gobject-gir
Summary: GObject introspection data for the libvirt-gobject library
Group: System/Libraries
Requires: libvirt-gobject = %version-%release
Requires: %name-gir = %version-%release libvirt-gconfig-gir = %version-%release

%description -n libvirt-gobject-gir
GObject introspection data for the libvirt-gobject library

%package -n libvirt-gobject-gir-devel
Summary: GObject introspection devel data for the libvirt-gobject library
Group: Development/Other
BuildArch: noarch
Requires: libvirt-gobject-gir = %version-%release libvirt-gobject-devel = %version-%release
Requires: %name-gir-devel = %version-%release libvirt-gconfig-gir-devel = %version-%release

%description -n libvirt-gobject-gir-devel
GObject introspection devel data for the libvirt-gobject library

%prep
%setup -q

%build
touch ChangeLog AUTHORS
mkdir -p build-aux
intltoolize --force
%autoreconf
%configure \
	--disable-static \
	--enable-introspection \
	--enable-vala \
	--enable-gtk-doc

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%check
%make_build check

%files -f %name.lang
%doc README COPYING NEWS
%_libdir/libvirt-glib-*.so.*

%files gir
%_libdir/girepository-1.0/LibvirtGLib-*.typelib

%files gir-devel
%_datadir/gir-1.0/LibvirtGLib-*.gir

%files -n libvirt-gconfig
%_libdir/libvirt-gconfig-*.so.*

%files -n libvirt-gconfig-gir
%_libdir/girepository-1.0/LibvirtGConfig-*.typelib

%files -n libvirt-gconfig-gir-devel
%_datadir/gir-1.0/LibvirtGConfig-*.gir

%files -n libvirt-gobject
%_libdir/libvirt-gobject-*.so.*

%files -n libvirt-gobject-gir
%_libdir/girepository-1.0/LibvirtGObject-*.typelib

%files -n libvirt-gobject-gir-devel
%_datadir/gir-1.0/LibvirtGObject-*.gir

%files devel
%doc examples/event-test.c
%_libdir/libvirt-glib-*.so
%_pkgconfigdir/libvirt-glib-*.pc
%dir %_includedir/libvirt-glib-1.0
%_includedir/libvirt-glib-1.0/*
%_vapidir/libvirt-glib-*

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n libvirt-gconfig-devel
%_libdir/libvirt-gconfig-*.so
%_pkgconfigdir/libvirt-gconfig-*.pc
%dir %_includedir/libvirt-gconfig-1.0
%_includedir/libvirt-gconfig-1.0/*
%_vapidir/libvirt-gconfig-*

%files -n libvirt-gobject-devel
%_libdir/libvirt-gobject-*.so
%_pkgconfigdir/libvirt-gobject-*.pc
%dir %_includedir/libvirt-gobject-1.0
%_includedir/libvirt-gobject-1.0/*
%_vapidir/libvirt-gobject-*

%changelog
* Fri Oct 19 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt0.git.d70587
- build upstream master snapshot

* Sat Nov 05 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Tue Jun 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Dec 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Wed Aug 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Thu Mar 21 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Wed May 16 2012 Alexey Shabalin <shaba@altlinux.ru> 0.0.8-alt1
- 0.0.8

* Wed Apr 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.0.7-alt1
- 0.0.7

* Thu Mar 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.0.6-alt1
- 0.0.6
- rewrited spec without fcimport

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt1_1
- update to new release by fcimport

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2_1
- spec cleanup thanks to ldv@

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_1
- update to new release by fcimport

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_1
- initial import by fcimport

