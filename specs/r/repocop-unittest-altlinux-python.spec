#define testname spec-has-obsolete-macroses
%define install_all_tests 1

Name: repocop-unittest-altlinux-python
Version: 0.14
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Url: http://repocop.altlinux.org

Summary: repocop package checks for conformance with Python Packaging Policy.
Group: Development/Other
License: GPL-1.0-only or Artistic
Source: %name-%version.tar

Requires: repocop > 0.40
Requires: repocop-collector-specfile
Requires: repocop-collector-repocop-hint

%description
set of ALTLinux-specific integration tests for repocop test platform.
The tests checks packages for conformance with Python Packaging Policy.

%prep
%setup

%build

%install
%if %install_all_tests
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

install -d -m 755 %buildroot%_datadir/repocop/fixscripts/
install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/
%else 
    testnames="altlinux-python-test-is-packaged altlinux-python-python3-requires-python altlinux-python-python-requires-python3"
    for testname in $testnames; do
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
    done
%endif

install -pD -m 755 repocop-helper-altlinux-python-filelist-pattern-filter \
    %buildroot%_datadir/repocop/pkgtests/altlinux-python-test-is-packaged/repocop-helper-altlinux-python-filelist-pattern-filter





%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/*
%if %install_all_tests
%_datadir/repocop/fixscripts/*
%endif

%changelog
* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added exception for python-module-pygobject3-common-devel

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- enabled all tests

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- python mismatch tests

* Tue Mar 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added support for repocop hints

* Wed Jul 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3
- test exception for python3-module-testscenarios (requested by REAL@)

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- test exception for python3-module-testtools (requested by REAL@)

* Sun Jun 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- test exceptions (requested by REAL@).

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3
- check for Test (requested by REAL@).

* Tue Sep 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- autotest exception (requested by REAL@).

* Wed Apr 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- extra python-module-petsc-config exception (requested by REAL@).

* Mon Mar 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- test level increased to info (requested by REAL@).

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- added python-module-petsc-config exception (requested by REAL@).

* Sun Jan 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added -testing exception (requested by REAL@).

* Thu Jan 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt6
- added tests/examples exception (requested by REAL@).

* Fri Jan 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt5
- added .tests exception (requested by REAL@).

* Wed Jan 06 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt4
- fixed summary thanks to lav@ and REAL@.

* Thu Nov 26 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- added exceptions to test-is-packaged test

* Tue Nov 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- added exceptions to test-is-packaged test

* Tue Nov 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- altlinux-python-test-is-packaged changes suggested by REAL@

* Sat Nov 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added altlinux-python-test-is-packaged
- all other tests are disabled (no policy is written yet).

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- posttests migration

* Thu Jul 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fixed altlinux-python-obsolete-buildreq-python-dev

* Wed Jul 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added test for buildrequires

* Wed Jul 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
