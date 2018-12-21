%define _unpackaged_files_terminate_build 1

%define lib_name libpfs
%def_without octave
%def_without opencv

Name: pfstools
Version: 2.1.0
Release: alt3

Summary: High Dynamic Range (HDR) Images and Video manipulation tools
License: GPLv2+
Group: Graphics

Url: http://pfstools.sourceforge.net/
Source: %name-%version.tar

BuildRequires: gcc-c++ libImageMagick-devel libfftw3-devel libGLUT-devel libgeos-devel
BuildRequires: libjpeg-devel liblapack-devel libncurses-devel libnetpbm-devel
BuildRequires: libreadline-devel openexr-devel cmake libgsl-devel libexif-devel
BuildRequires: libgomp-devel libtbb-devel zlib-devel

%if_with opencv
BuildRequires: libopencv-devel-static
%endif

%if_with octave
BuildRequires: octave-devel
%endif

# Optimized out build requirements we want to add as safety belt
# (so pfstools build will not fail if due to changes in other packages
# deps listed below packages will not be pulled for build)
BuildRequires: qt5-base-devel libtiff-devel
BuildRequires: gcc-fortran
BuildRequires(pre): rpm-macros-cmake

Requires: %lib_name = %version-%release

# TODO: Move pfsglview and pfsview to own packages to prevent users from
# having to install OpenGL/GLUT and Qt?

%description
pfstools package is a set of command line (and one GUI) programs for reading,
writing, manipulating and viewing high-dynamic range (HDR) images and video
frames. All programs in the package exchange data using a simple generic file
format (pfs) for HDR data. The concept of the pfstools is similar to netpbm
package for low-dynamic range images.

%package -n %lib_name
Summary: Library for %name
Group: System/Libraries
License: LGPLv2.1+

%description -n %lib_name
This package contain the library needed to run programs linked with %lib_name.

%package -n %lib_name-devel
Summary: Headers for developing programs that will use %lib_name
Group: Development/C++
License: LGPLv2.1+
Requires: %lib_name = %version-%release

%description -n %lib_name-devel
This package contains the headers that programmers will need to develop

%if_with octave
%package octave
Summary: Octave interaction with PFS tools
Group: Graphics

%description octave
The pfstools-octave package contains programs to process red, green and blue
channels or luminance channels in pfs stream using Octave.
%endif

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/pfsabsolute
%if_with opencv
%_bindir/pfsalign
%endif
%_bindir/pfscolortransform
%_bindir/pfshdrcalibrate
%_bindir/pfsinhdrgen
%_bindir/pfsinme
%_bindir/pfsplotresponse
%_bindir/pfsretime
%_bindir/pfstmo_drago03
%_bindir/pfstmo_durand02
%_bindir/pfstmo_fattal02
%_bindir/pfstmo_ferradans11
%_bindir/pfstmo_mai11
%_bindir/pfstmo_mantiuk06
%_bindir/pfstmo_mantiuk08
%_bindir/pfstmo_pattanaik00
%_bindir/pfstmo_reinhard02
%_bindir/pfstmo_reinhard05
%_bindir/pfscat
%_bindir/pfsclamp
%_bindir/pfscut
%_bindir/pfsextractchannels
%_bindir/pfsdisplayfunction
%_bindir/pfsflip
%_bindir/pfsgamma
%_bindir/pfsin
%_bindir/pfsindcraw
%_bindir/pfsinpfm
%_bindir/pfsinppm
%_bindir/pfsinrgbe
%_bindir/pfsintiff
%_bindir/pfsout
%_bindir/pfsouthdrhtml
%_bindir/pfsoutpfm
%_bindir/pfsoutppm
%_bindir/pfsoutrgbe
%_bindir/pfsouttiff
%_bindir/pfspad
%_bindir/pfspanoramic
%_bindir/pfsrotate
%_bindir/pfssize
%_bindir/pfstag
%_bindir/dcraw2hdrgen
%_bindir/pfsinexr
%_bindir/pfsoutexr
%_bindir/pfsinimgmagick
%_bindir/pfsoutimgmagick
%_bindir/pfsglview
%_bindir/pfsview
%_bindir/pfsv
%_bindir/jpeg2hdrgen

%_bindir/pfsinyuv
%_bindir/pfsoutyuv

%_datadir/pfstools

