Name: bridge-utils
Version: 1.5
Release: alt3

Summary: Utilities for configuring the linux ethernet bridge
License: GPLv2+
Group: System/Base

URL: http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge
# git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/bridge-utils
# git://git.altlinux.org/gears/b/bridge-utils.git
Source: %name-%version-%release.tar

Obsoletes: bridgex

# /usr may be network-mounted, hence /usr/sbin/ is a bad place for brctl
%define _sbindir /sbin

%description
This package contains utilities for configuring the linux ethernet
bridge.  The linux ethernet bridge can be used for connecting multiple
ethernet devices together.  The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%prep
%setup -n %name-%version-%release

%build
autoconf
%configure --with-linux-headers=%_includedir/linux-default/include
%make_build CFLAGS='%optflags'

%install
%makeinstall_std

%files
%_sbindir/*
%_man8dir/*
%doc AUTHORS ChangeLog README THANKS TODO doc/[A-LN-Z]* tests

%post
%post_service bridge

%preun
%preun_service bridge

%changelog
* Sun Aug 17 2014 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt3
- remove initscript (ALT#25236)

* Thu Apr 11 2013 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt2
- Updated to v1.5-11-g97d6888.

* Mon Apr 25 2011 Victor Forsiuk <force@altlinux.org> 1.5-alt1
- 1.5 (supports hairpin mode).

* Fri Oct 17 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt2
- Fix segfault on bridge named "bridge" (ALT#16511). Patch from Debian
  (bug #431860).

* Sat Mar 29 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- 1.4

* Fri Jan 12 2007 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Finally place brctl in /sbin.

* Thu Sep 21 2006 Victor Forsyuk <force@altlinux.ru> 1.2-alt1
- 1.2
- This version gets rid of libsysfs.
- Add sysconfig file and initscript to start bridging as pseudo-service.

* Tue Apr 11 2006 Victor Forsyuk <force@altlinux.ru> 1.1-alt1
- 1.1

* Tue Dec 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.6-alt1.1
- Rebuild with libsysfs.so.2.0.0 .

* Thu Jul 28 2005 Victor Forsyuk <force@altlinux.ru> 1.0.6-alt1
- Add URL.
- Executable moved from /sbin to /usr/sbin.
- Buldreq'ed :)
- Patches from Fedora.
- Add tests/ to %%doc files.

* Sun Oct 13 2002 Rider <rider@altlinux.ru> 0.9.5-alt2
- Russian summary fix

* Fri Oct 11 2002 Rider <rider@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue Feb 06 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.2-ipl2
- Obsoletes: bridgex.

* Sat Feb 03 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.2-ipl1
- Initial revision.
