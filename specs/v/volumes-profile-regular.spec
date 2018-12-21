Name: volumes-profile-regular
Version: 0.4
Release: alt1

Summary: Volumes description for ALT Linux Regular builds
License: GPL
Group: System/Configuration/Other

Url: http://en.altlinux.org/regular
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
%summary
(and Starterkits)

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Mar 02 2018 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- e2k support (/boot)

* Tue Nov 28 2017 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Fix profile for disks > 120Gb.

* Fri Nov 17 2017 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Don't create separate /home if disk size <=120Gb.
- Take in account disks in KVM too.
- Don't use RAID in KVM.

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on -lite package)

