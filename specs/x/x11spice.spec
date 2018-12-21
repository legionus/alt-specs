Name: x11spice
Version: 1.1.0
Release: alt3
Summary: x11spice connects a running X server as a Spice server
Group: Networking/Remote access
License: GPLv3
Url: https://gitlab.com/spice/x11spice/
Source0: %name-%version.tar

Patch1: %name-alt-show-ip-address.patch
Patch2: %name-allow-access-in-config.patch

BuildRequires(pre): rpm-build-xdg
BuildRequires: libxcb-devel libxcbutil-devel libgtk+3-devel libspice-server-devel libpixman-devel libaudit-devel

%description
It owes a debt to the excellent x11vnc project,
from the libvncserver project. That project proved that
this could be done, and done well.  Some of the logic,
notably that of scan.c, was inspired by the code in x11vnc.

%prep
%setup
%patch1 -p2
%patch2 -p2

%build
%ifarch %ix86
#hack, excuse me, plz
export CFLAGS="-Wno-error=address -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -Wno-format"
%endif
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%config(noreplace) %_xdgconfigdir/%name
%_bindir/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_man1dir/*

%changelog
* Thu Dec 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Run with password spicey and allow control by default.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Show IP address(es) in dialog.

* Wed Feb 28 2018 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

