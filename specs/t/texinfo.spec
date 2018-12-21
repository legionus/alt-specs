Name: texinfo
Version: 6.5
Release: alt1.1

Summary: Tools needed to create Texinfo format documentation files
License: GPLv3+
Group: Publishing
Url: http://www.gnu.org/software/texinfo/

# ftp://ftp.gnu.org/gnu/texinfo/texinfo-%version.tar.xz
Source0: texinfo-%version.tar
Source1: update-info-dir
Source2: update-info-dir.8
Source3: info-dir.filetrigger
Source4: info-install.macros
Source5: install_info
Source6: uninstall_info
Source7: texi2pdf
Source8: texi2pdf.man

Patch1: texinfo-alt-install-info-dot_exe.patch
Patch2: texinfo-alt-install-info-zio.patch
Patch3: texinfo-alt-install-info-rpm.patch
Patch4: texinfo-alt-texi2dvi-baroque-shells.patch
Patch5: texinfo-alt-texi2any-version.patch
Patch6: texinfo-alt-makeinfo-split-size.patch
Patch7: texinfo-alt-perl_vendor_libdir.patch
Patch8: texinfo-alt-tests.patch

Requires: makeinfo = %version-%release
Requires: texi2dvi = %version-%release

BuildRequires(pre): rpm-build-tex
BuildRequires: cvs bzlib-devel help2man libtinfo-devel libzio-devel zlib-devel
BuildRequires: perl-devel
BuildRequires: perl(Locale/Messages.pm)
BuildRequires: perl(Pod/Simple/PullParser.pm)
BuildRequires: perl(Text/Unidecode.pm)
BuildRequires: perl(Unicode/EastAsianWidth.pm)
BuildRequires: perl(Unicode/Normalize.pm)
%{?!_without_check:%{?!_disable_check:BuildRequires: gzip-utils /dev/pts}}

%package -n makeinfo
Summary: Utilities for translating texinfo source documentation to various other formats
Group: Publishing
Requires: rpm-macros-info-install = %version-%release

%package -n texi2dvi
Summary: Utilities for translating texinfo source documents to dvi, ps, and pdf
Group: Publishing
BuildArch: noarch
Requires: rpm-macros-info-install = %version-%release
# due to texi2pdf and %_texmfmain/tex/texinfo
Conflicts: tetex-core <= 0:2.0-alt8

%package -n info-install
Summary: A program to update the GNU texinfo config file
Group: System/Base
PreReq: libzio >= 0:0.1-alt4

%package -n info
Summary: A standalone tty-based reader for GNU texinfo documentation
Group: System/Base
Requires: info-install = %version-%release

%package -n rpm-macros-info-install
Summary: Set of RPM macros for packaging texinfo files
Group: System/Base
BuildArch: noarch

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file.  Normally,
you'd have to write two separate documents: one for online help or other
online information and the other for a typeset manual or other printed
work.  Using Texinfo, you only need to write one source document.
Then when the work needs revision, you only have to revise one source
document.  The GNU Project uses the Texinfo file format for most of its
documentation.

%description -n makeinfo
This package contains texi2all a.k.a. makeinfo - a translator of
texinfo source documentation to various other formats.

%description -n texi2dvi
This package contains texi2dvi and related utilities for translating
texinfo source documents to dvi, ps, and pdf.

%description -n info
The GNU project uses the texinfo file format for much of its
documentation.  The info package provides a standalone tty-based browser
program for viewing texinfo files.

%description -n info-install
This packages contains install-info - a program to update menu entries
in the Info system config files.

%description -n rpm-macros-info-install
This packages contains new RPM macros for packaging texinfo files.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

install -pm755 %_sourcedir/texi2pdf util/

