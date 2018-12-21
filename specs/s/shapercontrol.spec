Name: shapercontrol
Version: 1.5.7
Release: alt2
License: GPLv2+
Summary: Administration tool for Linux-based ISP traffic shaper 
Group: Security/Networking
Url: http://sourceforge.net/projects/sc-tool/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch
Requires: iproute2 >= 4.12.0 perl-DBD-SQLite perl-AppConfig

# Automatically added by buildreq on Fri Feb 04 2011
BuildRequires: perl-Pod-Parser perl-DBD-SQLite perl-AppConfig

%description
Administration tool for Linux-based ISP traffic shaper 

%prep
%setup
%patch0 -p1

%build
%make

%install
%makeinstall DESTDIR=%buildroot SBINDIR=%_sbindir INITDIR=%_initdir MANDIR=%_mandir CFGDIR=%_sysconfdir/sc
mkdir -p %buildroot%_sysconfdir/sysconfig
echo "SC_OPTS=" > %buildroot%_sysconfdir/sysconfig/sc

%post
%post_service sc

%preun
%preun_service sc

%files
%config %_initdir/sc
%dir %_sysconfdir/sc
%config(noreplace) %_sysconfdir/sc/sc.conf.default
%config(noreplace) %_sysconfdir/sysconfig/sc
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Fri Jul 21 2017 Anton Farygin <rider@altlinux.ru> 1.5.7-alt2
- fixed work with recent iproute2 

* Thu Jul 13 2017 Anton Farygin <rider@altlinux.ru> 1.5.7-alt1
- new version

* Sat Aug 30 2014 Anton Farygin <rider@altlinux.ru> 1.5.1-alt5
- fixed typo in iniscript (closes: #30268)

* Mon Jun 30 2014 Anton Farygin <rider@altlinux.ru> 1.5.1-alt4
- return code fixed for loading rules from database

* Mon Jun 30 2014 Anton Farygin <rider@altlinux.ru> 1.5.1-alt3
- initscript fixed for status

* Sat Jun 14 2014 Anton Farygin <rider@altlinux.ru> 1.5.1-alt2
- fixed rul_change call

* Mon Jun 02 2014 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- new version

* Wed Nov 02 2011 Anton Farygin <rider@altlinux.ru> 1.3.4-alt1
- new version

* Fri Feb 04 2011 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- first build for Sisyphus
