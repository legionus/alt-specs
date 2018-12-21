%define _localstatedir %_var
%define _libexecdir %_prefix/libexec
%define _userunitdir %_prefix/lib/systemd/user

%define xdg_name org.freedesktop.Flatpak
%define api_ver 1.0

# peer to peer support requires ostree >= 2018.2 with experimental/P2P API
%def_disable p2p
%def_enable docs

Name: flatpak
Version: 1.0.6
Release: alt1

Summary: Application deployment framework for desktop apps

Group: Development/Tools
License: LGPLv2.1+
Url: http://flatpak.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/flatpak/flatpak/releases/download/%version/%name-%version.tar.xz
Source: %name-%version.tar

%define ostree_ver 2018.7
%define bwrap_ver 0.2.1
%define libarchive_ver 2.8.0

Requires: lib%name = %version-%release
Requires: %_bindir/fusermount
Requires: %_bindir/bwrap
Requires: bubblewrap >= %bwrap_ver

BuildRequires: gtk-doc gobject-introspection-devel
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libarchive) >= %libarchive_ver
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(ostree-1) >= %ostree_ver
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(xau)
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libgpgme-devel
BuildRequires: udev-rules
BuildRequires: %_bindir/bwrap
BuildRequires: bubblewrap >= %bwrap_ver
BuildRequires: %_bindir/xsltproc
%{?_enable_docs:BuildRequires: %_bindir/xmlto docbook-dtds docbook-style-xsl}
BuildRequires: /proc

%description
Flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package -n lib%name
Summary: Libraries for %name
Group: Development/Other
License: LGPLv2+
Requires: %_bindir/bwrap

%description -n lib%name
This package contains libflatpak.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
License: LGPLv2+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the pkg-config file and development headers for %name.


%prep
%setup

%build
# workaround for collision with new copy_file_range glibc function. remove it when it's no longer needed.
%add_optflags -DHAVE_DECL_COPY_FILE_RANGE
# User namespace support is sufficient.
%configure --with-priv-mode=none \
           --with-system-bubblewrap \
           %{?_enable_docs:--enable-docbook-docs} \
           --with-systemdsystemunitdir=%_unitdir \
           --with-systemduserunitdir=%_userunitdir
%make_build

%install
%makeinstall_std
# The system repo is not installed by the flatpak build system.
install -d %buildroot%_localstatedir/lib/flatpak

%find_lang %name

%post
# Create an (empty) system-wide repo.
%_bindir/flatpak remote-list --system

%files -f %name.lang
%_bindir/%name
%_bindir/%name-bisect
%_bindir/%name-coredumpctl
%_datadir/bash-completion
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/system-services/%xdg_name.SystemHelper.service
# Co-own directory.
%_datadir/gdm/env.d
%_datadir/%name
%_datadir/polkit-1/actions/%xdg_name.policy
%_datadir/polkit-1/rules.d/%xdg_name.rules
%_libexecdir/%name-portal
%_libexecdir/%name-dbus-proxy
%_libexecdir/%name-session-helper
%_libexecdir/%name-system-helper
%dir %_localstatedir/lib/%name
%_man1dir/%{name}*.1*
%_sysconfdir/dbus-1/system.d/%xdg_name.SystemHelper.conf
%_datadir/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
%_datadir/dbus-1/services/org.freedesktop.portal.Flatpak.service
%_sysconfdir/profile.d/%name.sh
%_unitdir/%name-system-helper.service
%_userunitdir/%name-portal.service
%_userunitdir/%name-session-helper.service
%_userunitdir/dbus.service.d
%_man5dir/*
%doc NEWS README.md
%{?_enable_docs:%doc %_docdir/%name/}

%files -n lib%name
%_libdir/lib%name.so.*
%_typelibdir/Flatpak-%api_ver.typelib

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_datadir/dbus-1/interfaces/%xdg_name.xml
%_girdir/Flatpak-%api_ver.gir
%doc %_datadir/gtk-doc/html/%name


%changelog
* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Jun 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.8-alt1
- 0.11.8

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11.7-alt2
- removed -builder subpackage (since 0.9.9 flatpak-builder was split out into separate project)
- updated buildreqs
- removed obsolete metadata-xml.patch

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.7-alt1
- new version 0.11.7 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.11.3-alt1
- new version 0.11.3 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt1
- new version 0.10.4 (with rpmrb script)

* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3.

* Tue Dec 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt2
- move dbus-1/interfaces to libflatpak-devel

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2.1-alt1
- new version 0.10.2.1 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.99-alt1
- new version 0.9.99 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.98.2-alt1
- new version 0.9.98.2 (with rpmrb script)

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version (0.9.7) with rpmgs script

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.11-alt1
- new version 0.6.11 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.8-alt1
- initial build for ALT Linux Sisyphus

* Mon Aug 01 2016 David King <amigadave@amigadave.com> - 0.6.8-1
- Update to 0.6.8 (#1361823)

* Thu Jul 21 2016 David King <amigadave@amigadave.com> - 0.6.7-2
- Use system bubblewrap

* Fri Jul 01 2016 David King <amigadave@amigadave.com> - 0.6.7-1
- Update to 0.6.7

* Thu Jun 23 2016 David King <amigadave@amigadave.com> - 0.6.6-1
- Update to 0.6.6

* Fri Jun 10 2016 David King <amigadave@amigadave.com> - 0.6.5-1
- Update to 0.6.5

* Wed Jun 01 2016 David King <amigadave@amigadave.com> - 0.6.4-1
- Update to 0.6.4

* Tue May 31 2016 David King <amigadave@amigadave.com> - 0.6.3-1
- Update to 0.6.3
- Move bwrap to main package

* Tue May 24 2016 David King <amigadave@amigadave.com> - 0.6.2-1
- Rename from xdg-app to flatpak (#1337434)
