# see http://lists.altlinux.org/pipermail/devel/2012-February/193243.html
%def_disable python

# see http://bugzilla.altlinux.org/31466
%def_disable guile

# https://lists.altlinux.org/pipermail/devel/2018-August/205163.html
%def_enable mh

%define use_chrpath 0
%define snapshot    0

Name: mailutils

%define baseversion 3.5

%if %snapshot
%define snapshotdate 20170306
Version: %baseversion
Release: alt0.%snapshotdate.1
%define srcdir %name-%snapshotdate
%else
Version: %baseversion
Release: alt2
%define srcdir %name-%version
%endif

Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: GNU Mailutils

License: %gpl3plus

%if %snapshot
Source0:        %name-%version-%snapshotdate.tar.gz
%else
Source0:        %name-%version.tar.gz
%endif

Patch1: mailutils-2.0.90-pkg-config-hack.diff

URL: http://www.gnu.org/software/%{name}/%{name}.html
Group: Networking/Mail

Conflicts: mailx

Provides: /bin/mail

%add_findreq_skiplist */usr/bin/guimb

BuildRequires(pre): rpm-build-licenses

Requires: libmailutils = %{version}-%{release}
Requires: libreadline

# Automatically added by buildreq on Mon Feb 06 2012
# optimized out: emacs-X11 emacs-base emacs-cedet-speedbar emacs-common fontconfig guile18 libX11-locales libgdk-pixbuf libgmp-devel libgpg-error libltdl7-devel libncurses-devel libstdc++-devel libtinfo-devel python-base python-modules
BuildRequires: bzlib-devel flex gcc-c++ glibc-devel libdb4-devel libgcrypt-devel libgdbm-devel libgnutls-devel libldap-devel libpam-devel libreadline-devel libtokyocabinet-devel python-devel zlib-devel

BuildRequires: /dev/pts
BuildRequires: emacs-X11
BuildRequires: makeinfo

BuildRequires: libltdl7-devel

BuildRequires: perl-podlators

%if %use_chrpath
BuildRequires: chrpath
%endif

%description
GNU Mailutils contains a series of useful mail clients, servers, and
libraries. These are the primary mail utilities of the GNU system.
This package provides a replacement for /bin/mail(x) conforming to
the UNIX98 specification for mailx. It provides also a mail delivery
agent maidag, and other tools including guimb, dotlock, movemail, frm.

%package -n libmailutils
Summary: GNU Mailutils: mailbox access library.
License: %lgpl3plus
Group: System/Libraries
Provides: libmailutils-sieve = %{version}
Obsoletes: libmailutils-sieve

%description -n libmailutils
The runtime library libmailbox contains various mailbox access
routines and support for a number of mailbox types, such as mbox,
maildir, mh, POP3, and IMAP4. It also supports MIME message
handling, and sending mail via SMTP and /sbin/sendmail.

%package -n libmailutils-devel
Summary: GNU Mailutils: mailbox access development.
License: %lgpl3plus
Requires: libmailutils, libmailutils-sieve
Group: Development/Other

%description -n libmailutils-devel
GNU Mailutils: mailbox access development.

%package -n libmailutils-devel-static
Summary: GNU Mailutils: mailbox access static library development.
License: %lgpl3plus
Requires: libmailutils-devel
Group: Development/Other

%description -n libmailutils-devel-static
GNU Mailutils: mailbox access static library development.

%package doc
Summary: GNU Mailutils: documentation.
License: %fdl
Group: Development/Documentation
BuildArch: noarch

%description doc
API reference for libmailbox and user documentation for the rest of
the GNU Mailutils.

%package pop3d
Summary: GNU Mailutils: POP3 daemon.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Conflicts: courier-imap
Group: System/Servers

%description pop3d
The GNU POP3 daemon. Uses libmailbox to support different styles of
mailboxes.

%package imap4d
Summary: GNU Mailutils: IMAP4 daemon.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Group: System/Servers

%description imap4d
The GNU IMAP4 daemon. Uses libmailbox to support different styles of
mailboxes.

%package sieve
Summary: GNU Mailutils: mail filtering language Sieve.
License: %lgpl3plus
Requires: libmailutils = %{version}-%{release}, libmailutils-sieve = %{version}-%{release}
Group: Networking/Mail

%description sieve
GNU implementation of the mail filtering language Sieve, described in
RFC 3028 and RFC 3431. This packages contains also the Sieve interpreter
and Sieve to Scheme translator and filter.

%package comsatd
Summary: GNU Mailutils: Comsat daemon.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Group: System/Servers

