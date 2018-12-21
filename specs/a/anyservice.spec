Name: anyservice
Version: 1.3
Release: alt1

Summary: Anyservice - scripts for making systemd like service from any programs

License: MIT
Group: System/Base
Url: http://wiki.etersoft.ru/Anyservice

# Source-git: https://github.com/Etersoft/anyservice.git
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-intro >= 2.1.1

Requires: eepm >= 1.9.7

%description
Anyservice - scripts for making systemd like service from any programs

%prep
%setup

%build
%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/etc/%name/
mkdir -p %buildroot%_logdir/%name/

cp example.service %buildroot/etc/%name/example.service.off
cp %name.sh %buildroot/%_bindir/%name

%check
#check that port listening

%pre
%files
%dir /etc/%name/
%config(noreplace) /etc/%name/*.service.off
%attr(755,root,root) %_bindir/%name

%dir %_logdir/%name/

%changelog
* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- check /etc/systemd first
- remove PID file after stop

* Fri Dec 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- export environment variables like systemd does
- mask functions used from /etc/init.d/functions

* Wed Dec 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- drop SERVNAME before prestartd
- precreate pid file and set owner
- redhat: drop tee and fix status

* Mon Nov 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- add RHEL/CentOS support
- add statusd command
- fix monit dir detection
- add support for daemon start from /etc/init.d/functions
- move to clear shell
- move PID file to /var/run

* Fri Nov 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- anyservice.sh: drop warning about missed pid file on first start
- add support for /etc/monitrc.d/*.conf
- move list command handling to base part

* Tue Nov 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add support for /etc/systemd/system place for service files

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- anyservice.sh: fix tabs
- add sleep to fix restart issue (eterbug #11688)

* Thu Oct 13 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- replace $MYMONIT with monit (add monit to requires)

* Fri Sep 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- implement reload (supports ExecReload too)
- more correct options handling
- add --quiet support for list

* Tue Aug 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- fix EnvironmentFile using

* Tue Aug 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- fix logdir and drop obsoleted DEFAULTLOGDIR
- fix Environment, set TMPDIR and HOME

* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- big refactoring
- realize checkd and isautostarted
- add prefix for monit
- put example.service disabled by default
- improve monit status checking
- Caution: use /etc/anyservice as anyservice dir

* Mon Aug 15 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- anyservice.sh: some refactoring
- anyservice.sh: use .off file if exists
- anyservice.sh: add support for EnviromentFile and Environment fields

* Fri Aug 12 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt4
- build for ALT Linux Sisyphus

* Thu May 12 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt3
- added example, put into right folder

* Mon Apr 25 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt2
- building version

* Mon Apr 25 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt1
- initial package version

