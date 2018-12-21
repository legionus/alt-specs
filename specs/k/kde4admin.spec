%add_findpackage_path %_kde4_bindir


%define rname kdeadmin
Name: kde4admin
%define major 4
%define minor 14
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Administrative Tools
URL: http://www.kde.org
License: GPL
Packager: Sergey V Turchin <zerg at altlinux dot org>

Requires: %name-kcron = %version-%release
Requires: %name-ksystemlog = %version-%release
Requires: kde4-print-manager

#Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar.bz2
Source: %rname-%version.tar
# ALT
Patch11: kdeadmin-4.6.0-alt-def-ksystemlog.patch

# Automatically added by buildreq on Thu Dec 20 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel openssh-common phonon-devel pkg-config python-base ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: cvs gcc-c++ git-core glib2-devel kde4libs-devel libicu libqt3-devel mercurial python-module-distribute rpm-build-ruby subversion valgrind xorg-xf86miscproto-devel zlib-devel-static
BuildRequires(pre): kde4pimlibs-devel
BuildRequires: gcc-c++ kde4base-runtime-devel >= %version kde4pimlibs-devel >= %version

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
- kcron: editor for the cron command scheduler.
- kdat: tape backup tool.
- kfile-plugins: make Konquerer display additional info on about *.dep and *.rpm files.
- ksysv: an editor for System V startup schemes.
- ksystemlog: a system log viewer tool.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
%description common
%name common package

%package kuser
Group: Graphical desktop/KDE
Summary:  Users and groups manager
Requires: %name-common = %version-%release
%description kuser
Kuser is a tool to create, remove and modify user accounts and groups.

%package kcron
Group:      Graphical desktop/KDE
Summary:    Graphical task scheduler
Requires: %name-common = %version-%release
%description kcron
Kcron is a graphical frontend to the cron system, used to schedule regular 
tasks on a Unix system.

%package ksystemlog
Group: Monitoring
Summary:  System log viewer tool for KDE4
Requires: %name-common = %version-%release
Provides: ksystemlog = %version-%release
Obsoletes: ksystemlog < %version-%release
%description ksystemlog
This program is developed for being used by beginner users,
which don't know how to find information about their Linux system,
and how the log files are in their computer.
But it is also designed for advanced users,
who want to quickly see problems occuring on their server.

%package knetworkconf
Group: Graphical desktop/KDE
Summary: KDE Control Center module to configure network
Requires: %name-common = %version-%release
%description knetworkconf
KNetworkConf is a KDE Control Center module to configure TCP/IP settings on a 
Linux machine.

%package liloconfig
Group:      Graphical desktop/KDE
Summary:    Configure lilo
Requires: %name-common = %version-%release
%description liloconfig
lilo-config is a kcontrol plugin for configuring LILO, the most commonly
used Linux boot loader.

%package print
Summary: Configure new printers
Group: System/Configuration/Printing
URL: http://utils.kde.org/projects/printer-applet
Requires: %name-common = %version-%release
Requires: kde4base-runtime printer-testpages
Requires: python-module-kde4 >= %version
%description print
Utility to configure new printers.

%prep
%setup -q -n %rname-%version
#
%patch11 -p1

ls -d1 * | \
while read d
do
    [ "$d" != "altlinux" ] || continue
    [ -d "$d" ] || continue
    echo "add_subdirectory($d)" >> CMakeLists.txt
done

%build
NO_BUILD+=" -DBUILD_kuser=FALSE"
NO_BUILD+=" -DBUILD_lilo-config=FALSE"
NO_BUILD+=" -DBUILD_knetworkconf=FALSE"
NO_BUILD+=" -DBUILD_kpackage=FALSE"
%K4cmake $NO_BUILD
%K4make

%install
%K4install



%files
%files common
#exclude %_K4doc/*/kpackage
#exclude %_K4doc/*/kuser
#exclude %_K4doc/*/kcontrol/knetworkconf
#exclude %_K4doc/*/lilo-config

%files kcron
%doc kcron/README kcron/TODO
%_K4srv/kcm_cron.desktop
%_K4lib/kcm_cron.so
%_K4doc/*/kcron

%files ksystemlog
%_K4bindir/ksystemlog
%_K4apps/ksystemlog
#%_K4iconsdir/hicolor/*/apps/ksystemlog.*
%_K4xdg_apps/ksystemlog.desktop
%_K4doc/*/ksystemlog


%changelog
* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Thu Dec 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Mon Sep 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Thu Jun 23 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt3
- fix to start printer configuration

* Tue Jun 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt2
- remove printer configuration from systemsettings

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Mon Apr 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt3
- add patch for smb printer browser

* Tue Mar 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- move to standart place
- obsolete ksystemlog

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1.M51.1
- built for M51

* Wed Apr 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- fix printer config menu entry

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Tue Feb 16 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt2
- fix printer configurator startup

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Mon Dec 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2.M51.1
- built for M51

* Mon Dec 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt3
- set default paths to logfiles for ksystemlog

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1.M51.1
- new built for M51

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- add menu entry for printing setup

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Fri Nov 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Thu Oct 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt3
- update system-config-printer files from 1.1.13

* Thu Oct 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt2
- fix find ALT Linux printer testpages (ALT#22026)

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Fri Oct 24 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile

