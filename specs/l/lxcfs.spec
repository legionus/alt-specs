Name:		lxcfs
Version:	3.0.2
Release:	alt1
Summary:	FUSE filesystem for LXC

Group:		Development/Other
License:	Apache-2.0
URL:		https://github.com/lxc/lxcfs

Packager:	Denis Pynkin <dans@altlinux.ru>

Source0:	%name-%version.tar
Source1:	lxcfs.sysvinit

Requires: libfuse

BuildRequires: libfuse-devel
BuildRequires: help2man

%define _check_contents_method relaxed

%description
FUSE filesystem for LXC, offering the following features:
 - a cgroupfs compatible view for unprivileged containers
 - a set of cgroup-aware files:
   - cpuinfo
   - meminfo
   - stat
   - uptime

%prep
%setup

%build
./bootstrap.sh
%configure --disable-static --with-init-script=systemd --localstatedir=%_var
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/%name
#mkdir -p %buildroot%_initdir
install -Dm0755 %SOURCE1 %buildroot%_initdir/lxcfs

%post
[ -d "%_localstatedir/%name" ] || mkdir -p %_localstatedir/%name
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING README.md
%_bindir/*
%_libdir/%name/*
%_man1dir/*
%_initdir/*
%_unitdir/*
%_datadir/lxc/config/common.conf.d/*
%dir %_datadir/%name
%_datadir/%name/*
%ghost %dir %_localstatedir/%name

%changelog
* Sun Sep  9 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Jul 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt2
- packaged with SysVinit script

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.0.1-alt1
- Update
- pam moved to lxc package

* Sun Jan 24 2018 Denis Pynkin <dans@altlinux.org> 2.0.8-alt1
- Update

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.7-alt2
- Fixed localstatedir location.

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt1
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.5-alt1
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt1
- Update

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.0.3-alt1
- Update

* Mon Apr 11 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt3
- Release 2.0

* Thu Mar 03 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc2
- Added service restart

* Tue Mar 01 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1.rc2
- Removed devel package.
  liblxcfs.so is loaded via dlopen.

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc2
- Version update

* Wed Feb 24 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
