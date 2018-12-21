%define rname kirigami2

Name: kf5-kirigami
Version: 5.53.0
Release: alt1
%K5init

Group: System/Libraries
Summary: A QtQuick based components set
Url: https://techbase.kde.org/Kirigami
License: LGPLv2

Requires: %name-common = %version-%release
Requires: qt5-quickcontrols2 qt5-graphicaleffects

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-quickcontrols2-devel
BuildRequires: qt5-svg-devel qt5-tools-devel
BuildRequires: kf5-kpackage-devel kf5-kservice-devel kf5-kwindowsystem-devel
#BuildRequires: kf5-plasma-framework-devel

%description
Kirigami is a set of QtQuick components at the moment targeted for mobile use
(in the future desktop as well) targeting both Plasma Mobile and Android. It's
not a whole set of components, all the "Primitive" ones like buttons and
textboxes are a job for QtQuickControls (soon QtQuickControls2) but it's a set
of high level components to make the creation of applications that look and feel
great on mobile as well as desktop devices and follow the
https://community.kde.org/KDE_Visual_Design_Group/KirigamiHIG . The target of
those components is anybody that wants to do an application using QtQuick as its
main UI, especially if targeting a mobile platform, without adding many
dependencies. They work on a variety of platforms, such as Plasma Mobile,
Desktop Linux, Android and Windows. It will eventually become a Tier-1 KDE
Framework.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %version-%release
%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name

%package -n libkf5kirigami2
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kirigami2
KF5 library

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%files
%_K5qml/org/kde/kirigami.2/

%files devel
%_K5link/lib*.so
%_K5inc/Kirigami2/
%_libdir/cmake/KF5Kirigami2/
%_K5archdata/mkspecs/modules/qt_Kirigami2.pri

%files -n libkf5kirigami2
%_K5lib/libKF5Kirigami2.so.*

%changelog
* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1%ubt
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1%ubt
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1%ubt
- new version

* Tue Apr 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt2%ubt
- update from 5.45

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt2%ubt
- cleanup specfile

* Wed Aug 16 2017 Stanislav Levin <slev@altlinux.org> 5.37.0-alt1%ubt
- Updated to newest upstream version

* Thu Aug 03 2017 Levin Stanislav  <slev@altlinux.org> 2.2.0-alt1%ubt
- Initial build

