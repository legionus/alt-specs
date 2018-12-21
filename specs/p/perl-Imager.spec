# SPEC file for Perl module Imager

Name: perl-Imager
Version: 1.006
Release: alt1.1

Summary: Perl module for generating 24 bit Images
Summary(ru_RU.UTF-8): Модуль Perl для создания 24-x битных изображений

License: %perl_license
Group: Development/Perl
URL: http://imager.perl.org/

Source: Imager-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Sep 10 2017
# optimized out: perl perl-Class-Inspector perl-Class-Tiny perl-Devel-Symdump perl-Encode perl-File-ShareDir perl-Lingua-EN-Inflect perl-Path-Tiny perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Text-Balanced perl-devel perl-parent perl-threads pkg-config python-base python-modules python3 python3-base ruby ruby-stdlibs t1lib
BuildRequires: git-core libfreetype-devel libgif-devel libjpeg-devel libpng-devel libtiff-devel perl-Affix-Infix2Postfix perl-Image-Math-Constrain perl-Parse-RecDescent perl-PerlIO-utf8_strict perl-Pod-Spell perl-Test-Pod-Coverage t1lib-devel xorg-rgb

%description
Imager is a module for creating and altering images. It can
read and write various image formats, draw primitive shapes
like lines,and polygons,  blend multiple images together in
various ways, scale, crop, render text and more.

%description -l ru_RU.UTF-8
Imager - модуль  Perl для  создания  и работы с  графическими
изображениями.  Он может  читать и записывать  изображения  в
различных форматах,  рисовать  линии и  полигоны,  объединять
несколько изображений вместе различными способами, обрезать и
масштабировать их, отрисовывать текст и т.д.

%prep
%setup  -n Imager-%version

%build
IM_SUPPRESS_PROM=1 %perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README samples*
%perl_vendor_archlib/Imager*
%perl_vendor_autolib/Imager
%exclude /.perl.req

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1.1
- rebuild with new perl 5.26.1

* Sun Sep 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.006-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1.1
- rebuild with new perl 5.24.1

* Sat May 28 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.005-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1.1
- rebuild with new perl 5.22.0

* Sun Nov 15 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.004-alt1
- New version

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.003-alt1
- New version 1.003

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1.1
- rebuild with new perl 5.20.1

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- New version 1.000

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.98-alt1
- New version 0.98

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.97-alt2
- built for perl 5.18

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.97-alt1
- New version 0.97

* Wed Jun 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.96-alt1
- New version 0.96

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.95-alt1
- New version 0.95

* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.94-alt1
- New version 0.94

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.93-alt1
- New version 0.93

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.86-alt2
- rebuilt for perl-5.16

* Fri Nov 04 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.86-alt1
- New version 0.86

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.85-alt1
- 0.84 -> 0.85
- built for perl-5.14

* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.84-alt1
- New version 0.84

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.78-alt1
- New version 0.78

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1.1
- rebuilt with perl 5.12

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.72-alt1
- New version 0.72

* Sun Oct 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.70-alt1
- New version 0.70

* Wed Apr 30 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.64-alt1
- New version 0.64
  -- fix buffer overflow in image fills (CVE-2008-1928)
  -- multiple improvements in image converting code
  -- several other bug fixes and improvements, see Changes for details

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.62-alt1
- New version 0.62
  -- added SGI/RGB file format support
  -- major TIFF support re-work
  -- several bug fixes, see Changes for details

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.59-alt1
- New version 0.59
  -- fixes a regression introduced by the fixes for RT #11972
  -- cropping outside the image would return an Imager object with 
     no low-level image object, instead of returning false

* Thu May 17 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.58-alt1
- New version 0.58
  -- added to_rgb16 to produce a 16-bit/sample version of an image
  -- improve freetype 1.x text output efficiency
  -- several bug fixes, see Changes for details

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.57-alt1
- New version 0.57
  -- CRITICAL: a specially crafted compressed BMP file can cause a buffer
     overflow in malloced memory. For details and further discussion see 
     http://rt.cpan.org/Ticket/Display.html?id=26811

* Thu Apr 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.56-alt1
- New version 0.56
  -- added support for reading/writing 16-bit/sample PGM/PPM images
  -- added a new make_colors value - "mono"
  -- switched from the svn log Changes to a manual Changes to reduce noise
  -- Fix memory leak, http://rt.cpan.org/Ticket/Display.html?id=24992
  -- other improvements and bug fixes, see Changes for details

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt1
- New version 0.55
-- several bugs fixed

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.54-alt1
- New version 0.54
-- a new qtype value 'mixing' has been added to the scale() method
-- the rubthrough() method can now render onto images with an alpha channel
-- the GIF loop extension can now be written
-- for full list of improvements see doc/Changes

* Thu Jul 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.53-alt1
- New version 0.53
-- fix a crash bug introduced in 0.52

* Thu Jul 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.52-alt1
- New version 0.52
-- several bugs fixed in bounding_box function for T1 driver
-- fixes for CMYK images reading problems
-- documentation fixes and impovements
-- for full list of improvements see doc/Changes

* Mon Jul 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt1.02
- New test version 0.51_02
-- Window Icon/Cursor (ICO/CUR) file support
-- file handler plugins
-- flood_fill to a border color in addition to flood_fill of a region
   the same color as the seed pixel
-- setcolors() and addcolors() now accept color names and not just color objects
-- improving documentation
-- bugfixes
-- New Changes file format

* Tue Apr 25 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt1
- New version 0.51
-- fix a validation bug when processing JPEG EXIF data that can cause a crash
-- fix a mis-processing of the src_maxx and src_maxy parameters of the paste() method 
-- fix a problem in Imager's "smart" handling of the color parameter to various methods

* Tue Apr 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.50-alt1
- New version 0.50
-- Numerouse improvements and bugfixes, see doc/Changes for details

* Sat Jan 07 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.47-alt1
- New version 0.47:
-- Numerouse improvements and bugfixes, see doc/Changes for details
-- reading a gif file will now read the first image from the 
   file rather than the a consolidated image

* Mon Jul 18 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.45-alt2
- Removing freetype support as obsolete in ALT Linux. Now TTF fonts
  are handled by freetype2 library.

* Sun Jun 12 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.45-alt1
- New version 0.45

* Thu Mar 03 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.44-alt1
- Initial build for ALT Linux

