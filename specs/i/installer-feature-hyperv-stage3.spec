Name: installer-feature-hyperv-stage3
Version: 0.1
Release: alt3

Summary: Tweak things for a Hyper-V guest system
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
ExclusiveArch: x86_64
Requires: hyperv-daemons

%description
%summary

%prep

%post
for s in bridge cpufreq-simple smartd powertop; do
	chkconfig $s off ||:
done 2>/dev/null

%files

%changelog
* Fri Nov 23 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- restrict to x86_64

* Wed Apr 27 2016 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- don't bail out, it's okay

* Wed Apr 27 2016 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

