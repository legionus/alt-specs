Name: bmake
Version: 20171207
Release: alt1

Summary: The NetBSD make(1) tool
License: BSD with advertising
Group: Development/Tools

Url: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/
Source: %name-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Requires: pkgsrc-mk-files

%description
bmake, the NetBSD make(1) tool, is a program designed to simplify
the maintenance of other programs.  The input of bmake is a list
of specifications indicating the files upon which the targets
(programs and other files) depend.  bmake then detects which
targets are out of date based on their dependencies and triggers
the necessary commands to bring them up to date when that
happens.

bmake is similar to GNU make, even though the syntax for the
advanced features supported in Makefiles is very different.

%prep
%setup -n %name

%build
unset MAKEFLAGS
./boot-strap -q -o Linux \
	--prefix=%prefix \
	--with-default-sys-path=%_datadir/mk \
	--mksrc none \
	--sysconfdir=%_sysconfdir

%install
mkdir -p %buildroot%_datadir/mk
install -pDm644 bmake.1 %buildroot%_man1dir/bmake.1
install -pDm755 Linux/bmake %buildroot%_bindir/bmake

%files
%doc ChangeLog README
%_bindir/bmake
%_man1dir/*
%dir %_datadir/mk/

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 20171207-alt1
- Autobuild version bump to 20171207

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 20170812-alt1
- Autobuild version bump to 20170812

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 20170510-alt1
- Autobuild version bump to 20170510

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 20170301-alt1
- Autobuild version bump to 20170301

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 20160926-alt1
- Autobuild version bump to 20160926

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 20160606-alt1
- Autobuild version bump to 20160606

* Mon Apr 11 2016 Fr. Br. George <george@altlinux.ru> 20160315-alt1
- Autobuild version bump to 20160315

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 20151201-alt1
- Autobuild version bump to 20151201

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 20151022-alt1
- Autobuild version bump to 20151022

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 20150606-alt1
- Autobuild version bump to 20150606

* Mon Jun 01 2015 Fr. Br. George <george@altlinux.ru> 20150505-alt1
- Autobuild version bump to 20150505

* Sun Jan 08 2012 Michael Shigorin <mike@altlinux.org> 20111010-alt1
- built for Sisyphus
- minor spec cleanup

* Mon Jan 02 2012 Aleksey Cheusov <cheusov@NetBSD.org> 20111010-alt1
- update to 20111010

* Tue Dec 08 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt4
- add pkgsrc-mk-files require

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt3
- create dir for bmake macros

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 20081111-alt2
- Now bmake doesn't depend on mk-files

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080515-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 2 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20080515-1
- Initial release for Fedora.
