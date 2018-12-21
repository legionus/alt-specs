%ifndef EVR
%define EVR %{?epoch:%epoch:}%{version}-%{release}
%endif

Name: phonon-backend-gstreamer
Version: 4.8.2
Release: alt1

Group: System/Libraries
Summary: Gstreamer phonon backend
License: LGPLv2+
Url: http://phonon.kde.org/

Source: %name-%version.tar

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig glib2-devel gstreamer-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libgst-plugins libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-xml libstdc++-devel libxkbfile-devel libxml2-devel pkg-config python-base ruby xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: automoc cmake gcc-c++ glibc-devel-static gst-plugins-devel libXxf86misc-devel libalsa-devel libqt3-devel libqt4-opengl phonon-devel rpm-build-ruby
BuildRequires(pre): phonon-devel
BuildRequires: automoc cmake gcc-c++ glibc-devel gst-plugins1.0-devel libalsa-devel phonon-devel libxml2-devel libGL-devel
BuildRequires: kde-common-devel

%description
Gstreamer phonon backend

%package -n phonon-backend-5-gstreamer
Group: System/Libraries
Summary: Gstreamer phonon backend
Provides: phonon-backend = %{get_version phonon-devel}
Provides: phonon-backend-gstreamer = %EVR phonon-gstreamer = %EVR
Obsoletes: phonon-gstreamer < %EVR
Obsoletes: phonon-backend-xine < 4.5 phonon-xine < 4.5 phonon-backend-0-xine < 4.5
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0
%description -n phonon-backend-5-gstreamer
Gstreamer phonon backend

%prep
%setup -q

%build
%K4cmake \
    -DINCLUDE_INSTALL_DIR=%_K4includedir \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt4dir \
    -DUSE_INSTALL_PLUGIN:BOOL=ON \
    #
pushd BUILD-*/gstreamer
if [ ! -e %_includedir/gstreamer-1.0/gst/gstconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gstconfig.h ]
then
    mkdir -p gst
    [ -e gst/gstconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gstconfig.h gst/gstconfig.h
fi
if [ ! -e %_includedir/gstreamer-1.0/gst/gl/gstglconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h ]
then
    mkdir -p gst/gl
    [ -e gst/gl/gstglconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h gst/gl/gstglconfig.h
fi
popd
%K4make VERBOSE=1

%install
%K4install

%files -n phonon-backend-5-gstreamer
%_qt4dir/plugins/phonon_backend/phonon_gstreamer.so
%_K4srv/phononbackends/gstreamer.desktop
%_iconsdir/hicolor/*/apps/phonon-gstreamer.*

%changelog
* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Dec 09 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Tue Jun 24 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Mon Feb 24 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- add more requires to gst-plugins

* Mon Dec 16 2013 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Thu Oct 17 2013 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2.M70P.1
- built for M70P

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt3
- obsolete phonon-backend-0-xine

* Thu Oct 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- obsolete phonon-xine

* Mon Mar 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt0.M60P.1
- build for M60P

* Fri Mar 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version
- sync patches with FC

* Wed Nov 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Apr 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2.M60P.1
- build for M60P

* Thu Apr 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- fix requires

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1.M60P.1
- built for M60P

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- update code from 4.6 branch

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt0.M60P.1
- built for M60P

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Tue Feb 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.90-alt0.M60P.1
- built for M60P

* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.90-alt1
- 4.6 RC1

* Mon Aug 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt3
- fix build requires

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- fix requires

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- initial build
