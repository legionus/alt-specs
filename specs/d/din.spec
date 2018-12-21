Name: din
Version: 5.2.1
Release: alt2
License: GPLv2
Summary: Edit waveforms in a GUI, and watch the sound change before your ears
Group: Sound
Source: %name-%version.tar.gz
Patch1: din-5.2.1-alt-ftbfs.patch
Url: http://dinisnoise.org/

# Automatically added by buildreq on Sun Sep 09 2012
# optimized out: fontconfig libX11-devel libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: ImageMagick-tools gcc-c++ libGL-devel libfftw3-devel libircclient-devel libjack-devel liblo-devel tcl-devel

%description
If Puredata and Supercollider are two synths, din is a synth of a 3rd kind.
It forgets history, To not repeat it.
It doesnt hide analog music hardware, In digital music software.
You had pulse, sine, triangle and sawtooth,
And went forth and made electronic music.
Now there is just the Bezier curve. Go make your pulse, sine, triangle and sawtooths.
This is nothing new. Some old men did it in the 60s!
Punched numbers into cards. Now you edit waveforms in a GUI,
And watch the sound change before your ears.
Has it got ADSR? It's got DADSARSADS.
Filters? Infinite length delay lines.
With Bezier envelope for feedback and volume.
Modulation? Bezier on Carrier and Modulator. Eat that Chowning.
Notes? Notes! Notes! Notes! Infinite microtones between two tones.
Livecoding? In Tcl. Like LISP, but no ((((:-))))

Collaboration? MIDI. OSC. IRC.

%prep
%setup
%patch1 -p2
sed -i 's@\[tcl8\.5/tcl\.h\]@@' configure.ac
sed -i 's@tcl8\.5@tcl8.6@g' src/Makefile.in
sed -i 's@tcl8\.5@tcl8.6@g' src/Makefile.am
sed -i 's@/usr/local@/usr@g' data/checkdotdin

%build
%autoreconf
%configure
%make_build
for N in 96 64 48 32 24 16; do convert data/din.png $N.png; done

%install
%makeinstall
for N in 96 64 48 32 24 16; do
	install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc README
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Sat Mar 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.2.1-alt2
- Rebuilt against Tcl/Tk 8.6
- Fixed FTBFS

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 5.2.1-alt1.1
- Rebuild with new version liblo

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 5.2.1-alt1
- Autobuild version bump to 5.2.1
- Fix paths

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 4.2.1-alt1
- Autobuild version bump to 4.2.1

* Sun Sep 09 2012 Fr. Br. George <george@altlinux.ru> 4.0-alt1
- Initial build from scratch

