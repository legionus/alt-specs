%define _unpackaged_files_terminate_build 1

Summary: A popular and easy to use graphical IRC (chat) client
Name: hexchat
Version: 2.14.2
Release: alt1
License: GPLv2+
Group: Networking/IRC
Url: https://hexchat.github.io

# https://github.com/hexchat/hexchat.git
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(lua)
BuildRequires: perl-devel perl(ExtUtils/Embed.pm)

Requires: enchant2

Provides: xchat = %EVR
Obsoletes: xchat
Provides: xchat2 = %EVR
Obsoletes: xchat2

%description
HexChat is an easy to use graphical IRC chat client for the X Window System.
It allows you to join multiple IRC channels (chat rooms) at the same time,
talk publicly, private one-on-one conversations etc. Even file transfers
are possible.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains the development files for %name.

%prep
%setup

%build
%meson -Dwith-lua=lua
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING readme.md
%_bindir/hexchat
%dir %_libdir/hexchat
%dir %_libdir/hexchat/plugins
%_libdir/hexchat/plugins/checksum.so
%_libdir/hexchat/plugins/fishlim.so
%_libdir/hexchat/plugins/lua.so
%_libdir/hexchat/plugins/sysinfo.so
%_libdir/hexchat/plugins/perl.so
%_libdir/hexchat/plugins/python.so
%_desktopdir/*.desktop
%_iconsdir//hicolor/*/apps/%name.*
%_datadir/metainfo/*.appdata.xml
%_datadir/dbus-1/services/org.hexchat.service.service
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*

%changelog
* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.14.2-alt1
- Initial build for ALT.
