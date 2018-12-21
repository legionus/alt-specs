%define realname automake
%define dialect _1.6
%define dialect_regex _1\.6
%define suff -1.6

Name: %realname%dialect
Version: 1.6.3
Release: alt10
Epoch: 1

%add_findreq_skiplist %_datadir/%realname%suff/config.guess
%set_compress_method xz
%define _perl_lib_path %perl_vendor_privlib:%_datadir/%realname%suff

Summary: A GNU tool for automatically creating Makefiles
License: GPL
Group: Development/Other
Url: http://www.gnu.org/software/automake/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

%define srcname %realname-%version

Source: ftp://ftp.gnu.org/gnu/%realname/%srcname.tar.bz2

Patch1: automake-1.6.1-alt-texinfo.patch
Patch2: automake-1.6.3-alt-aclocal_libtool.patch
Patch3: automake-1.6-cvs-pythondir.patch

PreReq: automake-common

BuildRequires: makeinfo

%description
Automake is a tool for automatically generating Makefiles compliant with the
GNU Coding Standards.

You should install Automake if you are developing software and would like to
use its capabilities of automatically generating GNU standard Makefiles.  If
you install Automake, you will also need to install GNU Autoconf package.

%prep
%setup -q -n %srcname
%patch1 -p1
%patch2 -p1
%patch3 -p1
xz -k9 ChangeLog NEWS TODO

%build
%set_autoconf_version 2.5
%configure
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall MAKEINFOFLAGS=--no-split

install -p -m644 %realname%suff.info %buildroot%_infodir/

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat <<EOF >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
^/usr/share/aclocal(%dialect_regex)?/.+\.m4$
EOF

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/*
%_bindir/*%suff
%_datadir/aclocal%suff
%_datadir/%realname%suff
%_infodir/*.info*
%doc AUTHORS README THANKS ChangeLog.* NEWS.* TODO.*

%changelog
* Wed Aug 08 2018 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt10
- Dropped alternatives in favour of automake-defaults setup.
- Changed the compression method applied to documentation files
  from bzip2 to xz.

* Mon Dec 07 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.6.3-alt9
- Added BR: makeinfo.
- Switched to compress_method xz.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt8
- Removed obsolete %%install_info/%%uninstall_info calls.
- Switched to alternatives-0.4.

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt7
- Merged fixes from 1.10-alt2.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt6
- aclocal: enhanced $LIBTOOL_VERSION support.

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt5
- aclocal: added $LIBTOOL_VERSION support.

* Sat May 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt4
- Deal with info dir entries such that the menu looks pretty.

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.6.3-alt3.2
- new alternatives format

* Thu Mar 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.6.3-alt3.1
- move to new altenatives scheme

* Mon Dec 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt3
- Corrected provides.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt2
- Added automake-common support.
- Raised alternatives priority.

* Tue Oct 22 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt1
- Updated to 1.6.3.

* Wed May 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.1-alt2
- Added buildreq substitution rules.

* Sat May 18 2002 Alexey Voinov <voins@voins.program.ru> 1:1.6.1-alt1
- Renamed to automake_1.6, based on automake-1.4-alt4.p5
- New version (1.6.1).
- Added update-alternatives support.

* Tue Jan 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.4-alt4.p5
- Added aclocal filter for buildreq.

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt3.p5
- Dont raise error when there is source in a subdirectory (hjl, rh #35156).
  This was preventing automake from working in binutuls/gas
  [patch from HJ Lu <hjl@gnu.org>]
- Format long lines of output properly with backslash + newlines as in 1.4
  (hjl, rh #35259)

* Mon Aug 20 2001 Sergey Vlasov <vsu@altlinux.ru> 1.4-alt2.p5
- Bugfix for Elisp file installation.
- Bugfix for lex file handling.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1.p5
- 1.4-p5

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1.p4
- 1.4-p4

* Sat Jun 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl16mdk
- 1.4-p3

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl15mdk
- 1.4-p2

* Fri May 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl14mdk
- 1.4-p1

* Sun May 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl13mdk
- Updated vendor information.

* Thu Oct 05 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl12mdk
- Merge RH patch.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl11mdk
- RE and Fandra adaptions.

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4-8mdk
- new groups

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with Jeff package.

* Tue Jun 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 1.4 version.
- Merging with RedHat patch.

* Thu May 13 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- 1.4a

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- arm netwinder patch

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb  8 1999 Jeff Johnson <jbj@redhat.com>
- add patches from CVS for 6.0beta1

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.4.

* Mon Nov 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.3b.
- add URL.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 1.3

* Tue Oct 28 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot; added aclocal files

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- made it a noarch package

* Thu Oct 16 1997 Michael Fulbright <msf@redhat.com>
- Fixed some tag lines to conform to 5.0 guidelines.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- updated to 1.2

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- first version (1.0)
