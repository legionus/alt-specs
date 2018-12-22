%define rname kimagemapeditor

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Development/Other
Summary: An HTML imagemap editor
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 20 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libssl-devel libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gtk-update-icon-cache kf5-kdelibs4support-devel kf5-khtml-devel kf5-kio-devel kf5-kjs-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdelibs4support-devel kf5-khtml-devel kf5-kio-devel kf5-kjs-devel

%description
An HTML imagemap editor.

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

%package -n libkf5imagemapeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5imagemapeditor
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kimagemapeditor
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*.*categories
%_K5bin/kimagemapeditor
%_K5plug/kimagemapeditor.so
%_K5xdgapp/org.kde.kimagemapeditor.desktop
%_K5icon/*/*/actions/*.*
%_K5icon/*/*/apps/kimagemapeditor.*
%_K5data/kimagemapeditor/
%_K5srv/kimagemapeditorpart.desktop
%_K5xmlgui/kimagemapeditor/

%changelog
* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- initial build
