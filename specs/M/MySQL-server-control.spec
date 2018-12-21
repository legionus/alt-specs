# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: MySQL-server-control
Version: 0.2
Release: %branch_release alt1

Summary: MySQL and mariadb server facilities control
License: %gpl2plus
Group: System/Servers

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name.sh

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: control

%description
This package contains control rules for MySQL server.
See control(8) for details.

%install
install -pD -m0755 %SOURCE0 %buildroot%_controldir/MySQL-server

%files
%_controldir/*

%changelog
* Wed Apr 24 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added mariadb support

* Tue Apr 17 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
