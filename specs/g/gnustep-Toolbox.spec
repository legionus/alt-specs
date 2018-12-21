%set_verify_elf_method unresolved=strict

Name: gnustep-Toolbox
Version: 0.8
Release: alt4
Summary: Collection of tools for GNUstep
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: https://www.freshports.org/deskutils/toolbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
Toolbox is a collection of tools. Each tool is in the form of bundle. In
a given category, you can add new items. Each item contains the value of
location and of bundle (tool). Depending on the location, items can have
different contents even with the same bundle. Conceptually, it is
similar to the bookmark. It does not only store the location, but also
the tool to access the location. The item is not supposed to change its
location frequently. It is designed to access the fixed location, either
on file system or over internet. Some items don't access any location,
such as calculator.

%package -n lib%name
Summary: Shared libraries of Toolbox
Group: System/Libraries

%description -n lib%name
Toolbox is a collection of tools. Each tool is in the form of bundle. In
a given category, you can add new items. Each item contains the value of
location and of bundle (tool). Depending on the location, items can have
different contents even with the same bundle. Conceptually, it is
similar to the bookmark. It does not only store the location, but also
the tool to access the location. The item is not supposed to change its
location frequently. It is designed to access the fixed location, either
on file system or over internet. Some items don't access any location,
such as calculator.

This package contains shared libraries of Toolbox.

%package -n lib%name-devel
Summary: Development files of Toolbox
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Toolbox is a collection of tools. Each tool is in the form of bundle. In
a given category, you can add new items. Each item contains the value of
location and of bundle (tool). Depending on the location, items can have
different contents even with the same bundle. Conceptually, it is
similar to the bookmark. It does not only store the location, but also
the tool to access the location. The item is not supposed to change its
location frequently. It is designed to access the fixed location, either
on file system or over internet. Some items don't access any location,
such as calculator.

This package contains development files of Toolbox.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2' \
	OBJCFLAGS='%optflags -DGNUSTEP' \
	USE_NONFRAGILE_ABI=no \
	TOPDIR=$PWD
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

pushd %buildroot%_libdir
cp GNUstep/Libraries/*.so* ./
for j in Toolbox; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Libraries/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Libraries/$i
		done
	done
done
popd

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/Toolbox.app/Toolbox \
	%buildroot%_bindir/
install -d %buildroot%_includedir
ln -s %_libdir/GNUstep/Headers/Toolbox %buildroot%_includedir/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc DEVELOPER README TODO
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Headers
%_menudir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Headers

%changelog
* Mon Feb 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

