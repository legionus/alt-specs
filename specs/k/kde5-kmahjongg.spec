%define rname kmahjongg

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Games/Boards
Summary: A tile laying patience
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 04 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-kwidgetsaddons-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkdegames-devel kde5-libkmahjongg-devel kf5-kcompletion-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-knewstuff-devel kf5-kpackage-devel kf5-kservice-devel kf5-kxmlgui-devel python-module-google python3-dev qt5-svg-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel
BuildRequires: kde5-libkdegames-devel kde5-libkmahjongg-devel
BuildRequires: kf5-kcompletion-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-knewstuff-devel kf5-kpackage-devel kf5-kservice-devel kf5-kxmlgui-devel

%description
KMahjongg is a fun board game created after the famous oriental game of Mahjong.
Unlike the original however, KMahjongg is a tile matching game for one player,
a variation usually known as Mahjong Solitaire.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kmahjongg
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kmahjongg
%_K5data/kmahjongg/
%_K5xmlgui/kmahjongg/
%_K5xdgapp/*kmahjongg*.desktop
%_K5cfg/*kmahjongg*
%_K5icon/*/*/apps/*kmahjongg*

%changelog
* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
