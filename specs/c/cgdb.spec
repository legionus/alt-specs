Name: cgdb
Summary: Frontend for GDB
Version: 0.6.8
Release: alt1
Url: http://cgdb.github.io/
License: GPL-2.0-only
Group: Development/Debuggers

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %name-%version.tar.bz2

Requires: gdb

# Automatically added by buildreq on Fri Sep 26 2008
BuildRequires: flex libncurses-devel libreadline-devel
BuildRequires: texinfo help2man

%description
CGDB is a curses (terminal-based) interface to the GNU Debugger (GDB).
Its goal is to be lightweight and responsive; not encumbered with
unnecessary features.

%prep
%setup -q

%build
%configure
printf '#define HAVE_DEV_PTMX 1\n' >> config.h

%make_build

%install
%makeinstall_std

%files
%doc README NEWS
%_bindir/*
%_datadir/%name
%_infodir/*
%_man1dir/*

%changelog
* Thu Dec 10 2015 Alexey Gladkov <legion@altlinux.ru> 0.6.8-alt1
- New version (0.6.8).

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.4-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Dec 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt3
- Remove obsolete macros.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt2
- Fix requires.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux Sisyphus
