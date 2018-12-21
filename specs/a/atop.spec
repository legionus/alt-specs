Name: atop
Version: 2.2
Release: alt2
Summary: AT Computing's System & Process Monitor
License: GPLv2+
Group: Monitoring
URL: http://www.%{name}tool.nl
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libncurses-devel zlib-devel

%description
%name is an interactive monitor to view the load on a Linux-system. It shows the
occupation of the most critical hardware-resources (from a performance point of
view) on system-level, i.e. cpu, memory, disk and network. It also shows which
processes are responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).
The program can also be used to log system- and process-level information in raw
format for long-term analysis.


%prep
%setup
%patch -p1


%build
%make_build CFLAGS="%optflags"
gzip -c9 ChangeLog > ChangeLog.gz


%install
mkdir -p %buildroot/usr/lib/pm-utils/sleep.d
for i in systemdinstall sysvinstall;do
make $i DESTDIR=%buildroot INIPATH=%_initddir SYSDPATH=%_unitdir
done
:> %buildroot%_sysconfdir/%{name}rc


%post
%post_service %name ||:


%preun
%preun_service %name ||:


%files
%doc AUTHOR ChangeLog.* README
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%ghost %config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_sbindir/atopacctd
%_man1dir/*
%_man5dir/*
%_man8dir/atopacctd.8.*
%_sysconfdir/cron.d/*
%_sysconfdir/logrotate.d/*
%_initdir/*
%_unitdir/%name.service
%_unitdir/atopacct.service
%_logdir/%name
%_libexecdir/pm-utils/sleep.d/45atoppm

%changelog
* Thu Sep 24 2015 Terechkov Evgenii <evg@altlinux.org> 2.2-alt2
- Systemd unit file fixed

* Sat Sep 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.2-alt1
- 2.2

* Sun Dec 23 2012 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2
- updated URL
- cleaned up BuildRequires

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.27-alt1
- 1.27-3

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt2
- Bugfix release for two bug fixes related to segmentation faults

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.26-alt1
- 1.26

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 1.25-alt1.1
- built for Sisyphus

* Mon Sep 06 2010 Led <led@altlinux.ru> 1.25-alt1
- 1.25

* Mon Sep 06 2010 Led <led@altlinux.ru> 1.23-alt4
- fixed %_sysconfdir/%name dir is not owned package %name
  (ALT #24023)
- tagged %_sysconfdir/%name/* as %%config(noreplace)
- set _optlevel to 2

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.23-alt3
- cleaned up spec

* Mon Jul 07 2008 Led <led@altlinux.ru> 1.23-alt2
- added %name-1.23-makefile.patch
- cleaned up spec
- added %_sysconfdir/logrotate.d/*
- fixed #16288

* Wed Mar 12 2008 Led <led@altlinux.ru> 1.23-alt1
- 1.23

* Sat Dec 22 2007 Led <led@altlinux.ru> 1.22-alt1
- 1.22
- cleaned up spec
- added %name-1.22-alt-init.patch
- added init script

* Wed Nov 29 2006 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17
- spec cleanup
- buildreq

* Tue Oct 08 2002 Michael Shigorin <mike@altlinux.ru> 1.7-alt1
- built for ALT Linux
