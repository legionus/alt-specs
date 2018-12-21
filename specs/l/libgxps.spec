%define ver_major 0.3
%define api_ver 0.1
%def_enable introspection
%def_enable man
%def_enable check
%def_enable test

Name: libgxps
Version: %ver_major.0
Release: alt2

Summary: GObject based library for handling and rendering XPS documents
Group: System/Libraries
License: LGPLv2+
Url: http://live.gnome.org/libgxps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires(pre): meson
BuildRequires: gtk-doc
BuildRequires: libgio-devel libcairo-devel libcairo-gobject-devel libfreetype-devel
BuildRequires: libarchive-devel libjpeg-devel libtiff-devel libpng-devel liblcms2-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_test:BuildRequires: libgtk+3-devel}
%{?_enable_man:BuildRequires: xsltproc}

%description
%name is a GObject based library for handling and rendering XPS
documents.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

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
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package utils
Summary: Utilities to manipulate XPS files
Group: Graphics
Requires: %name = %version-%release

%description utils
This package contains utilities to manipulate XPS files from %name
package.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup

%build
%meson \
	%{?_disable_introspection:-Ddisable-introspection=true} \
	%{?_enable_man:-Denable-man=true} \
	%{?_disable_test:-Denable-test=false} \
	-Denable-gtk-doc=true

%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files gir
%_typelibdir/GXPS-%api_ver.typelib

%files gir-devel
%_girdir/GXPS-%api_ver.gir
%endif

%files utils
%_bindir/xpstojpeg
%_bindir/xpstopdf
%_bindir/xpstopng
%_bindir/xpstops
%_bindir/xpstosvg
%{?_enable_man:%_man1dir/*}

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt2
- fixed meson options

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1.1
- rebuilt for e2kv4

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sat Feb 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.3.2-alt1
- 0.2.3.2

* Fri Aug 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.3.1-alt1
- 0.2.3.1

* Thu Aug 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt2
- rebuilt against libarchive.so.13

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Sat Jan 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

