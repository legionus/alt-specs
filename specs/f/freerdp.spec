%def_without ffmpeg
%def_without x264
%def_without directfb
# see https://github.com/FreeRDP/FreeRDP/issues/4348
%def_without gss

Name: freerdp
Version: 2.0.0
Release: alt1.git20181120

Group: Networking/Remote access
Summary: Remote Desktop Protocol functionality
License: Apache License 2.0
URL: http://www.freerdp.com
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %name-%version.tar

Requires: xfreerdp = %EVR
Requires: wlfreerdp = %EVR
Requires: %name-plugins-standard = %EVR

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake gcc-c++
BuildRequires: docbook-style-xsl git-core xmlto libpcre-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpcsclite)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(libpulse)
%{?_with_directfb:BuildRequires: pkgconfig(directfb)}
BuildRequires: libcups-devel libjpeg-devel zlib-devel
%{?_with_ffmpeg:BuildRequires: libavcodec-devel libavutil-devel}
%{?_with_x264:BuildRequires: libx264-devel}
BuildRequires: libkrb5-devel

%description
freerdp implements Remote Desktop Protocol (RDP), used in a number of Microsoft
products. Rdesktop analog.

This is metapackage.


%package -n xfreerdp
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
#Requires: %name-plugins-standard
Requires: lib%name = %EVR

%description -n xfreerdp
xfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains X11 UI.

%package -n dfreerdp
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
Provides: dfbfreerdp
Requires: lib%name = %EVR

%description -n dfreerdp
dfbfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains DirectFB UI.

%package -n wlfreerdp
Summary: Remote Desktop Protocol client
Group: Networking/Remote access
#Requires: %name-plugins-standard
Requires: lib%name = %EVR

%description -n wlfreerdp
wlfreerdp is a client for Remote Desktop Protocol (RDP), used in a number of
Microsoft products.

This package contains Wayland UI.

%package -n lib%name
Summary: Core libraries implementing the RDP protocol
Group: System/Libraries

%description -n lib%name
libfreerdp can be embedded in applications.

%package -n lib%name-server
Summary: Remote Desktop Viewer server library
Group: System/Libraries

%description -n lib%name-server
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the server.

%package -n libwinpr
Summary: Windows Portable Runtime
Group: System/Libraries

%description -n libwinpr
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n libwinpr-devel
Summary: Windows Portable Runtime development files
Group: Development/C
Requires: libwinpr = %EVR

%description -n libwinpr-devel
The libwinpr-devel package contains libraries and header files for
developing applications that use libwinpr.

%package -n libuwac
Summary: Use wayland as a client
Group: System/Libraries

%description -n libuwac
Remote Desktop Toolkit library. Contains the libuwac libraries.

%package -n     libuwac-devel
Summary: Remote Desktop Toolkit libuwac development files
Group: Development/C
Requires: libuwac = %EVR

%description -n libuwac-devel
The libuwac-devel package contains libraries and header files for
developing applications that use libuwac.

%package plugins-standard
Summary: Plugins for handling the standard RDP channels
Group: Networking/Remote access
Requires: lib%name = %EVR

%description plugins-standard
A set of plugins to the channel manager implementing the standard virtual
channels extending RDP core functionality.  For example, sounds, clipboard
sync, disk/printer redirection, etc.

%package -n lib%name-devel
Summary: Libraries and header files for embedding and extending freerdp
Group: Development/C
Requires: lib%name = %EVR
Provides: freerdp-devel
Obsoletes: freerdp-devel

%description -n lib%name-devel
Header files and unversioned libraries for libfreerdp.

%package server
Summary: Server support for %{name}
Group: Networking/Remote access
Requires: lib%name = %EVR
Requires: lib%name-server = %EVR

%description server
The %{name}-server package contains servers which can export a desktop via
the RDP protocol.

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_SKIP_RPATH=ON \
    -DWITH_ALSA=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON -DBUILTIN_CHANNELS=OFF \
    -DWITH_CLIENT=ON \
    %{?_without_directfb:-DWITH_DIRECTFB=OFF} \
    %{?_without_ffmpeg:-DWITH_FFMPEG=OFF} \
    %{?_without_x264:-DWITH_X264=OFF} \
    -DWITH_GSM=OFF \
    %{?_without_gss:-DWITH_GSSAPI=OFF} \
    -DWITH_GSTREAMER_1_0=ON \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_LIBRARY_VERSIONING=ON \
    -DWITH_MANPAGES=ON \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER=ON \
    -DWITH_WAYLAND=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64
    -DWITH_SSE2=ON \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch armh
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
    #

%cmake_build

%install
%cmakeinstall_std

