Name: xfce4-notes-plugin
Version: 1.8.1
Release: alt2

Summary: Sticky notes plugin for the Xfce panel
Summary(ru_RU.UTF-8): Липкие записки для Xfce.
License: %gpl2plus
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

Url: https://goodies.xfce.org/projects/panel-plugins/%name
# git://git.xfce.org/panel-plugins/xfce4-notes-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfconf-devel xfce4-vala
BuildRequires: libunique-devel

%define _unpackaged_files_terminate_build 1

%description
%name is the sticky notes plugin for the Xfce panel.

%description -l ru_RU.UTF-8
Липкие записки для окружения рабочего стола Xfce.

%prep
%setup
%patch -p1

%build
%xfce4reconf
# GTK+3 build seems broken for now
%configure \
    --disable-static \
	--disable-gtk3 \
	--enable-maintainer-mode \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/*
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/
%_sysconfdir/xdg/autostart/xfce4-notes-autostart.desktop
%_desktopdir/xfce4-notes.desktop

%changelog
* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt2
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Update translations from upstream git.

* Thu Jun 25 2015 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Updated to 1.8.1.

* Mon Apr 20 2015 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Avoid an ambiguous reference for Timeout object.
- Drop obsoleted patch.
- Updated to 1.8.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.7.7-alt5
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFce,XFCE -> Xfce).

* Sat May 05 2012 Mikhail Efremov <sem@altlinux.org> 1.7.7-alt4
- Fix plugin linking.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.7.7-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.7.7-alt2
- Rebuild with xfce4-panel-4.9.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 1.7.7-alt1
- Fix desktop file path.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 1.7.7.

* Thu Aug 12 2010 Denis Koryavov <dkoryavov@altlinux.org> 1.7.6-alt1
- New version.

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.4-alt1
- 1.6.4
- update requires

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.6.3-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.6.2-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.6.1-alt1
- new version
- add watch file

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 1.4.1-alt1.1
- NMU
  + fix build with new intltool

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 1.4.1-alt1
- new version

* Mon Nov 27 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.4-alt1
- new version - 1.4

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.3.99.1-alt1
- 1.3.99.1

* Tue Jan 18 2005 Andrey Astafiev <andrei@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Dec 27 2004 Andrey Astafiev <andrei@altlinux.ru> 0.9.7-alt2
- Rebuilt with libxfcegui4.so.3

* Mon Oct 20 2003 Andrey Astafiev <andrei@altlinux.ru> 0.9.7-alt1
- First version of RPM package for Sisyphus.
