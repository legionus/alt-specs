Name:     apt-repo
Version:  1.3.9
Release:  alt1

Summary:  Script for manipulation APT repository list
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/apt-repo
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source:   %name-%version.tar
BuildRequires: gzip
Requires:  apt
Requires:  curl

%description
The apt-repo script allow to show, add and remove APT repositories
specified by address in sources.list(5) format, URL with optional
component, branch name or task number.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_man1dir
install -Dpm 644 %name.8 %buildroot%_man8dir/%name.8
gzip %buildroot%_man8dir/%name.8

%find_lang %name

%files -f %name.lang
%doc TODO
%_bindir/%name
%_man8dir/%name.8*

%changelog
* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- Add braches c8 and altlinuxclub.p8

* Tue Oct 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.8-alt1
- apt-repo test: do not confuse "remote" package names with local dirs/files

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.7-alt1
- Support https://www.altlinux.org/Autoimports sources

* Mon Jun 06 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.6-alt1
- Fix process writing to file with permission denied

* Mon May  9 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.5-alt1
- handle both cases without arepo: none (noarch) or empty (ALT #31577).
- "apt-repo test [task] '' pkg1 ..." will install the packages without
  modifying APT repos. (With --hsh-apt-config, this feature is useful
  to do an install check for a package in a minimal system.)

* Mon May 09 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt1
- task_has_arepo(): check whether plan/arepo-add-x86_64-i586 is not
  empty (ALT #31577).
- get rid of NO_TASK_AREPO_HACK environment variable (now, as
  task_has_arepo should work correctly).

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Fix remove all branches or tasks

* Sun May 01 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- Fix enexpected warning (ALT #32045)

* Fri Apr 29 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Remove arepo task source even for removed task
- Fix check length of tested package list

* Mon Apr 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Add p8 branch (ALT #32006)
- Add support for altlinuxclub sources
- Add arepo repo for task only if it exists (ALT #31577)
- Use new format of source (ALT #31974)
- Optional package name(s) support in apt-repo test
- Remove duplicate package names in task list
- Do not use strict extension for compessed man page

* Wed Dec 02 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.2.4-alt1
- prepare a smaller basesystem in hasher as girar's install check does
  (rather than the default one with rpm-build). This will allow to
  catch the same bugs as in girar, like that one:
  https://bugzilla.altlinux.org/show_bug.cgi?id=31576 .

* Tue Dec  1 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.2.3-alt1
- do not proceed if hsh --initroot-only hasn't completed successfully

* Mon Nov 30 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1
- implement the support for hasher (for "update" and "test" commands)
  if an explicit apt.conf is given.
  (TODO: update the manpage; apt-repo --help is already up-to-date)
  + "no task arepo" hack: if NO_TASK_AREPO_HACK is not empty,
    the x86_64-i586 source is not added for a task.
    (Otherwise "update" and "test" fails on such tasks.)
    (TODO: come up with a clean fix for such tasks.)
- warn about non-expanded tilde in APT_CONFIG, and give info about it.
- minor corrections in the new Perl code (from 1.2.1) for querying `apt-config`.

* Mon Nov 30 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1
- added the ability to manipulate arbitrary local sources.list
  by relying on `apt-config` and honoring APT_CONFIG (ALT#31385).
- manpage: fix formattting bugs (closes: ALT#31562).

* Thu Nov 07 2013 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Add `apt-repo test task <num>` for install all task packages
  (except *-debuginfo)
- Get package list from task
- Add t7 and c7 in available repository list

* Tue Oct 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- Add task source with Arepo on x86_64

* Fri Aug 30 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Add copy:// protocol support in sources (ALT #29071)
- Fix man page:
  - Move man page to section 8 (System administration commands and daemons)
  - Fix OS name in section name (Linux instead of BSD)
  - Add copy:// protocol support
  - Remove trailing whitespace and empty lines

* Sat May 25 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- Set common key `update` for all branches for easy migration to newer
  branch because there is no branch-specific key without apt-conf update

* Thu May 23 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- Add arepo 2.0 source too on adding x86_64 branch
- Show only one warning on non-existing source removal
- Add official keys for p6 and p7 brahches
- Display warning about unsupported command

* Sat Apr 27 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Add support for branches t6, p7, t7
- Use apt-repo clean instead clear

* Tue Nov 20 2012 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Add apt-repo clear command to remove all cdrom and task repositories
- Fix add cdrom source if it exist in list
- Check for wrong type on mass source deletion
- Remove error message on empty deletion

* Tue Nov 29 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Remove man page from program to separate file
- Support remove only specified type of sources
- Fix cdrom source remove

* Mon May 16 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Describe source definition in help
- Add keyword `all` in tm command to remove all active sources
- Fix use source as one string

* Mon May 09 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Make error messages more informational (closes: #25417)
- Inform about missed task number
- Show all available branch names
- Complete documentation
- Support sources.list(5) tokens in command line
- Pass all arguments as parts of source line (closes: #25418)
- Support quick forms of source: known branch name or number for task
- Fix URL for Sisyphus. Support absolute pathname for hasher repo.

* Tue Apr 19 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Fix arch definition on x86_64 (closes: #25464)

* Thu Mar 31 2011 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

