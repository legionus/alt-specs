Url: http://www.altlinux.org/Appliances
Name: appliance-base-minimal
Summary: Virtual package that require some essential packages
BuildArch: noarch
Version: 4.0.1
Release: alt3
License: GPL
Group: System/Base

# System
Requires: appliance-base-interactivesystem

Requires: hostinfo
Requires: netlist
Requires: rsync
Requires: shadow-edit
Requires: syslogd-daemon
Requires: vim-console

%description
%summary
This appliance need to be required from every other appliance

%files

%changelog
* Tue Aug 28 2018 Dmitry V. Levin <ldv@altlinux.org> 4.0.1-alt3
- Replaced sysklogd with syslogd-daemon.

* Sun Jun 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- add Url tag

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

