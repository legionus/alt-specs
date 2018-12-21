%define _unpackaged_files_terminate_build 1

Name: zoom
Version: 1.0.5
Release: alt3
Summary: Z-Machine: it plays text adventure games written in ZCode
License: GPL
Group: Games/Other
Url: http://www.logicalshift.demon.co.uk/unix/zoom/

Source: %name-%version.tar

BuildRequires: fontconfig-devel zlib-devel libpng-devel t1lib-devel libXt-devel libXrender-devel libXft-devel libXext-devel

%description
zoom is an interpreter for playing all of Infocom's text adventures and
newer games using the same format.

zoom has a fast interpreter core behind an X11 interface.
%prep
%setup

%build
%add_optflags -fgnu89-inline
%configure --with-x
%make

%install
%makeinstall

rm manual/Makefile*

%files
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/%{name}rc

%doc README THANKS TODO manual

%changelog
* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt3
- Fixed build with new toolchain.

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2.1
- Rebuilt with libpng15

* Wed Apr 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt2
- fix build

* Fri Jul 21 2006 Alex V. Myltsev <avm@altlinux.ru> 1.0.5-alt1
- New version (no upstream changelog available).

* Thu Mar 02 2006 Alex V. Myltsev <avm@altlinux.ru> 1.0.4-alt0.a
- Initial build for Sisyphus

