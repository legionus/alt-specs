%define rname akonadi-notes

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: System/Libraries
Summary: Management of notes in Akonadi
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Aug 26 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-widgets libqt5-xml libstdc++-devel perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-devel kde5-kmime-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules qt5-base-devel
BuildRequires: kde5-akonadi-devel kde5-kmime-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel

%description
Libraries and daemons to implement management of notes in Akonadi.

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

%package -n libkf5akonadinotes
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadinotes
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K5inc/akonadi-notes_version.h
%_K5inc/Akonadi/Notes/
%_K5inc/akonadi/notes/
%_K5link/lib*.so
%_K5lib/cmake/KF5AkonadiNotes/
%_K5archdata/mkspecs/modules/qt_AkonadiNotes.pri

%files -n libkf5akonadinotes
%_K5lib/libKF5AkonadiNotes.so.*

%changelog
* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Aug 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- initial build
