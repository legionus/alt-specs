%define ver_major 3.30

Name: gnome-backgrounds
Version: %ver_major.0
Release: alt1

Summary: A collection of GNOME backgrounds
License: GPLv2
Group: Graphical desktop/GNOME
URL: http://www.gnome.org
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildRequires: meson

%description
The gnome-backgrounds package contains images and tiles
to use for your desktop background which are packaged
with the GNOME desktop.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_datadir/backgrounds/gnome/
%_datadir/gnome-background-properties/*.xml
%doc NEWS README

%changelog
* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Oct 04 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20-alt1
- 3.20

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.91-alt1
- 3.5.91

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Fri Dec 07 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- 2.20.0
- add Packager

* Thu Oct 31 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.0-alt1
- ALTLinux build

