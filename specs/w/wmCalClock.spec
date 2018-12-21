Name: wmCalClock
Version: 1.25
Release: alt10

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: wmCalClock is a simple Calendar Clock for Window Maker
Summary(ru_RU.KOI8-R): �����������, �� ����� ������� ���� ��� Window Maker

Url: http://dockapps.windowmaker.org/file.php/id/9
License: GPL
Group: Graphical desktop/Window Maker

Source0: http://nis-www.lanl.gov/~mgh/WindowMaker/%name-%version.tar.bz2
Source1: %name.menu

# Automatically added by buildreq on Sun Mar 05 2006
BuildRequires: libX11-devel libXext-devel libXpm-devel xorg-proto-devel

%description
wmCalClock is a simple Calendar Clock that uses anti-aliased characters and
drop shadows. Doesnt do much except tell time...

%description -l ru_RU.KOI8-R
�����������, �� ����� ������� ���� ��� Window Maker. ���������� c����������
������� � ����.

%prep
%setup

%build
%make_build -C Src INCDIR= LIBDIR=

%install
install -D -pm755 Src/%name %buildroot%_bindir/%name
install -D -pm644 Src/%name.1 %buildroot%_man1dir/%name.1
install -D -pm644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc BUGS CHANGES HINTS INSTALL README TODO
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Tue Oct 15 2013 Michael Shigorin <mike@altlinux.org> 1.25-alt10
- fixed menu file
- minor spec cleanup
- updated the Url: (dockapps.org is no more, hail d.w.o)

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 1.25-alt9
- updated BR:

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.25-alt8.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmCalClock
  * postclean-05-filetriggers for spec file

* Sun Mar 05 2006 Alexey Voinov <voins@altlinux.ru> 1.25-alt8
- fixed build with new xorg
- menu file updated [/usr/X11R6 -> usr]
- url updated 
- buildreqs updated

* Thu Jun 24 2004 Alexey Voinov <voins@altlinux.ru> 1.25-alt7
- removed hourly beep from default settings. [fix for #3277]

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.25-alt6
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Tue May  8 2001 Alexey Voinov <voins@voins.program.ru>
- conditional NoSource added.

* Fri May  4 2001 Alexey Voinov <voins@voins.program.ru>
- automatic buildreqs added

* Sun Apr 15 2001 Alexey Voinov <voins@voins.program.ru>
- menu file added
- documentation files added

* Thu Apr 12 2001 Alexey Voinov <voins@voins.program.ru>
- rebuild for MDK Spring 2001
- description/summary translated

* Fri Feb 17 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

