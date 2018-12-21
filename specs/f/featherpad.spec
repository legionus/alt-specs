Name: featherpad
Version: 0.8
Release: alt1.1
Summary: A lightweight Qt5 plain-text editor for Linux
Group: Editors
Url: https://github.com/tsujan/FeatherPad
License: GPLv3+
Source: V%version.tar.gz

# Automatically added by buildreq on Mon May 07 2018
# optimized out: GraphicsMagick GraphicsMagick-common gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libX11-devel libqt5-core libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel xorg-xproto-devel
BuildRequires: GraphicsMagick-ImageMagick-compat qt5-3d-devel qt5-charts-devel qt5-connectivity-devel qt5-datavis3d-devel qt5-gamepad-devel qt5-multimedia-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-script-devel qt5-scxml-devel qt5-sensors-devel qt5-serialbus-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-webview-devel qt5-x11extras-devel qt5-xmlpatterns-devel

%description
FeatherPad is a lightweight Qt5 plain-text editor for Linux.

* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness
* An optionally permanent search-bar with a different search entry for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving with encoding;
* Syntax highlighting for common programming languages;
* Session management;
* Side-pane mode;
* Printing;
* Text zooming;
* Appropriate but non-interrupting prompts;

%prep
%setup -n FeatherPad-%version

%define _PX 128 16 192 24 256 32 48 64 72 96

%build
%qmake_qt5
%make_build
for n in %_PX; do
	convert featherpad/data/icons/featherpad.svg %n.png
done

%install
%makeinstall INSTALL_ROOT=%buildroot
for n in %_PX; do
	install -D %n.png %buildroot%_iconsdir/hicolor/${n}x$n/apps/%name.png
done

%files
%_bindir/*
%_desktopdir/*
%_datadir/%name/*
%_iconsdir/*/*/*/*

%changelog
* Thu May 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1.1
- NMU: added Url

* Mon May 07 2018 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Autobuild version bump to 0.8

* Mon May 07 2018 Fr. Br. George <george@altlinux.ru> 0.7-alt1
- Initial build for ALT

