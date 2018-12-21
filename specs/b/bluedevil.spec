%define _kde_alternate_placement 1

Name: bluedevil
Version: 2.1.1
Release: alt1

Group: Graphical desktop/KDE
Summary: BlueDevil is the new bluetooth stack for KDE4
License: GPL
Url: http://www.kde.org

Provides: kde4-kbluetooth
Obsoletes: kde4-kbluetooth
Provides: kdebluetooth4
Obsoletes: kdebluetooth4
Provides: bluez-pin
Requires: bluez >= 5.0 obexd

# upstream/kdelibs branch
Source: %name-%version.tar
# SuSE
Patch1: typo2.diff

# Automatically added by buildreq on Thu Sep 02 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libbluedevil-devel libqt3-devel libxkbfile-devel qt4-designer rpm-build-ruby
BuildRequires: gcc-c++ glib2-devel glibc-devel kde4libs-devel libbluedevil-devel

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
%description devel
This package contains header files needed if you wish to build applications
based on %name .


%prep
%setup -q
%patch1 -p1

mv altlinux/po ./
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__

%build
%K4build

%install
%K4install

# rename service desktopfiles
find %buildroot/%_K4srv -type f -name \*.desktop | \
while read f
do
    fdir=`dirname "$f"`
    fname=`basename "$f"`
    newfname=`echo "$fname" | sed 's|-|_|g'`
    [ "$fname" == "$newfname" ] || mv "$fdir/$fname" "$fdir/$newfname"
done

%K4find_lang --with-kde %name

%files -f %name.lang
%_kde4_bindir/bluedevil-*
%_K4exec/bluedevil-*
#%_K4libdir/libbluedevilaction.so
#%_K4lib/bluedevil*plugin.so
%_K4lib/bluetoothfileitemaction.so
%_K4lib/kcm_bluedevil*.so
%_K4lib/kded_bluedevil.so
%_K4lib/kded_obexftpdaemon.so
%_K4lib/kio_bluetooth.so
%_K4lib/kio_obexftp.so
#%_K4dbus_services/org.kde.BlueDevil.Service.service
%_kde4_xdg_apps/bluedevil-*.desktop
%_K4apps/bluedevil
%_K4apps/bluedevilwizard
%_K4srv/bluedevil*.desktop
%_K4srv/kded/bluedevil.desktop
%_K4srv/kded/obexftpdaemon.desktop
%_K4srv/obexftp.protocol
%_K4srv/bluetooth.protocol
#%_K4srvtyp/actionplugin.desktop
%_K4xdg_mime/bluedevil-mime.xml


#%files devel
#%_K4includedir/bluedevil/

%changelog
* Fri Apr 24 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Fri Dec 05 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- 2.0 release

* Mon Dec 02 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.1
- bluez5 version

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt0.M70P.1
- built for M70P

* Mon Oct 07 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Mon Mar 18 2013 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Fri Nov 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt0.M60P.1
- built for M60P

* Fri Nov 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt1
- new version

* Mon Jun 25 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt0.M60P.1
- built for M60P

* Wed Jun 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2.M60P.2
- built for M60P

* Mon Feb 06 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt3
- fix requires

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1.M60P.1
- built for M60P

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2
- update from 1.2 branch

* Wed Oct 12 2011 Sergey V Turchin <zerg at altlinux dot org> 1.2.2-alt0.M60P.1
- built for M60P (ATL#26322)

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- new version

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt0.M60P.1
- built for M60P

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Tue May 17 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt2
- obsolete kdebluetooth4

* Fri Apr 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Thu Mar 24 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Tue Feb 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3
- obsolete kde4-kbluetooth

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- fix package translations

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Mon Dec 27 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.4
- update patches and translations from Ubuntu

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.3
- add russian translation

* Tue Sep 28 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.1.M51.1
- built for M51

* Tue Sep 28 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.2
- 1.0-rc4-1

* Fri Sep 10 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.0.M51.1
- built for M51

* Thu Sep 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt0.1
- 1.0-rc3
- initial specfile
