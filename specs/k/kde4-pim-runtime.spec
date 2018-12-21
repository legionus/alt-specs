
%add_findpackage_path %_kde4_bindir

%def_disable gcc5ready

%define rname kdepim-runtime
%define major 4
%define minor 14
%define bugfix 10
Name: kde4-pim-runtime
Version: %major.%minor.%bugfix
Release: alt3

Group: Graphical desktop/KDE
Summary: KDE Akonadi resources
License: GPLv2
Url: http://www.kde.org

Requires: %name-common = %version-%release
Requires: kde4pimlibs

Provides: kde4-pim-runtime-google = %version-%release
Obsoletes: kde4-pim-runtime-google < %version-%release
Provides: kde4pim-wizards = %version-%release
Obsoletes: kde4pim-wizards < %version-%release
Conflicts: kde4pim-akonadi < 4.8

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
# Upstream
# FC
Patch50: kdepim-runtime-4.4.93-show_akonadi_kcm.patch
# ALT
Patch102: kdepim-4.12.2-alt-akonadi-sqlite3.patch
#
Patch104: kdepim-4.13.0-alt-def-mixedmaildir-path.patch
Patch105: kdepim-4.13.0-alt-migrate-pop3-passwords.patch
Patch106: kdepim-4.7.3-alt-ignore-empty-accounts.patch
Patch107: kdepim-4.13.0-alt-maildir-checks.patch
Patch108: kdepim-4.11.1-alt-def-nepomuk.patch

# Automatically added by buildreq on Tue Feb 09 2010
#BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libassuan-devel libgpgme-devel libindicate-qt-devel libxkbfile-devel soprano soprano-backend-redland xorg-xf86vidmodeproto-devel xsltproc
BuildRequires(pre): kde4libs-devel libassuan-devel
BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4pimlibs-devel libgpgme-devel
#BuildRequires: soprano soprano-backend-redland
BuildRequires: xsltproc grantlee-devel libsasl2-devel
#BuildRequires: dblatex
BuildRequires: libkgapi-devel qjson-devel libkfbapi-devel
BuildRequires: kde4libs-devel kde4pimlibs-devel
BuildRequires: kde4base-workspace-devel
BuildRequires: libcurl-devel
%if_enabled gcc5ready
BuildRequires: libxerces-c-devel libkolab-devel libkolabxml-devel
%endif

%description
This package contains the Akonadi resources from kdepim which can be used without the applications in kdepim.

%package common
Summary: Core files for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdepim-common <= 1:3.5.12-alt1
%description common
Common package for  %name

#%package core
#Summary: Core files for %name
#Group: Graphical desktop/KDE
#Requires: %name-common = %version-%release
#%description core
#Core files for %name

%package -n libkmindexreader4
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libkmindexreader4
KDE 4 library

%package -n libakonadi4-filestore
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libakonadi4-filestore
KDE 4 library

%package -n libmaildir4
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libmaildir4
KDE 4 library

%package -n libkdepim4-copy
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libkdepim4-copy
KDE 4 library

%package -n libakonadi4-xml
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libakonadi4-xml
KDE 4 library

%package -n libkdepim4-runtime-dms-copy
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libkdepim4-runtime-dms-copy
KDE 4 library

%package -n libfolderarchivesettings4
Summary: KDE 4 library
Group: System/Libraries
License: LGPLv2
Requires: %name-common = %version-%release
%description -n libfolderarchivesettings4
KDE 4 library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on kdepim.


%prep
%setup -q -n %rname-%version
%patch50 -p1
#
%patch102 -p2
#
%patch104 -p2
%patch105 -p2
%patch106 -p2
%patch107 -p1
#%patch108 -p1

%build
%K4build \
    -DKDE4_BUILD_TESTS=OFF \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DKDEPIM_BUILD_DESKTOP:BOOL=ON \
    -DKDEPIM_BUILD_MOBILE:BOOL=ON \
    -DAKONADI_INSTALL_PREFIX:STRING=%_prefix

%install
%K4install

%files common
%_K4xdg_mime/accountwizard-mime.xml
%_K4xdg_mime/kdepim-mime.xml
%_K4iconsdir/hicolor/*/*/*
%_K4xdg_mime/x-vnd.akonadi.socialnotification.xml
#%_datadir/ontology/kde/aneo.*

%files
#  mobile
%dir %_K4lib/imports/
%dir %_K4lib/imports/org
%dir %_K4lib/imports/org/kde/
%_K4lib/imports/org/kde/*
#
%_K4bindir/akonadi_*
%_K4bindir/akonaditray
%_K4bindir/accountwizard
%_K4bindir/gidmigrator
%_K4bindir/kaddressbookmigrator
%_K4bindir/kjotsmigrator
%_K4bindir/kmail-migrator
%_K4bindir/knotes-migrator
%_K4bindir/kres-migrator
#%_K4bindir/nepomukpimindexerutility
%_K4lib/accountwizard_plugin.so
%_K4lib/kcal_akonadi.so
%_K4lib/kio_akonadi.so
%_K4lib/kabc_akonadi.so
%_K4lib/akonadi_*
%_K4lib/kcm_akonadi.so
%_K4lib/kcm_akonadi_*.so
%_datadir/akonadi/
%dir %_K4apps/akonadi/
%_K4apps/akonadi/firstrun/
%dir %_K4apps/akonadi/plugins/
%dir %_K4apps/akonadi/plugins/serializer/
%_K4apps/akonadi/plugins/serializer/akonadi_serializer_*.desktop
%_K4apps/akonadi/accountwizard/
%_K4apps/akonadi_*/
#%_K4apps/nepomukpimindexerutility/
%_K4conf/kmail-migratorrc
%_K4conf/kres-migratorrc
%_K4conf/accountwizard.knsrc
%_K4conf_update/*
%_K4start/kaddressbookmigrator.desktop
%_K4xdg_apps/accountwizard.desktop
%_K4xdg_apps/akonaditray.desktop
%_K4srv/akonadi.protocol
%_K4srv/akonadi/davgroupware-providers/
%_K4srv/kcm_akonadi.desktop
%_K4srv/kcm_akonadi_resources.desktop
%_K4srv/kcm_akonadi_server.desktop
%_K4srv/kresources/kabc/akonadi.desktop
%_K4srv/kresources/kcal/akonadi.desktop
#%_K4srv/nepomuk*.desktop
%_K4srvtyp/davgroupwareprovider.desktop
#%_K4srvtyp/akonadinepomukfeeder.desktop

%files -n libkdepim4-copy
%_K4libdir/libkdepim-copy.so.*
%files -n libmaildir4
%_K4libdir/libmaildir.so.*
%files -n libakonadi4-filestore
%_K4libdir/libakonadi-filestore.so.*
%files -n libkmindexreader4
%_K4libdir/libkmindexreader.so.*
%files -n libfolderarchivesettings4
%_K4libdir/libfolderarchivesettings.so.*

%files devel
%_K4link/*.so
#%_K4includedir/*
#%_K4apps/cmake/modules/*
%_K4dbus_interfaces/*


%changelog
* Mon Nov 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt3
- update from 4.14 branch

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt2
- update from 4.14 branch

* Thu Jul 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt1
- new version

* Fri Jun 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt2
- temporary build without libkolab

* Fri Jun 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt1
- new version

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.8-alt1
- new version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt2
- new version

* Thu Mar 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.6-alt1
- new version

* Fri Feb 06 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.5-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.4-alt1
- new version

* Fri Nov 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Tue Oct 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Wed Aug 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Jul 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt2
- built with new libkgapi

* Thu Jul 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Mon May 13 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt2
- update from 4.10 branch

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Fri Mar 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Tue Jan 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Dec 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Mon Nov 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Mon Oct 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Wed Jun 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2.M60P.1
- built for M60P

* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3
- update from 4.8 branch

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update from 4.8 branch

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Mon Mar 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- update from 4.8 branch

* Wed Mar 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt4
- disable mail indexing by default

* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- update from 4.8 branch

* Tue Jan 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- update from 4.8 branch

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- split from kdepim
