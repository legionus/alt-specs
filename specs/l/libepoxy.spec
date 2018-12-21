%define ver_major 1.5
%def_enable x11
%def_enable egl
%def_enable check

Name: libepoxy
Version: %ver_major.3
Release: alt1

Summary: Direct Rendering Manager runtime library
Group: System/Libraries
License: MIT
Url: https://github.com/anholt/libepoxy

Source: %url/releases/download/%version/%name-%version.tar.xz
#Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: python3 libGL-devel
%{?_enable_x11:BuildRequires: libX11-devel xorg-util-macros}
%{?_enable_egl:BuildRequires: libEGL-devel}

%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable x11}\
	%{subst_enable egl}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name.so.*
%doc README.md COPYING

%files devel
%_includedir/epoxy/
%_libdir/%name.so
%_pkgconfigdir/epoxy.pc


%changelog
* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun May 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Jun 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Feb 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Sat Jul 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

