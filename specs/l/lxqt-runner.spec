Name: lxqt-runner
Version: 0.13.0
Release: alt1

Summary: Tool used to launch programs quickly by typing their names
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel qt5-script-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: rpm-build-xdg libqtxdg-devel libmenu-cache-devel
BuildRequires: lxqt-globalkeys-devel
BuildRequires: libpcre-devel libmuparser-devel

Provides: razorqt-runner = %version
Obsoletes: razorqt-runner < 0.7.0

%description
%summary

%prep
%setup

%build
%cmake -DPULL_TRANSLATIONS=OFF \
       -DUPDATE_TRANSLATIONS=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_xdgconfigdir/*/*
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-runner

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

