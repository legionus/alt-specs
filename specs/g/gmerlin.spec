%define _gavl_version	1.2.0

Summary: Base library for gmerlin applications
Name: gmerlin
Version: 1.2.0
Release: alt2
License: GPL
Group: Development/C++
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.gz
Source90: %name-rpmlintrc

Patch: %name-0.4.3-conf.patch
Patch1: gmerlin-0.4.3-package.patch
#Patch5: %name-0.4.3-alt-camelot.patch
Patch2: gmerlin-1.2.0_glibc.patch
#Patch3: gmerlin-1.2.0_no_test.patch
#Patch4: gmerlin-1.2.0_app.patch

Patch11: gmerlin-1.2.0-vt4l1.patch

# http://git.pld-linux.org/gitweb.cgi?p=packages/gmerlin.git
Patch20: gmerlin-1.2.0-pld-cdio.patch
Patch21: %name-link.patch
Patch22: %name-icons.patch
Patch23: %name-info.patch
Patch24: %name-am.patch

Url: http://gmerlin.sourceforge.net/

# Automatically added by buildreq on Wed Jul 22 2015
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libatk-devel libaudiofile-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libjpeg-devel libpango-devel libpng-devel libquicktime111-core libwayland-client libwayland-server makeinfo pkg-config xorg-fixesproto-devel xorg-inputproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: doxygen imake libXinerama-devel libXtst-devel libXv-devel
BuildRequires: libalsa-devel libcddb-devel libesd-devel libexif-devel
BuildRequires: libgavl-devel libgtk+2-devel libjack-devel libmusicbrainz-devel
BuildRequires: libpulseaudio-devel libtiff-devel libv4l-devel libvisual0.4-devel
BuildRequires: libxml2-devel xorg-cf-files libjpeg-devel

BuildRequires: libcdio-paranoia-devel libcdio-devel >=  0.93
BuildRequires: desktop-file-utils
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
Base library for gmerlin applications.

#
# gmerlin shared libs
#
%package -n libgmerlin
Summary: Shared libraries for gmerlin
Group: System/Libraries

%description -n libgmerlin
Shared libraries for package gmerlin.

#
# libgmerlin-devel
#
%package -n libgmerlin-devel
Summary: Header files for compiling gmerlin applications and plugins
Group: Development/C++
Requires: libgmerlin = %version

%description -n libgmerlin-devel
Header files for compiling gmerlin applications and plugins.

#
# gmerlin-gtk
#
%package -n libgmerlin_gtk
Summary: Gtk support library for gmerlin
Group: System/Libraries
Requires: libgmerlin = %version

%description -n libgmerlin_gtk
Gtk support library for package gmerlin.

#
# gmerlin-gtk-devel
#
%package -n libgmerlin-gtk-devel
Summary: Header files for compiling gmerlin gtk applications
Group: Development/C++
Requires: libgmerlin-devel = %version
Requires: libgmerlin_gtk = %version

%description -n libgmerlin-gtk-devel
Header files for compiling gmerlin gtk applications.

# Alsa
#
%package alsa
Summary: Alsa plugins for gmerlin
Group: Sound
Provides: %name-soundcard-plugin

