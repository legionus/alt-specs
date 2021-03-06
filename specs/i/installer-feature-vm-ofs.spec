Name: installer-feature-vm-ofs
Version: 0.3
Release: alt1

Summary: Installer alterator-vm profile tuning and filesystem layout hooks
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains alterator-vm profile tuning and
filesystem layout hooks for Office Server.

%package stage2
Summary: Installer stage2 alterator-vm profile tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
This package contains alterator-vm profile tuning hook for
Office Server installer stage2.

%package stage3
Summary: Installer stage3 filesystem layout hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage3

%description stage3
This package contains filesystem layout hooks for
Office Server installer stage3.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall}.d
install -pm755 05-* %buildroot%hookdir/initinstall.d/
install -pm755 01-* %buildroot%hookdir/preinstall.d/

%files stage2
%hookdir/initinstall.d/*

%files stage3
%hookdir/preinstall.d/*

%changelog
* Tue Jun 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- 01-move-fs-ofs: Changed symlinking to bindmounting
  (untested; closes: #25786).

* Mon Jun 15 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- 05-vm-profile-ofs: Use feature implemented in alterator-vm-0.4.1-alt8.

* Wed Apr 01 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision based on installer-distro-office-server hooks.
