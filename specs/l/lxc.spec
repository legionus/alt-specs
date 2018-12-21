#
# lxc: linux Container library
#
# (C) Copyright IBM Corp. 2007, 2008
# (C) ALT Linux Team 2009-2018
#
# Authors:
# Daniel Lezcano <dlezcano at fr.ibm.com>
# Denis Pynkin <dans at altlinux.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Spec file adapted for ALT Linux.

%def_with systemd
%define init_script systemd,sysvinit

Name: lxc
Version: 3.0.2
Release: alt1
Packager: Denis Pynkin <dans@altlinux.org>

URL: https://linuxcontainers.org/
Source: %name-%version.tar
Source1: lxc-net.sysconfig
Patch: %name-%version-%release.patch

Summary: %name : Linux Container
Group: System/Configuration/Other
License: LGPL
Requires: libcap gzip-utils
%ifarch x86_64 %arm
Requires: criu
%endif
Requires: iproute2 bridge-utils dnsmasq
BuildRequires: libcap-devel docbook-utils glibc-kernheaders
BuildRequires: docbook2X xsltproc
BuildRequires: rpm-macros-alternatives
BuildRequires: libnih-devel
BuildRequires: libdbus-devel
BuildRequires: libgnutls-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel

# Needed to disable auto requirements from distro templates
%add_findreq_skiplist %_datadir/%name/*

# Do not need to check
%add_findreq_skiplist %_libexecdir/%name/lxc-apparmor-load
%add_findreq_skiplist %_libexecdir/%name/lxc-net

Requires: openssl rsync
BuildRequires: libcap libcap-devel docbook2X graphviz

%{?_with_systemd:BuildRequires: systemd-devel}

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools, which can be used to start a single
daemon in a container, or to boot an entire "containerized" system, and to
manage and debug your containers.

%package	sysvinit
Summary:	%{name} init scripts for SysVinit
Group:		System/Configuration/Other
Requires:	%{name}
Requires:	/sbin/chkconfig
BuildArch:	noarch
%description	sysvinit
The %{name}-sysvinit package contains init scripts for SysVinit
# Skip automatic dependency to optional lsb scripts
%add_findreq_skiplist %{_initdir}/*

%package	libs
Summary:	Shared library files for %{name}
Group:		System/Configuration/Other
%description	libs
The %{name}-libs package contains libraries for running %{name} applications.

%package devel
Summary: development library for %name
Group: Development/Other

%description devel
The %name-devel package contains header files and library needed for
development of the linux containers.

%set_pam_name pam_cgfs
%package -n %pam_name
Summary: %summary
Group: System/Base
BuildRequires(pre): libpam-devel

%description -n %pam_name
%summary
This package provides a Pluggable Authentication Module (PAM) to provide
logged-in users with a set of cgroups which they can administer.
This allows for instance unprivileged containers, and session
management using cgroup process tracking.

%prep
%setup
%patch -p1
%ifarch %e2k
# redefined typedef unsigned int __u32;
sed -i 's,-Werror,,' configure.ac
%endif

%build
%autoreconf
%configure -disable-rpath \
    --disable-cgmanager \
    --localstatedir=%_var \
    --with-config-path=%_var/lib/lxc \
    --with-distro=altlinux \
    --enable-capabilities \
    --enable-pam \
    --enable-seccomp \
    --enable-selinux \
    --with-init-script=%{init_script}

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_cachedir/%name
install -pm644 %SOURCE1 %buildroot/%_sysconfdir/sysconfig/lxc-net

%post sysvinit
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add lxc
	/sbin/chkconfig --add lxc-net
fi

%preun sysvinit
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del lxc
	/sbin/chkconfig --del lxc-net
fi

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/lxc*
%{_mandir}/man5/lxc*
%{_mandir}/man7/lxc*
%{_mandir}/ja/man1/lxc*
%{_mandir}/ja/man5/lxc*
%{_mandir}/ja/man7/lxc*
%{_mandir}/ko/man1/lxc*
%{_mandir}/ko/man5/lxc*
%{_mandir}/ko/man7/lxc*
%{_datadir}/doc/*
%{_datadir}/lxc/*
%{_sysconfdir}/bash_completion.d/*
%config(noreplace) %{_sysconfdir}/lxc/*
%config(noreplace) %{_sysconfdir}/sysconfig/lxc*
%{_unitdir}/lxc.service
%{_unitdir}/lxc@.service
%{_unitdir}/lxc-net.service

%files sysvinit
%{_initdir}/*

%files libs
%defattr(-,root,root)
%{_sbindir}/*
%{_libdir}/*.so.*
%{_libdir}/%{name}
%{_localstatedir}/*
%{_libexecdir}/%{name}/lxc-apparmor-load
%{_libexecdir}/%{name}/lxc-monitord
%attr(555,root,root) %{_libexecdir}/%{name}/lxc-containers
%attr(555,root,root) %{_libexecdir}/%{name}/lxc-net
%attr(4111,root,root) %{_libexecdir}/%{name}/lxc-user-nic
%{_libexecdir}/%{name}/hooks/*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %pam_name
%_pam_modules_dir/*

%changelog
* Sun Sep 09 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.2-alt1
- 3.0.2
- rebuilt with seccomp and SELinux support
- explicitly enabled capability support which was enabled automatically in
  previous builds

* Wed Aug 01 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt4
- really disable SysVinit scripts by default

* Tue Jul 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt3
- tuned SysVinit scripts for ALT
- disable SysVinit scripts by default (according to services policy)

* Tue Jun 26 2018 Michael Shigorin <mike@altlinux.org> 3.0.1-alt2
- Worked around FTBFS on e2k
- Minor spec cleanup

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.0.1-alt1
- Version updated

* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 3.0.0-alt1
- New major version
- python bindings are moved to separate source tree
- pam0_cgfs module has been moved from lxcfs to lxc

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Sep 06 2017 Denis Pynkin <dans@altlinux.org> 2.1.0-alt1
- Version updated
- New script 'lxc-update-config' can be used to upgrade existing
  legacy LXC configurations to valid LXC 2.1
- Updated copyright info in spec file due a lot of local changes

* Tue Aug 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt4
- Based on patch by Michael Shigorin: introduced systemd knob (on by default)
- Removed dependency to lsb scripts for lxc-sysvinit package

* Tue Aug 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt3
- Build with both init systems sysvinit and systemd
- new package lxc-sysvinit provided for classic SysVinit boot

* Mon Aug 28 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt2
- Fixes #33814
- Fixes #33799

* Thu Jun 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt1
- Version updated

* Wed Apr 26 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt4
- Fixes #33399

* Thu Mar 30 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt3
- Fixes #33302

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt2
- Disable cgmanager support

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt1
- Version updated

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.6-alt1
- Version updated

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.0.5-alt1
- Version updated

* Mon Aug 22 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt1
- Bugfix release
- Fixes #32391

* Mon Apr 11 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1
- Release version

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt0.rc9.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt0.rc9.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc9
- Version updated
- Fix of altlinux template

* Mon Feb 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc4
- Version updated
- Added cgmanager support (for lxd)

* Mon Nov 09 2015 Denis Pynkin <dans@altlinux.org> 1.1.4-alt1
- New version.

* Tue Sep 15 2015 Denis Pynkin <dans@altlinux.org> 1.1.3-alt1
- New version.
  Security fixes and ABI changes in upstream.

* Thu Apr 23 2015 Denis Pynkin <dans@altlinux.org> 1.1.2-alt2
- Removed creation/deletion of unneeded lxc-dnsmasq user.

* Sat Apr 11 2015 Denis Pynkin <dans@altlinux.org> 1.1.2-alt1
- Bugfix release

* Wed Mar 11 2015 Denis Pynkin <dans@altlinux.org> 1.1.0-alt1
- Version 1.1.0
  Added criu (crtools) to dependencies for container dump/restore.
  Added network service and configuration.
  Fixed #30232

* Tue Aug 19 2014 Denis Pynkin <dans@altlinux.org> 1.0.5-alt2
- Fixed reopened #30158
  Added check of services in container before start or stop.
  Added check of syslog config existence prior changing.

* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.5-alt1
- New version

* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt2
- Fixed: #30154 #30119
- New subpackage lxc-python3
- Build both lxc-ls -- legacy and python.
  Correct version is selected via alternatives
- Fixed: #30158 #30159
- Updated template for ALTLinux
- Now used default list of packages in case
  if /etc/lxc/profiles/default is absent


* Sat Jun 14 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt1
- New version

* Sun Nov 24 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt3
- Fixed rebuild problem

* Mon Jul 01 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt2
- 0.9.0 release
- fixed #29113, Thanks to legion@.

* Sun Mar 10 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt1.alpha3
- New version

* Fri May 11 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt3
- Merged bc31b303c48c615c2cd15dd54831e55196b983f0 to fix 
  build with new autotools

* Mon Jan 02 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt2
- Merged 1c41ddcb4af633ac906f1d7c9ef1dc7d121d7850 for rpath option

* Mon Oct 03 2011 Denis Pynkin <dans@altlinux.org> 0.7.5-alt1
- New version
- Template for ALTLinux by Alexey Shabalin

* Thu Jul 21 2011 Denis Pynkin <dans@altlinux.org> 0.7.4.2-alt1
- New version

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 0.7.4.1-alt1
- New version

* Sun Nov 07 2010 Denis Pynkin <dans@altlinux.ru> 0.7.3-alt1
- New version

* Sat Jul 31 2010 Denis Pynkin <dans@altlinux.ru> 0.7.2-alt1
- New version

* Fri May 28 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt2
- added zgrep in requirements
- added patch c08556c6ece8ad8308f7636adb0ad25b60e3a16d for lazy umount

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt1
- New version

* Sat Dec 12 2009 Denis Pynkin <dans@altlinux.ru> 0.6.4-alt1
- New version

* Wed Nov 11 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt2
- fixed #22235 (added dirs /var/lib/lxc and /var/cache/lxc)

* Sat Jul 25 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt1
- New version
- Patch for --as-needed

* Thu Jul 23 2009 Denis Pynkin <dans@altlinux.ru> 0.6.2-alt1
- Initial spec for ALT Linux

* Mon Mar 24 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.1
- Removed capability setting, let the user to do that through "lxc-setcap"

* Mon Feb 16 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Added more capabilities to the executables

* Sun Jan 25 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Reduced spec file

* Sun Aug 3 2008 Daniel Lezcano <dlezcano@fr.ibm.com> - Version 0.1.0
- Initial RPM release.
