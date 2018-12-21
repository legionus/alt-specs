%set_verify_elf_method unresolved=strict

Name: gnustep-ucsdata
Version: r31318
Release: alt8.svn20100910
Summary: The GNUstep Unicode Character Set Data Library
License: LGPLv2+
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/ucsdata/trunk/
Source: %name-%version.tar
Source1: ftp://ftp.unicode.org/Public/UNIDATA/UnicodeData.txt

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel /proc

Requires: gnustep-back

%description
The GNUstep Unicode Character Set Data Library is a small library which
loads the contents of the file UnicodeData.txt into a set of Objective C
objects.

%package -n lib%name
Summary: Shared libraries of gnustep-ucsdata
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
The GNUstep Unicode Character Set Data Library is a small library which
loads the contents of the file UnicodeData.txt into a set of Objective C
objects.

This package contains shared libraries of gnustep-ucsdata.

%package -n lib%name-devel
Summary: Development files of gnustep-ucsdata
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
The GNUstep Unicode Character Set Data Library is a small library which
loads the contents of the file UnicodeData.txt into a set of Objective C
objects.

This package contains development files of gnustep-ucsdata.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -d %buildroot%_libdir/GNUstep/Unicode
install -p -m644 %SOURCE1 %buildroot%_libdir/GNUstep/Unicode/

%files
%doc BUGS README
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt8.svn20100910
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt7.svn20100910
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt7.git20100910
- Rebuilt with new gnustep-gui

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt6.git20100910
- Rebuilt with libobjc2 instead of libobjc

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt5.svn20100910
- Added synonym: lib%name-devel -> %name-devel

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt4.svn20100910
- Put UnicodeData.txt into %_libdir/GNUstep/Unicode

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt3.svn20100910
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt2.svn20100910
- Built with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31318-alt1.svn20100910
- Initial build for Sisyphus

