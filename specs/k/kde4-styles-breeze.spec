%define rname breeze

%define sover 5
%define libbreezecommon libbreezecommon4_%{sover}

Name: kde4-styles-%rname
Version: 5.14.2
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE4 visual style
Url: http://www.kde.org
License: GPL-2.0-or-later or LGPLv2+

Requires: icon-theme-breeze

Source: %rname-%version.tar
Patch1: alt-install-colors.patch

# Automatically added by buildreq on Fri Oct 26 2018 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxcb-devel libxkbfile-devel perl phonon-devel pkg-config python-base python-modules python3 python3-base rpm-build-python3 ruby-stdlibs sh3 xorg-proto-devel xorg-xf86miscproto-devel zlib-devel
#BuildRequires: gcc-c++ glibc-devel-static kde4libs-devel libXxf86misc-devel libfftw3-devel libicu62 libqt4-webkit-devel python3-dev ruby
BuildRequires(pre): kde-common-devel rpm-build-ubt
BuildRequires: gcc-c++
BuildRequires: glibc-devel kde4libs-devel libXxf86misc-devel libfftw3-devel libqt4-webkit-devel zlib-devel

%description
Artwork, styles and assets for the Breeze visual style for KDE4

%package -n %libbreezecommon
Group: System/Libraries
Summary: KDE4 library
#Requires: %name-common = %version-%release
%description -n %libbreezecommon
KDE4 library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K4build \
    -DUSE_KDE4=ON \
    -DWITH_WALLPAPERS=OFF \
    #

%install
%K4install

%K4find_lang --with-kde %name

%files -f %name.lang
%doc COPYING*
%_K4lib/kstyle_breeze_config.so
%_K4plug/styles/breeze.so
%_K4apps/kstyle/themes/breeze.themerc
%_K4apps/color-schemes/Breeze*.colors

%files -n %libbreezecommon
%_K4libdir/libbreezecommon4.so.%sover
%_K4libdir/libbreezecommon4.so.*

%changelog
* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.14.2-alt1
- new version

* Fri Jan 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version
- package color schemes

* Tue Apr 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- initial build
