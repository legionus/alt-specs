%define _kde_alternate_placement 1

Name: kde4-webkitpart
Version: 1.3.4
Release: alt2
Epoch: 1

Group: Networking/WWW
Summary: WebKit render engine for Konqueror
License: LGPLv2+
Url: https://projects.kde.org/projects/extragear/base/kwebkitpart

#Requires: libkwebkit4 = %version-%release
Provides: kde4-kwebkitpart = %EVR

Source0: kwebkitpart-%version.tar
Patch1: sanitize-html.patch

BuildRequires: gcc-c++ kde4libs-devel

%description
A HTML kparts component based on WebKit

%package devel
Group: Development/KDE and QT
Summary: WebKit render engine for Konqueror
%description devel
A HTML kparts component based on WebKit

%package -n libkwebkit4
Summary: KDE 4 library
Group: System/Libraries
Epoch: 0
%description -n libkwebkit4
KDE 4 library


%prep
%setup -q -n kwebkitpart-%version
%patch1 -p1

sed -i '/add_subdirectory(kdelauncher)/d' CMakeLists.txt

for f in icons/*-webkit.png; do mv $f `echo $f| sed "s|-webkit\.png$|-kwebkit.png|"`; done
sed -i "s|^Icon=.*|Icon=kwebkit|" src/kwebkitpart.desktop


%build
%K4build


%install
%K4install
%K4find_lang --with-kde kwebkitpart


%files -f kwebkitpart.lang
%_K4lib/kwebkitpart.so*
%_kde4_iconsdir/hicolor/*/apps/kwebkit.*
%_K4apps/kwebkitpart/
%_K4srv/kwebkitpart.desktop

#%files -n libkwebkit4
#%_K4libdir/libkwebkit.so.*

#%files devel
#%_K4link/*.so
#%_K4includedir/*
#%_K4apps/cmake/modules/*.cmake

%changelog
* Fri May 15 2015 Sergey V Turchin <zerg@altlinux.org> 1:1.3.4-alt2
- security fix: CVE-2014-8600

* Wed Oct 08 2014 Sergey V Turchin <zerg@altlinux.org> 1:1.3.4-alt0.M70P.1
- built for M70P

* Wed Oct 08 2014 Sergey V Turchin <zerg@altlinux.org> 1:1.3.4-alt1
- new version

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 1:1.3.3-alt0.M70P.1
- built for M70P

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 1:1.3.3-alt1
- new version

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 1:1.3.2-alt1
- new version

* Thu Nov 29 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.3.1-alt1
- new version

* Mon Sep 24 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.3.0-alt1
- new version

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 1:1.2.0-alt0.0.M60P.1
- built for M60P

* Tue Nov 15 2011 Sergey V Turchin <zerg@altlinux.org> 1:1.2.0-alt0.1
- 1.2.0 git20111019

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1:1.1.0-alt1
- new version

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 1:0.9.6-alt2
- fix packaging

* Fri Aug 20 2010 Sergey V Turchin <zerg@altlinux.org> 1:0.9.6-alt0.M51.1
- built for M51

* Thu Aug 19 2010 Sergey V Turchin <zerg@altlinux.org> 1:0.9.6-alt1
- 0.9.6

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 1:0.4-alt0.M51.1
- build for M51

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 1:0.4-alt1
- update for KDE-4.4

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt0.2
- svn r962657

* Tue Apr 07 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.2-alt0.1
- initial specfile
- svn r947598
