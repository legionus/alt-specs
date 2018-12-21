Name: cutecom
Version: 0.40.0
Release: alt1

Summary: A graphical serial terminal
License: GPLv2
Group: Communications

Url: http://cutecom.sourceforge.net
Source: %name-%version.tgz
Patch: cutecom-0.40.0-mga-fixinstall.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Nov 05 2008
BuildRequires: cmake gcc-c++

Summary(pl): Graficzny terminal szeregowy
Summary(ru_RU.UTF-8): Графический последовательный терминал
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: pkgconfig(Qt5Widgets)

# Required for xmodem support
Requires: lrzsz

%description
Cutecom is a graphical serial terminal, like minicom. It is aimed
mainly at hardware developers or other people who need a terminal to
talk to their devices.

%description -l ru_RU.UTF-8
Cutecom - графический последовательный терминал, похожий на minicom.
В основном он предназначен для разработчиков электронной аппаратуры
и для тех, кому нужен терминал для передачи команд устройствам.
Среди его особенностей: строчный интерфейс (в отличие от символьного),
поддержка xmodem, ymodem и zmodem (требуется пакет lrzsz),
шестнадцатеричный ввод/вывод и др.  Cutecom написан с использованием
библиотеки Qt.

%prep
%setup
%patch -p1

%build
PATH=$PATH:%_libdir/qt4/bin
%cmake_insource
%make_build

%install
%makeinstall_std

# Upstream script does not install the .desktop file if KDE is not installed,
# so we install it manually
mkdir -p %buildroot%_desktopdir
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-key=Path --remove-key=Encoding \
	--remove-category=Utility \
	--add-category=System \
	cutecom.desktop

%files
%doc Changelog LICENSE README* TODO
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/hicolor/scalable/apps/cutecom.svg

%changelog
* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 0.40.0-alt1
- 0.40.0
  + Qt5 version
  + use mageia patch and spec bits, drop my patch
- added Russian package description (fixed up debian's one)
- dropped Polish package description
  (couldn't bother converting to UTF-8, sorry)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.22.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cutecom

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 0.22.0-alt1
- 0.22.0
- fixed desktop file (repocop)

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 0.20.0-alt2
- applied repocop patch

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.20.0-alt1
- 0.20.0 (qt4)
- buildreq

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.14.2-alt1
- 0.14.2

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.14.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for cutecom
 * update_menus for cutecom

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 0.14.1-alt1
- 0.14.1
- buildreq

* Wed Mar 01 2006 Michael Shigorin <mike@altlinux.org> 0.13.2-alt1
- initial build for ALT Linux Sisyphus (spec from PLD Team)
  + these PLD people worked on it: blekot, qboosh, bszx
  + they can be reached at <cvs_login>@pld-linux.org
- spec cleanup
- buildreq
