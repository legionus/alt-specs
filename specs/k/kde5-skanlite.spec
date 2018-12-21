%define rname skanlite

Name: kde5-%rname
Version: 2.1.0
Release: alt1%ubt
%K5init

Group: Graphics
Summary: Image scanning application
Url: http://www.kde.org
License: GPLv2+

#Requires: hplip-sane

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Feb 01 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base xml-common xml-utils zlib-devel
#BuildRequires: extra-cmake-modules kde5-libksane-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libpng-devel python-module-google qt5-base-devel rpm-build-python3 ruby ruby-stdlibs zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libpng-devel
BuildRequires: kde5-libksane-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Skanlite is a simple image scanning application that does nothing more
than scan and save images. It can open a save dialog for every image
scanned or save the images immediately in a specified directory
with auto-generated names and format.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc src/COPYING*
%_K5bin/skanlite
%_K5xdgapp/org.kde.skanlite.desktop

%changelog
* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1%ubt
- new version

* Mon Oct 31 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt0.M80P.1
- build for M80P

* Mon Oct 31 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1
- initial build
