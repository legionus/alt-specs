Name: installer-feature-quota-stage2
Version: 0.6.1
Release: alt1

Summary: Setup quota on local filesystems
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer stage2 hook to setup quota
on local filesystems.

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Oct 29 2014 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Don't skip /var if there is no OVZ.

* Tue Jul 01 2014 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- Setup quota for all supported filesystems.

* Wed Dec 05 2012 Andriy Stepanov <stanv@altlinux.ru> 0.5-alt1
- Migrate from ext3 to ext4. vm-profiles by default crates Ext4.

* Mon Jun 15 2009 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Changed hook to handle ovz filesystems.

* Tue May 26 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Changed hook to avoid failure in case of quota manipulation errors.

* Tue May 26 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Changed from stage3 to stage2.

* Thu May 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