%build
rm po/*.gmo po/stamp*
find -name configure.ac -printf '%%h\n' |while read dir; do
	pushd "$dir"
	rm aclocal.m4
	%autoreconf
	popd
done
%configure \
	--with-external-libintl-perl \
	--with-external-Text-Unidecode \
	--with-external-Unicode-EastAsianWidth \
	--enable-perl-xs \
	#
%make_build MAKEINFOFLAGS=--no-split \
	perl_vendor_privlibdir=%perl_vendor_privlib \
	perl_vendor_archlibdir=%perl_vendor_archlib \
	#
xz -k9 NEWS

%install
%makeinstall_std install-tex \
	TEXMF=%_texmfmain MAKEINFOFLAGS=--no-split \
	perl_vendor_privlibdir=%perl_vendor_privlib \
	perl_vendor_archlibdir=%perl_vendor_archlib \
	#

# these files shouldn't be packaged
rm %buildroot%perl_vendor_archlib/Texinfo/Convert/XSParagraph/*.{l,}a
rm %buildroot%perl_vendor_privlib/Texinfo/Convert/XSParagraph/TestXS.pm

# generic/epsf/epsf.tex is packaged in tetex and texlive
rm -r %buildroot%_texmfmain/tex/generic

# Install catalogue.
mkdir -p %buildroot%_sysconfdir
touch %buildroot%_sysconfdir/info-dir{,.old}
ln -fnrs %buildroot%_sysconfdir/info-dir %buildroot%_infodir/dir

# Relocate install-info.
mkdir -p %buildroot/sbin
mv %buildroot%_bindir/install-info %buildroot/sbin/

# Install info-dir filetrigger.
mkdir -p %buildroot%_rpmlibdir
install -pm755 %_sourcedir/info-dir.filetrigger %buildroot%_rpmlibdir/

# Install new rpm macros.
install -pDm644 %_sourcedir/info-install.macros %buildroot%_rpmmacrosdir/info-install

# Install install_info and uninstall_info stub scripts.
mkdir -p %buildroot%_sbindir
install -pm755 %_sourcedir/{,un}install_info %buildroot%_sbindir/

install -pm644 %_sourcedir/texi2pdf.man %buildroot%_man1dir/texi2pdf.1
install -pm755 %_sourcedir/update-info-dir %buildroot%_sbindir/
mkdir -p %buildroot%_man8dir
install -pm644 %_sourcedir/update-info-dir.8 %buildroot%_man8dir/

%find_lang --output=texinfo.lang texinfo texinfo_document

%check
export ALL_TESTS=yes LANG=en_US.utf8
%make_build -k check VERBOSE=1
unset ALL_TESTS LANG

%files -f texinfo.lang
%doc AUTHORS NEWS.* README TODO

%files -n makeinfo
%_bindir/makeinfo
%_bindir/texi2any
%_bindir/pod2texi
%_man1dir/makeinfo.*
%_man1dir/texi2any.*
%_man1dir/pod2texi.*
%_man5dir/texinfo.*
%_infodir/texinfo.*
%_datadir/texinfo/
%perl_vendor_archlib/Texinfo/
%perl_vendor_privlib/*Texinfo/
%perl_vendor_privlib/Pod/Simple/*

%files -n texi2dvi
%_bindir/*texi2dvi
%_bindir/texi2pdf
%_bindir/texindex
%_man1dir/*texi2dvi.*
%_man1dir/texi2pdf.*
%_man1dir/texindex.*
%_texmfmain/tex/texinfo/

%files -n info
%_bindir/info
%_mandir/man?/info.*
%_infodir/info*.info*

%files -n info-install
%config(noreplace) %verify(not md5 mtime size) %ghost %_sysconfdir/info-dir*
%_rpmlibdir/*.filetrigger
/sbin/install-info
%_sbindir/*
%_infodir/dir
%_mandir/man?/install-info.*
%_man8dir/update-info-dir.*

%files -n rpm-macros-info-install
%_rpmmacrosdir/*

%changelog
* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 6.5-alt1.1
- NMU: build with rpm-build-tex

* Sat Dec 09 2017 Dmitry V. Levin <ldv@altlinux.org> 6.5-alt1
- 6.0 -> 6.5 (closes: #34299).

* Fri Dec 11 2015 Dmitry V. Levin <ldv@altlinux.org> 6.0-alt3
- makeinfo: changed --version output to be compatible
  with earlier versions of makeinfo.

* Thu Dec 03 2015 Dmitry V. Levin <ldv@altlinux.org> 6.0-alt2
- Raised default split size from 300000 to 33554432.

* Mon Nov 30 2015 Dmitry V. Levin <ldv@altlinux.org> 6.0-alt1
- Updated to 6.0 (closes: #31449).

* Sat Nov 02 2013 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- Updated to 5.2.

* Sat Nov 02 2013 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt9
- Split texinfo into makeinfo and texi2dvi.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.13-alt8.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov 13 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt8
- Use rpm-build-texmf for build, to get autogenerated texmf dependencies.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt7
- Added "make check" to %%check section.

* Sat Jun 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt6
- info-install: Removed redundant %%post script,
  enhanced warning messages.

* Wed May 20 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt5
- makeinfo: Backported fixes from cvs (closes: #19997).

* Mon May 18 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt4
- update-info-dir: Changed to make separate index
  for each subdirectory inside info directory.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt3
- info: Backported fixes from cvs.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt2
- Packaged %%ghost /etc/info-dir.old.

* Sat May 16 2009 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt1
- Updated to 4.13.
- Packaged %_datadir/texmf/tex/texinfo (closes: #20032).
- Adopted %_sbindir/update-info-dir from Debian.
- Implemented info-dir filetrigger.
- Packaged new RPM macros.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt4
- Dropped obsolete %_sysconfdir/rpm/macros.d/texinfo file.
- Fixed build with fresh autoconf.

* Fri Mar 21 2008 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt3
- Disabled md5, mtime and size verification for /etc/info-dir (#15013).
- Imported upstream fix for makeinfo(1) producing invalid direntry (#15014).
- Imported upstream fix for info(1) crash after window resize (RH#243971).
- Imported patches from debian 4.11.dfsg.1-4 package.
- Compressed NEWS, dropped ChangeLog.

* Thu Feb 23 2008 Alex V. Myltsev <avm@altlinux.ru> 4.11-alt2
- texinfo: Drop the requirement on tetex-dvips introduced in previous release.

* Thu Feb 14 2008 Alex V. Myltsev <avm@altlinux.ru> 4.11-alt1
- new version.

* Thu Dec 14 2006 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt4
- texindex: Remove offline sorting (patch from Miloslav Trmac).

* Tue Dec 12 2006 Slava Semushin <php-coder@altlinux.ru> 4.8-alt3.1
- NMU
- Fix multibyte input/output in info utility (#10307)

* Sat Oct 28 2006 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt3
- texindex: Fixed potential heap buffer overflow
  (CVE-2006-4810, patch from Miloslav Trmac).
- info-install: Updated package dependencies.

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt2
- Do not package texi2pdf which was added in 4.8-alt1
  since it already owned by with tetex-core package.

* Tue Jan 04 2005 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt1
- Updated to 4.8.
- Updated patches.

* Thu Dec 30 2004 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt1
- Updated to 4.7.
- Reviewed and updated patches.
- Implemented .gz/.bz2 support using libzio.

* Mon Jul 28 2003 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt1
- Updated to 4.6, updated/rediffed patches.
- Updated texinfo.tex to version 2003-07-24.06.
- install-info:
  + corrected russian translation;
  + exit silently when RPM_EXCLUDEDOCS environment variable is set.

* Fri May 02 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt2
- info-install: added install_info and uninstall_info scripts.
- texinfo:
  + updated texinfo.tex to version 2003-04-28.10;
  + added %_sysconfdir/rpm/macros.d/texinfo with new macros.
- Deal with info dir entries such that the menu looks pretty.

* Wed Mar 05 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt1
- Updated to 4.5.
- Updated russian translation, to fix Ctrl-H crash bug.

* Sun Nov 17 2002 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt1
- Updated to 4.3, reviewed patches:
  + rh-texi2dvi-fileext - merged;
  + owl-alt-texindex-tmp - updated;
  + alt-bz2_support - updated;
  + alt-texi2dvi-tmp - updated;
  + deb-alt-texi2dvi-tex - updated.
- Added texinfo.tex to this package (#0001319).

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 4.2-alt3
- Patched to link with libtinfo.

* Fri Jun 07 2002 Dmitry V. Levin <ldv@altlinux.org> 4.2-alt2
- Reviewed patches; two was obsolete, rest have been repackaged.
- texi2dvi: fixed tmp handling.
- texi2dvi: extra check for tex presence (deb).
- info/{infodoc,infomap,session}.c: applied fixes (deb).
- Added infokey to the info subpackage.
- Added manpages to all subpackages.
- Dropped unneeded %_sysconfdir/X11/wmconfig/info.
- Fixed interpackage dependencies.
- Updated buildrequires.

* Tue May 14 2002 Alexey Morozov <morozov@novosoft.ru> 4.2-alt1
- A new version (.po recoding doesn't needed anymore)
- (inger) release changed to alt1

* Sat Apr 13 2002 Alexey Morozov <morozov@novosoft.ru> 4.1-local1
- A new version (4.1, patch7 is from RedHat's rawhide)
- Small build dependencies fixup

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 4.0-ipl18mdk
- Added patch from Owl (for tmpdirs).

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0-ipl17mdk
- Merged RH patches.

* Sat Dec 02 2000 Dmitry V. Levin <ldv@fandra.org> 4.0-ipl16mdk
- Added: info-install: PreReq: gzip, bzip2.
- Fixed info-dir.

* Mon Aug 21 2000 Dmitry V. Levin <ldv@fandra.org> 4.0-ipl15mdk
- RE adaptions.

* Thu Aug 10 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 4.0-15mdk
- use more macros, add no replace to make rpmlint happy

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0-14mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.0-13mdk
- fix broken link (Anton Graham)

* Tue Jul 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.0-12mdk
- build release for BM
- use new macros

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 4.0-11mdk
- built for 7.1 (new group structure)
- relocate the info-tty package.

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 4.0-10mdk
- add info prerequires install-info (because some packages have trigger on package "info")

* Sat Mar  4 2000 Pixel <pixel@mandrakesoft.com> 4.0-9mdk
- add info requires install-info (because some packages have trigger on package "info")

* Fri Mar  3 2000 Pixel <pixel@mandrakesoft.com> 4.0-8mdk
- have /sbin/install-info in its own package (for prereq pb at install)

* Wed Dec  1 1999 Pixel <pixel@linux-mandrake.com>
- removed the glibc prereq for info

* Mon Nov 15 1999 Pixel <pixel@mandrakesoft.com>
- changed the deps. Forced info (and so install-info) to not depends on gpm :(
- unremoved gpm as it can't be done

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Sep 28 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 4.0

* Mon Aug 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Increase release (oups).

* Sun Aug 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Made a patch for install-info.c to handle bzip2 (where the old patch is gone ?)

* Tue Aug 17 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 3.12q
- rewrite zlib patch (incompatibility with 3.12q)

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Updated to 3.12n
- Add french description

* Tue Jul  6 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- info Provides install-info and now knows so.

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.12h.
- Upgrading patch.

* Thu Apr 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch to handle bzip2 and other compresion on install-info.
- Making dependence explicitly from bzip2.

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch from RedHat 6.0.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Thu Mar 11 1999 Cristian Gafton <gafton@redhat.com>
- version 3.12f
- make %_infodir/dir to be a %%config(noreplace)

* Wed Nov 25 1998 Jeff Johnson <jbj@redhat.com>
- rebuild to fix docdir perms.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- fix allocation problems in install-info

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- /sbin/install-info should not depend on %_libdir/libz.so.1 -- statically
  link with %_libdir/libz.a.

* Fri Aug 07 1998 Erik Troan <ewt@redhat.com>
- added a prereq of bash to the info package -- see the comment for a
  description of why that was done

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add %%attr to permit non-root build.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean
- manhattan build

* Wed Mar 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 3.12
- added buildroot

* Sun Nov 09 1997 Donnie Barnes <djb@redhat.com>
- moved %_infodir/dir to /etc/info-dir and made %_infodir/dir a
  symlink to /etc/info-dir.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry for info

* Wed Oct 01 1997 Donnie Barnes <djb@redhat.com>
- stripped /sbin/install-info

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added info-dir to filelist

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- added patch from sopwith to let install-info understand gzip'ed info files
- use skeletal dir file from texinfo tarball (w/ bash entry to reduce
  dependency chain) instead (and install-info command everywhere else)
- patches install-info to handle .gz names correctly

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- patched install-info.c for glibc.
- added %_bindir/install-info to the filelist

* Tue Feb 18 1997 Michael Fulbright <msf@redhat.com>
- upgraded to version 3.9.
