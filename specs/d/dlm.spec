Name: dlm
Version: 4.0.6
Release: alt1
Summary: dlm control daemon and tool
License: GPL-2.0-only and GPL-2.0-or-later and LGPLv2+
Group: System/Servers
URL: https://fedorahosted.org/cluster

Requires: corosync2

Source0: %name-%version.tar.gz
Patch0: 0001-dlm_controld-libsystemd-broke-itself.patch
Patch1: dlm-4.0.5-alt.patch

BuildRequires: libpacemaker-devel libsystemd-devel

%description
The kernel dlm requires a user daemon to control membership.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
The lib%name package contains the libraries needed to use the dlm
from userland applications.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make
%make -C fence

%install
%make LIBNUM=/%_lib UDEVDIR=%_udevrulesdir DESTDIR=%buildroot install
%make -C fence DESTDIR=%buildroot install

install -Dm 0644 init/dlm.service %buildroot%_unitdir/dlm.service
install -Dm 0644 init/dlm.sysconfig %buildroot%_sysconfdir/sysconfig/dlm

mkdir -p %buildroot%_sysconfdir/dlm
touch %buildroot%_sysconfdir/dlm/dlm.conf

%files
%doc README.license
%config(noreplace) %_sysconfdir/sysconfig/dlm
%dir %_sysconfdir/dlm
%ghost %_sysconfdir/dlm/dlm.conf
%_unitdir/dlm.service
%_sbindir/dlm_controld
%_sbindir/dlm_tool
%_sbindir/dlm_stonith
%_man8dir/dlm*
%_man5dir/dlm*
%_man3dir/*dlm*

%files -n lib%name
%_udevrulesdir/*-dlm.rules
%_libdir/libdlm*.so.*

%files -n lib%name-devel
%_includedir/libdlm*.h
%_libdir/libdlm*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Aug 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Wed Sep 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Mon Sep 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt2
- fixed build with latest systemd

* Mon Mar 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt1
- 4.0.2
