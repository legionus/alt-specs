Name: consolehelper
Version: 0.3.2
Release: alt1

Group: System/Configuration/Other
Summary: A wrapper that helps console users run system programs
License: GPLv2+

Source: %name-%version.tar

Obsoletes: usermode

BuildPreReq: libgtk+2-devel libpam-devel pkgconfig

%define conshelpdir %_libexecdir/%name

Provides: %_libexecdir/%name/helper

%description
consolehelper is a tool that makes it easy for console users to run system
programs, doing authentication via PAM (which can be set up to trust all
console users or to ask for a password at the system administrator's
discretion).  When possible, the authentication is done graphically;
otherwise, it is done within the text console from which consolehelper
was started.

consolehelper requires that a PAM configuration for every managed
program exist.  So to make /sbin/foo or /usr/sbin/foo managed, you need
to create a link from /usr/bin/foo to %conshelpdir/helper and create
the file /etc/pam.d/foo, normally using the pam_console(8) PAM module.

%prep
%setup

%build
%make_build libexecdir=%_libexecdir helperdir=%conshelpdir

%install
%makeinstall_std libexecdir=%_libexecdir helperdir=%conshelpdir

# compatibility.
pushd %buildroot
	mkdir -p .%_bindir ./usr/lib/helper
	ln -s `relative %conshelpdir/helper /usr/lib/helper/` \
		./usr/lib/helper/%name
	ln -s `relative %conshelpdir/helper %_bindir/` \
		.%_bindir/%name
popd

%find_lang %name

%pre
/usr/sbin/groupadd -r -f conshelp
%pre_control %name

%post
%post_control %name

