%define K_if_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define K_if_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define K_if_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define K_if_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define rpm_ver %{get_SVR rpm}

Name: kde-common-devel
Version: 14.12.1
Release: alt1

Group: Development/KDE and QT
Summary: Development utils for KDE
License: GPL
Url: http://www.altlinux.org

BuildArch: noarch

Requires: rpm-utils

Source11: macrosd
Requires: rpm-macros-%name = %version-%release

%description
Development utils for Menu system

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# uncomment if macroses are platform-neutral
#BuildArch: noarch
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: kde-common-devel <= 4.3.0-alt1

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE11 %buildroot/%_rpmmacrosdir/%name

%files

%files -n rpm-macros-%name
%_rpmmacrosdir/%name

%changelog
* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Fri Dec 26 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- add mt language to list

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.0-alt1
- new version
- turn off build verbosity by default

* Tue Sep 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.0-alt1
- new version

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- don't use own find_lang because rpm find_lang was fixed

* Fri Feb 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt3
- fix to install python files in python prefix

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update languages list

* Fri Dec 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- bump version

* Mon Sep 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- bump version

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- set default CMAKE_BUILD_TYPE to Release (-g provided by rpm flags)

* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- fix to build with rpm-4.0.4-alt100.51

* Sun Feb 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Wed Oct 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- fix changelog

* Thu Sep 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt0.M60P.1
- built for M60P

* Thu Sep 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt1
- fix find KDE4 includes

* Thu May 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- fix requires

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- fix SOUND_INSTALL_DIR AUTOSTART_INSTALL_DIR XDG_DIRECTORY_INSTALL_DIR
  for Kcmake macro

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- fix Kbuild macro

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt5
- install kde3 locolor icons to alternate place

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt4
- add K3find_lang macro
- remove _iskde macro support (added Kcmake Kmake Kinstall macroses)

* Thu Feb 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- add new KDE3 placement macroses

* Thu Feb 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- compile with -DDBUS_SYSTEM_SERVICES_INSTALL_DIR

* Wed Jan 26 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- bump version

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- add K3configure macro

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- use uniprocessor make in K3make

* Tue Nov 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- initial support of K3* macroses
- allow to build non-kde apps via K4* macroses

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- bump release

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- build for M51

* Mon Apr 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- add _kde_langlist macro
- allow _K4build with _K4cmake's arguments

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- add _K4dbus_system macro

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- fix typo when using _K4xdg_apps macros

* Thu Jan 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- deprecate macroses started with '__'

* Thu Jan 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- move macroses to special package

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- use %%_libexecdir/kde4/bin for default binaries path

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- install docs always to kde4 data dir

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt0.M50.1
- built for M50

* Mon May 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- add _K4link macros for directory contains linking libraries
- move linking libraries to _K4link by default

* Mon Feb 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- add more search library paths

* Fri Jan 16 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- fix cmake files at install to find kde libraries at %_libdir/kde4link

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt2
- allow define build type via _K4buildtype (Debug/Release/RelWithDebInfo/MinSizeRel)

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- remove debug output from K4cmake

* Mon Sep 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt2
- bump release

* Mon Sep 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- fix to don't break macroses in cmake files

* Thu May 29 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- don't add RPATH to shared libraries by default

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- add K4find_lang

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt5
- add kde link dir to all lib search paths

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt4
- move KDE4 internal xdg/menus, data to alternate placement

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt3
- rename K4configure to K4cmake

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt2
- change docs alternate placement

* Wed Feb 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- add KDE4 macroses

* Wed May 30 2007 Sergey V Turchin <zerg at altlinux dot org> 0.3.2-alt1
- change _Kconfig macros to /etc/kde/share/config

* Tue Oct 24 2006 Sergey V Turchin <zerg at altlinux dot org> 0.3.1-alt1
- fix _K_if_ver_*

* Mon Oct 16 2006 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- add version compariosion macroses

* Thu Dec 15 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- add new macroses

* Tue Mar 09 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- initial spec