%_man1dir/pfsabsolute.*
%if_with opencv
%_man1dir/pfsalign.*
%endif
%_man1dir/pfscolortransform.*
%_man1dir/pfshdrcalibrate.*
%_man1dir/pfsinhdrgen.*
%_man1dir/pfsinme.*
%_man1dir/pfsplotresponse.*
%_man1dir/pfsretime.*
%_man1dir/pfstmo_drago03.*
%_man1dir/pfstmo_durand02.*
%_man1dir/pfstmo_fattal02.*
%_man1dir/pfstmo_ferradans11.*
%_man1dir/pfstmo_mai11.*
%_man1dir/pfstmo_mantiuk06.*
%_man1dir/pfstmo_mantiuk08.*
%_man1dir/pfstmo_pattanaik00.*
%_man1dir/pfstmo_reinhard02.*
%_man1dir/pfstmo_reinhard05.*
%_man1dir/pfscat.*
%_man1dir/pfsclamp.*
%_man1dir/pfscut.*
%_man1dir/pfsdisplayfunction.*
%_man1dir/pfsextractchannels.*
%_man1dir/pfsflip.*
%_man1dir/pfsgamma.*
%_man1dir/pfsin.*
%_man1dir/pfsindcraw.*
%_man1dir/pfsinpfm.*
%_man1dir/pfsinppm.*
%_man1dir/pfsinrgbe.*
%_man1dir/pfsintiff.*
%_man1dir/pfsout.*
%_man1dir/pfsouthdrhtml.*
%_man1dir/pfsoutpfm.*
%_man1dir/pfsoutppm.*
%_man1dir/pfsoutrgbe.*
%_man1dir/pfsouttiff.*
%_man1dir/pfspad.*
%_man1dir/pfspanoramic.*
%_man1dir/pfsrotate.*
%_man1dir/pfssize.*
%_man1dir/pfstag.*
%_man1dir/dcraw2hdrgen.*
%_man1dir/jpeg2hdrgen.*
%_man1dir/pfsinexr.*
%_man1dir/pfsoutexr.*
%_man1dir/pfsinimgmagick.*
%_man1dir/pfsoutimgmagick.*

%_man1dir/pfsglview.*
%_man1dir/pfsview.*

%_man1dir/pfsinyuv.*
%_man1dir/pfsoutyuv.*

%files -n %lib_name
%_libdir/*.so.*

%files -n %lib_name-devel
%_includedir/pfs
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%if_with octave
%files octave
%_bindir/pfsoctavelum
%_bindir/pfsoctavergb
%_bindir/pfsstat
%_libdir/octave/*/site/oct/*/pfstools
%_datadir/octave/*/site/m/pfstools
%_man1dir/pfsoctavelum.*
%_man1dir/pfsoctavergb.*
%_man1dir/pfsstat.*
%endif

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt3
- rebuilt with libGLUT

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt2
- rebuilt for ImageMagick

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 2.0.6-alt1
- new version

* Wed Mar 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.5-alt1.8.3
- Rebuild with new gdal

* Wed Jul 08 2015 Paul Wolneykien <manowar@altlinux.org> 1.8.5-alt1.8.2
- Disable Octave package (rebuilding with Octave v4.0.0 fails).

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.5-alt1.8.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Feb 17 2015 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.8
- Rebuild with new libImageMagick

* Thu Oct 23 2014 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.7
- Rebuild with new libImageMagick

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.org> 1.8.5-alt1.6
- Rebuild with the new version of Octave: 3.8.0.

* Thu Sep 26 2013 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.5
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.4
- Rebuild with new libImageMagick

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.3
- Rebuilt with libtiff5

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.2
- Fixed build

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.1
- Rebuild with new libImageMagick

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 1.8.5-alt1
- 1.8.5

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Apr 27 2011 Paul Wolneykien <manowar@altlinux.ru> 1.8.3-alt2.1
- Rebuild with the new version of Octave (3.4.0).

* Tue Apr 26 2011 Victor Forsiuk <force@altlinux.org> 1.8.3-alt2
- Renew build requirements.

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 1.8.3-alt1
- 1.8.3
- Build with gdal and octave integration but separate them in
  subpackages to avoid excessive run-time deps of main package.

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1.1
- rebuild with new ImageMagick

* Wed Jul 14 2010 Victor Forsiuk <force@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Jun 23 2009 Victor Forsyuk <force@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Nov 18 2008 Victor Forsyuk <force@altlinux.org> 1.7.0-alt1
- 1.7.0
- Remove obsolete ldconfig calls in post-scripts.

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 1.6.5-alt1
- 1.6.5

* Sat Mar 01 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.4-alt1.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Tue Feb 26 2008 Victor Forsyuk <force@altlinux.org> 1.6.4-alt1
- 1.6.4

* Fri Jul 06 2007 Victor Forsyuk <force@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Jun 18 2007 Victor Forsyuk <force@altlinux.org> 1.6.1-alt2
- Build with libnetpbm-devel and libImageMagick-devel.

* Thu Jun 07 2007 Victor Forsyuk <force@altlinux.org> 1.6.1-alt1
- Initial build.
