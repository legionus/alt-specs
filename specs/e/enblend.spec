Name: enblend
Version: 4.2
Release: alt3

Summary: A tool for combine images (make a panoramas) using a multiresolution spline
License: GPLv2+
Group: Graphics
URL: http://enblend.sourceforge.net/
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %name-%version.tar.gz
Source1: %name.readme

Provides: enfuse

BuildRequires: boost-devel gcc-c++ libstdc++-devel boost-filesystem-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libglew-devel liblcms2-devel libvigra-devel
BuildRequires: libxmi-devel libXmu-devel libXi-devel
BuildRequires: libGLU-devel libGLUT-devel openexr-devel
BuildRequires: gnuplot texinfo fonts-ttf-freefont ghostscript perl transfig tidy help2man
BuildRequires: libgsl-devel
# since 4.2
BuildRequires: perl-TimeDate perl-Readonly
BuildRequires: librsvg-utils /usr/bin/convert graphviz hevea

%description
enblend overlays multiple TIFF images using the Burt & Adelson
multiresolution spline. This technique tries to make the seams between
the input images invisible and very suitable to make panoramas.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%_bindir/*
%_man1dir/*


%changelog
* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt3
- rebuilt against libgsl.so.23/boost-1.65

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt2
- rebuilt with gcc6/boost-1.63
- fixed buildreqs

* Mon Apr 18 2016 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 4.1.4-alt1
- 4.1.4

* Sun Jul 12 2015 Yuri N. Sedunov <aris@altlinux.org> 4.1.3-alt1
- 4.1.3

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 4.1.2-alt1.1
- rebuild with boost 1.57.0

* Wed Jan 29 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.2-alt1
- New version
- compat patches removed

* Wed Feb 13 2013 Sergei Epiphanov <serpiph@altlinux.ru> 4.0-alt4
- Rebuild with new libboost version

* Tue Dec 04 2012 Sergei Epiphanov <serpiph@altlinux.ru> 4.0-alt3
- Rebuild with new libboost version

* Sat Sep 22 2012 Sergei Epiphanov <serpiph@altlinux.ru> 4.0-alt2
- Fix build with png15 and boost1.51.0.

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0-alt1.1
- build fixed

* Wed Nov 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 4.0-alt1
- New version

* Tue Jun 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt3.1
- rebuild with libpng.git=1.2.37-alt2

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt3
- build fixed: added INFO-DIR-SECTION into .info 

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 3.2-alt2
- Fix due to repocop warning

* Sat Nov 01 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt1
- New version 

* Fri Jul 25 2008 Sergei Epiphanov <serpiph@altlinux.ru> 3.0-alt2
- Add Packager tag

* Sun Feb 11 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.0-alt1
- New version

* Fri Dec 16 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.5-alt1
- New version needed for hugin-0.5. Changes and bugfixes from 2.3:
  + Fixed a bug where Enblend would crash when the -w parameter was used.
  + Fixed a bug where Enblend would sometimes say "mask transition line bounding box undefined."
  + Added support for cropped and shifted TIFF files, such as those produced by Nona.
  + Enblend will now create output files with embedded ICC profiles, if a profile is found in one of the input images.
  + Improved the speed of the mask generation algorithm.
  + See the complete release notes at Sourceforge.

* Fri Jun 17 2005 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3-alt1
- The maximum number of levels you can specify with the -l parameter has been reduced from 30 to 29. While both of these are impractically large, at least 29 does not lead to arithmetic overflow and a subsequent crash.
- TIFF library warning messages have been turned off
-  Fixed a bug that caused primary-color spots to appear in overexposed areas of 16-bpp images.
- Fixed a problem with Enblend crashing on large panoramas.
- Support for signed and unsigned 16-bit, 32-bit, single- and double-precision floating point pixel types.
- No more banding artifacts in the sky, even with 8-bit images.
- Sophisticated memory/disk balancing. You can tell Enblend how much memory it is allowed to use, and it will swap to disk after that.
- Support for large panoramas. I have tested that Enblend can blend a 1.2 gigapixel, 16-bit per channel color image. You should be able to go right up to 4 gigabyte limit of the TIFF format.
- Optional blending in CIE L*a*b* color space

* Mon May 24 2004 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt1
- first build for ALTLinux
