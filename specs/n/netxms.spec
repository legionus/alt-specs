Name: netxms
Version: 2.0.8
Release: alt3

Summary: Open source network monitoring system
License: GPL
Group: System/Servers
URL: http://http://www.netxms.org
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar
Source1: netxmsd.init
Source2: nxagentd.init
Source3: netxmsd.service
Source4: nxagentd.service

BuildRequires: flex gcc-c++ zlib-devel libexpat-devel libssl-devel libgd2-devel libreadline-devel libsqlite3-devel libMySQL-devel postgresql-devel libunixODBC-devel libsensors-devel

%description
NetXMS is an enterprise grade multi-platform open source network management and monitoring system.

%package common
Summary: NetXMS common libraries
Group: System/Libraries
%description common
%summary

%package server
Summary: NetXMS server
Group: System/Servers
%description server
%summary

%package client
Summary: NetXMS client
Group: Networking/Remote access
%description client
%summary

%package agent
Summary: NetXMS agent
Group: Networking/Remote access
Requires: %name-sqlite = %version-%release
%description agent
%summary

%package mysql
Summary: MySQL resources for NetXMS server
Group: System/Servers
%description mysql
%summary

%package pgsql
Summary: PostgreSQL resources for NetXMS server
Group: System/Servers
%description pgsql
%summary

%package sqlite
Summary: SQLite resources for NetXMS server
Group: System/Servers
%description sqlite
%summary

%package odbc
Summary: ODBC resources for NetXMS server
Group: System/Servers
%description odbc
%summary

%prep
%setup

%build
./reconf
%configure              \
  --localstatedir=/var  \
  --sharedstatedir=/var \
  --enable-unicode      \
  --with-server \
  --with-snmp   \
  --with-mysql  \
  --with-pgsql  \
  --with-sqlite \
  --with-odbc   \
  --with-client \
  --with-agent
