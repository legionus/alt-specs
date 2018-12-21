Name: kcollectd
Version: 0.9
Release: alt5.1

Summary: collectd graphing frontend for KDE
License: %gpl3plus
Group: Office
Url: http://www.forwiss.uni-passau.de/~berberic/Linux/kcollectd.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-0.9-alt-boost_v3.patch
Patch1: %name-0.9-alt-kde4_dtd.patch
Patch2: %name-0.9-alt-desktop_fix.patch
Patch3: %name-0.9-alt-license_fix.patch
Patch4: %name-0.9-alt-isnan.patch

BuildRequires(pre): rpm-build-licenses kde-common-devel

%define _unpackaged_files_terminate_build 1
%define __kde4_alternate_placement 1

# Automatically added by buildreq on Sat May 07 2011
# optimized out: automoc boost-devel boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl fontconfig fontconfig-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
BuildRequires: boost-filesystem-devel gcc-c++ kde4libs-devel librrd-devel

%description
Kcollectd is a graphical KDE4-frontend to collectd  that allows
to view RRD files that have been created by collectd. It allows
to easily navigate in the data with the mouse and can be used
as a chart recorder.

%prep
%setup
%patch0
%patch1
%patch2
%patch3
%patch4

# Fix path to collecd files
sed -e 's#/var/lib/collectd/rrd#/var/lib/collectd#' -i CMakeLists.txt
sed -e 's#/var/lib/collectd/rrd#/var/lib/collectd#' -i kcollectd/gui.cc


mv -f -- COPYING COPYING.GPL3.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING) COPYING

%build
%K4build

%install
%K4install VERBOSE=1
%K4find_lang --with-kde %name

mkdir -p -- %buildroot%_bindir
ln -rs -- %buildroot{%_kde4_bindir/%name,%_bindir/%name}

%files -f %name.lang
%doc ChangeLog AUTHORS
%doc --no-dereference COPYING
%_bindir/%name
%_kde4_bindir/%name
%_K4iconsdir/*
%_K4datadir/applications/kde4/*.desktop
%_K4xdg_mime/%name.*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt5.1
- NMU: rebuilt with boost-1.67.0

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 0.9-alt5
- Rebuilt with librrd8

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.9-alt4
- Rebuilt with GCC 6.3

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9-alt2.qa8
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2.1
- rebuild with boost 1.57.0

* Sun Feb 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.9-alt2
- Rebuilt with Boost 1.53.0

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.5
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.4
- Rebuilt with Boost 1.51.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.1
- Rebuilt with Boost 1.47.0

* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.9-alt1
- Initial build for ALT Linux Sisyphus

