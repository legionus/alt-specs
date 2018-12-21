Name: livecd-tmpfs
Version: 0.2
Release: alt1

Summary: Provide enough tmpfs for hasher/mkimage to work efficiently
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/tmpfs
Source0: %name.init
Source1: %name.sysconfig
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package might be useful for distribution images or virtual machines
whose job is building packages with hasher and/or images with mkimage.

It uses some heuristics based on experience, however, those can be
amended via sysconfig file in some peculiar situations where just
configuring tmpfs statically via /etc/fstab is suboptimal.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_initdir/%name
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_sysconfdir/sysconfig/%name

%changelog
* Tue Dec 30 2014 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- drop DIFF for good, just set all RAM/VM to tmpfs as it won't eat
  it all up and if it does we were in trouble already anyways
  (closes: #28007)

* Thu Dec 11 2014 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- don't override manually specified DIFF

* Tue Nov 01 2011 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

