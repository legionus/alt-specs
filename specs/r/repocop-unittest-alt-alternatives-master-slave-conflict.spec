%define testname alt-alternatives-master-slave-conflict

Name: repocop-unittest-%testname
Version: 0.05
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop test for alternatives master/slave intersections.
Group: Development/Other
License: GPL-1.0-only or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop > 0.59
Requires: repocop-collector-altlinux-alternatives > 0.05
Requires: sqlite3


%description
Repocop integration test for alternatives master/slave intersections.
ALT Linux specific.

%prep

%build
cat > %testname.distrotest <<'EOF'
#!/bin/sh
#--select rpm_files.pkgid, group_concat(FILENAME), group_concat(altlinux_alternatives.pkgid) from altlinux_alternatives, rpm_files WHERE ALTALTERNATIVE=FILENAME GROUP BY rpm_files.pkgid;
sqlite3 "$REPOCOP_DISTROTEST_DBDIR/altlinux-alternatives.db" <<EOSQL
attach database '$REPOCOP_DISTROTEST_DBDIR/rpm.db' as rpm;
.mode tabs
.output $REPOCOP_TEST_TMPDIR/msg
select a.pkgid, a.ALTALTERNATIVE, b.pkgid from altlinux_alternatives as a, altlinux_alternatives as b where a.ALTISMASTER=0 and b.ALTISMASTER=1 and a.ALTALTERNATIVE = b.ALTALTERNATIVE and a.pkgid <> b.pkgid;
EOSQL
perl -ne 'chomp;@a=split /\t/;system("repocop-test-fail -k $a[0] slave alternative $a[1] is already registered as a master in package: $a[2]")' $REPOCOP_TEST_TMPDIR/msg
rm $REPOCOP_TEST_TMPDIR/msg
EOF

%install

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 %testname.distrotest $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/distrotest

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- moved to distrotests

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- posttests migration

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- added url

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- use ismaster coulumn (repocop-collector-alternatives >= 0.06)

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
