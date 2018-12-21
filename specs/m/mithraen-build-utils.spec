Name: mithraen-build-utils
Summary: Simple utilites that simplify development to me
Version: 0.1.29
Release: alt1
License: GPL
Group: Development/Other

Obsoletes: seiros-build-utils

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: git-svn

Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 12 2012 (-bb)
# optimized out: apt-repo-tools diffstat gear git-core hasher openssh-clients perl-Gear-Rules perl-Log-Agent perl-RPM python-base rpm-utils termutils
BuildRequires: csed dialog etersoft-build-utils girar-nmu perl-DBM perl-LockFile-Simple perl-unicore specgen

Requires: specgen

%description
%summary

%prep
%setup
%build
%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/%name
install -m755 bin/* %buildroot/%_bindir/
install -m644 share/* %buildroot%_datadir/%name
%files
%_bindir/*
%_datadir/%name
%changelog
* Tue Mar 28 2017 Denis Smirnov <mithraen@altlinux.org> 0.1.29-alt1
- gear-rel: add support for .gear/specfile
- update Co and Status
- fix so-graph

* Fri Nov 13 2015 Denis Smirnov <mithraen@altlinux.ru> 0.1.28-alt1
- gear-clone: fix origin remote config (ALT #31479)

* Wed Nov 11 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.1.27-alt2
- gear-clone: minor tweak (unneeded extra argument in the code removed)
  (ALT#31473).

* Tue Aug 11 2015 Denis Smirnov <mithraen@altlinux.ru> 0.1.27-alt1
- use gear.alt for commands and git.alt for git repo

* Thu Mar 26 2015 Denis Smirnov <mithraen@altlinux.ru> 0.1.26-alt1
- use git push --follow-tags
- remove update-asterisk-1.6.2

* Mon Feb 02 2015 Denis Smirnov <mithraen@altlinux.ru> 0.1.25-alt1
- disable build asterisk*-devel-doc

* Sun Sep 07 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.24-alt1
- gear-clone: add git.alt:/srpms support

* Mon Aug 18 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.23-alt1
- gear-rel: push only build tag

* Sat Aug 09 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.22-alt1
- fix task-add and subtask-add when git.alt is 'alt', not 'origin' remote

* Mon Jun 23 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.21-alt1
- fix asterisk*-update with new gear-cronbuild

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.20-alt1
- fix Status and Pull utilites

* Thu Aug 29 2013 Denis Smirnov <mithraen@altlinux.ru> 0.1.19-alt1
- gear-rel -- cleanup and -f (force) flag support

* Sun Aug 18 2013 Denis Smirnov <mithraen@altlinux.ru> 0.1.18-alt1
- add utilites for asterisk update
- add specgen-update

* Sun Apr 21 2013 Denis Smirnov <mithraen@altlinux.ru> 0.1.17-alt1
- build-daemon: oneshot mode

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 0.1.16-alt1
- add /bin/bash shebang to scripts that need bash
- add subtask-add utility

* Wed Nov 07 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.15-alt1
- cl-add/cl-edit fixes

* Sat Oct 27 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt1
- cl-add/cl-edit: add '-e' option

* Sat Oct 27 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.13-alt1
- cl-add/cl-edit refactoring and specgen support

* Tue Oct 02 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.12-alt1
- huge refactoring

* Wed Sep 12 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.11-alt1
- fix build-daemon
- use $EDITOR in cl-edit

* Mon Jun 25 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.10-alt1
- gear-clone: fix work with new girar-nmu

* Tue Jun 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.9-alt1
- add gear-clone utility

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.8-alt1
- Add:
  + mass-push.
  + mass-task-add.
  + option '-f' to Gpush.
  + update-asterisk-1.6.2.

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.7-alt1
- Add:
  + git-show-roots.
  + git-clone-bare-hardlink.
  + find-big-gits.
  + altlinux-fetch-gear.
- multiple small fixes.

* Thu May 06 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.6-alt1
- fix h-gen

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.5-alt1
- add requires to specgen

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.4-alt1
- Add:
  + branch-5.1 and build-5.1 scripts.
- cleanup to build-daemon.

* Sat Mar 20 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt1
- Add:
  + tasks-rerun.
  + task-rm.
  + task-ls-queue.
  + git-autobranches.
- Update:
  + task-run.
  + task-add.

* Mon Oct 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- add build-daemon

* Mon Oct 05 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1.1-alt1
- small fixes in h-cleanup-*

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
