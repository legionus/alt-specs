%define ver_major 3.11

Name: alacarte
Version: %ver_major.91
Release: alt1

Summary: Menu editor for GNOME
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source1: %name-icons.tar.bz2
BuildArch: noarch

# use python3
#AutoReqProv: nopython
#%define __python %nil

%define menus_ver 3.5.3

BuildPreReq: intltool >= 0.40
BuildPreReq: libgnome-menus-devel >= %menus_ver
#BuildRequires: rpm-build-python3 python3-module-pygobject3-devel
BuildRequires: python-module-pygobject3-devel
BuildRequires: docbook-dtds docbook-style-xsl xsltproc

%description
Alacarte is a menu editor for GNOME using the freedesktop.org menu
specification.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%python_sitelibdir_noarch/Alacarte/
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/%name.1.*
%doc README AUTHORS NEWS

%changelog
* Mon Mar 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.91-alt1
- 3.11.91

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- 3.7.90

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.5-alt1
- 3.5.5

* Fri Jun 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4
- removed XFCE specific patches

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.2-alt2.1
- Rebuild with Python-2.7

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.13.2-alt2
- Make alacarte able to work in Xfce (closes: #26344).

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt2
- build as noarch

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Mon May 04 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Sun Mar 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.11.10-alt1
- 0.11.10
- removed obsolete %%{update,clean}_menus
- removed unneeded icons
- updated {build,}reqs

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.6-alt1
- 0.11.6

* Thu Aug 07 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.5-alt3
- remove noarch

* Sun Aug 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.5-alt1
- Initial build for ALTLinux

