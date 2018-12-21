Name: hexedit
Version: 1.2.13
Release: alt1

Summary: A hexadecimal file viewer and editor
License: GPLv2+
Group: Editors
URL: http://rigaux.org/hexedit.html

# http://rigaux.org/%name-%version.src.tgz
Source: %name-%version.tar
Patch1: hexedit-rh-config.patch
Patch2: hexedit-rh-man-color.patch

BuildRequires: libncurses-devel

%description
hexedit shows a file both in ASCII and in hexadecimal.  The file can be
a device as the file is read a piece at a time.  You can modify the file
and search through it.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc *.lsm Changes TODO
%_bindir/*
%_man1dir/*

%changelog
* Wed Apr 17 2013 Dmitry V. Levin <ldv@altlinux.org> 1.2.13-alt1
- Updated to 1.2.13.

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.12-alt1.0
- Automated rebuild.

* Thu Sep 29 2005 Victor Forsyuk <force@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Tue Apr 12 2005 Victor Forsyuk <force@altlinux.ru> 1.2.10-alt1
- Update buildreqs.

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.2.9-alt1
- 1.2.9

* Tue Jan 27 2004 Stanislav Ievlev <inger@altlinux.org> 1.2.8-alt1
- 1.2.8

* Mon Dec 29 2003 Stanislav Ievlev <inger@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Mar 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.3-alt2
- Rebuild with gcc3

* Fri Aug 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.2.1-alt1
- new version

* Wed Apr 10 2001 Rider <rider@altlinux.ru> 1.2-alt1
- new version

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.2-ipl2mdk
- Automatically added BuildRequires.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.2-ipl1mdk
- RE adaptions.
- Russian translation for Description and Summary tags.

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.1.2-1mdk
- new version
- cleanup
- BM, macroization

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 1.1.1-4mdk
- new group

* Mon Nov 22 1999 Pixel <pixel@linux-mandrake.com>
- build release

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 source

