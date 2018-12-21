Name: gtv-dvb
Version: 2.2
Release: alt1%ubt

Summary: Media Player & IPTV & Digital TV (DVB, ATSC, DTMB)

License: LGPLv2
Group: Video
Url: https://github.com/vl-nix/gtv

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Buildrequires(pre): rpm-build-ubt
BuildRequires: pkgconfig(gtk+-3.0) pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(gstreamer-plugins-bad-1.0) 
Requires: v4l-utils gst-libav

%description
DVB-T/T2, DVB-S/S2, DVB-C, ATSC, DTMB
Graphical user interface - Gtk+3
Audio & Video & Digital TV - Gstreamer 1.0

%prep
%setup

%build
%make_build CFLAG='%optflags' prefix=%prefix

%install
%makeinstall_std prefix=%prefix
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/*
%doc README.md LICENSE

%changelog
* Sun Apr 15 2018 Anton Midyukov <antohami@altlinux.org> 2.2-alt1%ubt
- new version 2.2

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 2.1-alt1%ubt
- new version 2.1

* Sat Apr 07 2018 Anton Midyukov <antohami@altlinux.org> 2.0-alt1%ubt
- new version 2.0

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 1.1.9-alt1%ubt
- ubt release

* Thu Mar 29 2018 Anton Midyukov <antohami@altlinux.org> 1.1.9-alt1
- new version 1.1.9

* Wed Mar 28 2018 Anton Midyukov <antohami@altlinux.org> 1.1.8-alt1%ubt
- new version 1.1.8

* Sat Dec 23 2017 Anton Midyukov <antohami@altlinux.org> 1.1-alt1%ubt
- New version 1.1

* Sun Nov 26 2017 Anton Midyukov <antohami@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT Sisyphus.
