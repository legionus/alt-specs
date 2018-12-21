%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-common-internals
Name: kde4-ktp-common-internals
Version: 0.9.0
Release: alt2

Group: Graphical desktop/KDE
Summary: Common internals for KDE Telepathy
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 03 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libtelepathy-qt4 libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libtelepathy-qt4-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel libdbus-glib-devel
BuildRequires: libtelepathy-glib-devel libtelepathy-qt4-devel
BuildRequires: libtelepathy-logger-devel telepathy-logger-qt4-devel
BuildRequires: kde4libs-devel kde4pimlibs-devel libkpeople-devel
BuildRequires: libotr5-devel libgcrypt-devel
BuildRequires: kde-common-devel

%description
%summary.

%package common
Summary: Common files for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common files for %rname

%package core
Summary: Core files for %name
Group: System/Libraries
Requires: %name-common = %version-%release
Requires: libkpeople-core
%description core
Core files for %name

%package -n libktpcommoninternalsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpcommoninternalsprivate4
%name library.

%package -n libktpmodelsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpmodelsprivate4
%name library.

%package -n libktpwidgetsprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpwidgetsprivate4
%name library.

%package -n libktploggerprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktploggerprivate4
%name library.

%package -n libktpotrprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpotrprivate4
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libtelepathy-qt4-devel
Requires: libtelepathy-logger-devel telepathy-logger-qt4-devel
%description devel
%summary.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

# fix paths in ontology descriptions
find %buildroot/%_datadir/ontology -type f -name \*.ontology | \
while read f
do
    sed -i 's|Path=.*/share/ontology/\(.*\.trig\)|Path=%_datadir/ontology/\1|' "$f"
done


%files common -f %rname.lang
%_kde4_iconsdir/hicolor/*/actions/im-*.*
%_kde4_iconsdir/hicolor/*/actions/sort-*.*
%_kde4_iconsdir/hicolor/*/actions/show-offline.*
%_kde4_iconsdir/hicolor/*/apps/telepathy-kde.*
%_K4apps/ktelepathy/
#%dir %_datadir/ontology/telepathy/
#%_datadir/ontology/telepathy/*

%files core
%_K4exec/ktp-proxy
%_K4lib/imports/org/kde/telepathy/
%_K4lib/*plugin.so
%_K4lib/ktploggerplugin_tplogger.so
%_K4cfg/ktp-proxy-config.kcfg
#%_K4lib/nepomuktelepathyservice.so
%_K4srv/*plugin.desktop
%_K4srv/ktploggerplugin_tplogger.desktop
#%_K4srv/nepomuktelepathyservice.desktop
%_K4srvtyp/ktp_logger_plugin.desktop
%_K4dbus_services/org.freedesktop.Telepathy.Client.KTp.Proxy.service
%_datadir/telepathy/clients/KTp.Proxy.client

%files  -n libktpcommoninternalsprivate4
%_K4libdir/libktpcommoninternalsprivate.so.*
%files  -n libktpmodelsprivate4
%_K4libdir/libktpmodelsprivate.so.*
%files  -n libktpwidgetsprivate4
%_K4libdir/libktpwidgetsprivate.so.*
%files  -n libktploggerprivate4
%_K4libdir/libktploggerprivate.so.*
%files  -n libktpotrprivate4
%_K4libdir/libktpotrprivate.so.*

%files devel
%_K4apps/katepart/syntax/*
%_kde4_bindir/ktp-debugger
%_K4link/lib*.so
%_K4includedir/KTp/

%changelog
* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- rebuild with new libgcrypt

* Fri Oct 31 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M70P.1
- built for M70P

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Wed May 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt0.M70P.1
- built for M70P

* Tue May 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M70P.1
- built for M70P

* Wed Mar 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt0.M70P.1
- built for M70P

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt0.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt0.M70P.1
- built for M70P

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version

* Thu Jun 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Fri May 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Wed Apr 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
