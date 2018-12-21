Name: potrace
Version: 1.15
Release: alt2

Summary: Potrace is a utility for transform bitmaps into vector graphics
License: GPLv2+
Group: Graphics
Url: http://%name.sourceforge.net

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz

Requires: lib%name = %EVR

BuildRequires: zlib-devel

# for check
BuildRequires: ghostscript

%description
Potrace is a utility for tracing a bitmap, which means, transforming a bitmap
into a smooth, scalable image. The input is a portable bitmap (PBM), and the
default output is an encapsulated PostScript file (EPS). A typical use is to
create EPS files from scanned data, such as company or university logos,
handwritten notes, etc. The resulting image is not "jaggy" like a bitmap, but
smooth. It can then be rendered at any resolution.

%package -n lib%name
Summary: Potrace library
Group: System/Libraries

%description -n lib%name
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.

This package provides shared Potrace library.

%package -n lib%name-devel
Summary: Potrace development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.

This package provides files necessary to develop applications that use
Potrace library.


%prep
%setup
subst 's/ 1200/ 1500/;s/ 1000/ 1200/' check/pdf-check.sh check/postscript-check.sh

%build
%autoreconf
%configure \
	--with-libpotrace \
	--enable-shared \
	--disable-static \
	--with-pic \
	--enable-metric \
	--enable-a4
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/mkbitmap
%_bindir/%name
%_man1dir/mkbitmap.1.*
%_man1dir/%name.1.*
%doc NEWS README ChangeLog doc/placement.pdf

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/potracelib.h
%_libdir/lib%name.so


%changelog
* Wed Oct 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.15-alt2
- Increase diff level for tests.

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- 1.15 (fixed CVE-2017-12067)

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.14-alt1
- 1.14 (fixed CVE-2016-8685, CVE-2016-8686)

* Thu Oct 29 2015 Yuri N. Sedunov <aris@altlinux.org> 1.13-alt1
- 1.13

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt2
- new lib%%name{,-devel} subpackages (ALT #30432)

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11

* Tue Aug 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10
- %%check section

* Fri Dec 24 2010 Victor Forsiuk <force@altlinux.org> 1.9-alt1
- 1.9

* Mon Oct 29 2007 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8
- Use A4 as the default papersize.

* Mon Mar 07 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.7-alt1
- 1.7

* Mon Feb 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.6-alt1
- 1.6

* Thu Jul 15 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt2
- rebuild

* Mon Jul 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt1
- new version

* Sun Mar 7 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.4-alt1
- 1.4
- further optimized the speed of the function path.c:pathlist_to_tree
- fixed compression bug where garbage was added after the end of stream
- removed potrace.{ps,pdf} from	distribution

* Sat Jan 17 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- 1.3
- the bounding box in the xfig backend was fixed
- the postscript output now has better page encapsulation
- bitmaps of dimension 0 are now tolerated better.

* Wed Dec 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- 1.2

* Fri Aug 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1-alt1
- 1.1

* Thu Aug 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- First version of RPM package.
