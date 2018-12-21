Name: tintin++
Version: 2.01.4
Release: alt1
Summary: Console MUD client
License: GPLv2
Group: Games/Other
Url: http://tintin.sourceforge.net/
Packager: %packager

Source: %name-%version.tar

Patch0: alt-tintin++-pcre.patch
Patch1: alt-tintin++-noadv.patch

# Automatically added by buildreq on Tue Jun 07 2011
BuildRequires: libpcre-devel zlib-devel

%description
TinTin++, aka tt++, is a free MUD client for Mac OS X, Linux,
and Windows. The Windows port named WinTin++ (using the PuTTY
derived mintty terminal) is available for those who do not
use Cygwin (A Linux/Unix emulator for Windows) and runs on Windows Xp,
Windows Vista, and Windows 7. Besides MUDs, TinTin++ also works well
with MUSH, Rogue, BBS, and Linux servers.

%description -l ru_RU.UTF-8
TinTin++ или tt++ - это свободный клиент для игр MUD
(многопользовательских подземелий, к примеру Discworld MUD).
Интерфейс классического TinTin++ консольный, поддерживаются
различные пользовательские скрипты.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
cd src
%configure
%make

%install
%define docdir %_docdir/%name-%version

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%docdir

install -pm755 src/tt++ %buildroot/%_bindir/

install -pm644 docs/* %buildroot%docdir/
install -pm644 COPYING %buildroot%docdir/
install -pm644 CREDITS %buildroot%docdir/
install -pm644 FAQ %buildroot%docdir/
install -pm644 README %buildroot%docdir/
install -pm644 SCRIPTS %buildroot%docdir/
install -pm644 TODO %buildroot%docdir/

%files
%_bindir/tt++
%dir %docdir
%docdir/*

%changelog
* Fri Mar 30 2018 Andrey Bergman <vkni@altlinux.org> 2.01.4-alt1
- Update to a new version.

* Fri Oct 13 2017 Andrey Bergman <vkni@altlinux.org> 2.01.3-alt1
- Update to a new version.

* Sat Jan 21 2017 Andrey Bergman <vkni@altlinux.org> 2.01.2-alt1
- Update to a new version.

* Sun Feb 01 2015 Andrey Bergman <vkni@altlinux.org> 2.01.1-alt1
- Update to a new version.

* Tue Jan 28 2014 Andrey Bergman <vkni@altlinux.org> 2.01.0-alt1
- Update to a new version.

* Fri Jan 18 2013 Andrey Bergman <vkni@altlinux.org> 2.00.9-alt1
- Update to a new version.

* Mon Sep 10 2012 Andrey Bergman <vkni@altlinux.org> 2.00.8-alt2
- Corrected spec error (removed unnecessary directories from doc)

* Sat Feb 25 2012 Andrey Bergman <vkni@altlinux.org> 2.00.8-alt1
- Update to a new version.

* Thu Aug 04 2011 Andrey Bergman <vkni@altlinux.org> 2.00.7-alt1
- Update to a new version.

* Tue Jun 07 2011 Andrey Bergman <vkni@altlinux.org> 2.00.6-alt2
- Removed advertisement.

* Tue Jun 07 2011 Andrey Bergman <vkni@altlinux.org> 2.00.6-alt1
- initial build for ALT Linux Sisyphus

