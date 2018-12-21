%define _localstatedir /var
#Use GTK+ instead of Xlib
%def_with gtk

Name: spice-vdagent
Version: 0.18.0
Release: alt1%ubt
Summary: Agent for Spice guests
Group: Networking/Remote access
License: GPLv3+
Url: http://spice-space.org/

# VCS-git: https://gitlab.freedesktop.org/spice/linux/vd_agent.git
Source: %name-%version.tar
Source2: spice-vdagentd.init-alt
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: pkgconfig(glib-2.0) >= 2.34
%{?_with_gtk:BuildRequires: pkgconfig(gtk+-3.0) >= 3.10}
BuildRequires: pkgconfig(xfixes) pkgconfig(xrandr) >= 1.3 pkgconfig(xinerama) pkgconfig(x11)
BuildRequires: pkgconfig(spice-protocol) >= 0.12.13
BuildRequires: pkgconfig(alsa) >= 1.0.22
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(pciaccess) >= 0.10
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(systemd) pkgconfig(libsystemd) >= 209
BuildRequires: pkgconfig(udev)

%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    %{subst_with gtk} \
	--with-session-info=auto \
	--with-init-script=systemd+redhat

%make_build

%install
%makeinstall_std
install -m 0755 %SOURCE2 %buildroot%_initdir/spice-vdagentd

%post
%post_service spice-vdagentd

%preun
%preun_service spice-vdagentd

%files
%doc COPYING ChangeLog README TODO NEWS
/lib/udev/rules.d/*.rules
/lib/tmpfiles.d/spice-vdagentd.conf
%_initddir/spice-vdagentd
%_unitdir/*
%_bindir/spice-vdagent
%_sbindir/spice-vdagentd
%_var/run/spice-vdagentd
%_sysconfdir/xdg/autostart/spice-vdagent.desktop
%_datadir/gdm/autostart/LoginWindow/spice-vdagent.desktop
%_datadir/gdm/greeter/autostart/spice-vdagent.desktop
%_man1dir/*

%changelog
* Mon Jul 09 2018 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1%ubt
- 0.18.0
- Use GTK+ instead of Xlib

* Thu Jun 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1.git7d858d
- upstream git snaphot 7d858d5064fd0c26454b72bf9fe3e0472f31e34f

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Apr 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
