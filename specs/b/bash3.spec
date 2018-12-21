%define _unpackaged_files_terminate_build 1

Name: bash3
%define bash_version 3.2
%define bash_patchlevel 57
Version: %bash_version.%bash_patchlevel
Release: alt4

Summary: The GNU Bourne Again SHell (Bash)
Group: Shells
License: GPLv2+
Url: http://www.gnu.org/software/%name/

# ftp://ftp.gnu.org/gnu/bash/bash-%bash_version.tar.bz2
# ftp://ftp.gnu.org/gnu/bash/bash-%bash_version-patches/
Source0: bash-%version.tar
# ftp://ftp.gnu.org/gnu/bash/bash-doc-%bash_version.tar.bz2
Source1: bash-doc-%version.tar

Patch: bash-%version-%release.patch

# bashbug produces a lot of unneeded dependencies.
AutoReq: yes, noshell

Requires: sh3 = %EVR
Provides: bash2 = %EVR
Obsoletes: bash2
Conflicts: bash < %EVR

BuildPreReq: libreadline-devel >= 5.1, mktemp >= 1:1.3.1
BuildRequires: makeinfo texi2dvi

%package -n sh3
Summary: The GNU Bourne Again SHell (/bin/sh)
Group: Shells
Requires: bashrc
Conflicts: sh < %EVR
AutoReq: yes

%package doc
Group: Shells
Summary: Documentation for the GNU Bourne Again SHell
BuildArch: noarch
Requires: %name = %EVR
Obsoletes: bash2-doc
AutoReq: yes

%package examples
Group: Development/Other
Summary: Examples for the GNU Bourne Again SHell
BuildArch: noarch
Requires: %name = %EVR
Obsoletes: bash2-examples
AutoReq: yes

%package devel
Group: Development/Other
Summary: Bash loadable builtins development files
Requires: %name = %EVR

%description
Bash is an sh-compatible command language interpreter that executes
commands read from the standard input or from a file.  Bash also
incorporates useful features from the Korn and C shells (ksh and csh).
Most sh scripts can be run by bash without modification.

Bash is ultimately intended to be a conformant implementation of the
IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).

%description -n sh3
Bash is an sh-compatible command language interpreter that executes
commands read from the standard input or from a file.  Bash also
incorporates useful features from the Korn and C shells (ksh and csh).
Most sh scripts can be run by bash without modification.

Bash is ultimately intended to be a conformant implementation of the
IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).

This package contains /bin/sh.

%description doc
Bash is an sh-compatible command language interpreter that executes
commands read from the standard input or from a file.  Bash also
incorporates useful features from the Korn and C shells (ksh and csh).
Most sh scripts can be run by bash without modification.

Bash is ultimately intended to be a conformant implementation of the
IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).

This package contains documentation for the GNU Bourne Again SHell.

%description examples
Bash is an sh-compatible command language interpreter that executes
commands read from the standard input or from a file.  Bash also
incorporates useful features from the Korn and C shells (ksh and csh).
Most sh scripts can be run by bash without modification.

Bash is ultimately intended to be a conformant implementation of the
IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2).

This package contains examples for the GNU Bourne Again SHell.

%description devel
Bash can dynamically load new builtin commands.
Included are the necessary headers to compile custom builtins.

%prep
%setup -q -n bash-%version -a1
%patch -p1

