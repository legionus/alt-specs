Name: acct
Version: 6.6.4
Release: alt1

Summary: Utilities for monitoring process activities.
License: GPLv3+
Group: Monitoring
Url: http://www.gnu.org/software/acct/

# ftp://ftp.gnu.org/gnu/acct/acct-%version.tar.gz
Source: acct-%version.tar

Source1: mklog.sh
Source2: acct.init
Source3: acct.service
Source4: acct.log
Source5: dump-acct.8

Patch1: acct-owl-doc.patch
Patch2: acct-alt-program_name.patch
Patch3: acct-rh-doc.patch
patch4: acct-rh-ub.patch
Patch5: acct-deb-alt-doc.patch
Patch6: acct-deb-alt-cross-build-support.patch

Provides: psacct = %version-%release
Obsoletes: psacct < %version-%release

BuildRequires: makeinfo

%description
The acct package contains several utilities for monitoring process
activities, including ac, lastcomm, accton and sa.  The ac command
displays statistics about how long users have been logged on.  The
lastcomm command displays information about previous executed commands.
The accton command turns process accounting on or off.  The sa command
summarizes information about previously executed commands.

%prep
%setup
rm *.info
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%autoreconf
%configure --enable-linux-multiformat
%make_build

%install
mkdir -p %buildroot{/sbin,/var/account}
%makeinstall_std
install -pm644 %_sourcedir/dump-acct.8 %buildroot%_man8dir/

# These come from SysVinit.
mv %buildroot%_bindir/last %buildroot%_bindir/last-acct
mv %buildroot%_man1dir/last.1 %buildroot%_man1dir/last-acct.1

# Move accton to /sbin, leaving historical symlink
mv %buildroot%_sbindir/accton %buildroot/sbin/accton
ln -r -s %buildroot/sbin/accton %buildroot%_sbindir/

touch %buildroot/var/account/{p,usr,sav}acct
install -pD -m755 %_sourcedir/acct.init \
	%buildroot%_initdir/acct
install -pD -m644 %_sourcedir/acct.service \
	%buildroot%_unitdir/acct.service
install -pD -m640 %_sourcedir/acct.log \
	%buildroot%_sysconfdir/logrotate.d/acct
install -pm700 %_sourcedir/mklog.sh \
	%buildroot/sbin/acct-mklog

%post
/sbin/acct-mklog {p,usr,sav}acct
%post_service acct

%preun
%preun_service acct

%files
%config(noreplace) %_sysconfdir/logrotate.d/acct
%_initdir/acct
%_unitdir/acct.service
/sbin/*
%_bindir/*
%_sbindir/*
%_infodir/*.info*
%_mandir/man?/*
%attr(700,root,root) %dir /var/account
%attr(600,root,root) %ghost /var/account/*
%doc AUTHORS README NEWS ChangeLog TODO

%changelog
* Thu Nov 29 2018 Dmitry V. Levin <ldv@altlinux.org> 6.6.4-alt1
- 6.6.1 -> 6.6.4.

* Thu Apr 18 2013 Dmitry V. Levin <ldv@altlinux.org> 6.6.1-alt1
- Updated to 6.6.1.
- Added systemd support (closes: #28012).

* Mon Nov 09 2009 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.6
- Remove obsolete %%install_info/%%uninstall_info calls.
- Remove obsolete explicit package requirements.

* Mon Oct 08 2007 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.5
- Fixed more compilation warnings.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.4
- Fixed compilation warnings.

* Sat Aug 05 2006 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.3
- Dropped acctoff.

* Tue Jun 20 2006 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.2
- Adjusted the logrotate configuration file to redirect stdout to /dev/null.

* Sun May 21 2006 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt0.1
- Updated to 6.4-pre1.
- Build with system getopt.

* Thu Apr 07 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3.5-alt5
- Fixed 64bit issues in calls to ctime().

* Mon May 05 2003 Dmitry V. Levin <ldv@altlinux.org> 6.3.5-alt4
- Added a patch from Denis Ducamp to support /dev/pts in lastcomm(1).
- Deal with info dir entries such that the menu looks pretty.

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 6.3.5-alt3
- Explicitly use autoconf-2.13 and automake-1.4 for build.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 6.3.5-alt2
- Heavy documentation corrections and cleanups (Owl).
- Build without included getopt code.

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 6.3.5-alt1
- 6.3.5
- Renamed back to acct.
- Moved logfiles to /var/account (FHS-2.2).
- Added dump-acct and dump-utmp manpages from Debian.
- Fixed logrotate script (ideas from Owl).

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 6.3.2-ipl3mdk
- Fixed typo in %%postinstall section.

* Thu Feb 01 2001 Dmitry V. Levin <ldv@fandra.org> 6.3.2-ipl2mdk
- Updated startup and logrotate scripts.

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 6.3.2-ipl1mdk
- FHSification.
- Fix texinfo documentation.
- Added progname patch.

* Mon Mar 27 2000 Dmitry V. Levin <ldv@fandra.org>
- 6.3.2

* Sat Jan  1 2000 Dmitry V. Levin <ldv@fandra.org>
- fix startup script

* Wed Sep 28 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- wrap post script with reference count.

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- install-info sucks.  Still.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 8)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- #define HAVE_LINUX_ACCT_H too, so it works. :)

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- accton needs to be accessible to /etc/rc.d/init.d/halt

* Fri May 08 1998 Erik Troan <ewt@redhat.com>
- install-info sucks

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 6.2 to 6.3

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
