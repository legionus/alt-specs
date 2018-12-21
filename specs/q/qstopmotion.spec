Name: 	  qstopmotion
Version:  2.3.2
Release:  alt1

Summary:  A program for stopmotion animation
License:  GPLv2
Group:    Other
Url: 	  https://sourceforge.net/p/qstopmotion/

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake
BuildRequires: libv4l-devel  libexif-devel libavdevice57 v4l-utils qt5-qtbase qt5-imageformats qt5-qtbase-gui qt5-base-devel ffmpeg gstreamer-devel libgphoto2-devel libv4l 


%description
This program qStopMotion is a program to create stop motion pictures.


%prep
%setup

%build
#%%cmake
%cmake_insource
%make_build # VERBOSE=1

%install
%makeinstall_std


%files
%_bindir/*
/usr/share/applications/*.desktop
/usr/share/doc/qstopmotion*
/usr/share/icons/hicolor/128x128/apps/*
/usr/share/icons/hicolor/256x256/apps/*
/usr/share/icons/hicolor/32x32/apps/*
/usr/share/icons/hicolor/48x48/apps/*
/usr/share/icons/hicolor/scalable/apps/*
%_man1dir/*
/usr/share/qstopmotion/*
%doc AUTHORS COPYING

%changelog
* Tue Jun 27 2017 Denis Medvedev <nbr@altlinux.org> 2.3.2-alt1
- Initial Sisyphus release
