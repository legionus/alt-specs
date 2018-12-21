%define ver_major 1.5
%define _libexecdir %_prefix/libexec

Name: gnome-epub-thumbnailer
Version: %ver_major
Release: alt1

Summary: Thumbnailer for EPub and MOBI books
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: libgio-devel libgdk-pixbuf-devel libxml2-devel libarchive-devel >= 3.1

%description
This package provides a thumbnailer for EPub and MOBI books files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gnome-mobi-thumbnailer
%_datadir/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%_datadir/thumbnailers/gnome-mobi-thumbnailer.thumbnailer
%doc README AUTHORS NEWS

%changelog
* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Mon Jul 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Wed Jul 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Sun Jul 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus

