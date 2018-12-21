%define abi_ver 3.0
%define ver_major 3.0
%def_enable spell
%def_disable ots
%def_with goffice
%def_with champlain
%def_with libical
%def_with eds
%def_with python
%def_enable collabnet

Name: abiword
Version: %ver_major.2
Release: alt4

Summary: Lean and fast full-featured word processor
Group: Office
License: GPL
Url: http://www.abisource.com/

Source: http://www.abisource.com/downloads/abiword/%version/source/%name-%version.tar.gz

#fedora patches
Source11: abiword.mime
Source12: abiword.keys
Source13: abiword.xml

Patch: abiword-3.0.2-deb-libical-3.0.patch

Patch11: abiword-2.8.3-desktop.patch
Patch12: abiword-2.6.0-boolean.patch
Patch13: abiword-3.0.0-librevenge.patch
Patch14: abiword-3.0.2-fix-black-drawing-regression.patch

Obsoletes: abisuite, abisuite-koi8, abisuite-cp1251, abisuite-iso8859-8
Obsoletes: %name-%abi_ver
Provides: %name-%abi_ver = %version-%release
Conflicts: %name-light

Requires: %name-data = %version-%release

BuildRequires: gcc-c++ boost-devel libreadline-devel flex
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgsf-gir-devel
BuildRequires: libgtk+3-devel librsvg-devel libfribidi-devel libredland-devel
BuildRequires: liblink-grammar-devel libgsf-devel bzlib-devel zlib-devel libjpeg-devel libpng-devel libxslt-devel
BuildRequires: libwv-devel libwpd10-devel libwpg-devel libwmf-devel libwps-devel libexpat-devel
BuildRequires: telepathy-glib-devel libdbus-glib-devel
#BuildRequires: libaiksaurus-devel
%{?_enable_spell:BuildRequires: libenchant-devel}
%{?_with_goffice:BuildRequires: libgnomeoffice0.10-devel}
%{?_with_champlain:BuildRequires: libchamplain-gtk3-devel}
%{?_with_libical:BuildRequires: libical-devel}
%{?_with_eds:BuildRequires: evolution-data-server-devel}
%{?_with_python:BuildRequires: python-module-pygobject3-devel python-module-setuptools}
%{?_enable_collabnet:BuildRequires: libgnutls-devel libsoup-devel libgcrypt-devel asio-devel}
%{?_enable_ots:BuildRequires: libots-devel}

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.
(http://www.abisource.com)
It is a lean and fast full-featured word processor. It works on Microsoft
Windows and most Unix Systems. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of Word97 and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Document Templates
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   and much more...

%package data
Summary: Arch independent files for AbiWord
Group: Office
BuildArch: noarch
Obsoletes: %name-%abi_ver-data
Provides: %name-%abi_ver-data = %version-%release

%description data
This package provides noarch data needed for AbiWord to work.

%package devel
Group: Development/C++
Summary: Headers for Abiword plugins
Requires: %name = %version-%release
Obsoletes: %name-%abi_ver-devel
Provides: %name-%abi_ver-devel = %version-%release

%description devel
Headers and pkgconfig support for  Abiword plugin building.
Conflicts: %name-devel %name-light-devel

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release
Obsoletes: %name-%abi_ver-gir
Provides: %name-%abi_ver-gir = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Obsoletes: %name-%abi_ver-gir-devel
Provides: %name-%abi_ver-gir-devel = %version-%release

%description gir-devel
GObject introspection devel data for the AbiWord

%package -n python-module-%name
Summary: Python bindings for developing with AbiWord
Group: Development/Python
Requires: %name-gir = %version-%release

%description -n python-module-%name
Python bindings for developing with AbiWord library

%prep
%setup

# fedora patches
%patch -p1 -b .libical
%patch11 -p1 -b .desktop
%patch12 -p1 -b .boolean
%patch13 -p0 -b .librevenge
%patch14 -p1 -b .black

%build
%add_optflags -std=c++11 -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	--enable-print \
	--enable-plugins \
	--enable-templates \
	--enable-clipart \
	--enable-introspection \
	%{subst_enable spell} \
	%{subst_with goffice} \
	%{subst_with champlain} \
	%{subst_with libical} \
	%{?_without_eds:--without-evolution-data-server} \
	%{?_enable_collabnet:--enable-collab-backend-service} \
	--disable-static
%make_build

%install
%makeinstall_std

install -p -m 0644 -D %SOURCE11 %buildroot%_datadir/mime-info/abiword.mime
install -p -m 0644 -D %SOURCE12 %buildroot%_datadir/mime-info/abiword.keys
install -p -m 0644 -D %SOURCE13 %buildroot%_datadir/mime/packages/abiword.xml

%files
%_bindir/%name
%_libdir/lib%name-%ver_major.so
%dir %_libdir/%name-%ver_major
%dir %_libdir/%name-%ver_major/plugins
%_libdir/%name-%ver_major/plugins/*.so
%exclude %_libdir/abiword-%ver_major/plugins/*.la
%{?_enable_collabnet:%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service}
%{?_enable_collabnet:%_datadir/telepathy/clients/AbiCollab.client}

%files data
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/%name-%ver_major/
%_datadir/mime-info/*
%_datadir/mime/packages/*
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files -n python-module-%name
%python_sitelibdir/gi/overrides/*

%changelog
* Sun Aug 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt4
- disabled Open Text Summarizer support (ALT #35266)

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt3.1
- rebuilt for e2kv4

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt3
- rebuilt against libical.so.3

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed buildreqs

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2
- enabled abicollab.net support again
- enabled WPS support
- built against liblink-grammar-5.3.13

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt5
- renamed to abiword
- built against libical.so.2

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt4
- temporarily disabled abicollab.net support incompatible with gnutls > 3.4

* Mon Aug 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt3
- rebuilt against libebook-contacts-1.2.so.2

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2
- rebuilt against libebook-contacts-1.2.so.1

* Sat Jan 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1
- removed some upstreamed fedora patches

* Tue Dec 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt7
- updated fedora patches for link-grammar-5 support

* Sun Jun 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt6
- new python-module-abiword subpackage (ALT #30134)
- e-d-s support enabled
- built against liblink-grammar.so.5

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt5
- add patches from fedora for porting to librevenge framework

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt4
- updated buildreqs

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- rebuilt against libical.so.1

* Fri Oct 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- fixed http://bugzilla.abisource.com/show_bug.cgi?id=13564

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Nov 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.9.4-alt1
- first build for Sisyphus

