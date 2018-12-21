%define rname kdiagram

%define kchart_sover 2
%define libkchart libkchart%kchart_sover
%define kgantt_sover 2
%define libkgantt libkgantt%kgantt_sover


Name: kf5-%rname
Version: 2.6.0
Release: alt1%ubt
%K5init

Group: System/Libraries
Summary: KDE business diagrams libraries
Url: http://www.kde.org
License: GPLv2+

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
# Automatically added by buildreq on Tue Mar 14 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-printsupport libqt5-sql libqt5-svg libqt5-widgets libstdc++-devel perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires: extra-cmake-modules qt5-svg-devel

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

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

%package -n %libkchart
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkchart
KF5 library

%package -n %libkgantt
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkgantt
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files devel
%_K5inc/*_version.h
%_K5inc/KChart/
%_K5inc/KGantt/
%_K5link/lib*.so
%_K5lib/cmake/KChart/
%_K5lib/cmake/KGantt/
%_K5archdata/mkspecs/modules/qt_*.pri

%files -n %libkchart
%_K5lib/libKChart.so.%kchart_sover
%_K5lib/libKChart.so.*
%files -n %libkgantt
%_K5lib/libKGantt.so.%kgantt_sover
%_K5lib/libKGantt.so.*

%changelog
* Tue Mar 14 2017 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1%ubt
- initial build