rm -f %buildroot%_libdir/*.a \
      %buildroot%_libdir/freerdp/*.a

# workaround, add compat
ln -s freerdp2.pc %buildroot%_pkgconfigdir/freerdp.pc

%files

%files -n xfreerdp
%_bindir/xfreerdp
%_man1dir/xfreerdp*
%_bindir/winpr-*
%_man1dir/winpr-*

%files -n wlfreerdp
%_bindir/wlfreerdp
%_man1dir/wlfreerdp*

%if_with directfb
%files -n dfreerdp
%_bindir/dfreerdp
%endif

%files server
%_bindir/freerdp-shadow-cli
%_man1dir/freerdp-shadow-cli.*

%files -n lib%name
%doc LICENSE README ChangeLog
%_libdir/lib%{name}2.so.*
%_libdir/lib%{name}-client2.so.*
%dir %_libdir/freerdp*
%_man7dir/wlog*

%files -n lib%name-server
%_libdir/lib%{name}-server2.so.*
%_libdir/lib%{name}-shadow-subsystem2.so.*
%_libdir/lib%{name}-shadow2.so.*

%files plugins-standard
%_libdir/freerdp*/*.so

%files -n libwinpr
%_libdir/libwinpr2.so.*
%_libdir/libwinpr-tools2.so.*

%files -n libwinpr-devel
%_libdir/cmake/WinPR*
%_includedir/winpr*
%_libdir/libwinpr2.so
%_libdir/libwinpr-tools2.so
%_pkgconfigdir/winpr*.pc

%files -n libuwac
%_libdir/libuwac0.so.*

%files -n libuwac-devel
%_libdir/cmake/uwac*
%_includedir/uwac*
%_libdir/libuwac0.so
%_pkgconfigdir/uwac*.pc

%files -n lib%name-devel
%_libdir/cmake/FreeRDP*
%_includedir/%{name}*
%_libdir/lib%{name}*.so
%_pkgconfigdir/freerdp*.pc

%changelog
* Wed Nov 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20181120
- Fifth release candidate for 2.0.0:
- multiple CVE fixes
- various bugfixes and improvements

* Thu Aug 30 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1.git20180801.S1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Aug 02 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20180801%ubt
- Fourth release candidate for 2.0.0

* Tue Apr 17 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.0.0-alt1.git20180411%ubt
- Third release candidate for 2.0.0
- Fix gstreamer-1.0 detection is not needed now

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1.git20170724%ubt
- Fix gstreamer-1.0 detection
- increase release number for allow backport to p8

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170724
- First release candidate for 2.0.0

* Wed Jan 11 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170109.2
- move libfreerdp-shadow.so.* to libfreerdp-server package

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20170109
- upstream git snapshot 8fd926f08524bcdad8adbb5d908ebb1ad2ce6106

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20160411
- upstream git snapshot 11d113872fe254a2472e99a40f8be7237d5a82d3

* Wed Apr 06 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt0.git20160331
- upstream git snapshot a0d9969a3030a8056eacbe8b2e7362274d0a9c4b
- drop directfb dfreerdp package
- build with wayland support
- build with gstreamer-1.0 support
- split libwinpr,librdtk,libuwac library and devel files
- build server package

* Mon Jun 15 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.0-alt2.beta1
- disable gstreamer support (ALT #31013)

* Sun Mar 22 2015 Mikhail Kolchin <mvk@altlinux.org> 1.1.0-alt1.beta1
- stable-1.1 snapshot 770c67d340d5f0a7b48d53a1ae0fc23aff748fc4

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- fix typo for compile on arm

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3
- don't build ffmpeg module (ALT#29416)

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- separate patches
- fix compile flags

* Wed Sep 18 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New verson (ALT #28716)
- Pack freerdp keymaps

* Thu Mar 22 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt2
- Build git fd465f551c34b1ae415f76be4aefeb0fef770de7

* Tue Feb 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New release

* Tue Jan 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- New release

* Sun Jan 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta5
- New version

* Sat Dec 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta3
- New version

* Sat Nov 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1.beta1
- New version (ALT #24784)
- Update spec for use cmake
- Change license
- Rename subpackage dfbfreerdp -> dfreerdp

* Mon Nov 15 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.2-alt1
- new version

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt2
- added patch

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.8.1-alt1
- new version

* Fri Aug 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt2
- Rename subpackage freerdp-devel -> libfreerdp-devel

* Thu Aug 05 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Fri Jul 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt2
- Fix undefined symbols

* Fri Jul 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- Build for ALT

* Tue Mar 16 2010 Mads Kiilerich <mads@kiilerich.com> - 0.0.1-1
- Initial "upstream" freerdp spec - made and tested for Fedora 12
