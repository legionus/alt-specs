
Name: qt5-phonon-backend-vlc
Version: 0.10.1
Release: alt2%ubt

Group: Sound
Summary: VLC plugin for Phonon
Url: http://phonon.kde.org/
License: LGPLv2+

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt qt5-base-devel qt5-phonon-devel
BuildRequires: cmake extra-cmake-modules automoc libEGL-devel
BuildRequires: libvlc-devel >= 1.1
BuildRequires: kde-common-devel



%description
Phonon-VLC is a backend for KDE4 Multimedia Framework

%package -n qt5-phonon-backend-3-vlc
Group: System/Libraries
Summary: VLC Phonon backend
Provides: qt5-phonon-backend = %{get_version qt5-phonon-devel}
Provides: qt5-phonon-backend-vlc = %EVR qt5-phonon-vlc = %EVR
#
Requires: vlc-mini
#
Requires: vlc-plugin-alsa
Requires: vlc-plugin-pulseaudio
#
Requires: vlc-plugin-ffmpeg
Requires: vlc-plugin-flac
Requires: vlc-plugin-mpeg2
Requires: vlc-plugin-ogg
#
Requires: vlc-plugin-dvdnav
Requires: vlc-plugin-dvdread
Requires: vlc-plugin-audiocd
#
Requires: vlc-plugin-v4l
Requires: vlc-plugin-xcb
Requires: vlc-plugin-ts
Requires: vlc-plugin-live555
Requires: vlc-plugin-smb
Requires: vlc-plugin-xml
Requires: vlc-plugin-dbus
Requires: vlc-plugin-taglib
%description -n qt5-phonon-backend-3-vlc
Phonon-VLC is a backend for KDE4 Multimedia Framework

%prep
%setup -q

%build
%add_optflags %optflags_shared -UPIE -U__PIE__
%Kbuild \
    -DPHONON_BUILD_PHONON4QT5=ON \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DPLUGIN_INSTALL_DIR=%_qt5_archdatadir \
    -DINCLUDE_INSTALL_DIR=%_includedir/kde5 \
    -DICON_INSTALL_DIR=%_datadir/kde5/share/icons \
    #

%install
%Kinstall

%files -n qt5-phonon-backend-3-vlc
%_qt5_plugindir/phonon4qt5_backend/phonon_vlc.so
#%_K5srv/phononbackends/vlc.desktop

%changelog
* Fri Jul 13 2018 Sergey V Turchin <zerg@altlinux.org> 0.10.1-alt2%ubt
- fix provides

* Fri Apr 27 2018 Sergey V Turchin <zerg@altlinux.org> 0.10.1-alt1%ubt
- new version

* Sat Feb 10 2018 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt2%ubt
- rebuild with new vlc

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M80P.1
- build for M80P

* Mon Nov 14 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt3
- fix to compile

* Thu Mar 05 2015 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt2
- rebuild with new vlc

* Fri Dec 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt1
- new version

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Mon Sep 01 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.80-alt0.M70P.1
- build for M70P

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.80-alt1
- new version

* Wed Jul 02 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- initial build
