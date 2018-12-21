%define testname init-but-no-native-systemd

Name: repocop-unittest-%testname
Version: 0.01
Release: alt3
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: repocop > 0.55
Url: http://repocop.altlinux.org

Summary: %testname integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

%description
The test warns packages that have support for Sys-V init
but not for systemd

%prep

%build
cat > %testname.posttest <<'EOF'
#!/bin/sh
sqlite3 "$REPOCOP_TEST_DBDIR/rpm.db" <<EOSQL
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select distinct a.pkgid from rpm_files as a where a.filename glob '/etc/rc.d/init.d/*' and a.pkgid not in (select c.pkgid from rpm_files as c where (c.filename glob '/lib/systemd/*' or c.filename glob '/usr/lib/systemd/*'));
EOSQL
sed -i -e '/^service-/d' $REPOCOP_TEST_TMPDIR/msg
sed -i -e '/^systemd-/d' $REPOCOP_TEST_TMPDIR/msg
for i in `cat $REPOCOP_TEST_TMPDIR/msg`; do repocop-test-info -k $i "The package have SysV init script(s) but no native systemd files."; done
rm $REPOCOP_TEST_TMPDIR/*
EOF

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

#mkdir -p %buildroot%_datadir/repocop/fixscripts/
#install -p -m 755 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/%testname/
#%_datadir/repocop/fixscripts/*.pl

%changelog
* Tue Feb 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt3
- fixed description

* Sat Jan 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- added exception for systemd-*

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial version
