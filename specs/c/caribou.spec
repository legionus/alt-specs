%def_enable snapshot

%define _libexecdir %prefix/libexec
%define ver_major 0.4
%define api_ver 1.0
%def_enable gtk2_module
%def_enable gtk3_module

Name: caribou
Version: %ver_major.22
Release: alt0.1

Summary: A simplified in-place on-screen keyboard
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://live.gnome.org/Caribou

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch:  %name-0.4.22-change_autostart_cinnamon.patch
Patch1: %name-0.4.20-fix-python-exec.patch
Patch2: %name-0.4.22-alt-russian_layouts.patch
Patch4: %name-0.4.2-use-reserved-bar-keycode.patch
Patch5: %name-0.4.2-fix-keys.patch

Provides: on-screen-keyboard
Requires: lib%name = %version-%release
Requires: lib%name-gir = %version-%release

%define gee_ver 0.8

BuildRequires(pre): rpm-build-python3 rpm-build-gir
%{?_enable_gtk2_module:BuildRequires: libgtk+2-devel}
%{?_enable_gtk3_module:BuildRequires: libgtk+3-devel libgtk+3-gir-devel}
BuildPreReq: libgee-devel >= %gee_ver
BuildRequires: libat-spi2-core-devel libclutter-devel libxklavier-devel libXtst-devel
BuildRequires: gobject-introspection-devel python3-module-pygobject3-devel libxml2-devel
BuildRequires: intltool xsltproc gnome-doc-utils vala-tools >= 0.13

%description
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

%package -n lib%name
Summary: Caribou library
Group: System/Libraries

%description -n lib%name
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

This package contains Caribou library.

%package -n lib%name-devel
Summary: Development files for Caribou
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and headers files for
developing applications that use Caribou.

%package -n lib%name-gir
Summary: GObject introspection data for the Caribou
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Caribou library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Caribou
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Caribou library.

%prep
%setup
%patch -p1 -b .cinnamon
%patch1 -p1 -b .python_exec
%patch2 -p1 -b .rus
%patch4 -p2 -b .res_keycode
#%%patch5 -p2

%build
%autoreconf
%configure --disable-static \
	%{?_disable_gtk2_module:--disable-gtk2-module} \
	%{?_disable_gtk3_module:--disable-gtk3-module} \
	PYTHON=%__python3

# Clean generated C files:
%make clean

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name-preferences
%_libexecdir/%name
%_datadir/%name
%_datadir/antler/
%_datadir/dbus-1/services/org.gnome.Caribou.Antler.service
%_datadir/dbus-1/services/org.gnome.Caribou.Daemon.service
%_libexecdir/antler-keyboard
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_datadir/glib-2.0/schemas/org.gnome.antler.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%_libdir/gnome-settings-daemon-3.0/gtk-modules/%name-gtk-module.desktop
%{?_enable_gtk2_module:%_libdir/gtk-2.0/modules/lib%name-gtk-module.so}
%{?_enable_gtk3_module:%_libdir/gtk-3.0/modules/lib%name-gtk-module.so}
%python3_sitelibdir_noarch/%name/
%doc NEWS README

%exclude %_libdir/gtk-*/modules/lib%name-gtk-module.la

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/lib%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/Caribou-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Caribou-%api_ver.gir

%changelog
* Sat Aug 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.22-alt0.1
- updated to 0.4.21-60-gec9041b, switched to Python3
- caribou-autostart.desktop changed as gnome-shell has it's own OSK

* Fri Jul 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.21-alt1
- 0.4.21

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.20-alt1
- 0.4.20

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt1
- 0.4.19

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.18.1-alt1
- 0.4.18.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.18-alt1
- 0.4.18

* Mon Feb 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.17-alt1
- 0.4.17

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.16-alt1
- 0.4.16

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.15-alt1
- 0.4.15

* Wed Nov 20 2013 Paul Wolneykien <manowar@altlinux.org> 0.4.13-alt1
- Fresh up to v0.4.13.

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Tue Dec 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Tue Nov 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.4.2-alt1
- 0.4.4.2

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Thu May 03 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4.2-alt2
- Fix Escape key, add "^" symbol to "touch" and "fullscale" layouts.
- Use patch for singleton daemon.
- Use patch for proper input of the bar ("|") symbol.
- Re-generate C files from Vala.

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Feb 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2
- built module for gtk2
- fixed pythonpath
- russian layouts for touch and fullscale modes (ALT #26934)

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Thu Oct 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Sep 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- first build for Sisyphus

