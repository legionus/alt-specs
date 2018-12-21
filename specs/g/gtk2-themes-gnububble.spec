%define base gtk2-themes
%define _name gnububble

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GTK+2 theme - Gnu Bubble
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gtk2/

Source: %name.tar.gz

BuildArch: noarch
Requires: gtk-engines-pixmap

%description
GTK2 theme based on bluebubble and ideas from AquaGraphite (GTK+-1.2
theme). This theme is meant to give an Aqua feel to things without being
another clone.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_datadir/themes/%_name
%__cp -r gtk-2* %buildroot%_datadir/themes/%_name

%files
%_datadir/themes/*
%doc README

%changelog
* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0-alt1
- First build for Sisyphus.
