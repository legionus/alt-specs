Name: polkit-sysvinit
Version: 0.3.4
Release: alt2

Summary: Allow media/network changes to xgrp users
License: ALT-Public-Domain
Group: System/Configuration/Hardware

Url: http://altlinux.org/sysvinit
Source0: 60-sysvinit-mount.rules
Source1: 60-sysvinit-nm.rules
Source2: 60-xfsm-shutdown-helper.rules
Source3: 60-sysvinit-console-kit.rules
Source4: 60-xfce4-pm-helper.rules
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
AutoReqProv: no
Requires: polkit

%define pkdir %_sysconfdir/polkit-1/rules.d

%description
%summary
on SysVinit-based systems.

%prep

%install
mkdir -p %buildroot%pkdir
install -pm644 %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %buildroot%pkdir

%files
%pkdir/*

%changelog
* Thu Jul 13 2017 Anton Midyukov <antohami@altlinux.org> 0.3.4-alt2
- Added missing empty string to the end of xfce4-pm-helper

* Wed Jul 12 2017 Anton Midyukov <antohami@altlinux.org> 0.3.4-alt1
- Added rules for xfce4-pm-helper (thx Speccyfighter)

* Mon Feb 06 2017 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt1
- Added rules for ConsoleKit2

* Tue Dec 06 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt3
- R: polkit

* Fri Nov 04 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt2
- built for sisyphus (closes: #31501)

* Fri Aug 12 2016 Yury Pakin <zxwarior@yandex.ru> 0.3.2-alt1
- fixed: absence of LF at the end of file 60-sysvinit-mount.rules

* Thu May  5 2016 Yury Pakin <zxwarior@yandex.ru> 0.3.1-alt1
- added 60-sysvinit-console-kit.rules

* Sat Mar 12 2016 Daniil Golovanov <dangolan@yandex.ru> 0.3-alt1
- change 60-sysvinit-mount.rules (thx Speccyfighter)

* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added xfsm-shutdown-helper rule (thx Speccyfighter)

* Sat Mar 14 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thx sem@)

