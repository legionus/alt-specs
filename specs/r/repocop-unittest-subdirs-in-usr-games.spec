Name: repocop-unittest-subdirs-in-usr-games
Version: 0.1
Release: alt4

Summary: subdirs-in-usr-games intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: subdirs-in-usr-games.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.09-alt1

%description
subdirs-in-usr-games intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/subdirs-in-usr-games/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/subdirs-in-usr-games/posttest

%files
%dir %_datadir/repocop/pkgtests/subdirs-in-usr-games/
%_datadir/repocop/pkgtests/subdirs-in-usr-games/posttest

%changelog
* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4
- tests declared as posttests

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt2
- add Url:

* Sun Jan 18 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus


