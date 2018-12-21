Name: libglvnd
Version: 1.1.0
Release: alt3
Epoch: 7
Group: System/Libraries
Summary: The GL Vendor-Neutral Dispatch library
Url: https://github.com/NVIDIA/libglvnd
License: MIT

Provides: libGLdispatch = %epoch:%version-%release libglvnd0 = %epoch:%version-%release
Obsoletes: libGLdispatch < %epoch:%version-%release libglvnd0 < %epoch:%version-%release

Source: %name-%version.tar

BuildRequires: libXext-devel python-modules-compiler python-modules-xml xorg-glproto-devel

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis

%package devel
Summary: Development files for %name
Group: Development/C
Provides: libglvnd0-devel = %epoch:%version-%release
Obsoletes: libglvnd0-devel < %epoch:%version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%package -n libOpenGL
Summary: OpenGL support for libglvnd
Group: System/Libraries
Provides: libglvnd0-opengl = %epoch:%version-%release
Obsoletes: libglvnd0-opengl < %epoch:%version-%release

%description -n libOpenGL
libOpenGL is the common dispatch interface for the workstation OpenGL API

%package -n libGLES
Summary: GLES support for libglvnd
Group: System/Libraries

%description -n libGLES
libGLESv2 are the common dispatch interface for the GLES API

%package -n libEGL
Summary: EGL support for libglvnd
Group: System/Libraries
Requires: libEGL-mesa

%description -n libEGL
libEGL are the common dispatch interface for the EGL API

%package -n libGLX
Summary: GLX support for libglvnd
Group: System/Libraries
Requires: libGLX-mesa
Provides: libglvnd0-glx = %epoch:%version-%release
Obsoletes: libglvnd0-glx < %epoch:%version-%release

%description -n libGLX
libGLX are the common dispatch interface for the GLX API

%package -n libGL
Summary: GL support for libglvnd
Group: System/Libraries

%description -n libGL
libGL are the common dispatch interface for the GLX API

%set_verify_elf_method textrel=relaxed

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot{%_sysconfdir,%_datadir}/glvnd/egl_vendor.d
mkdir -p %buildroot{%_sysconfdir,%_datadir}/egl/egl_external_platform.d

rm -f %buildroot%_libdir/libGLESv1*

%files
%doc README.md
%dir %_sysconfdir/glvnd
%dir %_datadir/glvnd
%_libdir/libGLdispatch.so.*

%files -n libOpenGL
%_libdir/libOpenGL.so.*

%files -n libGLES
%_libdir/libGLESv2.so.*

%files -n libGLX
%_libdir/libGLX.so.*

%files -n libGL
%_libdir/libGL.so.*

%files -n libEGL
%dir %_sysconfdir/glvnd/egl_vendor.d
%dir %_datadir/glvnd/egl_vendor.d
%dir %_sysconfdir/egl
%dir %_sysconfdir/egl/egl_external_platform.d
%dir %_datadir/egl
%dir %_datadir/egl/egl_external_platform.d
%_libdir/libEGL.so.*

%files devel
%_includedir/glvnd
%_libdir/lib*.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Nov 01 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt3
- git snapshot master.012fe39

* Thu Oct 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt2
- 1.1.0
