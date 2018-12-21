# vim:set ft=spec:
Name: swig
Epoch: 1
Version: 3.0.12
Release: alt5

Summary: Simplified Wrapper and Interface Generator (SWIG)
License: Open Source
Group: Development/C
Url: http://www.swig.org/

# http://download.sourceforge.net/swig/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: fix_import_package.patch
Patch1: swig308-Do-not-use-isystem.patch
Patch2: disable_gdb_interface.patch
Patch3: fix-ocaml-int64-type.patch
Patch4: fix-ocaml-tests.patch
Patch5: fix-chicken-tests.patch
# Based on https://github.com/swig/swig/commit/7c034ead322faa79ad7b94fe72250ce8a4fd5848
Patch6: upstream-issue-1259-preparation.patch
# Based on https://github.com/swig/swig/commit/7f9883011029674553a2a4b623d459f02b512458
Patch7: upstream-issue-1259.patch

%def_disable testsuite

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel yodl chicken
BuildPreReq: R-devel libpcre-devel boost-devel
BuildPreReq: python3-devel python-tools-2to3 zlib-devel
%ifarch %ix86 x86_64
BuildRequires: libracket-devel racket
%endif
# Automatically added by buildreq on Thu Sep 04 2008
BuildRequires: ocaml-findlib gcc-c++ guile22-devel imake java-devel
BuildRequires: libXt-devel liblua5-devel libruby-devel lua5.3
BuildRequires: perl-devel php5-devel python-devel ruby ruby-module-etc
BuildRequires: tcl-devel xorg-cf-files tidy htmldoc perl-devel

%if_enabled testsuite
BuildRequires: perl(Math/BigInt.pm) ocaml-camlp4-devel
%endif

Provides: %name-devel = %version
Obsoletes: %name-deve
Obsoletes: %name-runtime-guile  %name-runtime-php  %name-runtime-python  %name-runtime-perl  %name-runtime-ruby  %name-runtime-tcl
Requires: %name-data = %EVR

%package data
BuildArch: noarch
Summary: SWIG data files
Group: Development/C
Conflicts: %name < %EVR

%package doc
BuildArch: noarch
Summary: SWIG documentation
Group: Books/Other
Requires: %name = %EVR

%package runtime-guile
Group: System/Libraries
Summary: SWIG runtime guile library

%package runtime-php
Group: System/Libraries
Summary: SWIG runtime php library

%package runtime-perl
Group: System/Libraries
Summary: SWIG runtime perl library
Requires: %name = %EVR

%package runtime-python
Group: System/Libraries
Summary: SWIG runtime python library

%package runtime-ruby
Group: System/Libraries
Summary: SWIG runtime ruby library

%package runtime-tcl
Group: System/Libraries
Summary: SWIG runtime tcl library

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

%description doc
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG documentation.

%description data
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG data files.

%description runtime-guile
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime guile library.

%description runtime-php
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime php library.

%description runtime-perl
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime perl library.

%description runtime-python
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime python library.

%description runtime-ruby
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime ruby library.

%description runtime-tcl
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime tcl library.

%prep
%setup
%patch0 -p2
%patch1 -p1
%patch2 -p1
%if_enabled testsuite
%patch3 -p2
%patch4 -p2
%patch5 -p2
%endif
%patch6 -p2
%patch7 -p2

%build
./autogen.sh
subst 's/PYLIBDIR="lib"/PYLIBDIR="%_lib"/' configure
subst 's/PY3LIBDIR="lib"/PY3LIBDIR="%_lib"/' configure
%configure \
	--with-python=python \
	--with-python3=python3 \
	--with-ocamlc=ocamlc \
	--with-boost \
	--with-pyinc=%_includedir/python%_python_version \
	--with-pylib=%_libdir/python%_python_version \
	--with-tclconfig=%_libdir \
	--with-perl5
	#--with-tcl --with-python --with-perl5 --with-java --with-guile --with-ruby --with-php4

#%__subst -p 's,/usr/local/include/Py,%_includedir/python%__python_version,g' Runtime/Makefile
# SMP incompatible
# no `all' target
%make_build
#%make docs
#%make runtime
#pushd Runtime
#%make
#popd
bzip2 -9fk CHANGES TODO

%install
%makeinstall_std \
	M4_INSTALL_DIR=%buildroot%_datadir/aclocal
