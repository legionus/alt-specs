%define _unpackaged_files_terminate_build 1

Name: gpsbabel
Version: 1.5.4
Release: alt2%ubt

Summary: A tool to convert between various formats used by GPS devices
License: GPL
Group: Sciences/Geosciences
Url: http://www.gpsbabel.org

# https://github.com/gpsbabel/gpsbabel.git
Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: libexpat-devel libusb-devel zlib-devel libminizip-devel gcc-c++
BuildRequires: libshape-devel
BuildRequires: qt5-base-devel qt5-tools
BuildRequires: qt5-webengine-devel

%description
GPSBabel converts waypoints, tracks, and routes from one format to another,
whether that format is a common mapping format like Delorme, Streets and
Trips, or even a serial upload or download to a GPS unit such as those from
Garmin and Magellan. By flatting the Tower of Babel that the authors of
various programs for manipulating GPS data have imposed upon us, it returns
to us the ability to freely move our own waypoint data between the programs
and hardware we choose to use.

It contains extensive data manipulation abilities making it a
convenient for server-side processing or as the backend for other
tools.

It does not convert, transfer, send, or manipulate maps. We process
data that may (or may not be) placed on a map, such as waypoints,
tracks, and routes.

%package gui
Group: Sciences/Geosciences
Summary: A tool to convert between various formats used by GPS devices

%description gui
This package contains gui for gpsbabel.

%prep
%setup
%patch1 -p1

rm -rf zlib shapelib

%build
%configure \
	--with-zlib=system \
	--with-libminizip=system \
	--enable-pdb=no

%make_build

pushd gui
qmake-qt5 USE_GUI=qtwebengine
lrelease-qt5 *.ts
%make_build
popd

%install
%makeinstall_std
%makeinstall_std -C gui

install -m 0755 -d %buildroot%_bindir
install -m 0755 -p gui/objects/gpsbabelfe %buildroot%_bindir/

install -m 0755 -d %buildroot%_qt5_translationdir
install -m 0644 -p gui/gpsbabel*_*.qm %buildroot%_qt5_translationdir/

install -m 0755 -d %buildroot%_datadir/gpsbabel
install -m 0644 -p gui/gmapbase.html %buildroot%_datadir/gpsbabel/

install -m 0755 -d %buildroot%_desktopdir
install -m 0644 -p gui/gpsbabel.desktop %buildroot%_desktopdir/

install -m 0755 -d %buildroot%_iconsdir/hicolor/256x256/apps
install -m 0644 -p gpsbabel.png %buildroot%_iconsdir/hicolor/256x256/apps/

%find_lang %name --with-qt --all-name

%files
%doc AUTHORS README* intdoc gpsbabel.html
%_bindir/%name

%files gui -f %{name}.lang
%doc gui/AUTHORS gui/README*
%_bindir/gpsbabelfe
%_datadir/gpsbabel
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt2%ubt
- Built Qt5 gui.

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt1
- Updated to upstream version 1.5.4.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.6-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 31 2009 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt2
- Rebuilt with texlive.

* Wed Dec 10 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1
- New upstream release.

* Fri Sep 12 2008 Grigory Batalov <bga@altlinux.ru> 1.3.5-alt1
- New upstream release.

* Sun Nov 18 2007 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1
- New upstream release.

* Thu Jun 21 2007 Grigory Batalov <bga@altlinux.ru> 1.3.3-alt1
- Build for ALT Linux.

* Wed Apr 16 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.3-1
- Make first Fedora spec based on the one provided upstream
