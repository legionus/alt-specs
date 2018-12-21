Name: jack_capture
Version: 0.9.69
Release: alt1
Summary: Record sound files with JACK
Group: Sound
# As explained in the COPYING file,
# jack_capture.c and atomicity/* are GPLv2+,
# jack_capture_gui2.cpp is BSD,
# atomic/* are LGPLv2+.
# The icon is borrowed from oxygen icon theme, which is LGPLv3+
License: GPLv2+ and BSD and LGPLv3+
Url: http://www.musix.org.ar/wiki/index.php/Jack_capture
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://archive.notam02.no/arkiv/src/%name-%version.tar.gz
# Extra sources sent upstream via email on 2009-05-08
# since there is no upstream bugtracker.
Source1: %name.desktop
Source2: %name.png

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
#BuildRequires: meterbridge
BuildRequires: libncurses++-devel

#Requires:	meterbridge
Requires: vorbis-tools

%description
Jack_capture is a program for recording sound files with JACK. It's default
operation is to capture whatever sound is going out to your speakers into a
file, but it can do a number of other operations as well.

%prep
%setup

%build
#make %{?_smp_mflags} OPTIMIZE="%optflags"
%make_build

%install
#make install DESTDIR=%buildroot PREFIX=%prefix
%makeinstall_std PREFIX=%prefix

# Desktop file
mkdir -p %buildroot/%_desktopdir
desktop-file-install --dir=%buildroot%_desktopdir %SOURCE1

# Icon
mkdir -p %buildroot/%_iconsdir/hicolor/48x48/apps
install -pm 644 %SOURCE2 %buildroot/%_iconsdir/hicolor/48x48/apps/

%files
%doc COPYING README
%_bindir/*
%_iconsdir/hicolor/48x48/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Mon May 29 2017 Anton Midyukov <antohami@altlinux.org> 0.9.69-alt1
- Initial build for ALT Linux Sisyphus.
