Name: lxqt-openssh-askpass
Version: 0.13.0
Release: alt1

Summary: Used to ask for user/password with GUI for OpenSSH
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel libqtxdg-devel
BuildRequires: kf5-kwindowsystem-devel

Provides: razorqt-openssh-askpass = %version
Obsoletes: razorqt-openssh-askpass < 0.7.0

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

* Tue Feb 10 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-openssh-askpass

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