%description comsatd
GNU Comsatd is the server which receives reports of incoming mail and
notifies users, wishing to get this service. It can be started either
from `inetd.conf' or as a standalone daemon.

%package maidag
Summary: GNU Mailutils: General-purpose Mail Delivery Agent.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Group: System/Servers

%description maidag
The name `maidag' stands for Mail Delivery Agent. It is a
general-purpose MDA offering a rich set of features. It can operate
both in traditional mode, reading the message from its standard input,
and in LMTP mode. Maidag is able to deliver mail to any mailbox
format, supported by GNU Mailutils.

%if_enabled guile
%package guile
Summary: GNU Mailutils: Guile bindings.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Requires: guile >= 1.8
Group: System/Libraries

BuildRequires: guile18-devel

%description guile
Guile bindings for GNU Mailutils.
%endif

%package locales
Summary: National Language files for mailutils
License: %gpl3plus
Group: Networking/Mail
BuildArch: noarch

%description locales
National Language files for mailutils

%if_enabled mh
%package mh
Summary: GNU Mailutils: The Message Handling System.
License: %gpl3plus
Requires: libmailutils = %{version}-%{release}
Requires: emacs-base
Group: Networking/Mail

%description mh
The GNU MH (Message Handling System).
%endif

%if_enabled python
%package -n libmailutils-python
Summary: GNU Mailutils: libraries for integration with Python
License: %lgpl3plus
Requires: libmailutils = %{version}-%{release}
Group: System/Libraries

%description -n libmailutils-python
The libraries for integration with Python

%package -n python-module-mailutils
Summary: A Python interface to Mailutils framework
License: %gpl3plus
Group: Networking/Mail
BuildArch: noarch
Requires: python-module-mailutils-api = %version-%release

%description -n python-module-mailutils
This package contains Python bindings for GNU Mailutils.

%package -n python-module-mailutils-api
Summary: A Python interface to Mailutils framework, arch specific part
License: %gpl3plus
Group: Networking/Mail
Requires: libmailutils = %version-%release
Conflicts: python-module-mailutils < %version-%release

%description -n python-module-mailutils-api
This package contains architecture specific part of the
python-module-mailutils.
%endif

%prep
%if %snapshot
%setup -q -n %name-%version-%snapshotdate
%else
%setup -q
%endif

#patch1 -p0

gzip ChangeLog

# some includes for info-documentation are absent in 2.9.91
pushd doc/texinfo
for file in addr http mailcap numaddr sfrom url-parse
do
 [ -f $file.inc ] || touch $file.inc
done
popd

# see http://bugzilla.altlinux.org/31449
sed "s/^@hashchar{}/#/" -i doc/texinfo/programs.texi

%build

%if ! %snapshot
%if ! %use_chrpath
# fixed RPATH issue (3.1.1 tarball created with wrong libtool)
%autoreconf
cp -f po/Makefile.in.in~ po/Makefile.in.in
%endif
%endif

%set_verify_elf_method unresolved=relaxed
#undefine __libtoolize

%add_optflags "-llber"

%configure \
    --disable-rpath \
    --enable-ipv6 \
    %if_enabled mh
    --with-mh-bindir=%_libexecdir/mu-mh \
    %else
    --disable-mh \
    %endif
    %if_enabled guile
    --with-guile-site-dir=%_datadir/guile/site \
    %else
    --without-guile \
    %endif
    %{!?_enable_python: --disable-python} \
    #

./config.status | sed -n '/[*]\+/,/[*]\+/p' > README-config.status

# SMP-incompatible build.
%make V=1

%check

#make check MH=/dev/null || { cat mh/tests/testsuite.log; exit 1; }
%make check

%install

%makeinstall_std

install -d $RPM_BUILD_ROOT/bin
ln -s ..%_bindir/mail "$RPM_BUILD_ROOT/bin/mail"
pushd $RPM_BUILD_ROOT%_bindir
    ln -s mail Mail
    ln -s mail mailx
popd

%if_enabled guile
pushd $RPM_BUILD_ROOT%_libdir
    NAME1=`ls libguile-mailutils*.so`
    NAME2=`find libmu_scm.so.* -type f`
    ln -sf $NAME2 $NAME1
popd
%endif

rm -f $RPM_BUILD_ROOT%python_sitelibdir/mailutils/c_api.a
rm -f $RPM_BUILD_ROOT%python_sitelibdir/mailutils/c_api.la

%if %use_chrpath
find $RPM_BUILD_ROOT -type f | while read f; do
    COUNT=`file $f | grep ELF | wc -l`
    if [ $[ $COUNT > 0 ] == 1 ]; then
       chrpath -d $f
    fi
done
%endif

%find_lang %name

