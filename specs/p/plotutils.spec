# do not use rpmrb (multiple Version entries here)

# FIXME: Version: will replacing with package version
%define LIBPLOT_VERSION 4.4
%define LIBXMI_VERSION 1.4
%define fname tek

Name: plotutils
Version: 2.6
Release: alt1.1.qa1

Summary: GNU Plotutils -- plotting utilities

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv3
Group: Graphics
Url: http://www.gnu.org/software/plotutils/plotutils.html

Source: ftp://ftp.gnu.org/gnu/plotutils/plotutils-%version.tar
Patch: %name-info.patch
Patch1: %name-c++.patch
Patch2: %name-2.5.1-alt-autoreconf.patch
Patch3: %name-2.5.1-alt-libpng15.patch

# Automatically added by buildreq on Sun Aug 04 2013
# optimized out: gnu-config libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libstdc++-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: flex gcc-c++ glibc-devel imake libXaw-devel libXext-devel libpng-devel xorg-cf-files

BuildPreReq: rpm-build-fonts gcc-fortran
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
The GNU plotting utilities include:
(1) GNU libplot, a shared library for exporting 2-D vector graphics
files and for performing vector graphics animation under the X
Window System. Its output file formats include pseudo-GIF, PNM, Adobe
Illustrator, Postscript (editable with the free 'idraw' drawing editor),
Fig (editable with the free g' drawing editor), PCL 5, HP-GL and HP-GL/2,
Tektronix, and GNU metafile format. Many Postscript, PCL, and Hershey
fonts are supported. A separate class library, 'libplotter', provides
a C++ binding to libplot's functionality.
(2) Sample command-line applications 'graph', 'plot', 'tek2plot',
'pic2plot', and 'plotfont', which are built on top of GNU libplot. 'graph'
is a powerful utility for XY plotting, 'plot' translates GNU metafiles to
other formats, 'tek2plot' translates legacy Tektronix data, 'pic2plot'
translates box-and-arrow diagrams in the pic language, and 'plotfont'
plots character maps.
(3) Command-line applications 'spline', 'double', and 'ode', which are
useful in scientific plotting. 'spline' does spline interpolation of input
data of arbitrary dimensionality. It uses cubic splines, splines under
tension, or cubic Bessel interpolation. 'ode' is an interactive program
that can integrate a user-specified system of ordinary differential
equations.

%package -n libplot
Summary: libplot plotting library - from plotutils package
Group: Development/C
Version: %LIBPLOT_VERSION

%description -n libplot
GNU libplot: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%package -n libplot-devel
Summary: libplot header files
Group: Development/C
Version: %LIBPLOT_VERSION
Requires: libplot = %LIBPLOT_VERSION-%release

%description -n libplot-devel
libplot header files.

%package -n libplotter
Summary: libplotter plotting library - from plotutils package
Group: Development/C
Version: %LIBPLOT_VERSION

%description -n libplotter
GNU libplotter: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%package -n libplotter-devel
Summary: libplotter header files
Group: Development/C
Requires: libplotter = %LIBPLOT_VERSION-%release
Version: %LIBPLOT_VERSION

%description -n libplotter-devel
libplotter header files.

%package -n libxmi
Summary: libxmi library - from plotutils package
Summary(pl):	libxmi - biblioteka z pakietu plotutils
Group: Development/C
Version: %LIBXMI_VERSION

%description -n libxmi
GNU libxmi: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%package -n libxmi-devel
Summary: libxmi header files
Group: Development/C
Requires: libxmi = %LIBXMI_VERSION-%release
Version: %LIBXMI_VERSION

%description -n libxmi-devel
libxmi header files.

%prep
%setup
%patch2 -p2
%patch3 -p2

%build
CXXFLAGS="-fno-rtti -fno-exceptions"
%autoreconf
%configure \
	--disable-static \
	--enable-libplotter \
	--enable-libxmi
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

cd fonts/pcf
gzip -9nf *.pcf || :
%bitmap_fonts_install %fname

%files
%doc AUTHORS COMPAT KNOWN_BUGS NEWS ONEWS PROBLEMS README THANKS TODO
%_bindir/*
%_infodir/plotutils.info*
%_man1dir/*
%_datadir/ode
%_datadir/pic2plot
%_datadir/tek2plot

%files -n libplot -f fonts/pcf/%fname.files
%doc doc/{*.txt,*.bib}
%doc libplot/{DEDICATION,HUMOR,README*,VERSION}
%_libdir/libplot.so.*
%_datadir/libplot/

%files -n libplot-devel
%_libdir/libplot.so
#_examplesdir/libplot-%LIBPLOT_VERSION
%_includedir/plot.h
%_includedir/plotcompat.h

%files -n libplotter
%_libdir/libplotter.so.*

%files -n libplotter-devel
%_libdir/libplotter.so
%_includedir/plotter.h

%files -n libxmi
%doc libxmi/{AUTHORS,NEWS,README*,TODO,VERSION}
%_libdir/libxmi.so.*

%files -n libxmi-devel
%_infodir/libxmi.info*
%_libdir/libxmi.so
%_includedir/xmi.h

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1.1.qa1
- NMU: applied repocop patch

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1.1
- NMU: added BR: texinfo

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.6-alt1
- new version 2.6 (with rpmrb script)

* Tue Jan 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.qa4
- Fixed build

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.qa3
- Rebuilt with libpng15

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.qa2
- Removed RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt3
- update buildreqs, remove post install_info sections

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt2
- rename font dir to tek (fix bug #17924)

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)
- change license to GPLv3
- drop post/postin_ldconfig
- use rpm-build-fonts
- update buildreqs

* Sat Feb 19 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
 - first build for ALT Linux Sisyphus
 - spec from PLD Team <feedback@pld.org.pl>
