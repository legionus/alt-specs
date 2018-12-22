Name: repocop-unittests-distribution
Version: 0.24
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: ALT Linux default set of tests for repocop test platform.
Group: Development/Other
License: GPL-1.0-only or Artistic
Url: http://repocop.altlinux.org 

Obsoletes: repocop-unittest < 0.24
Requires: repocop > 0.59
Requires: repocop-unittests-local
Requires: repocop-unittest-alt-alternatives-master-slave-conflict
Requires: repocop-unittest-alt-alternatives-vs-filesystem
Requires: repocop-unittest-alt-alternatives-vs-ghost
Requires: repocop-unittest-rpm-filesystem
Requires: repocop-unittest-sisyphus_check-check-dirlist
Requires: repocop-unittest-unmet-dependency

%description
Default set of repocop integration tests for ALT Linux.
It is the metapackage that requires all the recommended tests.

%prep

%build
%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- split into repocop-unittests-local and distribution

* Wed Jul 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- added:
  + repocop-unittest-checkbashisms
  + repocop-unittest-init-but-no-native-systemd
  + repocop-unittest-subdirs-in-usr-games

* Mon Aug 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- removed repocop-unittest-spec-has-obsolete-macroses

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added repocop-unittest-fonts.alias

* Thu Oct 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- added repocop-unittest-init-x-functions

* Wed Sep 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- removed repocop-unittest-spec-missing-packager

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- added repocop-unittest-alt-alternatives-vs-ghost

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- added url

* Thu Jan 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- added Igor Zubkov tests:
	+ repocop-unittest-big-changelog
	+ repocop-unittest-distribution-tag
	+ repocop-unittest-invalid-url
	+ repocop-unittest-missing-url
	+ repocop-unittest-subdirs-in-usr-games
	+ repocop-unittest-uncompressed-infos
	+ repocop-unittest-uncompressed-manpages
	+ repocop-unittest-vendor-tag
- added Conflicts: to repocop-unittest-package-installs-file-to-usr-games
  (needs discussion to bring forth Games Packaging Policy)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added 
	+ repocop-unittest-rpm-filesystem
	+ repocop-unittest-unmet-dependency

* Tue Dec 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added repocop-unittest-docdir-is-not-owned

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated required versions

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- updated required versions

* Thu Nov 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added rpm-filetriggers 

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added sisyphus_check-check-dirlist

* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added repocop-unittest-spec-has-obsolete-macroses

* Tue Jul 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added repocop-unittest-freedesktop to the set of recommended tests.

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added lintian-noncollectors to the set of recommended tests.

* Tue Apr 22 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added library-pkgnames to the set of recommended tests.

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added repocop-unittest-bin-permissions

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added init-lsb (info) to the set of recommended tests.

* Wed Mar 26 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- Requires: repocop-unittest-alt-alternatives-vs-filesystem
- Requires: repocop-unittest-alt-alternatives-xml
- Requires: repocop-unittest-alt-desktop-iconsdir

* Tue Mar 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- Requires: freedesktop-mime-test

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- requires freedesktop-categories

* Mon Mar 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build