%files -n mailutils
%_bindir/mailutils
%_bindir/dotlock
%_bindir/frm
%_bindir/from
%_bindir/mail
%_bindir/mailx
%_bindir/Mail
/bin/mail
%_bindir/popauth
%_bindir/messages
%_bindir/mimeview
%_bindir/movemail
%_bindir/readmsg
%_mandir/*/mail*

%dir %_libexecdir/mailutils
%_libexecdir/mailutils/mailutils-*

%files -n libmailutils

%dir %_libdir/mailutils
%_libdir/mailutils/moderator.so
%_libdir/mailutils/vacation.so
%_libdir/mailutils/pipe.so
%_libdir/mailutils/list.so
%_libdir/mailutils/numaddr.so
%_libdir/mailutils/spamd.so
%_libdir/mailutils/timestamp.so
%_libdir/mailutils/editheader.so

%_libdir/libmailutils.so.*
%_libdir/libmuaux.so.*

%exclude %_libdir/libmu_*.so
%_libdir/libmu_*.so.*

%if_enabled python
%exclude %_libdir/libmu_py.so.*
%endif

%files -n libmailutils-devel
%_includedir/*
%_bindir/mailutils-config
%_datadir/aclocal/mailutils.m4
#_libdir/libmu_argp.a
%_libdir/libmailutils.so
%_libdir/libmuaux.so
%_libdir/libmu_*.so

%files -n libmailutils-devel-static
%_libdir/libmailutils.*a
%_libdir/mailutils/moderator.*a
%_libdir/mailutils/vacation.*a
%_libdir/mailutils/pipe.*a
#exclude #_libdir/libmu_argp.a
%_libdir/libmu*.*a
%_libdir/mailutils/list.*a
%_libdir/mailutils/numaddr.*a
%_libdir/mailutils/spamd.*a
%_libdir/mailutils/timestamp.*a
%_libdir/mailutils/editheader.*a

%files doc
%doc AUTHORS THANKS COPYING* NEWS README* TODO ChangeLog.gz
%_infodir/*

%files pop3d
%_sbindir/pop3d
%_mandir/*/pop*

