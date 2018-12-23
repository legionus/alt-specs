%define rname kolf

%define sover 5
%define libkolfprivate libkolfprivate%sover

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Games/Arcade
Summary: Miniature golf
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Source: %rname-%version.tar
Patch1: alt-so-version.patch

# Automatically added by buildreq on Thu Dec 21 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libssl-devel libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gtk-update-icon-cache kde5-libkdegames-devel kf5-kdelibs4support-devel kf5-kio-devel qt5-declarative-devel qt5-phonon-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-phonon-devel
BuildRequires: kde5-libkdegames-devel kf5-kdelibs4support-devel kf5-kio-devel

%description
Kolf is a miniature golf game with 2d top-down view.
Courses are dynamic, and up to 10 people can play at once in competition.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkolfprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkolfprivate
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data kolf
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/kolf
%_K5icon/*/*/apps/kolf.*
%_K5xdgapp/org.kde.kolf.desktop
%_K5data/kolf/
%_K5xmlgui/kolf/

%files -n %libkolfprivate
%_K5lib/libkolfprivate.so.%sover
%_K5lib/libkolfprivate.so.*

%changelog
* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Fri Dec 22 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt2%ubt
- fix package

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- initial build
