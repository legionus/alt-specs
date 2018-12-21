Name: wmtunlo
Version: 0.1.3
Release: alt2

Summary: Booooring 2d tunnel Dockapp.
Group: Graphical desktop/Window Maker
License: GPL

URL: http://clay.ll.pl/dockapps.html

Source: %name-%version.tar.gz
Source1: %name.menu

# Automatically added by buildreq on Sat Apr 09 2005
BuildRequires: libXt-devel libXext-devel libXpm-devel

%description
Boring 2d tunnel Dockapp

%prep
%setup

%build
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS COPYING README Changelog examples/*
%_bindir/%name
%_menudir/%name

%changelog
* Tue Oct 15 2013 Michael Shigorin <mike@altlinux.org> 0.1.3-alt2
- fixed menu file to reference %_bindir/%name
- minor spec cleanup

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1.1.qa1
- Disclosure xorg-devel build requirement

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmtunlo

* Tue Jul 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.1.3-alt1
- Initial build for Sisyphus.