%description alsa
Alsa plugins for gmerlin (see http://alsa-project.org)

#
# Pulseaudio
#
%package pulseaudio
Summary: Pulseaudio plugins for gmerlin
Group: Sound
BuildRequires: libpulseaudio-devel
Provides: %name-soundcard-plugin

%description pulseaudio
Pulseaudio plugins for package gmerlin.

#
# Jpeg
#
%package jpeg
Summary: Jpeg plugins for gmerlin
Group: Graphics
Provides: %name-image-reader-plugin
Provides: %name-image-writer-plugin

%description jpeg
Jpeg plugins for package gmerlin.

#
# PNG
#
%package png
Summary: PNG plugins for gmerlin
Group: Graphics
Provides: %name-image-reader-plugin
Provides: %name-image-writer-plugin

%description png
PNG plugins for package gmerlin.

#
# TIFF
#
%package tiff
Summary: Tiff plugins for gmerlin
Group: Graphics
Provides: %name-image-reader-plugin
Provides: %name-image-writer-plugin

%description tiff
TIFF plugins for package gmerlin.

#
# OSS
#
%package oss
Summary: OSS plugins for gmerlin
Group: Sound
Requires: %name = %version
Provides: %name-soundcard-plugin

%description oss
OSS plugins for package gmerlin.

#
# mikmod
#
%package mikmod
Summary: MikMod plugins for gmerlin
Group: Sound
Requires: %name = %version

%description mikmod
MikMod plugins for package gmerlin.

#
# subtitles
#
%package subtitles
Summary: Subtitle-plugin for gmerlin
Group: Sound
Requires: %name = %version

%description subtitles
Subtitle-plugin for package gmerlin.

#
# postprocess
#
%package postprocess
Summary: Postprocess-plugins for gmerlin
Group: Sound

%description postprocess
Postprocessors for burning WAV files to audio CDs with CD-Text
(using cdrdao) and burning MPEG-files to VCDs (using vcdimager
and cdrdao).

#
# ESD
#
%package esd
Summary: Esd plugins for gmerlin
Group: Sound
BuildRequires: libesd-devel
Provides: %name-soundcard-plugin

%description esd
esd plugins for package gmerlin.

#
# EDL
#
%package edl
Summary: EDL plugins for gmerlin
Group: Sound

%description edl
EDL plugins for package gmerlin.

#
# X11
#
%package x11
Summary: X11 plugins for gmerlin
Group: Video
Provides: %name-video-playback-plugin

%description x11
X11 plugins for package gmerlin.

#
# V4l
#
%package v4l
Summary: Video4linux plugin for gmerlin
Group: Video
Provides: %name-video-recorder-plugin

%description v4l
Video4linux plugin for package gmerlin.

#
# cdaudio
#
%package cdaudio
Summary: Audio CD playing/ripping plugin for gmerlin
Group: Sound

%description cdaudio
Audio CD playing/ripping plugin for package gmerlin.

#
# Applications: Player
#
%package player
Summary: Multiformat media player
Group: Video
Requires: %name-soundcard-plugin
Requires: %name-video-playback-plugin

%description player
Multiformat media player for package gmerlin.

#
# Applications: Recorder
#
%package recorder
Summary: Multiformat recorder
Group: Video

%description recorder
Recorder for package gmerlin.

#
# Applications: Alsamixer
#
%package alsamixer
Summary: Alsa mixer
Group: Sound

%description alsamixer
Alsa mixer for package gmerlin.

#
# Applications: Transcoder
#
%package transcoder
Summary: Audio/Video transcoder
Group: Video

%description transcoder
Audio/Video transcoder for package gmerlin.

#
# Applications: Visualizer
#
%package visualizer
Summary: Run xmms visualization plugins without having to run xmms
Group: Video

%description visualizer
Run xmms visualization plugins without having to run xmms.

#
# Applications: Camelot
#

#%%package camelot
#Summary: Webcam application
#Group: Video
#Requires: %name-x11 = %version
#Requires: %name-v4l = %version
#Requires: %name-video-playback-plugin
#Requires: %name-video-recorder-plugin
#Requires: %name-image-writer-plugin

#%%description camelot
#Webcam application.

#
# Utilities
#
%package utils
Summary: Utilities for gmerlin
Group: Video

%description utils
Gmerlin Utilities.

#
# OSD
#
%package OSD
Summary: OSD support for gmerlin
Group: Video

%description OSD
OSD support for package gmerlin.

#
# Applications: Keyboard daemon
#
%package kbd
Summary: Keyboard daemon for gmerlin
Group: Video

%description kbd
Keyboard daemon for package gmerlin.

#
# audiofilter-plugins
#
%package audiofilters
Summary: Audiofilter plugins for gmerlin
Group: Sound

%description audiofilters
Audiofilter plugins for package gmerlin.

#
# videofilter-plugins
#
%package videofilters
Summary: Videofilter plugins for gmerlin
Group: Video

%description videofilters
Videofilter plugins for package gmerlin.

#
# jack
#
%package jack
Summary: Jack plugins for gmerlin
Group: Video

%description jack
Jack plugins for package gmerlin.

#
# gavl
#
%package gavl
Summary: Gavl plugins for gmerlin
Group: Video

%description gavl
Gavl plugins for gmerlin.

%prep
%setup gmerlin-%version
%patch0 -p1
%patch1 -p1
#patch5 -p2
%patch2 -p1
#patch3 -p1

%patch11 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1


%build
gettextize -f


sed -i 's|^\(.*_LDADD.*\)|\1 -lgavl -lgobject-2.0|' tests/Makefile.am
sed -i "s|^\(.*_LDADD =\)\(.*\)|\1 `pkg-config gtk+-2.0 --libs` -lX11 \2|" \
       apps/*/Makefile.am


AUTOPOINT=true %autoreconf

CFLAGS="-DGTK_DISABLE_DEPRECATED %(pkg-config --cflags gtk+-2.0)"
LIBS="-ldl" %configure \
    --prefix=%prefix \
    --enable-vtl \
    --disable-gtktest \
    --disable-rpath

%make_build \
	docdir=%_docdir/%name

%install
%makeinstall

install -d -m 755 %buildroot/%_niconsdir/

#rm -f  %buildroot/%_infodir/gmerlin.info.bz2
#rm -f  %buildroot/%_infodir/gmerlin.info
#rmdir  %buildroot/%_infodir

#install -p -m 644 doc/gmerlin.info %buildroot/%_infodir

pushd  %buildroot/%_niconsdir/
	mv %buildroot/%_datadir/gmerlin/icons/mixer_icon.png      gmerlin-alsamixer.png
	mv %buildroot/%_datadir/gmerlin/icons/player_icon.png     gmerlin-player.png
	mv %buildroot/%_datadir/gmerlin/icons/transcoder_icon.png gmerlin-transcoder.png
# 	mv %buildroot/%_datadir/gmerlin/icons/camelot_icon.png    gmerlin-camelot.png
	mv %buildroot/%_datadir/gmerlin/icons/kbd_icon.png        gmerlin-kbd.png
	mv %buildroot/%_datadir/gmerlin/icons/plugincfg_icon.png  gmerlin-plugincfg.png
	mv %buildroot/%_datadir/gmerlin/icons/recorder_icon.png   gmerlin-recorder.png
	mv %buildroot/%_datadir/gmerlin/icons/visualizer_icon.png gmerlin-visualizer.png
popd

# make rpmlint happy ..
#pushd %buildroot%_desktopdir
#	sed -i -e 's|.png||g' *.desktop
#popd

%find_lang %name

rm -f %buildroot%_libdir/%name/plugins/*.la
rm -f %buildroot%_libdir/*.la

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Mixer \
	%buildroot%_desktopdir/gmerlin-alsamixer.desktop

# desktop-file-install --dir %buildroot%_desktopdir \
# 	--remove-category=Application \
# 	--add-category=Video \
# 	--add-category=Recorder \
# 	%buildroot%_desktopdir/gmerlin-camelot.desktop

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/gmerlin-transcoder.desktop

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Recorder \
	%buildroot%_desktopdir/gmerlin-recorder.desktop

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Player \
	%buildroot%_desktopdir/gmerlin-player.desktop

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Audio \
	%buildroot%_desktopdir/gmerlin-visualizer.desktop

%files
%exclude %_docdir/gmerlin/apiref
%doc %_docdir/gmerlin
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/e_wav.so
%_libdir/%name/plugins/*_tga.so
%_libdir/%name/plugins/*_bmp.so
%dir %_datadir/%name
%dir %_datadir/%name/icons
%_datadir/%name/icons/*_16.png
%_datadir/%name/icons/digit_*.png
%_datadir/%name/icons/display_mode_*.png
%_datadir/%name/icons/%name.jpg
%_datadir/%name/icons/repeat_mode_*.png
%_datadir/%name/icons/state_*.png
%_datadir/%name/icons/tab_close.png
%_datadir/%name/icons/tracks_dnd_32.png
%_infodir/%name.info*
#%%exclude %_iconsdir/%name-camelot.png

%files -n libgmerlin
%_libdir/libgmerlin.so.*

%files -n libgmerlin-devel
%dir %_docdir/gmerlin/apiref
%doc %_docdir/gmerlin/apiref/*
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_includedir/%name/x11
%_includedir/%name/x11/x11.h
%_libdir/libgmerlin.so
%_datadir/%name/plugin.sym
%_pkgconfigdir/%name.pc

%files -n libgmerlin_gtk
%_libdir/libgmerlin_gtk.so.*

%files -n libgmerlin-gtk-devel
%dir %_includedir/%name
%dir %_includedir/%name/gui_gtk
%_includedir/%name/gui_gtk/*.h
%_libdir/libgmerlin_gtk.so
%_pkgconfigdir/%name-gtk.pc

%files alsa
%_libdir/%name/plugins/*alsa*.so

%files audiofilters
%_libdir/%name/plugins/fa_*.so

%files cdaudio
%_libdir/%name/plugins/*cdaudio*.so

%files edl
%_libdir/%name/plugins/i_edl.so

%files esd
%_libdir/%name/plugins/*esd*.so

%files gavl
%_libdir/%name/plugins/*_gavl.so

%files jack
%_libdir/%name/plugins/*_jack.so

%files jpeg
%_libdir/%name/plugins/*jpeg*.so

%files mikmod
%_libdir/%name/plugins/*mikmod*.so

%files oss
%_libdir/%name/plugins/*oss*.so

%files png
%_libdir/%name/plugins/*png*.so
%_libdir/%name/plugins/*pnm*.so
%_libdir/%name/plugins/*spumux*.so

%files postprocess
%_libdir/%name/plugins/e_pp_cdrdao.so
%_libdir/%name/plugins/e_pp_vcdimager.so

%files pulseaudio
%_libdir/%name/plugins/*pulse.so

%files subtitles
%_libdir/%name/plugins/*subtext*.so

%files tiff
%_libdir/%name/plugins/*tiff*.so

%files v4l
%_libdir/%name/plugins/*v4l*.so

%files videofilters
%_libdir/%name/plugins/fv_*.so

%files x11
%_libdir/%name/plugins/*x11*.so

%files OSD
%dir %_datadir/%name/osd
%_datadir/%name/osd/GmerlinOSD.*

#####
# Applications

%files alsamixer
%_bindir/%{name}_alsamixer
%_desktopdir/%name-alsamixer.desktop
%_niconsdir/%name-alsamixer.png
%exclude %_liconsdir/%name-alsamixer.png

#%files camelot
#%%_bindir/camelot
#%%_desktopdir/%name-camelot.desktop
#%%_niconsdir/%name-camelot.png
#%%_niconsdir/camelot_icon.png
#%%_iconsdir/camelot_icon.png

%files kbd
%_bindir/%{name}_kbd
%_bindir/%{name}_kbd_config
%_desktopdir/%name-kbd.desktop
%_niconsdir/%name-kbd.png
%exclude %_liconsdir/%name-kbd.png

%files player -f %name.lang
%_bindir/%name
%_bindir/%{name}_play
%_bindir/%{name}_remote
%_bindir/%{name}_launcher
%dir %_datadir/%name
%dir %_datadir/%name/skins
%dir %_datadir/%name/skins/Default
%_datadir/%name/skins/Default/*
%_desktopdir/%name-player.desktop
%_niconsdir/%name-player.png
%exclude %_liconsdir/%name-player.png
%doc %_man1dir/%name.1*
%doc %_man1dir/%{name}_play.1*
%doc %_man1dir/%{name}_remote.1*

%files recorder
%_bindir/%name-record
%_bindir/%{name}_recorder
%_desktopdir/%name-recorder.desktop
%_niconsdir/%name-recorder.png
%exclude %_liconsdir/%name-recorder.png
%doc %_man1dir/%name-record.1*

%files transcoder
%_bindir/%{name}_transcoder
%_bindir/%{name}_transcoder_remote
%_desktopdir/%name-transcoder.desktop
%_niconsdir/%name-transcoder.png
%exclude %_liconsdir/%name-transcoder.png
%doc %_man1dir/%{name}_transcoder.1*
%doc %_man1dir/%{name}_transcoder_remote.1*

%files visualizer
%_bindir/%{name}_visualize
%_bindir/%{name}_visualizer
%_bindir/%{name}_visualizer_slave
%_libdir/%name/plugins/vis_scope.so
%_desktopdir/%name-visualizer.desktop
%_niconsdir/%name-visualizer.png
%exclude %_liconsdir/%name-visualizer.png

%files utils
%_bindir/%{name}_imgconvert
%_bindir/%{name}_imgdiff
%_bindir/%{name}_psnr
%_bindir/%{name}_ssim
%_bindir/album2m3u
%_bindir/album2pls
%_bindir/gmerlin_vanalyze

%_bindir/%name-video-thumbnailer
%_bindir/%{name}_vpsnr
%_bindir/%{name}_plugincfg
%_desktopdir/%name-plugincfg.desktop
%_niconsdir/%name-plugincfg.png
%exclude %_liconsdir/%name-plugincfg.png

%changelog
* Wed Jun 20 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- disabled quicktime support

* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1.4.1
- rebuild against libcdio.so.18

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1.4
- NMU: added BR: texinfo

* Wed Aug 05 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.0-alt1.3
- Add Patchs from http://git.pld-linux.org/gitweb.cgi?p=packages/gmerlin.git

* Sat Aug 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.0-alt1.2
- add gmerlin-1.2.0-vtl1.patch

* Fri Jul 31 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1.1
- rebuilt against newest libcdio{,-paranoia}

* Tue Jul 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.0-alt1
- New version

* Sat Sep 24 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0-alt1
- New version

* Sun May 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.3-alt5
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gmerlin-alsamixer
  * freedesktop-desktop-file-proposed-patch for gmerlin-camelot
  * freedesktop-desktop-file-proposed-patch for gmerlin-transcoder
  * freedesktop-desktop-file-proposed-patch for gmerlin-recorder
  * freedesktop-desktop-file-proposed-patch for gmerlin-player
  * freedesktop-desktop-file-proposed-patch for gmerlin-visualizer
  * postclean-03-private-rpm-macros for the spec file
  * postclean-05-filetriggers for the spec file

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt4
- Fixed BuildRequires by Hihin Ruslan <ruslandh@altlinux.ru>
- BuildRequires: added libvisual0.4-devel, libmusicbrainz-devel and
  libmjpegtools-devel
- configure.ac: fixed checking of some requirements
- camelot: avoid breaking strict-aliasing rules

* Tue Dec 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt3
- Rebuilt for soname set-versions

* Sun Dec 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt2
- Added gtkfun patch (by ruslandh@)

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.1
- Fixed build

* Sun Apr 25 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.3-alt1
-Version for ALT Linux

* Sat Feb 27 2010 Toni Graffy <toni@links2linux.de> - 0.4.3-0.pm.1
- update to 0.4.3

