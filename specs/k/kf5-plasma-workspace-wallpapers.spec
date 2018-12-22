%define rname plasma-workspace-wallpapers

Name: kf5-%rname
Version: 5.5.4
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Wallpapers
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

BuildArch: noarch

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Oct 06 2015 (-bi)
# optimized out: cmake cmake-modules libqt5-core libstdc++-devel python-base python3 python3-base
#BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%files
%doc COPYING*
%_datadir/wallpapers/*

%changelog
* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Fri Dec 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- initial build