mkdir -p %buildroot%_includedir
cp -aL Source/Swig/*.h Source/DOH/*.h Source/Include/*.h \
	%buildroot%_includedir/
# symlinks
#__rm -fv Examples/perl Examples/test-suite/perl Examples/GIFPlot/Php4

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -p -m644 ANNOUNCE CHANGES* COPYRIGHT LICENSE* README RELEASENOTES TODO* \
	%buildroot%docdir/
cp -a Examples Doc %buildroot%docdir/

#pushd Runtime
#%make_install install DESTDIR=%buildroot
#popd

%if_enabled testsuite
%check
%__make check
%endif

%files
%_bindir/*
#%_datadir/aclocal/%name.m4
%_includedir/*
%dir %docdir
%docdir/[A-Z][A-Z]*

%files doc
%dir %docdir
%docdir/[A-Z][a-z]*
#%_man1dir/*

%files data
%_datadir/%{name}

#%files runtime-guile
#%_libdir/libswigguile*.so*
#%doc CHANGES.current LICENSE

#%files runtime-php
#%_libdir/libswigphp*.so*
#%doc CHANGES.current LICENSE

#files runtime-perl
#_libdir/libswigpl*.so*
#doc CHANGES.current LICENSE

#%files runtime-python
#%_libdir/libswigpy*.so*
#%doc CHANGES.current LICENSE

#%files runtime-ruby
#%_libdir/libswigrb*.so*
#%doc CHANGES.current LICENSE

#%files runtime-tcl
#%_libdir/libswigtcl*.so*
#%doc CHANGES.current LICENSE

%changelog
* Mon Dec 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0.12-alt5
- NMU: fixed code generated for python >= 2.3 and gcc-8.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.0.12-alt4.1
- (NMU) Rebuild with new Ruby autorequirements.
- Build with racket only on %ix86 and x86_64.

* Tue Sep 26 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:3.0.12-alt4
- Fix import package (https://github.com/swig/swig/issues/769)

* Thu Jul 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0.12-alt3
- Removed mono dependencies

* Wed Apr 26 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.12-alt2
- rebuilt with guile22

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.0.12-alt1
- 3.0.12
- removed obsolete patches
- updated lua* build dependencies
- built with boost-1.63

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1:3.0.8-alt1
- Version 3.0.8

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.7-alt1
- Version 3.0.7

* Wed Jul 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.6-alt1
- Version 3.0.6 (ALT #31128)

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.5-alt1
- Version 3.0.5

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.2-alt1
- Version 3.0.2

* Wed Sep 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt2
- Added perl support

* Fri May 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt1
- Version 3.0.0

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.11-alt1
- Version 2.0.11

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.10-alt1
- Version 2.0.10

* Thu Apr 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.9-alt1
- Version 2.0.9

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.8-alt1
- Back to version 2.0.8

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1
- Version 2.0.9

* Fri Aug 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.8-alt1
- Version 2.0.8

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt4
- Rebuilt without pike7.8-devel

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt3
- Built with Python 3 support

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Fixed for asdict

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0 (ALT #23734)

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.40-alt2
- Fixed previous error (build with old sources)

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.40-alt1
- Version 1.3.40

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.39-alt1.1
- Rebuilt with python 2.6

* Fri Jul 03 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.39-alt1
- [1.3.39]

* Tue Nov 25 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.36-alt2
- rebuild with php5-devel in buildreq

* Thu Sep 04 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.36-alt1
- new version
- fixed build req

* Mon Mar 17 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.34-alt1
- new version

* Mon Feb 18 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.31-alt2
- Remove python version from build requirements.
  (Thanks to Grigory Batalov <bga@altlinux.ru>)

* Fri Dec 15 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.3.31-alt1
- new version

* Tue May 23 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.3.29-alt1
- new version

* Fri Dec 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.27-alt1
- new version

* Thu Nov 17 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.25-alt2
- x86_64 build bug fixed

* Wed Aug 10 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.25-alt1
- new upstream release

* Wed Mar 30 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.24-alt2
- gcc3.3 depends fixed

* Thu Jan 06 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.24-alt1
- new version
- debian patch for runtime libs

* Sun Aug 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.21-alt6
- Updated build dependencies.
- Packaged docs in separate subpackage.
- Packaged other runtime libraries in separate subpackages,
  resurrected %%post/%%postun scripts.

* Fri Jun 11 2004 Gleb Stiblo <ulfR@altlinux.ru> 1.3.21-alt5
- libswigpy moved to swig-runtime-python

* Thu Jun 10 2004 Gleb Stiblo <ulfR@altlinux.ru> 1.3.21-alt4
- libswigpy.so added for subversion-python

* Fri Jun 04 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.3.21-alt3
- removed runtime libraries
- swig and swing-devel merged

* Thu Jun 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.3.21-alt2
- rebuild with new python building scheme

* Wed Jan 14 2004 Alexey Tourbin <at@altlinux.ru> 1.3.21-alt1
- 1.3.21
- built with python23

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 1.3.19-alt2
- do not package .la files
- post/postun ldconfig scripts added
- static libraries not packaged by default

* Thu Nov 13 2003 Alexey Tourbin <at@altlinux.ru> 1.3.19-alt1
- updated to 1.3.19

* Thu Oct 17 2002 Rider <rider@altlinux.ru> 1.3.16-alt1
- 1.3.16

* Wed Aug 14 2002 Rider <rider@altlinux.ru> 1.3.14-alt1
- 1.3.14
- specfile cleanup
- BuildRequires fix

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.3.11-alt1
- 1.3.11

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 1.3a5-alt1
- 1.3a5

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation
- build with pythin 2.0

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.3a3-2mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3a3-1mdk
- BM.
- Clean up specs.
- 1.3a3.

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1p5-5mdk
- Use makeinstall macros.

* Mon Apr 10 2000 Francis Galiegue <fg@mandrakesoft.com> 1.1p5-4mdk
- Provides: swig

* Mon Apr  3 2000 Pixel <pixel@mandrakesoft.com> 1.1p5-3mdk
- rebuild with new perl
- cleanup

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.1p5-2mdk
- Rebuilt on kenobi
- Don't use prefix

* Fri Mar 10 2000 Francis Galiegue <francis@mandrakesoft.com> 1.1p5-1mdk
- First RPM for Mandrake
