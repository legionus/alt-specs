%define _name   dgen

Name: dgen-sdl
Version: 1.33
Release: alt1

Packager: Ilya Mashkin <oddity@altlinux.ru>

Summary: Sega Genesis/MegaDrive emulator
Summary(ru_RU.KOI8-R): �������� Sega Genesis/Megadrive

License: DGEN
URL: http://dgen.sourceforge.net
Group: Emulators

Source0: dgen-sdl-%version.tar.gz
Patch0: dgen-sdl-1.23-lostbreak.patch
Patch1: dgen-sdl-1.23-m68kmake.c.patch

# Automatically added by buildreq on Fri Jan 21 2005
BuildRequires: esound gcc-c++ libSDL-devel libstdc++-devel nasm

%description
This is DGen/SDL, a semi-fantastic emulator for Unix-esque operating systems
supported by the Simple DirectMedia Layer (SDL) library. It produces a virtual
environment in which Sega Genesis (MegaDrive outside the US) games may run
with fairly accurate audio and video.

%description -l ru_RU.KOI8-R
Dgen/SDL - ��������, ����������� ����� � ������� ����� ��������� ���� ���
Sega MegaDrive � ������ ���������������� ����� � �����. 

%prep
%setup -q
#patch0 -p1
#patch1 -p1

%build

%configure --with-x
%make_build

%install

%make_install
install -D -pm 755 dgen %buildroot%_bindir/dgen
install -D -pm 755 dgen_tobin %buildroot%_bindir/dgen_tobin
install -D -pm 644 dgen.1 %buildroot%_man1dir/dgen.1
install -D -pm 644 dgenrc.5 %buildroot%_man5dir/dgenrc.5
install -D -pm 644 dgen_tobin.1 %buildroot%_man1dir/dgen_tobin.1
%__mkdir_p %buildroot%_docdir/%name-%version


%files
%doc AUTHORS COPYING ChangeLog README sample.dgenrc
%_bindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Mon Jul 28 2014 Ilya Mashkin <oddity@altlinux.ru> 1.33-alt1
- New version 1.33

* Sat Feb 16 2013 Ilya Mashkin <oddity@altlinux.ru> 1.32-alt1
- New version 1.32

* Tue Dec 04 2012 Ilya Mashkin <oddity@altlinux.ru> 1.31-alt1
- New version 1.31

* Tue May 08 2012 Ilya Mashkin <oddity@altlinux.ru> 1.30-alt0.M60T.1
- build for t6

* Sun Apr 29 2012 Ilya Mashkin <oddity@altlinux.ru> 1.30-alt1
- New version 1.30
- New url

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 1.23-alt9
- fix build

* Fri Sep 15 2006 Ilya Mashkin <oddity at altlinux.ru> 1.23-alt8
- fix build m68k code

* Fri Jan 21 2005 Ilya Mashkin <oddity at altlinux dot ru> 1.23-alt7
- correct build with g++-3.4.x
- update deps, add URL

* Sat Sep 12 2004 Ilya Mashkin <oddity at altlinux dot ru> 1.23-alt6
- Add sample.dgenrc file (see in /usr/share/doc/dgen-sdl-1.23)

* Sun Mar 27 2004 Ilya Mashkin <oddity@altlinux.ru> 1.23-alt5
- Add dgenrc.5 man page (#3894)
- Add tobin utility

* Sun Sep 14 2003 Ilya Mashkin <oddity@altlinux.ru> 1.23-alt4
- Change spec for current Sisyphus

* Sun Sep 14 2003 Ilya Mashkin <oddity@altlinux.ru> 1.23-alt3
- Delete menus

* Sun Aug 17 2003 Ilya Mashkin <oddity@altlinux.ru> 1.23-alt2
- Initial build.

