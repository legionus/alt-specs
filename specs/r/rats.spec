Name: rats
Version: 2.3
Release: alt2

Summary: Rough Auditing Tool for Security
License: GPLv2+
Group: Development/Other
Url: http://code.google.com/p/rough-auditing-tool-for-security/
# http://rough-auditing-tool-for-security.googlecode.com/files/%name-%version.tar.gz
Source: %name-%version.tar
Patch: rats-2.3-alt-flex.patch

# Automatically added by buildreq on Tue Sep 14 2010
BuildRequires: flex libexpat-devel

%description
RATS scans through code, finding potentially dangerous function calls.
The goal of this tool is not to definitively find bugs (yet).  The
current goal is to provide a reasonable starting point for performing
manual security audits.

The initial vulnerability database is taken directly from things that
could be easily found when starting with the forthcoming book,
"Building Secure Software" by Viega and McGraw.

%prep
%setup
rm lex.yy*
%patch -p1

%build
%configure --datadir=%_datadir/%name
%make_build lex
%make_build

%install
%makeinstall \
	BINDIR="%buildroot%_bindir" \
	SHAREDIR="%buildroot%_datadir/%name" \
	MANDIR="%buildroot%_mandir"

%files
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3-alt2
- Fixed build with flex >= 2.5.36.

* Tue Sep 14 2010 Victor Forsiuk <force@altlinux.org> 2.3-alt1
- New version, new URL.

* Sun Oct 23 2005 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt2
- Applied patch from Debian to fix build with new flex.

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt1
- Updated to 2.1

* Wed Apr 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.4-alt1
- 1.4

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2-alt1
- 1.2

* Thu Aug 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1-alt1
- 1.1

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9-alt1
- Initial revision.
