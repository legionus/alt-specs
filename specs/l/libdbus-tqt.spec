Name: libdbus-tqt
Version: 3.5.13.2
Release: alt1.1
Summary: TQT/KDE bindings for D-Bus
URL: http://dbus.freedesktop.org/
License: GPL-1.0-only or AFL-1.1
Group: System/Libraries

Source0: dbus-tqt-%version.tar

# Automatically added by buildreq on Mon Dec 18 2006
BuildRequires: gcc-c++ libXext-devel libXt-devel libdbus-devel libjpeg-devel libpng-devel libtqt-devel cmake kde-common-devel

%description
TQT/KDE bindings for D-Bus.

%package devel
Summary: Developer package for TQT/KDE bindings for D-Bus
Requires: %name = %version-%release
Requires: libdbus-devel >= 0.94
Requires: libtqt-devel
Group: Development/C++

%description devel
Developer package for TQT/KDE bindings for D-Bus.

%prep
%setup -q -n dbus-tqt-%version

%build
%Kbuild -DCMAKE_BUILD_TYPE=RelWithDebInfo -DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir

%install
%Kinstall

%files
%_libdir/*.so.*

%files devel
%_includedir/dbus-1.0/dbus/*.h
%_pkgconfigdir/dbus-tqt.pc
%_libdir/*.so

%changelog
* Thu Oct 29 2015 Andrey Cherepanov <cas@altlinux.org> 3.5.13.2-alt1.1
- Rebuilt for gcc5 C++11 ABI

* Sun Jun 23 2013 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.2-alt1
- Release TDE version 3.5.13.2

* Mon Oct 29 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.1-alt2
- Build with -O2 and -g.

* Sun Oct 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.1-alt1
- Release TDE version 3.5.13.1

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- Initial build for TDE 3.5.13
