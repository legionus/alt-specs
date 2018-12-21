%set_verify_elf_method unresolved=relaxed

Name: gpsim
Version: 0.30.0
Release: alt1

Summary: Software simulator for Microchip PIC microcontrollers
Summary(ru_RU.UTF-8): Программный эмулятор микроконтроллеров PIC фирмы Microchip

License: GPL
Group: Monitoring
Url: http://gpsim.sourceforge.net/gpsim.html

Source: http://prdownloads.sf.net/%name/%name/%version/%name-%version.tar

Patch3: %name-0.25.0-quit_gui.patch
Patch4: %name-0.25.0-get_version.patch
Patch5: %name-alt-desktop-fix.patch
# Patches sent to mainstream 02.10.2010:
# https://sourceforge.net/tracker/?func=detail&aid=3079981&group_id=2341&atid=302341#
# Updated: cas@ 26.08.2017
Patch6: 0001-fix-linking-with-libgpsim.patch
Patch7: 0002-libgpsim-fix-libdl-linking.patch

BuildRequires: flex gcc-c++ libgtk+extra2-devel libpopt-devel libreadline-devel
BuildRequires: libgtk+extra2-devel >= 2.1.1
BuildRequires: gputils
BuildRequires: desktop-file-utils

%description
gpsim is a full-featured software simulator for Microchip PIC
microcontrollers distributed under the GNU General Public License

gpsim has been designed to be as accurate as possible. Accuracy includes the
entire PIC - from the core to the I/O pins and including ALL of the internal
peripherals. Thus it's possible to create stimuli and tie them to the I/O
pins and test the PIC the same PIC the same way you would in the real world.

%description -l ru_RU.UTF8
gpsim - полноценный программный эмулятор микроконтроллеров PIC фирмы Mircochip,
распространяемый по лицензии GNU General Public License.

gpsim создан с целью быть настолько точным, насколько это возможно. Точность преследуется во всём -
от ядра до точек ввода-вывода, включая всю встроенную периферию. Так, возможно сгенерировать нужные 
входные сигналы и связать их с контактами ввода-вывода и протестировать микроконтроллер PIC в эмуляторе 
в точности таким же образом, как вы бы делали это с точно таким же настоящим микроконтроллером.

%package devel
Summary: Header files, libraries and development documentation for %name
Summary(ru_RU.UTF-8): Заголовочные файлы, библиотеки и документация разработчика для %name
Group: Development/Libraries
Requires: %name = %version-%release

%description devel
This package contains the header files and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%description devel -l ru_RU.UTF8
В этом пакете содержатся заголовочные файлы, библиотеки и документация разработчика для %name,
вам потребуется установить пакет %name-devel.

%package -n lib%name
Summary: Main library for %name
Summary(ru_RU.UTF-8): Главная библиотека для %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with libgpsim

%description -n lib%name -l ru_RU.UTF8
Этот пакет содержит необходимые библиотеки для запуска программ, динамически скомпонованных с libgpsim

%package -n lib%name-devel
Summary: Headers for developing programs that will use libgpsim
Summary(ru_RU.UTF-8): Заголовочные файлы для разработки программ, использующих libgpsim
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use libgpsim

%description -n lib%name-devel -l ru_RU.UTF8
В этом пакете содержатся заголовочные файлы для разработки программ, использующих libgpsim

%prep
%setup
%patch3
%patch4
%patch5 -p2
%patch6 -p2
%patch7 -p2

%build
%autoreconf
%configure --disable-static --enable-sockets
%make_build

%install
%makeinstall

# I really don't know why they are not stripped by rpmbuild
strip %buildroot%_bindir/%name %buildroot%_libdir/*.so.*

# install appdata, desktop file and icon
install -Dm 644 doc/metadata/gpsim.appdata.xml %buildroot%_datadir/appdata/gpsim.appdata.xml
install -Dm 644 doc/metadata/gpsim.desktop %buildroot%_desktopdir/gpsim.desktop
install -Dm 644 doc/metadata/gpsim.png %buildroot%_pixmapsdir/gpsim.png

%files
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%files -n lib%name
%doc ANNOUNCE AUTHORS COPYING COPYING.LESSER ChangeLog HISTORY NEWS
%doc README README.EXAMPLES README.MODULES TODO
%doc doc/gpsim.lyx doc/gpsim.pdf doc/gpsim.ps
%doc examples/
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Jul 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.30.0-alt1
- New version
- Adapt and use upstream appdata, desktop file and icon

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 0.29.0-alt1
- New version

* Wed Feb 11 2015 Andrey Cherepanov <cas@altlinux.org> 0.28.1-alt1
- New version

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25.0-alt1.qa2
- Fixed build with new glib2

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.25.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gpsim

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.25.0-alt1
- new version (0.25.0) import in git
- update buildreqs
- add spec translation (ALT bug #22157)

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.24.0-alt1
- 0.24.0
- fixed exit_gpsim (patch merged from FC)

* Fri Feb 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt2
- fix build on PPC (thanks, Sergey Bolshakov)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt1
- fix build with gcc4.3
- replace menu file with desktop file

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt0.1
- new version 0.22.0 (with rpmrb script)
- update as-needed patch

* Sat Jul 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.21.11-alt0.2
- add patch from http://ktechlab.org/download/gpsim.php
- fix gcc4 & as-needed issues
- disable verify elf due crossreferencing in libs

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.21.11-alt0.1
- new version (gtk2 build enable)
- fix source

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.21.4-alt0.1
- new version (still gtk1 - gtk2 build is broken)

* Mon Feb 14 2005 Vitaly Lipatov <lav@altlinux.ru> 0.21.2-alt0.2
- add update menu, fix menu section

* Mon Jan 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.21.2-alt0.1
- first build for ALT Linux Sisyphus

* Mon Jan 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.21.2-1 #2827
- Initial package.
