Name: libxfcegui4
Version: 4.10.0
Release: alt6

Summary: Various Gtk+2 widgets for Xfce
Summary (ru_RU.UTF-8): Набор виджетов GTK 2 для Xfce
License: %lgpl2plus
Group: Graphical desktop/XFce
Url: https://www.xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: https://git.xfce.org/archive/libxfcegui4
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfconf-devel
BuildRequires: gtk-doc intltool libSM-devel libglade-devel libgtk+2-devel libstartup-notification-devel xorg-cf-files

%define _unpackaged_files_terminate_build 1

%description
Various Gtk+2 widgets for Xfce.
It has been superseded by the libxfce4ui library.

%description -l ru_RU.UTF-8
Набор виджетов GTK 2 для Xfce

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
Header files for the %name library.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--disable-gtk-doc \
	--enable-startup-notification \
	--disable-gladeui \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%_libdir/*.so.*
%_libdir/libglade/2.0/libxfce4.so
%exclude %_libdir/libglade/2.0/libxfce4.*a
%_iconsdir/hicolor/scalable/apps/*.svg
%_liconsdir/*.png

%files devel
%_includedir/xfce4/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Fri Oct 19 2018 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt6
- Enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Updated for modern autotools.
- Use xfce_textdomain().

* Thu Mar 12 2015 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt5
- Disable development documentation build.
- Disable libgladeui support.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt4
- Fix Xfce name (XFce,XFCE -> Xfce).
- Rebuild with libxfce4util-4.12.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- Replace xfce_setenv() with g_setenv().

* Tue Dec 04 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Rebuild against libgladeui-1.so.11.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Drop obsoleted patches.
- Updated from upstream git (37af67a03f).
- Updated to 4.9.0.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Add patch from upstream for xfce-4.10 support.

* Mon Mar 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Added patches from Debian:
    + Call thunar instead of xftree4 which doesn't exist anymore.
    + Allow icon names with dots.
- Fix linking while doc generating.
- Updated to 4.8.1.

* Wed Jan 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Update description.
- Don't build static libraries.
- Fix group.
- Fix license.

* Sat Jan 08 2011 Mikhail Efremov <sem@altlinux.org> 4.6.4-alt1
- Slightly spec cleanup and updated.
- Updated to 4.6.4.

* Tue Jan 12 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.2-alt1
- New version.

* Tue Jan 05 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Fix build with gtkdocize.

* Sun May 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation updated

* Tue May 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt0.M50.2
- Russian translation updated

* Sun Apr 26 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt0.M50.1
- Backport to Desktop 5.0

* Sun Apr 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Mon Oct 20 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Wed Sep 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.3-alt1.1
- Rebuilt for new pkg-config dependencies.

* Mon Nov 14 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed Sep 14 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.2-alt2
- Fix bug with gtk > 2.8

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2
- Do not package %name-devel-static by default.

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt2
- *.la files removed.

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 11 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
