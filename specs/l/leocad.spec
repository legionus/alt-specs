Summary: Visual brick construction tool for kids
Summary (ru_RU.UTF-8): Детский конструктор, использующий блоки с шипами
Name: leocad
Version: 18.02
Release: alt1

License: GPL
Url: http://www.leocad.org
Source: %name-%version-src.tgz
Group: Games/Puzzles
Packager: Fr. Br. George <george@altlinux.ru>

Source1: %name.desktop

# Automatically added by buildreq on Mon Aug 26 2013
# optimized out: fontconfig libGL-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libstdc++-devel zlib-devel
BuildRequires: gcc-c++ phonon-devel

BuildPreReq: rpm-build-xdg

Requires: %name-data > 3000

%description
LeoCAD is a CAD program that uses bricks similar to those found in many
toys (but they don't represent any particular brand). Currently it has
a library of more than 1000 different pieces. LEGO is a trademark of the
LEGO Group of companies which does not sponsor, authorize or endorse
this software.

%description -l ru_RU.UTF-8
LeoCAD -- программа для конструирования чего угодно из блоков с шипами.
В прилагаемой библиотеке таких блоков содержится более 1000 различных
видов. Блоки похожи на те, что используются некоторыми фирмами,
производящими разборные игрушки. LEGO -- торговая марка группы компаний
LEGO, которые не спонсируют и не курируют LeoCAD, а также не имеют
авторских прав на эту программу.

%prep
%setup -n %name

%build
#make PREFIX=/usr
%qmake_qt4
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_iconsdir/*/*/*/*
%_pixmapsdir/%name.png
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_xdgmimedir/packages/*

%changelog
* Mon Jun 04 2018 Grigory Ustinov <grenka@altlinux.org> 18.02-alt1
- Rebuild, because of version number mistake in previous build (Closes: #34479).

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 18.01-alt1
- Build new version (Closes: #34479).

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 0.80.1-alt1
- Autobuild version bump to 0.80.1

* Mon Aug 26 2013 Fr. Br. George <george@altlinux.ru> 0.80-alt1
- Autobuild version bump to 0.80
- Fix build (upstream switched to Qt)

* Mon Mar 25 2013 Fr. Br. George <george@altlinux.ru> 0.79.3-alt1
- Autobuild version bump to 0.79.3
- Fix build

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.2
- Rebuilt with libpng15

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.1
- Fixed build

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt5
- fixed build:  added libGL-devel to BR:
- .desktop file cleanup

* Sun Mar 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4.1
- completely useless work (thanks to at@)

* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4
- added libpng-devel to BuildRequires: (thanks to at@)

* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 0.75-alt3
- [Igor Vlasenko] updated source from 0.75 branch (closes #22831)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.75-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for leocad
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75-alt2
- GCC4.4 build fixup

* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT

