%define rname kscreenlocker

%def_disable seccomp

%define sover 5
%define libkscreenlocker libkscreenlocker%sover

Name: plasma5-%rname
Version: 5.14.4
Release: alt1
Epoch: 1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Screen Locker
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Source10: pam-kf5-screenlocker
Patch1: alt-def-screenlocker.patch
Patch2: alt-greeter-path.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-x11extras-devel
BuildRequires: libpam-devel libwayland-client-devel libwayland-server-devel
%if_enabled seccomp
BuildRequires: libseccomp-devel
%endif
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel

Provides: kf5-kscreenlocker = %EVR
Obsoletes: kf5-kscreenlocker < %EVR

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-kscreenlocker-common = %EVR
Obsoletes: kf5-kscreenlocker-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-kscreenlocker-devel = %EVR
Obsoletes: kf5-kscreenlocker-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkscreenlocker
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkscreenlocker
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DKDE4_KSCREENSAVER_PAM_SERVICE="kf5-screenlocker" \
    -DKDE_KSCREENSAVER_PAM_SERVICE="kf5-screenlocker" \
    -DKSCREENSAVER_PAM_SERVICE="kf5-screenlocker" \
    #

%install
%K5install
%K5install_move exec all
%K5install_move data kconf_update ksmserver
%find_lang %name --all-name

# Install kde pam configuration files
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE10 %buildroot/%_sysconfdir/pam.d/kf5-screenlocker

%files common -f %name.lang
%doc COPYING

%files
%config(noreplace) %_sysconfdir/pam.d/kf5-screenlocker
%_K5exec/*
%attr(2711,root,chkpwd) %_K5exec/kcheckpass
%_K5plug/screenlocker_kcm.so
%_K5data/ksmserver/screenlocker/
#%_K5data/plasma/kcms/screenlocker_kcm/
%_K5conf_up/k*reenlock*
%_K5notif/*.notifyrc
%_K5srv/*.desktop

%files devel
#%_K5inc/kscreenlocker_version.h
%_K5inc/KScreenLocker/
%_K5link/lib*.so
%_K5lib/cmake/KScreenLocker/
%_K5lib/cmake/ScreenSaverDBusInterface/
%_K5dbus_iface/*ScreenSaver*.xml
#%_K5archdata/mkspecs/modules/qt_KScreenLocker.pri

%files -n %libkscreenlocker
%_K5lib/libKScreenLocker.so.*
%_K5lib/libKScreenLocker.so.%sover

%changelog
* Fri Dec 07 2018 Andrey Bychkov <mrdrew@altlinux.ru> 1:5.14.4-alt1
- Version updated to 5.14.4

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.12.7-alt1.qa1
- NMU: applied repocop patch

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2%ubt
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-kscreenlocker -> plasma5-kscreenlocker

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt3%ubt
- build without seccomp support again

* Thu Oct 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2%ubt
- build with fixed seccomp support

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Thu Aug 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt3%ubt
- build without seccomp support

* Mon Aug 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt2%ubt
- build with seccomp support

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Fri Mar 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt3%ubt
- fix changelog

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt2.S1
- update from 5.9 branch

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Sat Feb 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- update from 5.5 branch

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Wed Dec 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt2
- fix lock screen (ALT#31661)

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Thu Dec 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
