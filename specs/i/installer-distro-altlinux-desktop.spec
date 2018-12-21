Name: installer-distro-altlinux-desktop
Version: 8.1.0
Release: alt1

Summary: Installer configuration (desktop)
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

Packager: Michael Shigorin <mike@altlinux.org>

%description
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution.

It is derived from installer-distro-altlinux-generic.

%package stage2
Summary: Installer configuration and scripts (stage2 part)
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
# modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-vm-altlinux-generic-stage2
Requires: x-cursor-theme-jimmac

%description stage2
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPL
Group: System/Configuration/Other
Provides: installer-altlinux-generic-stage3 = %name-%version
#Requires: installer-stage3
# modules
# FIXME: grub/lilo
#Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-luks
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
#Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution.

The stage3 part is installed onto the new system's root
and executed off there during installation process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/*.d/*

%files stage3

%changelog
* Mon Oct 31 2016 Michael Shigorin <mike@altlinux.org> 8.1.0-alt1
- synced default groups with current alterator-users
- added 'vmusers' to those as well (for libvirt)

* Tue Apr 19 2016 Michael Shigorin <mike@altlinux.org> 8.0.0-alt1
- carried over 80-setup-user-groups from installer-distro-centaurus

* Mon Dec 23 2013 Michael Shigorin <mike@altlinux.org> 7.0.0-alt1
- initial release based on installer-distro-altlinux-generic 7.0.1-alt1