make

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot/%_initdir/netxmsd
cp %SOURCE2 %buildroot/%_initdir/nxagentd
mkdir -p %buildroot/%systemd_unitdir
cp %SOURCE3 %buildroot/%systemd_unitdir
cp %SOURCE4 %buildroot/%systemd_unitdir
mkdir -p %buildroot/%_sysconfdir
cp contrib/netxmsd.conf-dist %buildroot/%_sysconfdir/netxmsd.conf
cp contrib/nxagentd.conf-dist %buildroot/%_sysconfdir/nxagentd.conf
subst 's|^# LogFile = {syslog}|LogFile = {syslog}|g' %buildroot/%_sysconfdir/*.conf
subst 's|/var/nxagentd|/var/lib/netxms|g' %buildroot/%_sysconfdir/nxagentd.conf
subst "s|'\\\015\\\012'|chr(10)|g" %buildroot/%_datadir/%name/sql/dbinit_pgsql.sql
mkdir -p %buildroot/%_localstatedir/%name/agent

%files common
%_libdir/libnetxms.so*
%_libdir/libnxdb.so*
%_libdir/libnxlp.so*
%_libdir/libnxmap.so*
%_libdir/libnxtre.so*
%_libdir/libnxsnmp.so*
%dir %_libdir/%name

%files server
%_bindir/netxmsd
%_bindir/nxaction
%_bindir/nxadm
%_bindir/nxap
%_bindir/nxdbmgr
%_bindir/nxencpasswd
%_bindir/nxget
%_bindir/nxmibc
%_bindir/nxscript
%_bindir/nxsnmpget
%_bindir/nxsnmpset
%_bindir/nxsnmpwalk
%_bindir/nxupload
%_bindir/nxdevcfg
%_bindir/nxgenguid
%_bindir/nxappget
%_libdir/libavaya-ers.so
%_libdir/libcisco.so
%_libdir/libnxcore.so*
%_libdir/libnxsl.so*
%_libdir/libnxsms_dummy.so*
%_libdir/libnxsms_generic.so*
%_libdir/libnxsms_nxagent.so*
%_libdir/libnxsms_portech.so*
%_libdir/libnxsrv.so*
%_libdir/libnxjansson.so*
%_libdir/libnxsd.so*
%_libdir/libstrophe.so*
%_libdir/libnxcc.so*
%dir %_libdir/%name/dbdrv
%dir %_libdir/%name/ndd
%_libdir/%name/ndd/*.ndd
%dir %_libdir/%name/smsdrv
%_libdir/%name/smsdrv/*
%dir %_datadir/%name
%_datadir/%name/mibs
%dir %_datadir/%name/sql
%dir %_datadir/%name/templates
%_datadir/%name/templates/*
%dir %_localstatedir/%name
%_localstatedir/%name/%name.mib
%dir %_localstatedir/%name/files
%_localstatedir/%name/files/*
%dir %_localstatedir/%name/images
%_localstatedir/%name/images/*
%_initdir/netxmsd
%systemd_unitdir/netxmsd.service
%config(noreplace) %_sysconfdir/netxmsd.conf
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO doc/manuals/*.odt doc/manuals/*.doc

%files client
%_bindir/nxalarm
%_bindir/nxevent
%_bindir/nxpush
%_bindir/nxsms
%_libdir/libnxclient.so*

%files agent
%_bindir/nxapush
%_bindir/nxagentd
%_initdir/nxagentd
%systemd_unitdir/nxagentd.service
%_libdir/libnxagent.so*
%_libdir/libappagent.so*
%_libdir/libnsm_ecs.so*
%_libdir/libnsm_linux.so
%_libdir/libnsm_logwatch.so
%_libdir/libnsm_lmsensors.so
%_libdir/libnsm_ping.so
%_libdir/libnsm_portcheck.so
%_libdir/libnsm_sms.so
%_libdir/libnsm_ups.so
%_libdir/libnsm_dbquery.so
%_libdir/libnsm_devemu.so
%_libdir/libnsm_ds18x20.so
%_libdir/libnsm_filemgr.so
%_libdir/libnsm_gps.so
%_libdir/%name/ecs.nsm
%_libdir/%name/linux.nsm
%_libdir/%name/logwatch.nsm
%_libdir/%name/lmsensors.nsm
%_libdir/%name/dbquery.nsm
%_libdir/%name/devemu.nsm
%_libdir/%name/ping.nsm
%_libdir/%name/portcheck.nsm
%_libdir/%name/sms.nsm
%_libdir/%name/ups.nsm
%_libdir/%name/ds18x20.nsm
%_libdir/%name/filemgr.nsm
%_libdir/%name/gps.nsm
%config(noreplace) %_sysconfdir/nxagentd.conf

%files mysql
%_libdir/libnxddr_mysql.so
%_libdir/%name/dbdrv/mysql.ddr
%_datadir/%name/sql/dbinit_mysql.sql

%files pgsql
%_libdir/libnxddr_pgsql.so
%_libdir/%name/dbdrv/pgsql.ddr
%_datadir/%name/sql/dbinit_pgsql.sql

%files sqlite
%_libdir/libnxddr_sqlite.so
%_libdir/%name/dbdrv/sqlite.ddr
%_datadir/%name/sql/dbinit_sqlite.sql

%files odbc
%_libdir/libnxddr_odbc.so
%_libdir/%name/dbdrv/odbc.ddr

%changelog
* Thu May 18 2017 Eugene Prokopiev <enp@altlinux.ru> 2.0.8-alt3
- enable lmsensors
- fast fix for pgsql metadata (thanks to Vadim Illarionov <gbIMoBou@gmail.com>)

* Thu May 04 2017 Eugene Prokopiev <enp@altlinux.ru> 2.0.8-alt2
- add systemd units (thanks to Vadim Illarionov <gbIMoBou@gmail.com>)
- enable unicode

* Fri Apr 28 2017 Eugene Prokopiev <enp@altlinux.ru> 2.0.8-alt1
- new version

* Tue Sep 06 2016 Eugene Prokopiev <enp@altlinux.ru> 2.0.6-alt1
- new version

* Tue Mar 24 2015 Eugene Prokopiev <enp@altlinux.ru> 1.2.17-alt@release@1
- new version

* Mon Jun 09 2014 Eugene Prokopiev <enp@altlinux.ru> 1.2.14-alt@release@1
- new version

* Wed Dec 18 2013 Eugene Prokopiev <enp@altlinux.ru> 1.2.10-alt@release@1
- new version

* Tue Oct 15 2013 Eugene Prokopiev <enp@altlinux.ru> 1.2.9-alt@release@1
- new version

* Tue Aug 13 2013 Eugene Prokopiev <enp@altlinux.ru> 1.2.8-alt@release@1
- new version

* Fri Jun 14 2013 Eugene Prokopiev <enp@altlinux.ru> 1.2.7-alt@release@1
- new version

* Fri Jan 11 2013 Eugene Prokopiev <enp@altlinux.ru> 1.2.5-@release@
- new version

* Wed Dec 05 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.4-alt1
- new version

* Fri Jul 27 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.2-alt1
- new version

* Thu Jun 21 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.1-alt1
- new version

* Fri Apr 27 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.0-alt1
- first build for Sisyphus
