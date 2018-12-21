%define rname kig

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Education
Summary: Interactive Geometry
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 22 2016 (-bi)
# optimized out: boost-python-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms pkg-config python-base python-devel python-modules python3 qt5-base-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers boost-python-devel extra-cmake-modules kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google python3-base qt5-svg-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-xmlpatterns-devel
BuildRequires: boost-devel-headers boost-python-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
Kig is a program for exploring geometric constructions.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kig katepart
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kig
%_K5bin/pykig.py
%_K5plug/kigpart.so
%_K5data/kig/
%_datadir/katepart5/syntax/*-kig.xml
%_K5icon/*/*/apps/kig.*
%_K5icon/*/*/mimetypes/application-x-kig.*
%_K5xmlgui/kig/
%_K5xdgapp/org.kde.kig.desktop
%_K5srv/kig_part.desktop

%changelog
* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Wed Jun 06 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- rebuild with new boost

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
