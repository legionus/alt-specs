# Original spec file written by qboosh
# http://www.mail-archive.com/pld-cvs-commit@lists.pld-linux.org/msg241980.html

Name: pdtoolkit-gfortran
Version: 4.0.2
Release: alt4
Summary: Modified gfortran parser for use in PDToolkit
License: GPLv2+
Group: Development/Tools
Url: http://www.cs.uoregon.edu/Research/pdt/home.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libgmp-devel libmpfr-devel zlib-devel

%description
Modified gfortran parser for use in PDToolkit.

%prep
%setup

%build
install -d BUILD
pushd BUILD

ln -s ../configure .
%ifarch %ix86
%remove_optflags -mtune=generic
%add_optflags -mtune=i686
%endif
%add_optflags -fgnu89-inline
%configure \
	--enable-cmath \
	--enable-languages="c,f95" \
	--enable-long-long \
	--enable-threads=posix \
	--disable-multilib \
	--disable-nls \
	--with-demangler-in-ld \
	--with-system-zlib \
	--with-slibdir=/%_lib \
	--without-x \
	%_target_platform
%make

popd

%install
install -d %buildroot%_libdir/pdtoolkit/bin
install -m755 BUILD/gcc/{cc1,f951,gfortran} \
	%buildroot%_libdir/pdtoolkit/bin

%files
%dir %_libdir/pdtoolkit
%dir %_libdir/pdtoolkit/bin
%_libdir/pdtoolkit/bin/cc1
%_libdir/pdtoolkit/bin/f951
%_libdir/pdtoolkit/bin/gfortran

%changelog
* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.2-alt4
- Fixed build with gcc-6.

* Fri Jan 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3
- Fixed build for %%ix86

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Fixed build with new glibc

* Wed Mar 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus (thanx qboosh)