%files imap4d
%_sbindir/imap4d
%_mandir/*/imap4d*

%files comsatd
%_sbindir/comsatd

%files maidag
%_sbindir/maidag

%files sieve
%_bindir/sieve

%if_enabled guile
%files guile
%dir %_datadir/guile/site/mailutils
%dir %_datadir/guile/site/mailutils/sieve-modules
%_bindir/guimb
%_bindir/sieve2scm
%_datadir/guile/site/mailutils/*.scm
%_datadir/guile/site/mailutils/*.txt
%_datadir/guile/site/mailutils/sieve-modules/*.scm
%_libdir/libguile-mailutils*.so
%endif

%files locales -f %name.lang

%if_enabled mh
%files mh
%dir %_libexecdir/mu-mh
%dir %_datadir/mailutils
%dir %_datadir/mailutils/mh
%_libexecdir/mu-mh/*
%_datadir/mailutils/mh/*
%_datadir/emacs/site-lisp/*
%endif

%if_enabled python
%files -n libmailutils-python
%_libdir/libmu_py.so.*

%files -n python-module-mailutils
%dir %python_sitelibdir_noarch/mailutils/
%python_sitelibdir_noarch/mailutils/*.py*

%files -n python-module-mailutils-api
%dir %python_sitelibdir/mailutils/
%python_sitelibdir/mailutils/*.so
%endif

%changelog
* Tue Dec 11 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.5-alt2
- Removed emacs-git from BuildRequires (fixed FTBFS)

* Tue Nov 13 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.5-alt1
- New version
- Included info files to doc package (was excluded since 2.99.91-alt1)
- Packaged report of config.status

* Fri Aug 31 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.4.91-alt2
- disabled tcpwrappers support

* Wed Aug 15 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.4.91-alt1
- New version

* Fri Nov 10 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt1
- New version
- added perl-podlators to BuildRequires
- applied upstream patch b330af90

* Thu Mar 09 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.1.91-alt0.20170306.1
- New version

* Wed Feb 15 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt1
- New version

* Thu Apr 07 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.99.99-alt0.20151110.3
- moved libmu_argp.a from devel subpackage to devel-static

* Sat Jan 30 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.99.99-alt0.20151110.2
- Fixed FTBFS: added makeinfo to BuildRequires

* Wed Nov 11 2015 Sergey Y. Afonin <asy@altlinux.ru> 2.99.99-alt0.20151110.1
- New version
- disabled sub package with Guile ( see http://bugzilla.altlinux.org/31466 )

* Thu Sep 05 2013 Sergey Y. Afonin <asy@altlinux.ru> 2.99.98-alt0.20130822.1
- New version

* Mon May 14 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.96-alt0.20120513.1
- new snapshot

* Sat Mar 31 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.96-alt0.20120325.1
- new snapshot

* Sun Mar 18 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.96-alt0.20120317.1
- new snapshot

* Sat Mar 17 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.96-alt0.20120314.1
- New version

* Tue Feb 07 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.95-alt1.20120122.3
- disabled sub packages with Python again ( noarch check FAILED,
  http://lists.altlinux.org/pipermail/devel/2012-February/193243.html )

* Mon Feb 06 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.95-alt1.20120122.2
- added emacs-X11 to BuildRequires

* Mon Feb 06 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.95-alt1.20120122.1
- new snapshot

* Mon Feb 06 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.95-alt1.20120121.2
- regenerated BuildRequires (by gear-buildreq; thanks real@)
- added V=1 for make (thanks ldv@)
- removed version of python in pkg-config-hack.diff

* Sat Jan 21 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.99.95-alt1.20120121.1
- New version
- Enabled sub packages with python interface

* Wed Aug 24 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.99.92-alt1.20110804.1
- new snapshot
- merged libmailutils and libmailutils-sieve subpackages

* Sat Jul 16 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.99.92-alt1
- New version

* Thu Jul 07 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.99.91-alt1.20110707.1
- new snapshot

* Thu Jun 30 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.99.91-alt1
- New version (3.0 alpha, with IPv6 support)
- Excluded info files from doc package (not actual in this alpha)
- Disabled sub packages with python interface (not ready in this alpha)

* Wed Oct 20 2010 Sergey Y. Afonin <asy@altlinux.ru> 2.2-alt1
- New version

* Fri Oct 08 2010 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt1
- New version, 2.1 release.

* Sun Jan 31 2010 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt0.20091105.3
- Moved the arch specific part of python-module-mailutils to separate subpackage
  (fixed building for x86_64, thanks ldv@)
- Do not use %make_build because makefiles fail to handle parallelized builds
  (thanks ldv@)
- created symlinks (for better exchangeability with the mailx package):
  Mail -> mail
  mailx -> mail

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt0.20091105.2
- Rebuilt with python 2.6

* Thu Nov 19 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt0.20091105.1
- new snapshot
- separated libmailutils-python

* Tue Oct 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt0.20090928.3
- added missing %%dir in %%files sections

* Mon Oct 19 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt0.20090928.2
- changed flex-old to flex in BuildRequires
- added %%check section

* Tue Sep 29 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.1-alt0.20090928.1
- new snapshot

* Fri Aug 28 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090822.1
- new snapshot

* Fri Apr 17 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090417.1
- new snapshot

* Tue Mar 31 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090330.1
- new snapshot

* Sat Mar 28 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090328.1
- new snapshot
- some changes in spec according  mu-aux/mailutils.spec.in

* Wed Mar 25 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090325.1
- new snapshot (Requires: guile >= 1.8)

* Fri Mar 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090320.1
- new snapshot

* Thu Mar 12 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.0.90-alt0.20090311.1
- new snapshot (libsieve.so renamed to libmu_sieve.so)
- added "Conflicts: courier-imap" to mailutils-pop3d subpackage

* Thu Nov 13 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.9.92-alt0.20081111.2
- removed ldconfig calling due to new rpm

* Wed Nov 12 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.9.92-alt0.20081111.1
- new svn

* Sun Oct 19 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.9.92-alt0.20081019.1
- new svn
- separated mailutils-locales subpackage

* Thu Oct 16 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.9.92-alt0.20081015.1
- new svn
- separated libmailutils-sieve subpackage
- moved *.*a from mailutils-sieve to common libmailutils-devel-static

* Mon Jun 30 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.9.90-alt1.20080617
- new cvs
- fixed version of package (1.2.90 -> 1.9.90)

* Thu Apr 10 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.2.90-alt1.20080408
- new cvs

* Thu Feb 28 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.2-alt1
- new version (License changed to GPL/LGPL v3)

* Wed May 16 2007 Sergey Y. Afonin <asy@altlinux.ru> 1.1-alt1
- new version

* Wed Dec 13 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.0-alt4
- mailutils-1.0-send_mail.patch

* Fri Sep 22 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.0-alt3
- fix: add symlink /usr/bin/mail -> /bin/mail
- fix: Provides: /bin/mail

* Wed Jul 19 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.0-alt2
- fixed autogeneraded BuildRequires:
  guile16-devel guile18 -> guile16-devel guile16
- fixed: added Conflicts: mailx

* Tue Jul 18 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.0-alt1
- First build for Sisyphus