%files -f %name.lang
%config /etc/control.d/facilities/%name
%_bindir/*
/usr/lib/helper/*
%dir %conshelpdir
%attr(2711,root,conshelp) %conshelpdir/helper
%attr(710,root,conshelp) %dir %conshelpdir/priv
%attr(4711,root,root) %conshelpdir/priv/auth
%_datadir/pixmaps/*
%_man8dir/*

%changelog
* Mon Jan 25 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Return constant strings from svGetValue().
- shvar: Simplify svGetValue().
- shvar: Use read loop.
- shvar: Get rid of glib dependence.

* Thu Apr 18 2013 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Built with LFS support enabled.

* Tue Jul 20 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3.0-alt1
- consolehelper.8: described /etc/security/console.apps/ (closes: #10181).
- Changed error notification dialog to return back to
  authentication dialog by default (closes: #16698).
- Changed internal dialog layout to make dialogs look better.

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.2.12-alt3
- Provide %_libexecdir/%name/helper

* Wed Nov 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.2.12-alt2
- Export variables with proxy settings

* Thu May 08 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2.12-alt1
- Replaced "for user" with "for administrator" for root (#7163).
- Added gtk themes support (#14058).

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.2.11-alt1
- Fixed build with --as-needed.

* Thu Feb 23 2006 Dmitry V. Levin <ldv@altlinux.org> 0.2.10-alt1
- In client, avoid translating empty strings.

* Wed Jun 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.9.1-alt1
- Corrected bug introduced in previous release.

* Tue Jun 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.9-alt1
- Updated ui code for GTK2.

* Tue Nov 16 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.8-alt1
- Fixed communication bugs.
- Made libexecdir configurable during build.
- Updated and package manpage.

* Sat Nov 06 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.7-alt1
- Fixed misleading waitpid error diagnostics in client.
- Use control macros.
- Added help to control.

* Wed Feb 25 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.6-alt2
- Packaged %conshelpdir directory (#3032).
- Updated icons.

* Wed Feb 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.6-alt1
- Set dialog type to GTK_WINDOW_POPUP.
- Activate passwd entry widget by default.

* Mon Jan 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.5-alt1
- Restore SIGCHLD handler for executed processes (#0002077, svd).

* Thu Jan 16 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.4-alt1
- Fixed utf8 binding.

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt1
- 0.2.3 (Added control support for %name).

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- 0.2.2 (fixed gtk_widget_grab_default problem).

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt4
- Rebuilt with gtk 2.1

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt3
- Moved to gtk2.
- Added buildrequires.

* Fri Jun 07 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.1-alt2
- fixed suxx centering

* Wed Apr 10 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- 0.2.1 (fixed typo, #0000816).

* Tue Mar 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- 0.2

* Sun Mar 17 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Dropped all but consolehelper.
- Rewritten consolehelper from scratch.

* Wed Feb 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.43-alt2
- added true version of userpasswd
- dropped usermount and userinfo

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.43-alt1
- 1.43 (updated translations).

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt3
- Provides: consolehelper (until real consolehelper package appearance).

* Fri Aug 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt2
- Fixed latest sanitize_env patch.

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.42-alt1
- Specfile cleanup.
- Dropped outdated translations from mdk coz original are better.
- Dropped outdated mdk patches.
- Moved SysVinit stuff back to SysVinit package.
- Relocated %_sbindir/userhelper and %_bindir/consolehelper
 to %_libdir/helper/ according to FHS.
- Added progname patch.
- Added sanitize_env patch.
- Added getlogin patch.
 Here we need at most consolehelper and gui wrappers,
 all the rest will go into shadow-utils or like.

* Wed Jul 11 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.42-2mdk
- Use more macros
- Remove source 1, 2 + menu entry (not needed)
- Shutdown tools are back (conflict with msec < 0.15-17mdk)
- Call msec at install time if installed

* Tue May 22 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.42-1mdk
- Bump a nice and tasty 1.42 out for cooker.
- s/Copyright/License/;

* Tue Apr 10 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.37-5mdk
- Update patch 2 for better INITIAL_USER handling

* Mon Apr 09 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.37-4mdk
- included latest translations

* Tue Apr 3 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.37-3mdk
- Update patch 2 to set INITIAL_USER and BROWSER variable

* Wed Nov 29 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 1.37-2mdk
- use optflags.

* Fri Nov 10 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.37-1mdk
- bump up version for security fix. (RH).

* Tue Oct 10 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.36-2mdk
- patch to set some more environment variables

* Tue Oct 10 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.36-1mdk
- bump up version for security fix. (RH)

* Mon Oct 9 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.35-5mdk
- updated French, Spanish, etc. translations

* Mon Oct 9 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.35-4mdk
- included translations into the rpm; and added new ones (new ones still
 very incomplete)

* Mon Oct 9 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.35-3mdk
- set gid also when no session

* Fri Oct 6 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.35-2mdk
- patch in userhelper to set gid when executing a foreign program
 (-w option) (thanks to Fred Lepied)

* Thu Sep 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.35-1mdk
- Release 1.35

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.22-4mdk
- automatically added BuildRequires

* Wed Aug 02 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.22-3mdk
- macroszifications
- Makefile patch for new manpage location
- BM

* Tue Jul 18 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.22-2mdk
- remove pam console wrappers (security fix)

* Sat Apr 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.22-1mdk
- updated to new version
- updated group information
- added menu code
- There are no doc files available.

* Thu Mar 09 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix problem parsing userhelper's -w flag with other args

* Wed Mar 08 2000 Nalin Dahyabhai <nalin@redhat.com>
- ignore read() == 0 because the child exits

* Tue Mar 07 2000 Nalin Dahyabhai <nalin@redhat.com>
- queue notice messages until we get prompts in userhelper to fix bug #8745

* Fri Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- free trip through the build system

* Tue Jan 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- grab keyboard input focus for dialogs

* Fri Jan 07 2000 Michael K. Johnson <johnsonm@redhat.com>
- The root exploit fix created a bug that only showed up in certain
 circumstances. Unfortunately, we didn't test in those circumstances...

* Mon Jan 03 2000 Michael K. Johnson <johnsonm@redhat.com>
- fixed local root exploit

* Thu Sep 30 1999 Michael K. Johnson <johnsonm@redhat.com>
- fixed old complex broken gecos parsing, replaced with simple working parsing
- can now blank fields (was broken by previous fix for something else...)

* Tue Sep 21 1999 Michael K. Johnson <johnsonm@redhat.com>
- FALLBACK/RETRY in consolehelper/userhelper
- session management fixed for consolehelper/userhelper SESSION=true
- fix memory leak and failure to close in error condition (#3614)
- fix various bugs where not all elements in userinfo got set

* Mon Sep 20 1999 Michael K. Johnson <johnsonm@redhat.com>
- set $HOME when acting as consolehelper
- rebuild against new pwdb

* Tue Sep 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- honor "owner" flag to mount
- ask for passwords with username

* Tue Jul 06 1999 Bill Nottingham <notting@redhat.com>
- import pam_console wrappers from SysVinit, since they require usermode

* Mon Apr 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- even better check for X availability

* Wed Apr 07 1999 Michael K. Johnson <johnsonm@redhat.com>
- better check for X availability
- center windows to make authentication easier (improve later with
 transients and embedded windows where possible)
- applink -> applnk
- added a little padding, especially important when running without
 a window manager, as happens when running from session manager at
 logout time

* Wed Mar 31 1999 Michael K. Johnson <johnsonm@redhat.com>
- hm, need to be root...

* Fri Mar 19 1999 Michael K. Johnson <johnsonm@redhat.com>
- updated userhelper.8 man page for consolehelper capabilities
- moved from wmconfig to desktop entries

* Thu Mar 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- added consolehelper
- Changed conversation architecture to follow PAM spec

* Wed Mar 17 1999 Bill Nottingham <notting@redhat.com>
- remove gdk_input_remove (causing segfaults)

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix missing include files

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- use defattr
- fix spec file ( rm -rf $(RPM_BUILD_ROOT) is a stupid thing to do ! )

* Tue Oct 06 1998 Preston Brown <pbrown@redhat.com>
- fixed so that the close button on window managers quits the program properly

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- use gtk-config during build
- added make archive rule to Makefile
- uses a build root

* Fri Nov 7 1997 Otto Hammersmith <otto@redhat.com>
- new version that fixed memory leak bug.

* Mon Nov 3 1997 Otto Hammersmith <otto@redhat.com>
- updated version to fix bugs

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
- Wrote man pages for userpasswd and userhelper.

* Tue Oct 14 1997 Otto Hammersmith <otto@redhat.com>
- Updated the packages... now includes userpasswd for changing passwords
 and newer versions of usermount and userinfo. No known bugs or
 misfeatures.
- Fixed the file list...

* Mon Oct 6 1997 Otto Hammersmith <otto@redhat.com>
- Created the spec file.
