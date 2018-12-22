# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: fonts-bitmap-terminus.spec,v 1.5 2006/05/05 08:01:35 eugene Exp $

%define cname terminus
%define fontsdir %_datadir/fonts/bitmap/terminus
%define cfontsdir /lib/kbd/consolefonts

Name: fonts-bitmap-%cname
Version: 4.46
Release: alt1
Summary: Terminus Font - a clean fixed width font
Summary(ru_RU.UTF-8): Шрифт Terminus - растровый моноширинный шрифт
License: OFL-1.0
Group: System/Fonts/X11 bitmap
URL: http://sourceforge.net/projects/terminus-font/
BuildArch: noarch

Packager: Eugene Vlasov <eugvv@altlinux.ru>

Source0: %cname-font-%version.tar.gz
Source1: %cname-FAQ
Source2: ibm-866.uni

Patch0: %cname-4.40-alt-12pt_ve_fix.patch
Patch1: %cname-4.40-alt-be2.patch
Patch2: %cname-4.46-alt-cp866.patch

Provides: terminus-font = %version-%release

Obsoletes: %cname-fonts-bitmap < %version
Provides: %cname-fonts-bitmap = %version-%release

BuildPreReq: fontconfig python3 xorg-font-utils

%description
Terminus Font is designed for long (8 and more hours per day) work with
computers. Version 4.38 contains 879 characters, covers about 120 language
sets and supports ISO8859-1/2/5/9/13/15/16, Paratype-PT154/PT254, KOI8-R/U/E/F,
Esperanto many IBM, Windows and Macintosh code pages, as well as the IBM VGA,
vt100 and xterm pseudographic characters.
The sizes present are 6x12, 8x14, 8x16, 10x20, 11x22, 12x24, 14x28 and 16x32.
The styles are normal and bold (except for 6x12), plus EGA/VGA-bold for
8x14 and 8x16.
This package contains Terminus Font for X Window System.

%description -l ru_RU.UTF-8
Шрифт Terminus разработан для длительной (8 часов и более) работы с
компьютером. Версия 4.38 содержит 879 символов, полностью охватывая
около 120 языковых наборов и поддерживая ISO8859-1/2/5/9/13/15/16,
Paratype-PT154/PT254, KOI8-R/U/E/F, Esperanto, многие кодовые страницы IBM,
Windows и Macintosh. Также включены псевдографические символы IBM VGA, vt100 и
xterm.
Представлены размеры 6x12, 8x14, 8x16, 10x20, 11x22, 12x24, 14x28 и 16x32,
обычный и жирный шрифт (для размера 6x12 - только обычный), и жирный
шрифт для EGA/VGA размером 8x14 и 8x16.
Этот пакет содержит шрифт Terminus для X Window.


%package -n fonts-console-%cname
Summary: Terminus Font - a clean font for console
Summary(ru_RU.UTF-8): Шрифт Terminus для консоли
Group: System/Fonts/Console

Obsoletes: %cname-fonts-console <= 4.14-alt1
Provides: %cname-fonts-console = %version-%release

%description -n fonts-console-%cname
Terminus Font is designed for long (8 and more hours per day) work with
computers. Version 4.38 contains 879 characters, covers about 120 language
sets and supports ISO8859-1/2/5/9/13/15/16, Paratype-PT154/PT254, KOI8-R/U/E/F,
Esperanto many IBM, Windows and Macintosh code pages, as well as the IBM VGA,
vt100 and xterm pseudographic characters.
The sizes present are 6x12, 8x14, 8x16, 10x20, 11x22, 12x24, 14x28 and 16x32.
The styles are normal and bold (except for 6x12), plus EGA/VGA-bold for
8x14 and 8x16.
This package contains Terminus Font for Linux console.

%description -l ru_RU.UTF-8 -n fonts-console-%cname
Шрифт Terminus разработан для длительной (8 часов и более) работы с
компьютером. Версия 4.38 содержит 879 символов, полностью охватывая
около 120 языковых наборов и поддерживая ISO8859-1/2/5/9/13/15/16,
Paratype-PT154/PT254, KOI8-R/U/E/F, Esperanto, многие кодовые страницы IBM,
Windows и Macintosh. Также включены псевдографические символы IBM VGA, vt100 и
xterm.
Представлены размеры 6x12, 8x14, 8x16, 10x20, 11x22, 12x24, 14x28 и 16x32,
обычный и жирный шрифт (для размера 6x12 - только обычный), и жирный
шрифт для EGA/VGA размером 8x14 и 8x16.
Этот пакет содержит шрифт Terminus для консоли Linux.

%prep
%setup -n %cname-font-%version
#%%patch0 -p2
%patch1 -p2
%patch2 -p2
cp %SOURCE2 uni/
touch dup/ibm-866.dup

