# BEGIN SourceDeps(oneline):
BuildRequires: perl(Pod/Usage.pm) perl(RPM/Header.pm) perl(Parallel/ForkManager.pm)
# END SourceDeps(oneline)
URL: https://www.altlinux.org/Repofork-utils
Name: repofork-utils
Version: 0.09
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: tools to create a modified copy of a repository
Group: Development/Other
License: GPL-2.0-or-later
#Url: 
Source: %name-%version.tar

Requires: /usr/bin/pkglist-query

%description
mkrepofork tool creates a (hardlinked) modified copy of an
existing repository with given packages added/removed/replaced.

%prep
%setup

%build
#perl_vendor_build

%install
#perl_vendor_install

mkdir -p $RPM_BUILD_ROOT%_bindir
cp mkrepofork repofork-* $RPM_BUILD_ROOT%_bindir/
rm $RPM_BUILD_ROOT%_bindir/*.spec

%files
%_bindir/mkrepofork
%_bindir/repofork*

%changelog
* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new version

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- renamed: repofork-helper-create-* -> repofork-create-*

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added repofork-helper-...-for-each-given-autorepo-taskgood-subdir

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added repofork-rebuild

* Sat Dec 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Sat Nov 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Wed Nov 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Thu Oct 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build

