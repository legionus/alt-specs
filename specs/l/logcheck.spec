%define _logcheck_user     _logcheck
%define _logcheck_group    _logcheck
%define _logcheck_home     %_localstatedir/logcheck

Name: logcheck
Version: 1.3.17
Release: alt1.git20141024.qa1

Summary: Mails anomalies in the system logfiles to the administrator
License: GPL
Group: Monitoring

Url: http://logcheck.alioth.debian.org/
BuildArch: noarch

# git://anonscm.debian.org/logcheck/logcheck.git
Source: %name-%version.tar

Requires: logtail = %version-%release
Requires: perl-mime-construct

# Automatically added by buildreq on Wed Oct 29 2008 (-bi)
BuildRequires: OpenSP docbook-dtds docbook-to-man lockfile-progs

%description
Logcheck is a simple utility which is designed to allow a system
administrator to view the logfiles which are produced upon hosts under
their control.

It does this by mailing summaries of the logfiles to them, after first
filtering out "normal" entries.

Normal entries are entries which match one of the many included
regular expression files contain in the database.

Logcheck was part of the Abacus Project of security tools, but this
version has been rewritten.

%package database
Summary: Database of system log rules for the use of log checkers
Group: Monitoring

%description database
This database is part of the Logcheck package, but might be used by
others. It brings a database of regular expressions for matching
system log entries after various criteria.

%package -n logtail
Summary: Print log file lines that have not been read
Group: Monitoring

%description -n logtail
This program will read in a standard text file and create an offset
marker when it reads the end. The offset marker is read the next time
logtail is run and the text file pointer is moved to the offset
location. This allows logtail to read in the next lines of data
following the marker. This is good for marking log files for automatic
log file checkers to monitor system events.

This program is mainly used by logcheck, because it returns only parts
of the system logfiles that have not already been checked.

%prep
%setup

%install
install -d %buildroot%_lockdir/%name

%make_install install DESTDIR=%buildroot

# cron
install -pDm0644 debian/logcheck.cron.d %buildroot%_sysconfdir/cron.d/%name

# header
install -pD debian/header.txt %buildroot%_sysconfdir/%name/header.txt

# man-pages
install -pD docs/logtail.8 %buildroot%_man8dir/logtail.8
install -pD docs/logtail2.8 %buildroot%_man8dir/logtail2.8
docbook-to-man docs/logcheck.sgml >%buildroot%_man8dir/logcheck.8

install -d %buildroot%_tmpfilesdir
cat <<EOF >%buildroot%_tmpfilesdir/%name.conf
d /run/lock/%name 0755 %_logcheck_user %_logcheck_group -
EOF

%pre
/usr/sbin/groupadd -r -f %_logcheck_group ||:
/usr/sbin/useradd -g %_logcheck_group -c 'Logcheck User' -G adm \
        -d %_logcheck_home -s /dev/null -r %_logcheck_user >/dev/null 2>&1 ||:

%files
%doc AUTHORS CHANGES CREDITS TODO
%doc docs/README.{how.to.interpret,keywords,logcheck,Maintainer} docs/tools/log-summary-ssh
%_man8dir/logcheck*
%attr(710,root,%_logcheck_group) %dir %_sysconfdir/%name
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/cracking.d
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/cracking.ignore.d
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/violations.d
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/violations.ignore.d
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/ignore.d.workstation
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/ignore.d.server
%dir %attr(2750,root,%_logcheck_group) %_sysconfdir/%name/ignore.d.paranoid
%attr(640,root,%_logcheck_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/logcheck.conf
%attr(640,root,%_logcheck_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/logcheck.logfiles
%attr(640,root,%_logcheck_group) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/header.txt
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/cron.d/%name
%attr(644,%_logcheck_user,%_logcheck_group) %config %verify(not md5 mtime size) %_tmpfilesdir/%name.conf
%_sbindir/logcheck
%_bindir/logcheck-test
%dir %attr(0770,root,%_logcheck_group) %_localstatedir/%name
%dir %attr(0770,root,%_logcheck_group) %_lockdir/%name

%files database
%config %verify(not md5 mtime size) %_sysconfdir/%name/cracking.d/*
%config %verify(not md5 mtime size) %_sysconfdir/%name/violations.d/*
%config %verify(not md5 mtime size) %_sysconfdir/%name/violations.ignore.d/*
%config %verify(not md5 mtime size) %_sysconfdir/%name/ignore.d.workstation/*
%config %verify(not md5 mtime size) %_sysconfdir/%name/ignore.d.server/*
%config %verify(not md5 mtime size) %_sysconfdir/%name/ignore.d.paranoid/*

%files -n logtail
%_sbindir/logtail*
%_datadir/logtail
%_man8dir/logtail*

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.17-alt1.git20141024.qa1
- NMU: applied repocop patch

* Fri Jun 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.17-alt1.git20141024
- Version 1.3.17

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140902
- Version 1.3.6

* Fri Mar 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.68-alt3
- Fix pseudouser name in error message (Closes: #19091)

* Tue Mar 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.68-alt2
- Fix pseudouser name in cron file (Closes: #19091)
- Send mail to root by default (Closes: #19091)
- logcheck: add dependency on logtail (Closes: #19092)
- Update default logfiles in config (Closes: #19093)
- logcheck: do not call "run-parts --list" (Closes: #19094)
- logcheck: clear default MAILARGS value (Closes: #19095)
- Include logcheck pseudouser to 'adm' group by default (Closes: #19096)

* Wed Oct 29 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.68-alt1
- Initial build for ALT Linux (spec from PLD)
