%define rname ktuberling

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Games/Educational
Summary: "Potato editor" game
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 23 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkdegames-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google python3-base qt5-declarative-devel qt5-phonon-devel qt5-svg-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-svg-devel qt5-multimedia-devel
BuildRequires: qt5-phonon-devel
BuildRequires: kde5-libkdegames-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
KTuberling is a "potato editor" game intended for small
children and adults who remain young at heart. The game
has no winner; the only purpose is to make the funniest
faces you can.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data ktuberling
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/ktuberling
%_K5data/ktuberling/
%_K5xdgapp/org.kde.ktuberling.desktop
%_K5icon/*/*/apps/ktuberling.*
%_K5icon/*/*/mimetypes/application-x-tuberling.*
%_K5xmlgui/ktuberling/

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

* Tue Apr 11 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Fri Sep 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Mon May 16 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
