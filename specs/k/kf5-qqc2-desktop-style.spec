%define rname qqc2-desktop-style

Name: kf5-%rname
Version: 5.53.0
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 visual style
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Source: %rname-%version.tar
Patch: alt-test.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-quickcontrols2-devel qt5-x11extras-devel
BuildRequires: kf5-kauth-devel kf5-kcoreaddons-devel kf5-kconfigwidgets-devel kf5-kiconthemes-devel kf5-kirigami-devel

%description
QtQuickControls 2 style that uses QWidget's QStyle for painting

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-filesystem
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %rname-%version
%patch -p1

%build
%K5build

%install
%K5install

%files
%_K5qml/QtQuick/Controls.2/org.kde.desktop/
%_K5qml/org/kde/qqc2desktopstyle/
%_K5plug/kf5/kirigami/*.so

%files devel
%_libdir/cmake/KF5QQC2DeskopStyle/

%changelog
* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Thu Sep 06 2018 Oleg Solovyov <mcpain@altlinux.org> 5.49.0-alt2%ubt
- fix: clipped text

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

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Wed Dec 13 2017 Oleg Solovyov <mcpain@altlinux.org> 5.40.0-alt2%ubt
- fix files

* Tue Dec 12 2017 Oleg Solovyov <mcpain@altlinux.org> 5.40.0-alt1%ubt
- initial
