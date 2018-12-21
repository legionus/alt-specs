%define ver_major 3.18

# Enable parallel-installability with autoconf-archive,
# by disabling installation of its M4 macros
%def_with autoconf_archive

Name: gnome-common
Version: %ver_major.0
Release: alt1

Summary: Gnome-common contains useful things common to building gnome packages
License: GPLv2+
Group: Development/GNOME and GTK+
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

%{?_with_autoconf_archive:Requires: autoconf-archive}

%description
gnome-common is for building various GNOME modules from VCS.
It is not needed to run GNOME.

%prep
%setup

%build
%autoreconf
%configure %{?_with_autoconf_archive:--with-autoconf-archive}
%make_build

%install
%makeinstall_std

%files
%_bindir/gnome-autogen.sh
%_datadir/aclocal/gnome-common.m4
%_datadir/aclocal/gnome-compiler-flags.m4
%_datadir/aclocal/gnome-code-coverage.m4

%if_without autoconf_archive
%_datadir/aclocal/ax_check_enable_debug.m4
%_datadir/aclocal/ax_code_coverage.m4
%endif

%doc README ChangeLog

%changelog
* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0
- removed obsolete alt-no-libtool-check.patch

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.91-alt1
- 3.5.91

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Wed Nov 11 2009 Alexey Rusakov <ktirf@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon May 25 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.0-alt2
- moved to git.
- added autoreconf invocation (due to using original sources).
- cherry-picked automake 1.11 support from the upstream head
  (fixes ALT Bug 20169).

* Fri Mar 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version (2.20.0)
- add Packager

* Tue May 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)

* Fri Sep 23 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- un-checking of libtool.m4 is now a patch.

* Thu Sep 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt1
- Merged in some changes from CVS.

* Fri Feb 25 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1.1
- some fixes from cvs.
- don't check libtool.m4.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0
- remove gnomedesktop2mdkmenu.pl from sources.

* Mon Apr 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- updated from cvs.

* Fri Oct 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Sep 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt0.6
- requires automake_1.4 to build.

* Mon Jun 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt0.5
- 2.3.0 cvs snapshot.

* Wed May 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt3
- Added gnomedesktop2mdkmenu.pl a perl script to create menu files from
  desktop files. Now it is a copy of kdedesktop2mdkmenu.pl from
  kdelibs-devel package.

* Mon Nov 11 2002 AEN <aen@altlinux.ru> 1.2.4-alt2
- new pilot patch from MDK

* Mon Feb 04 2002 AEN <aen@logic.ru> 1.2.4-alt1
- built for Sisyphus

* Mon Jan 14 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-3mdk
- Patch0: Add gnome-pilot missing macros

* Mon Jan  7 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-2mdk
- Clean specfile (with help of Abel Cheung <maddog@linux.org.hk>) :
 - Corrected Source URL
 - No need for post and postun
 - Removed unnecessary BuildRequires
 - Don't use configure macro

* Fri Jan  4 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.4-1mdk
- Initial Mandrake package

