Name: unrtf
Version: 0.21.9
Release: alt1

Summary: UnRTF is a moderately complicated converter from RTF to other formats
License: GPLv3
Group: Text tools
Url: http://www.gnu.org/software/unrtf/unrtf.html

Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires:	automake

Source0: %name-%version.tar.gz

%description
The program unrtf is a converter from Rich Text Format (RTF) to a
growing number of document formats. At present it supports
Hypertext Markup Language (HTML), plain text, text with VT100 codes,
LaTeX, and PostScript. All output formats except HTML are "alpha" i.e.
limited and development has just begun. However with HTML, the program
supports tables, fonts, embedded images, hyperlinks, and paragraph alignment.
Font support includes face and size changes, as well as typical attributes
such as italic, bold, underlining, strikethrough, smallcaps, allcaps, expand,
compress and both foreground and background colors. Images are always stored
to separate files in the current directory, or they can be ignored.

%prep
%setup -q
# ALT bug#27309
sed -i 's,/usr/local/lib/unrtf/,%_libdir/unrtf/,g' src/path.h

%build
# The ./configure command (specifically the symlinks in the ./config/
# directory) assume that automake is present in an "automake-1.13" directory.
# That is the case on EL7, but it's not the case in Fedora. That is why we
# regenerate the automake/autoconf bits by running the ./bootstrap script here.
./bootstrap
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README tests
%_bindir/*
#_libdir/%name/*
%_man1dir/*
%_datadir/%name/*

%changelog
* Wed Jan 21 2015 Ilya Mashkin <oddity@altlinux.ru> 0.21.9-alt1
- 0.21.9

* Tue Dec 16 2014 Ilya Mashkin <oddity@altlinux.ru> 0.21.7-alt1
- 0.21.7

* Sat Sep 14 2013 Ilya Mashkin <oddity@altlinux.ru> 0.21.5-alt1
- 0.21.5

* Wed Nov 07 2012 Igor Zubkov <icesik@altlinux.org> 0.21.2-alt1
- 0.21.1 -> 0.21.2
- debuginfo
- fix search path (closes: #27309)

* Wed Dec 01 2010 Ilya Mashkin <oddity@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Tue Oct 23 2007 Slava Semushin <php-coder@altlinux.ru> 0.20.2-alt1.1
- NMU
- Updated Url tag (#13169)

* Tue Jul 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.2-alt1
- 0.20.2

* Thu Mar 23 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Thu Mar 09 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Tue Jan 10 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.19.9-alt1
- new version

* Thu Sep 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.19.7-alt1
- 0.19.7

* Fri Feb 20 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.19.3-alt1
- 0.19.3
- fix bug #225592: null pointer param in convert.c

* Wed Dec 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.19.0-alt1
- 0.19.0
- minor fixes to prevent segmentation violations
- further special character code; minor cleanups

* Fri Dec 19 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.18.1-alt1
- First version of RPM package

