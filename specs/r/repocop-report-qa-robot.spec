Name: repocop-report-qa-robot
Version: 0.42
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Repocop qa-robot mail reports.
Group: Development/Other
License: GPL-1.0-only or Artistic
Url: http://repocop.altlinux.org

Source: %name-%version.tar

Conflicts: repocop < 0.34
Requires: repocop > 0.76
BuildRequires: repocop > 0.76 perl(Pod/Text.pm)

%description
Repocop is a repository unit tests platform.
This package provides tools for repocop mail reports.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_datadir/repocop-report-email/bin}
install -m755 qa-robot-repocop repocop-report-email repocop-report-qa-robot-* $RPM_BUILD_ROOT%_bindir/
install -m755 bin/* $RPM_BUILD_ROOT%_datadir/repocop-report-email/bin/

%files
%_bindir/repocop-report-qa-robot-*
%_bindir/repocop-report-email
%_bindir/qa-robot-repocop
%_datadir/repocop-report-email

%changelog
* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- use repocop 0.77 api

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- use non-modified copy of qa-robot 0.3.9

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- use formatting routines
- use non-modified copy of qa-robot 0.3.8

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- sync with qa-robot 0.3.7

* Wed Aug 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- bugfix release

* Wed Aug 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- new version (code cleanup)

* Sun Aug 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- support for mutt1.5

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2
- NMU: added missing Pod dependencies

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- support for TestDB interface

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt3
- bugfix

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt2
- bugfix

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- added repocop-report-email

* Sun Jan 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- split from main repocop package
