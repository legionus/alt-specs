%define somver 1
%define sover %somver.1.25
%def_with doc
%define descr \
The tools that are part of the program development and maintenance environment.\
They are really a collection of mostly simple tools that help leverage many of \
the excellent Unix tools for programmers.

Name: sowing
Version: %sover
Release: alt1

Summary: The program development and maintenance environment
License: Free
Group: Development/Tools

Url: http://wgropp.cs.illinois.edu/projects/software/sowing/
Source: sowing.tar.gz
Patch: sowing-1.1.18-fix_brackets_for_perl5.26.patch

Requires: %name-common = %version-%release

BuildPreReq: gcc-c++
%{?_with_doc:BuildPreReq: ghostscript-utils}

%description
%descr

%package common
Summary: Architecture independend files of Sowing
Group: Development/Tools
BuildArch: noarch

%description common
%descr

This package contains architecture independend files of Sowing.

%package -n lib%name
Summary: Shared libraries of Sowing
Group: System/Libraries

%description -n lib%name
%descr

This package contains shared libraries of Sowing.

%package -n lib%name-devel
Summary: Development files of Sowing
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
%descr

This package contains development files of Sowing.

%package -n lib%name-devel-static
Summary: Static libraries of Sowing
Group: Development/C++
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
%descr

This package contains static libraries of Sowing.

%prep
%setup
%patch -p2

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--enable-strict \
	--enable-memorycheck \
	--with-wwwdir=$PWD/www/www1

# potentially SMP incompatible build
make

%install
%makeinstall \
	man1dir=%buildroot%_man1dir \
	datadir=%buildroot%_datadir/%name

install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -m644 lib/*.a %buildroot%_libdir
cp -fR include/* %buildroot%_includedir/

# shared libraries

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
for i in sowing tfilter; do
	ar x ../lib$i.a
	g++ -shared * \
		-Wl,-soname,lib$i.so.%somver -o ../lib$i.so.%sover
	ln -s lib$i.so.%sover ../lib$i.so.%somver
	ln -s lib$i.so.%somver ../lib$i.so
	rm -f *
done
popd
rmdir tmp
popd

sed -i '1s|/sh|/bash|' %buildroot%_bindir/pstoxbm

%files
%_bindir/*

%files common
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Tue May 15 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.25-alt1
- Build new version.

* Fri Mar 02 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.18-alt1.2
- Add patch for fix build with perl 5.26

* Mon Feb 15 2016 Michael Shigorin <mike@altlinux.org> 1.1.18-alt1.1
- BOOTSTRAP: require ghostscript-utils conditionally (doc knob)
- disable parallel build (at least lcc might choke)

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.18-alt1
- NMU: new version - bugfix for perl 5.22

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt4
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt3
- Rebuilt for soname set-versions

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt2
- Fixed for checkbashisms

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt1
- Version 1.1.16

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt4
- Added shared libraries

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt3
- Rebuild with PIC

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt2
- Add static libraries and headers

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt1
- Initial build for Sisyphus
