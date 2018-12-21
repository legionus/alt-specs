%def_disable snapshot

%define ver_major 0.999
%define api_ver 1.0
%define gst_api_ver 1.0
# gst-transcoder version
%define gst_ver 1.14.1
%define gtk_ver 3.20
%define gi_ver 1.32

Name: pitivi
Version: %ver_major
Release: alt1

Summary: PiTiVi allows users to easily edit audio/video projects
License: LGPLv2.1+
Group: Video
Url: http://www.pitivi.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: gst-transcoder = %gst_ver-%release

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/python

# should be provided by python3-module-gst1.0
%add_python3_req_skip gi.repository.GstPbutils

Requires: python3-module-gst%gst_api_ver >= %gst_ver
Requires: gstreamer-editing-services
Requires: gst-validate
Requires: gst-libav >= %gst_ver
Requires: gst-plugins-base%gst_api_ver >= %gst_ver
Requires: gst-plugins-good%gst_api_ver >= %gst_ver
Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
Requires: gst-plugins-ugly%gst_api_ver >= %gst_ver
Requires: python3-module-canberra

BuildRequires(pre): rpm-build-python3
BuildRequires: git meson gtk-doc python3-module-nose2
BuildRequires: intltool yelp-tools rpm-build-gir libappstream-glib-devel libcairo-devel
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: python3-module-pycairo-devel
BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: libgtk+3-devel >= %gtk_ver gobject-introspection-devel >= %gi_ver
BuildRequires: libgstreamer%gst_api_ver-gir-devel gst-plugins%gst_api_ver-gir-devel
BuildRequires: gst-validate libgtk+3-gir-devel

%description
Pitivi is a video editor built upon the GStreamer Editing Services.
It aims to be an intuitive and flexible application that can appeal to
newbies and professionals alike.

%package -n gst-transcoder
Version: %gst_ver
Summary: GStreamer Transcoding library
Group: System/Libraries

%description -n gst-transcoder
This package provides GStreamer Transcoding library, tool and
GStreamer plugin.

%package -n gst-transcoder-devel
Version: %gst_ver
Summary: Development files for GStreamer Transcoder
Group: Development/C
Requires: gst-transcoder = %gst_ver-%release

%description -n gst-transcoder-devel
This package provides development files for GStreamer Transcoder.

%package -n gst-transcoder-devel-doc
Version: %gst_ver
Summary: Development documentation for GStreamer Transcoder
Group: Development/Documentation
Conflicts: gst-transcoder-devel < %gst_ver

%description -n gst-transcoder-devel-doc
This package provides development documentation for GStreamer Transcoder.


%prep
%setup

%build
%meson --wrap-mode=default
%meson_build

%install
%meson_install
%find_lang --with-gnome %name


%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_datadir/gstreamer-%gst_api_ver/encoding-profiles/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/appdata/*.appdata.xml
%_datadir/mime/packages/*-mime.xml

%files -n gst-transcoder
%_bindir/gst-transcoder-%api_ver
%_libdir/libgsttranscoder-%api_ver.so.0
%_typelibdir/GstTranscoder-%api_ver.typelib
%_libdir/gstreamer-%gst_api_ver/libgsttranscode.so
%doc AUTHORS NEWS

%files -n gst-transcoder-devel
%_libdir/libgsttranscoder-%api_ver.so
%_pkgconfigdir/gst-transcoder-%api_ver.pc
%_includedir/gstreamer-%api_ver/gst/transcoder/
%_girdir/GstTranscoder-%api_ver.gir

%files -n gst-transcoder-devel-doc
%_datadir/gtk-doc/html/gstreamer-transcoder/

%changelog
* Mon Nov 12 2018 Leontiy Volodin <lvol@altlinux.org> 0.999-alt1
- new version 0.999 (with rpmrb script)
- fixed x86_64 build
- updated spec

* Fri Mar 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.99-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.99-alt1
- 0.99
- new gst-transcoder* subpackages

* Sat Jul 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.98.1-alt1
- 0.98.1 (ALT #33586)

* Thu Apr 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1.1
- exclude gst-transcoder development files (ALT #33373)

* Thu Dec 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1
- 0.98

* Mon Aug 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.97.1-alt1
- 0.97.1

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.96-alt1
- 0.96

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.95-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.95-alt1
- 0.95

* Thu Aug 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt3
- updated to 0.94-f346a5a9

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt2
- updated to 0.94-937f6cf0

* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt1
- 0.94

* Thu May 31 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.0-alt1.1
- Rebuild with Python-2.7

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Thu Jun 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Sat Dec 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.5-alt2
- fixed requires (closes: #24825)

* Thu Sep 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.5-alt1
- 0.13.5

* Thu Mar 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.13.4-alt1
- 0.13.4

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.3-alt2
- updated some translation

* Sun Sep 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2.4-alt1
- 0.13.2.4

* Fri Sep 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2.3-alt1
- 0.13.2.3

* Sat Aug 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.2-alt1
- 0.13.2

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.11.3-alt2
- arch package

* Sun Apr 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Mon Jun 16 2008 Igor Zubkov <icesik@altlinux.org> 0.11.1-alt2
- fix requires (closes #12154 and #12138)

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.11.1-alt1
- 0.11.0 -> 0.11.1

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.11.0-alt1
- 0.10.3 -> 0.11.0
- update license to LGPLv2.1+

* Tue Jun 05 2007 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt1
- 0.10.2 -> 0.10.3

* Mon May 07 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt1
- 0.10.0 -> 0.10.2
- change license to LGPL
- buildreq
- BuildArch -> noarch

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt0.3
- fix build

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt0.2
- new version

* Sat Dec 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.9.1-alt0.1
- initial build for ALT Linux Sisyphus

