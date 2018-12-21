%define base gdm-theme
%define _name flowers

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GDM2 theme - Flowers
Summary(ru_RU.UTF-8): Тема для GDM2 - Цветы
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gdm/
Source: %_name.tar.gz
BuildArch: noarch
Requires: gdm

%description
Theme with Flowers.

%description -l ru_RU.UTF-8
Цветочная тема.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_datadir/gdm/themes/%_name
%__cp -r * %buildroot%_datadir/gdm/themes/%_name

%files
%_datadir/gdm/themes/*

%changelog
* Thu Oct 31 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.0-alt1
- 1st build, translation