# Remove files which should be regenerated during build.
rm configure y.tab.? doc/*.info*

# Bundled texi2dvi is outdated.
install -pm755 /usr/bin/texi2dvi support/

# Fix temporary file handling.
sed -i 's,/tmp/,,g' *.m4

# Would anyone volunteer to fix those? Probably not.
#find examples -type f -print0 |
#	xargs -r0 grep -FlZ -- /tmp |
#	xargs -r0 rm -fv --

sed -n '1,/^\.SH "BASH BUILTIN COMMANDS"/p' doc/builtins.1 >builtins.1
sed -n '/^\.\\" start of bash_builtins/,/^\.\\" bash_builtins/p' doc/bash.1 >>builtins.1
sed -n '/^\.SH SEE ALSO/,$p' doc/builtins.1 >>builtins.1
mv builtins.1 doc/builtins.1

sed -n '1,/^\.SH "RESTRICTED SHELL"/p' doc/rbash.1 >rbash.1
sed -n '/^\.\\" rbash\.1/,/^\.\\" end of rbash\.1/p' doc/bash.1 >> rbash.1
sed -n '/^\.SH SEE ALSO/,$p' doc/rbash.1 >>rbash.1
mv rbash.1 doc/rbash.1

%build
autoconf

export \
	bash_cv_dev_fd=standard \
	bash_cv_dev_stdin=present \
	bash_cv_mail_dir=/var/mail \
	bash_cv_termcap_lib=libc \
	%{?__buildreqs:bash_cv_must_reinstall_sighandlers=no} \
	#

%define _configure_script ../configure

# Build sh.
mkdir build-sh
pushd build-sh
%configure \
	--without-bash-malloc \
	--disable-readline \
	--disable-command-timing \
	--disable-net-redirections \
	--disable-help-builtin \
	--disable-bang-history \
	--disable-history \
	--disable-progcomp \
	--disable-restricted \
	#
# SMP-incompatible build.
make
popd

# Build bash.
mkdir build-bash
pushd build-bash
%configure \
	--without-bash-malloc \
	--with-installed-readline \
	--disable-command-timing \
	--disable-net-redirections \
	--enable-separate-helpfiles \
	#
# SMP-incompatible build.
make
make info
ln doc/*.info* ../doc/
popd

%check
%make_build -k check -C build-sh
%make_build -k check -C build-bash

%install
%makeinstall -C build-bash

install -pD -m755 build-sh/bash %buildroot/bin/sh3
ln -s bash3.1 %buildroot%_man1dir/sh3.1

mv %buildroot%_bindir/bash %buildroot/bin/bash3
mv %buildroot%_man1dir/bash{,3}.1

ln -s bash3 %buildroot/bin/bash2
ln -s bash3.1 %buildroot%_man1dir/bash2.1

ln -s bash3 %buildroot/bin/rbash3
mv %buildroot%_man1dir/rbash{,3}.1

mv %buildroot%_bindir/bash{,3}bug
mv %buildroot%_man1dir/bash{,3}bug.1

mv %buildroot%_infodir/bash{,3}.info

mv %buildroot%_man1dir/{,bash3_}builtins.1

# Include files for building custom builtins.
pushd build-bash
mkdir -p %buildroot%_includedir/%name
for f in ../examples/loadables/*.c; do
	%__cc -MM -DHAVE_CONFIG_H -DSHELL -Iexamples/loadables -I. -I.. -I../lib -I../builtins -I../include "$f"
done |
	tr -d '\:' |
	tr -s '[:space:]' '\n' |
	fgrep .h |
	fgrep -v examples/loadables/ |
	sort -u |
	while read f; do
		install -pm644 "$f" %buildroot%_includedir/%name/
	done
popd

# Prepare documentation.
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/{html,ps,txt}
install -p -m644 \
	AUTHORS CHANGES COMPAT NEWS NOTES POSIX RBASH doc/{FAQ,INTRO} \
	%buildroot%docdir/
install -p -m644 doc/*.html %buildroot%docdir/html/
install -p -m644 doc/*.ps %buildroot%docdir/ps/
install -p -m644 doc/*.txt %buildroot%docdir/txt/
find %buildroot%docdir/{[A-Z],{ps,txt}/}* -type f -size +4k -print0 |
	xargs -r0 xz -9 --
cp -a examples %buildroot%docdir/
find %buildroot%docdir/examples/ -type f -name 'Makefile*' -delete -print

cat >%buildroot%docdir/examples/loadables/Makefile <<'EOF'
CC = %__cc
CPPFLAGS = -DHAVE_CONFIG_H -I. -I%_includedir/%name
CFLAGS = %optflags_default %optflags_shared
LDFLAGS = -shared -Wl,-soname,$@

%%.so: %%.c
	$(LINK.c) $^ $(LOADLIBES) $(LDLIBS) -o $@
EOF

%find_lang %name

%files -n sh3
/bin/sh3

%files -f %name.lang
/bin/*bash*
%_bindir/*
%_datadir/%name/
%_mandir/man?/*
%_infodir/*.info*
%dir %docdir
%docdir/[A-Z]*

%files doc
%dir %docdir
%docdir/html
%docdir/ps
%docdir/txt

%files examples
%dir %docdir
%docdir/examples

%files devel
%_includedir/*

%changelog
* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 3.2.57-alt4
- Moved bashrc files to a separate package.
- Renamed to bash3 (by Aleksei Nikiforov and me).

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 3.2.57-alt3
- Changed compression method applied to documentation files
  from bzip2 to xz.

* Wed Sep 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.2.57-alt2
- Applied upstream patch that drops inheritance of PS4 environment
  variable for root (by glebfm@; fixes CVE-2016-7543).

* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 3.2.57-alt1
- Updated to 3.2 patchlevel 57.

* Sun Sep 28 2014 Dmitry V. Levin <ldv@altlinux.org> 3.2.54-alt1
- Updated to 3.2 patchlevel 54.

* Fri Sep 26 2014 Dmitry V. Levin <ldv@altlinux.org> 3.2.53-alt1
- Updated to 3.2 patchlevel 53.
- Applied OOB array access fix from Florian Weimer
  (fixes: CVE-2014-7186, CVE-2014-7187).

* Thu Sep 25 2014 Dmitry V. Levin <ldv@altlinux.org> 3.2.52-alt1
- Updated to 3.2 patchlevel 52.
- Applied upstream fix for CVE-2014-7169.
- Applied functions export hardening patch from Florian Weimer
  (fixes: CVE-2014-6278).

* Mon Sep 22 2014 Dmitry V. Levin <ldv@altlinux.org> 3.2.51-alt3
- Applied upstream fix for CVE-2014-6271.

* Tue Nov 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.51-alt2
- Rebuilt with readline6.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.2.51-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 21 2010 Dmitry V. Levin <ldv@altlinux.org> 3.2.51-alt1
- Updated to 3.2 patchlevel 51.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.2.48-alt3
- Moved "make check" to %%check section.
- Packaged %name-examples subpackage as noarch.

* Wed Jul 29 2009 Alexey Tourbin <at@altlinux.ru> 3.2.48-alt2
- make_cmd.c: Enhanced --rpm-requires to recognize commands
  in conjunction with LC_* assignments.

* Fri Jun 05 2009 Dmitry V. Levin <ldv@altlinux.org> 3.2.48-alt1
- Updated to 3.2 patchlevel 48.
- Fixed ACL support in the source builtin (patch from Werner Fink).

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3.2.39-alt2
- Packaged -doc subpackage as noarch.

* Fri May 30 2008 Dmitry V. Levin <ldv@altlinux.org> 3.2.39-alt1
- Updated to 3.2 patchlevel 39.

* Thu Mar 27 2008 Dmitry V. Levin <ldv@altlinux.org> 3.2.33-alt1
- Updated to 3.2 patchlevel 33.

* Mon Oct 29 2007 Alexey Tourbin <at@altlinux.ru> 3.1.17-alt4
- updated rh-alt-requires.patch: output each function name defined in
  a file, for strong self-requires elimination in /usr/lib/rpm/shell.req

* Fri Oct 05 2007 Dmitry V. Levin <ldv@altlinux.org> 3.1.17-alt3
- Added missing check for unbound variables (Alexey Tourbin).
- Packaged include files required to build custom builtins.
- In "enable" builtin, use RTLD_NOW flag in dlopen().
- sh: Package /usr/lib/bash directory for external builtins.

* Wed Feb 21 2007 Dmitry V. Levin <ldv@altlinux.org> 3.1.17-alt2
- ulimit -a: Fixed redundant RLIMIT_LOCKS.
- bash.info: Imported FC fix for out of date tags (RH#150118).

* Fri Apr 14 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.17-alt1
- Updated to 3.1 patchlevel 17.

* Sat Apr 01 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.16-alt1
- Updated to 3.1 patchlevel 16.

* Mon Mar 20 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.14-alt1
- Updated to 3.1 patchlevel 14.

* Sat Mar 04 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.11-alt1
- Updated to 3.1 patchlevel 11.

* Tue Feb 21 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.10-alt1
- Updated to 3.1 patchlevel 10.

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.8-alt1
- Updated to 3.1 patchlevel 8.

* Mon Feb 06 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.7-alt1
- Updated to 3.1 patchlevel 7.
- Applied fix for "exec -l /bin/bash" bug from FC.

* Tue Jan 10 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.5-alt1
- Updated to 3.1 patchlevel 5.

* Thu Jan 05 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- Updated to 3.1 patchlevel 1.
- Reviewed and updated patches.
- Synced with 3.1.1-owl1 (Owl) and 3.1-2 (FC).
- Corrected bash(1) manpage (closes #8383).
- Added "su-" alias (closes #8227).

* Sat Dec 31 2005 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt8
- %_sysconfdir/bashrc: updated bash check (closes #3009).
- Backported upstream fix for WCONTINUED problem.

* Fri Feb 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt7
- %_sysconfdir/bashrc: updated PROMPT_COMMAND.
- Fixed build with gcc-3.4.x (closes #6082).

* Thu Oct 09 2003 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt6
- Fixed verbose shift with no argument (deb #159996).
- Better fix for rbash misbehaviour (rh #78455).
- Updated the Bash FAQ to version 3.26.
- Enhanced --rpm-requires support.

* Sun Apr 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt5
- Fixed rh-alt-requires patch so it works with builtins again.
- %_sysconfdir/bashrc: added Eterm to the list of terminal names
  which support title change escape sequence (#0002410).

* Sat Dec 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt4
- Updated the Bash FAQ to version 3.21.
- Fixed rbash misbehaviour, patch from Chet Ramey.
- jobs.c (initialize_job_control): always call get_tty_state().
- jobs.c (initialize_job_signals): always call set_sigwinch_handler().

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt3
- Fixed bashbug script.

* Sun Sep 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt2
- Applied two "official" patches from
  ftp://ftp.cwru.edu/pub/bash/bash-2.05b-patches/.

* Sun Sep 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05b-alt1
- 2.05b:
  updated patches:
  + owl-alt-fixes
  + owl-alt-tmp
  merged upstream:
  + rh-mailcheck
  obsolete:
  + rh-kill_builtin
  + deb-gnusource
  + deb-arm
- Build sh with --disable-help-builtin.
- Build bash with --enable-separate-helpfiles.

* Sun Sep 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05a-alt3
- Linked with readline-4.3.

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05a-alt2
- Linked with libtinfo.

* Fri Jun 07 2002 Dmitry V. Levin <ldv@altlinux.org> 2.05a-alt1
- 2.05a, updated patches.
- Use texi2dvi from texinfo package for bash build.
- Default to vitmp in fc (the history editor) and bashbug script (Owl).
- Don't mishandle negative pid in `kill' builtin (rh).
- Fix for SEGV when some special shell variables are declared as array (deb).
- Added service completion (Ian Macdonald).
- Built with --disable-net-redirections (use netcat instead).
- Make non-interactive shells begun with argv[0][0] == '-'
  run the startup files when not in posix mode.
- Check whether shell being run by sshd and source the .bashrc
  if so (like the rshd behavior).
- bashbug: send bug reports also to ALT bash maintainer.
- Introduced %_sysconfdir/bashrc.d directory.
- bashrc: changed scripts load directory:
  %_sysconfdir/profile.d/ --> %_sysconfdir/bashrc.d/
  (upgrading to glibc >= 2.2.5-alt6 is recommended).
- alias.sh: reduced ammount of default aliases and relocated it
  from %_sysconfdir/profile.d/ to %_sysconfdir/bashrc.d/.

* Wed Mar 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.05-alt6
- Reenable job control for /bin/sh.

* Wed Mar 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.05-alt5
- Merged in Owl patches:
  + bash-2.05-owl-alt-fixes
  + bash-2.05-owl-tmp
- Merged in Debian patches:
  + bash-2.05-deb-64bit
  + bash-2.05-deb-gnusource
  + bash-2.05-deb-print_cmd
  + bash-2.05-deb-random
  + bash-2.05-deb-man
- Merged in RedHat patches:
  + bash-2.05a-rh-loadables.patch
  + bash-2.05a-rh-mailcheck.patch
- Fixed bashrc interactive shell detection.
- Fixed bashrc $f setting (#0000663).
- Fixed build without readline support.
- Build /bin/sh as outstanding package sh
  (without interactive features).

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.05-alt4
- Added explicit prereqs on shared libraries.
- Added IPv6 patch (from pld).
- Added some bugfix patches from the maintainer.
- Added rbash link.
- Updated semantic of aliases loading (from mdk).
- Relocated documentation.
- Removed "which" alias.

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.05-alt3
- Fixed tmpfile handling in bashbug script.

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.05-alt2
- Don't use strcoll(3) for range comparisons in bracket expressions,
  as in %name-2.04.

* Fri Apr 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.05-alt1
- 2.05

* Tue Dec 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.04-ipl2mdk
- Added winsize patch; checkwinsize now enabled by default;
  added ROWS and COLUMNS dynamic variables.
- Moved examples to separate subpackage.

* Mon Oct 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.04-ipl1mdk
- RE adaptions.
- FHSification.
- Merge patches from RH.

* Sun Jun 11 2000 Dmitry V. Levin <ldv@fandra.org>
- Merge with MDK.

* Wed Mar 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.04

* Wed Sep 20 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Aug 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove the alias to ls colors in bash_alias (doble with fileutils scripts).

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong group in doc package.
- Increase version ;).

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong man links (#20).

* Fri Jul 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
  - Ken Estes <kestes@staff.mail.com>
    - patch to detect what executables are required by a script.

* Wed Jul 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove 'DarkTiti' hack.

* Fri Jul 16 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Make the `echo' builtin expand backslash-escaped characters by default,
  without requiring the `-e' option.  This makes the Bash `echo' behave
  more like the System V version.

* Tue Jul 9 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- french description

* Tue Jul 8 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- compiled against local libreadline (which is not compiled in now)
  => reduce the size of bash by 42%%.
  Moreover, a part of its memory is shared with other readline programs (bc, ...)
- disable built-in time command (incompatible with standard POSIX time command)

* Tue May 25 1999 Bernhard Rosenkr�nzer <bero@mandrakesoft.com>
- handle RPM_OPT_FLAGS

* Sat May 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- alias.sh fix with the new syntax of bash2.

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fixing many stupid forget :-((

* Tue Apr 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Relifting of the doc-section.
- Moving the alias to a new files.

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- handle RPM_OPT_FLAGS
- add de locale
- add some aliases (ls=ls --color, md, rd, cd..) to bashrc
- fix download URLs
- make it compile if the release number contains non-digits
- We're NOT a %%arch-redhat-linux

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.
- update to 2.03.

* Fri Feb 12 1999 Cristian Gafton <gafton@redhat.com>
- build it as bash2 instead of bash

* Tue Feb  9 1999 Bill Nottingham <notting@redhat.com>
- set 'NON_INTERACTIVE_LOGIN_SHELLS' so profile gets read

* Thu Jan 14 1999 Jeff Johnson <jbj@redhat.com>
- rename man pages in bash-doc to avoid packaging conflicts (#606).

* Wed Dec 02 1998 Cristian Gafton <gafton@redhat.com>
- patch for the arm
- use $RPM_ARCH-redhat-linux as the build target

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- rewrite %%pre, axe %%postun (to avoid prereq loops)

* Wed Aug 19 1998 Jeff Johnson <jbj@redhat.com>
- resurrect for RH 6.0.

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.02.1

* Thu Jun 11 1998 Jeff Johnson <jbj@redhat.com>
- Package for 5.2.

* Mon Apr 20 1998 Ian Macdonald <ianmacd@xs4all.nl>
- added POSIX.NOTES doc file
- some extraneous doc files removed
- minor .spec file changes

* Sun Apr 19 1998 Ian Macdonald <ianmacd@xs4all.nl>
- upgraded to version 2.02
- Alpha, MIPS & Sparc patches removed due to lack of test platforms
- glibc & signal patches no longer required
- added documentation subpackage (doc)

* Fri Nov 07 1997 Donnie Barnes <djb@redhat.com>
- added signal handling patch from Dean Gaudet <dgaudet@arctic.org> that
  is based on a change made in bash 2.0.  Should fix some early exit
  problems with suspends and fg.

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- added %%clean

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- added comment explaining why install-info isn't used
- added mips patch

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
