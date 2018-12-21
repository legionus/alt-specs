Name: ucl
Version: 1.03
Release: alt4
Packager: Fr. Br. George <george@altlinux.ru>
Summary: The UCL Compression Library
License: GPL
Group: System/Libraries
Url: http://www.oberhumer.com/opensource/ucl

Source: %url/download/%name-%version.tar.bz2

BuildPreReq: gcc-c++

%description
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- The decompressors can be squeezed into less than 200 bytes of code.
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced.
- Algorithm is thread safe.
- Algorithm is lossless.
UCL supports in-place decompression.

%package -n lib%name
Summary: The UCL Compression Library
Group: System/Libraries

%description -n lib%name
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- The decompressors can be squeezed into less than 200 bytes of code.
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced.
- Algorithm is thread safe.
- Algorithm is lossless.
UCL supports in-place decompression.

%package -n lib%name-devel
Summary: The UCL Compression Library - development environment
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
UCL implements a number of algorithms with the following features:
- Decompression is simple and *very* fast.
- Requires no memory for decompression.
- The decompressors can be squeezed into less than 200 bytes of code.
- Focuses on compression levels for generating pre-compressed data which
  achieve a quite competitive compression ratio.
- Allows you to dial up extra compression at a speed cost in the compressor.
  The speed of the decompressor is not reduced.
- Algorithm is thread safe.
- Algorithm is lossless.
UCL supports in-place decompression.

This package contains the %name development library and header files.

%prep
%setup

%build
%add_optflags "-std=c90"
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall

%files -n lib%name
%doc AUTHORS NEWS README THANKS TODO upx/00README.UPX
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri Dec 07 2018 Grigory Ustinov <grenka@altlinux.org> 1.03-alt4
- Fixed FTBFS (use c90 standart).

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.03-alt3.qa2
- NMU: rebuilt for debuginfo.

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 1.03-alt3
- Repocop fixed

* Tue Oct 24 2006 Fr. Br. George <george@altlinux.ru> 1.03-alt2
- GEAR adapted

* Fri Oct 08 2004 Dmitry V. Levin <ldv@altlinux.org> 1.03-alt1
- Specfile cleanup.

* Sat Oct  2 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.03-1mdk
- New release 1.03

* Wed Jun 30 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.02-1mdk
- major 1
- source URL
- New release 1.02

* Thu Jul 10 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.01-4mdk
- rebuild for new rpm

* Mon Apr 28 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.01-3mdk
- fix distriblint warning

* Sun Apr  6 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.01-2mdk
- use the right macros
- fix location of the headers

* Sun May 26 2002 G�tz Waschk <waschk@linux-mandrake.com> 1.01-1mdk
- macros, url
- new version

* Mon Jun 18 2001 HA Qu�c-Vi�t <viet@mandrakesoft.com> 0.92-1mdk
- Initial packaging.
