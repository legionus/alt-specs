%define _userinitdir %(pkg-config systemd --variable systemduserunitdir)

%def_enable snapshot
%define _libexecdir %_prefix/libexec

Name: gnome-remote-desktop
Version: 0.1.6
Release: alt1

Summary: GNOME Remote Desktop
Group: Networking/Remote access
License: GPLv2+
Url: https://gitlab.gnome.org/jadahl/gnome-remote-desktop

%if_disabled snapshot
Source: https://gitlab.gnome.org/jadahl/gnome-remote-desktop/uploads/7d3cc32efb12ca84284532f947487067/gnome-remote-desktop-0.1.2.tar.xz
%else
# VCS: https://gitlab.gnome.org/jadahl/gnome-remote-desktop.git
Source: %name-%version.tar
%endif

%define pipewire_ver 0.2.1
%define vnc_ver 0.9.11
%define gst_ver 1.10

Requires: pipewire >= %pipewire_ver

BuildRequires(pre): meson
BuildRequires: pkgconfig(libpipewire-0.2) >= %pipewire_ver
BuildRequires: libgio-devel libvncserver-devel >= %vnc_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-video-1.0) >= %gst_ver
BuildRequires: libsecret-devel libnotify-devel  libsystemd-devel

%description
Remote desktop daemon for GNOME using pipewire.

%prep
%setup
sed -i -e 's/\(pipewire-0.\)1/\12/' meson.build

%build
%meson -Dsystemd_user_unit_dir=%_userinitdir
%meson_build

%install
%meson_install

%files
%_libexecdir/%name-daemon
%_userinitdir/%name.service
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%doc README

%changelog
* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Sun Jun 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- fixed build with meson-0.43

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

