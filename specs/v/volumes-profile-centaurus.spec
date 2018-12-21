Name: volumes-profile-centaurus
Version: 0.12
Release: alt1

Summary: Volumes description for Centaurus distribution
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch

%description
Volumes description for Centaurus distribution

%prep
%setup

%install
%define hook1dir %_datadir/install2/initinstall.d
%define hook2dir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hook1dir
install -pm755 10-*.sh %buildroot%hook1dir/
mkdir -p %buildroot%hook2dir
install -pm755 20-*.sh %buildroot%hook2dir/

%files
%hook1dir/*
%hook2dir/*

%changelog
* Tue Aug 14 2018 Michael Shigorin <mike@altlinux.org> 0.12-alt1
- e2k support (/boot)

* Wed Dec 14 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.11-alt1
- even space for rootfs and even more on real hardware for desktops

* Fri Dec 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.10-alt1
- more space for rootfs and even more on real hardware

* Fri Mar 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- server and workstation profiles reordered

* Wed Sep 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- make usable inb hasher (while livecd building)

* Tue Sep 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt2
- more / space for server

* Wed Aug 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- bind directories only if server autopartitioning have used

* Thu Aug 11 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- bind directories

* Wed Aug 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- don't move directories

* Tue Feb 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- spaces fixed

* Mon Feb 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- don't create raids when virtualized

* Thu Jan 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- not more them 16Gb of swap

* Fri Oct 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- / size for server increased

* Tue Oct 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build