%build
patch < alt/dv1.diff
patch < alt/gq2.diff
patch < alt/ll2.diff
patch < alt/td1.diff
patch < alt/ij1.diff
chmod +x configure
./configure --prefix=%_prefix \
    --psfdir=%cfontsdir \
    --x11dir=%fontsdir
export GZIP=--best
%make_build

%install
cp %SOURCE1 FAQ
%makeinstall_std fontdir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%fontsdir %buildroot%_sysconfdir/X11/fontpath.d/bitmap-terminus:unscaled:pri=20

%triggerun -- %name < 4.20-alt2.1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
    %_sbindir/chkfontpath -q -r %fontsdir ||:
fi

%files
%doc CHANGES README FAQ OFL.TXT
%_sysconfdir/X11/fontpath.d/*
%fontsdir

%files -n fonts-console-%cname
%doc CHANGES README FAQ OFL.TXT
%cfontsdir/*.psf.gz

%changelog
* Wed Nov 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.46-alt1
- 4.46
- rediffed cp866 patch
- added new BR: python3

* Tue Apr 18 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.40-alt2
- applied missing ij1 patch.

* Sat Apr 9 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.40-alt1
- 4.40
- Build with next character patches:
  + dv1: Cyrillic "d" character looks differ than Latin "g"
  + gq2: single quote looks like reverse backquote
  + ij1: Cyrillic "i" looks differ than Latin "u"
  + ll2: Latin "l" looks differ than "1"
  + td1: center tilde character
- "ge" character variant resetted to default
- Remove patch for "ve" character due alternative "ve" character

* Tue Mar 25 2014 Fr. Br. George <george@altlinux.ru> 4.38-alt3
- Add cp866 encoding

* Thu Nov 01 2012 Ivan Ovcherenko <asdus@altlinux.org> 4.38-alt2
- Update specfile
- Some enhancement in the "ve" character
- Changes in the next character variants:
  + "dv" and "ij" character variants resetted to default
  + "ge" character variant applied
  + custom "be" character variant applied

* Fri Oct 26 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.38-alt1
- 4.38

* Sun Dec 13 2009 Eugene Vlasov <eugvv@altlinux.ru> 4.30-alt1
- New version, upstream changes:
  * size 22 (not very good), another 25 characters, various small fixes and
    improvements; changed the default prefix and x11dir
- Updated description and FAQ

* Sun Oct 26 2008 Eugene Vlasov <eugvv@altlinux.ru> 4.28-alt1
- New version, upstream changes:
  * heavy frames (written mostly by Tim Allen) and a few more letters, altered
    trianges and arrows, small bugfixes
  * reorganized the 512-character console font to include many more letters
    instead of the IBM-437 specific pseudographics
- Updated description and FAQ
- fonts-console-terminus subpackage comeback, console font dir changed to
  /lib/kbd/consolefonts (#11809)

* Sun Jun 01 2008 Eugene Vlasov <eugvv@altlinux.ru> 4.26-alt1
- Merged kas@ changes:
  * 4.26
  * Tag Packager added
- Updated FAQ
- Updated description

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 4.20-alt2.1
- NMU:
  + used %_sysconfdir/X11/fontpath.d, adieu chkfontpath

* Thu Jun 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 4.20-alt2
- fonts-console-terminus build now from separate source package, location
  of console fonts is arch-dependent (#11809)
- Removed %%__ macro

* Fri May 05 2006 Eugene Vlasov <eugvv@altlinux.ru> 4.20-alt1
- New version, lots of small fixes, improvements and changes
- Cyrillic "ka" fixed in upstream

* Fri Jan 06 2006 Eugene Vlasov <eugvv@altlinux.ru> 4.16-alt2
- Requires fontconfig >= 2.3.2-alt6
- Applied fix for cyrillic "ka", "be" and "ve" characters (#8904)

* Sat Dec 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 4.16-alt1
- New version
- Added 87 and fixed a dozen of characters
- Added information for the known bugs
- Renamed package for new font policy compatibility
- Moved files to /usr/share/fonts/bitmap

* Wed Jun 01 2005 Eugene Vlasov <eugvv@altlinux.ru> 4.14-alt1
- New version
- Fixed several characters; small fixes
- Added FAQ from author personal page

* Thu Mar 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 4.12-alt1
- New version
- Added several characters and fixed a few existing ones

* Tue Oct 19 2004 Eugene Vlasov <eugvv@altlinux.ru> 4.11-alt2
- Fixed BuildRequires

* Sat Oct 16 2004 Eugene Vlasov <eugvv@altlinux.ru> 4.11-alt1
- New version
- Added size 6x12 and codepage KOI8-U
- Improved 14x24 bold (about 60 characters) and Euro

* Sun Aug 08 2004 Eugene Vlasov <eugvv@altlinux.ru> 4.09-alt1
- First build for Sisyphus

