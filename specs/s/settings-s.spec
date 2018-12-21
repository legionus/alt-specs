Name:     settings-s
Version:  0.1
Release:  alt2

Summary:  settings for custom distro
License:  GPLv2
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/settings-s.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
Requires:  checker

%description
These are settings for custom distro.

%package -n integ
Summary: integrity checker settings
Group: System/Configuration/Other

%description -n integ
Integrity check setup only

%prep
%setup

%install
mkdir -p %buildroot/usr/share/install2/postinstall.d/
mkdir -p %buildroot/sbin
mkdir -p %buildroot/lib/systemd/system
install -Dm 0700 65-settings.sh  %buildroot/usr/share/install2/postinstall.d/
install -Dm 0700 integalert.service %buildroot/lib/systemd/system/
install -Dm 0700 integalert %buildroot/sbin



%files
/usr/share/install2/postinstall.d/65-settings.sh

%files -n integ
/lib/systemd/system/integalert.service
/sbin/integalert

%post

%post -n integ


%changelog
* Fri Aug 17 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt2
- build for sisyphus

* Wed Mar 28 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.15
- grub is modified adding option in some other place. Removed
addition of duplicated entry

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.14
- fixed delimiters

* Mon Mar 26 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.13
- removed perl parts of settings

* Thu Mar 22 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.12
- fixed place of postinstall.d

* Wed Mar 21 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.11
- moved to postinstall.d, added features from branding

* Thu Mar 01 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.10
- separated to two packets: general settings and integrity service
Removed rhosts from skel: it harms selinux settings.

* Thu Jan 18 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.9
- integrity check strictly before user login now

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.8
- added "Before" to  unit to make it start before DM

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.7
- changed wanted to required in unit

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.6
- added alerting on integrity checks on boot

* Wed Dec 13 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.5
- added fixed rhosts, added dependency to custom settings checker

* Mon Dec 11 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.3
- Updated settings

* Fri Dec 01 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.2
- fixed permissions

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt0.M80C.1
- backport to c8

* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt1
Initial release
