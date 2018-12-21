%define rname ksmtp

%define sover 5
%define libkpimsmtp libkpimsmtp%sover

Name: kde5-%rname
Version: 18.04.3
Release: alt1%ubt
%K5init

Group: Graphical desktop/KDE
Summary: A job-based API for interacting with SMTP servers
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 22 2018 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-kmime-devel kf5-ki18n-devel kf5-kio-devel libsasl2-devel libssl-devel python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libsasl2-devel libssl-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel
BuildRequires: kde5-kmime-devel

%description
This library provides a job-based API for interacting with an SMTP server.

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

%package -n %libkpimsmtp
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkpimsmtp
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*.*categories

%files devel
%dir %_includedir/KPim/
%_includedir/KPim/ksmtp_version.h
%_includedir/KPim/KSMTP/
%_K5link/lib*.so
%_K5lib/cmake/KPimSMTP/
%_K5archdata/mkspecs/modules/qt_KSMTP.pri

%files -n %libkpimsmtp
%_K5lib/libKPimSMTP.so.*
%_K5lib/libKPimSMTP.so.%sover

%changelog
* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Feb 22 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- initial build
