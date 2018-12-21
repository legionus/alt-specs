%define _unpackaged_files_terminate_build 1

%define ver_major 3.18
%define api_ver 3.0
%define libname gtkhex-3

Name: ghex
Version: %ver_major.3
Release: alt1

Summary: Binary editor for GNOME
Group: Development/Tools
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Ghex

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: ghex-3.7.90-alt-lfs.patch

%define glib_ver 2.31.10
%define gtk_ver 3.3.8

Requires: libgtkhex = %version-%release

BuildRequires: gnome-common glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgail3-devel intltool yelp-tools

%description
GHex is a hex editor for the GNOME desktop.

GHex can load raw data from binary files and display them for editing in
the traditional hex editor view. The display is split in two columns,
with hexadecimal values in one column and the ASCII representation in
the other. A useful tool for working with raw data.

%package -n libgtkhex
Summary: GtkHex shared library
Group: System/Libraries

%description -n libgtkhex
This package provides shared librarys needed for GtkGHex to work.

%package -n libgtkhex-devel
Summary: Development files for GtkHex
Group: Development/C
Requires: libgtkhex = %version-%release

%description -n libgtkhex-devel
This package contains libraries and header files for
developing applications that use GtkGHex library.

%prep
%setup
%patch -p1 -b .lfs

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name %name-%api_ver

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS NEWS README

%files -n libgtkhex
%_libdir/lib%libname.so.*

%files -n libgtkhex-devel
%_includedir/%libname/
%_libdir/lib%libname.so
%_pkgconfigdir/%libname.pc

%changelog
* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Jun 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2
- new libgtkhex{,-devel} subpackages

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.90-alt1
- 3.5.90

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus

