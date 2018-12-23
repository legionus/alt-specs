Name: opendx
Version: 4.4.4
Release: alt7
Summary: Open Visualization Data Explorer
License: IPL-1.0
Group: Graphics
Url: http://www.opendx.org/

Source: dx-%version.tar
Patch1: %name-%version-alt-gcc.patch

BuildRequires: libhdf5-devel libtiff-devel flex
BuildRequires: libnetcdf-devel libX11-devel libcdf-devel gcc-c++
BuildRequires: libICE-devel libSM-devel libXt-devel libopenmotif-devel
BuildRequires: libGL-devel libGLU-devel libXext-devel libXmu-devel
BuildRequires: libXp-devel libXpm-devel librx-devel liblcms-devel
BuildRequires: libfreetype-devel libjpeg-devel liblqr-devel glib2-devel
BuildRequires: fontconfig-devel bzlib-devel libXinerama-devel
BuildRequires: libImageMagick-devel

Requires: lib%name = %version-%release

%description
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

And if you are looking to build visualization applications for your end
users, OpenDX has what you need: power to support their requirements and
versatility for customized application development.

OpenDX is a uniquely powerful, full-featured software package for the
visualization of scientific, engineering and analytical data: Its open
system design is built on familiar standard interface environments. And
its sophisticated data model provides users with great flexibility in
creating visualizations.

%package -n lib%name
Summary: Shared libraries of Open Visualization Data Explorer
Group: System/Libraries

%description -n lib%name
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains shared libraries of OpenDX.

%package -n lib%name-devel
Summary: Development files of Open Visualization Data Explorer
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains development files of OpenDX.

%package docs
Summary: Documentation for Open Visualization Data Explorer
Group: Documentation
BuildArch: noarch

%description docs
If you need visualization for anything from examining simple data sets
to analyzing complex, time-dependent data from disparate sources, OpenDX
has what you need: features and functions that let you easily gain
meaningful insight into your data.

This package contains documentation for OpenDX.

%prep
%setup
%patch1 -p2
rm -f aclocal.m4

%build
%add_optflags -Wno-error=narrowing
%autoreconf
INCS="-I%_libexecdir/hdf5-seq/include -I%_libexecdir/hdf5-seq/include/netcdf-3"
INCS="$INCS -I%_includedir/ImageMagick"
%add_optflags $INCS -fno-strict-aliasing
%configure \
	--enable-shared \
	--enable-static=no \
	--with-hdf \
	--with-tiff \
	--with-netcdf \
	--with-magick \
	--with-large-arenas \
	--with-x \
	--enable-ddx
%make_build

%install
%makeinstall_std

install -d %buildroot%_mandir/manl

%files
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README
%_bindir/*
%_libexecdir/dx
%exclude %_libexecdir/dx/doc
%exclude %_libexecdir/dx/help
%exclude %_libexecdir/dx/html
%exclude %_libexecdir/dx/lib
%_mandir/manl/*
%exclude %prefix/dx

%files -n lib%name
%_libdir/*.so.*
%_libexecdir/dx/lib

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/arch.mak

%files docs
%_libexecdir/dx/doc
%_libexecdir/dx/help
%_libexecdir/dx/html

%changelog
* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.4-alt7
- Rebuilt with new toolchain.

* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.4-alt6
- Rebuilt with libnetcdf11.

* Thu Apr 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt5
- Rebuilt with new ImageMagick

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 4.4.4-alt4.1
- Rebuild with new libImageMagick

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt4
- Rebuilt with libnetcdf7

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt3
- Rebuilt for debuginfo
- Built with openmotif instead of lesstif

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt2
- Rebuilt for soname set-versions

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Initial build for Sisyphus

