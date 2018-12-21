%define _unpackaged_files_terminate_build 1

%define realname DevIL

Name: devil
Version: 1.7.8
Release: alt3

Summary: Cross-platform image loading and manipulation toolkit
Group: System/Libraries
License: LGPLv2+
Url: http://openil.sourceforge.net

Source: %name-%version.tar

Patch0: devil-1.7.8-alt-png_set_expand_gray.patch
Patch1: devil-1.7.8-deb-CVE-2009-3994.patch
Patch2: devil-deb-FTBFS-il.h.patch
Patch3: devil-1.7.8-fedora-jasper2.patch

BuildRequires: gcc-c++ libSDL-devel liballegro-devel libjpeg-devel
BuildRequires: liblcms-devel libmng-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libGL-devel libGLU-devel libGLUT-devel libX11-devel
BuildRequires: openexr-devel libjasper-devel libICE-devel libXext-devel
BuildRequires: libXrender-devel libSM-devel libXmu-devel libXi-devel

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax.
DevIL can load, save, convert, manipulate, filter and display a wide
variety of image formats.

%package -n lib%name
Summary: Cross-platform image loading and manipulation toolkit.
Group: System/Libraries

%description -n lib%name
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax.
DevIL can load, save, convert, manipulate, filter and display a wide
variety of image formats.

%package -n lib%name-devel
Summary: DevIL development files.
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. This package contains development files.

%package -n lib%name-devel-static
Summary: DevIL development static files.
Group: Development/C++
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
DevIL development static files.

%package -n lib%name-doc
Summary: DevIL documentation
Group: Development/Documentation

%description -n lib%name-doc
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. This package contains documentation

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
	--disable-win32 \
	--disable-directx \
	--with-pic \
        --enable-ILU \
        --enable-ILUT
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall devildir=%buildroot%_datadir/%name
rm -rf %buildroot%_infodir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/IL
%_pkgconfigdir/*
%_bindir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-doc
%doc README Libraries.txt TODO CREDITS AUTHORS

%changelog
* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.8-alt3
- NMU: fixed build with new libjasper.

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 1.7.8-alt2.qa4
- NMU: rebuild with new libmng

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7.8-alt1.qa4
- NMU: imported patches from Debian to fix FTBFS.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.3
- Rebuilt with libpng15

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.2
- Removed bad RPATH

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.8-alt1.1
- Rebuilt with liballegro4.4

* Sun Jun 07 2009 Maxim Ivanov <redbaron at altlinux.org> 1.7.8-alt1
- New version

* Thu Sep 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.8-alt5.rc2
- 1.6.8 RC2.
- Some spec cleanup.
- Added patch1 to fix include problems.

* Tue May 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.8-alt4.RC1
- New version.
- Added libmesa-devel and libX11-devel to buildreqs.

* Sun Jan 08 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt3
- Fixed building on current Sisyphus.

* Tue Oct 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt2
- Fixed textrel error.

* Fri Aug 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.6.7-alt1
- Initial build.
