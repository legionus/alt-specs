Name: wmlife
Version: 1.0.1
Release: alt2

Summary: WindowMaker dock-app running Conway's Game of Life
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.swanson.ukfsn.org
Source0: %url/%name/%name-%version.tar.gz
Source1: %name-icons.tar.gz
Source2: %name.desktop
Patch0: wmlife-1.0.0-stringh.patch
Patch1: wmlife-1.0.0-alt-configure.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Dec 10 2006 (-bi)
BuildRequires: imake libSM-devel libXext-devel libgtk+2-devel xorg-cf-files

%description
Wmlife is a dock app running Conway's Game of Life (and program
launcher). Life is played on a grid of square cells where a cell can
be either live or dead. In the rules, you count the number of live
neighbours for each cell to determine whether a cell lives or dies;

Birth: dead cell with exactly three live neighbours becomes a live cell.
Survival: a live cell with two or three live neighbours stays alive.
Overcrowding / Loneliness: in all other cases, a cell dies or remains
dead.

Normally Life is implemented on an infinite board but due to size
restraints wmlife implements the grid as a torus. In a torus,
the grid wraps at the edges from top to bottom and left to right.

%prep
%setup -a1
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="$CFLAGS %optflags -std=gnu89"
%autoreconf
%configure --enable-session
%make_build

%install
%makeinstall
install -pDm644 16x16.png %buildroot%_miconsdir/%name.png
install -pDm644 32x32.png %buildroot%_niconsdir/%name.png
install -pDm644 48x48.png %buildroot%_liconsdir/%name.png
install -pDm644 %SOURCE2  %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS README ChangeLog NEWS
%_man1dir/*
%_bindir/*
%_desktopdir/*
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png

%changelog
* Tue Oct 20 2015 Michael Shigorin <mike@altlinux.org> 1.0.1-alt2
- gcc5 FTBFS workaround (-std=gnu89)

* Mon Apr 28 2014 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1.1
- fix FTBFS (-lm)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- built for ALT Linux (spec based on wmfire)
- applied gentoo patch
