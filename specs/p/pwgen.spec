Name: pwgen
Version: 2.06
Release: alt2

Summary: Password generation utility
License: GPLv2+
Group: System/Base
Url: http://sourceforge.net/projects/pwgen/

# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar

%description
The pwgen utility generates random, meaningless but pronounceable
passwords.

%prep
%setup
sed -i 's/^AC_PROG_CC/&\nAC_SYS_LARGEFILE/' configure.in

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc ChangeLog

%changelog
* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 2.06-alt2
- Built with LFS support enabled.

* Wed Sep 29 2010 Dmitry V. Levin <ldv@altlinux.org> 2.06-alt1
- Updated to 2.06.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2.05-alt2
- Uncompressed tarball.

* Mon Jan 16 2006 Dmitry V. Levin <ldv@altlinux.org> 2.05-alt1
- Updated to 2.05.

* Thu Jun 16 2005 Dmitry V. Levin <ldv@altlinux.org> 2.04-alt1
- Updated to 2.04.

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.03-alt1
- Updated to 2.03.

* Tue Oct 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.01-alt2
- rebuild with gcc3

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.01-alt1
- Initial revision.
