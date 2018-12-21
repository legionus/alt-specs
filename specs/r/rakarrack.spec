Name: rakarrack
Version: 0.6.2
Release: alt4.git20140722
Summary: Guitar effects for Linux
License: GPLv2+
Group: Sound
Url: http://rakarrack.sourceforge.net/

Source: %name-%version.tar
Patch1: %name-%version-fedora-format-security.patch

Requires: %name-data = %version-%release

BuildRequires: alsa-utils gcc-c++ jackit-devel libXext-devel libXft-devel
BuildRequires: libXpm-devel libalsa-devel libfltk-devel libjpeg-devel 
BuildRequires: libpng-devel libsamplerate-devel libsndfile-devel

BuildRequires: libpixman-devel libcairo-devel libXinerama-devel
BuildRequires: libXfixes-devel libfftw3-devel libXcursor-devel
BuildRequires: desktop-file-utils

%description
Rakarrack is a richly featured multi-effects processor emulating a 
guitar effects pedalboard.  Effects include compressor, noise gate, 
expander, shuffle, ring, synthfilter, varyband, mutromojo, looper, arpie,
graphic equalizer, parametric equalizer, flanger, dual flange, chorus, echo 
with reverse playback, musical delay, reverb, digital phaser, analogic 
phaser, wah-wah, alien-wah, harmonizer, shifter, sequence, sustainer, 
shelfboost, vocoder, coil crafter, echoverse, convolotron, stompbox, 
exciter and four flexible distortion modules including sub-octave modulation 
and dirty octave up.  Most of the effects engine is built from modules 
found in the excellent software synthesizer ZynAddSubFX.  Presets and 
user interface are optimized for guitar, but Rakarrack processes signals 
in stereo while it does not apply internal band-limiting filtering, 
and thus is well suited to all musical instruments and vocals.  
Rakarrack is designed for Linux distributions with Jack Audio Connection Kit.

%package data
Summary: Data files and documentation for Rakarrack
Group: Sound
BuildArch: noarch

%description data
This package contains data files and documentation for Rakarrack.

%prep
%setup
%patch1 -p1

%build
%autoreconf

%configure \
%ifarch x86_64
	--enable-sse \
	--enable-sse2 \
%endif
	--enable-jack-session \
	--enable-datadir=yes \
	--enable-docdir=yes

%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	%buildroot%_desktopdir/rakarrack.desktop

%files
%_bindir/*

%files data
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_pixmapsdir/*
%_datadir/%name
%_datadir/doc/%name

%changelog
* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt4.git20140722
- Fixed build.

* Sun Sep 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt3.git20140722
- New snapshot

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git.56026bac.1.qa5
- Rebuilt with updated libfltk

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git.56026bac.1.qa4
- Fixed build

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git.56026bac.1.qa3
- Rebuilt with new FLTK

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.2-alt2.git.56026bac.1.qa2
- NMU: rebuilt for updated dependencies.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.2-alt2.git.56026bac.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for rakarrack-data

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git.56026bac.1
- Rebuilt with FLTK 1.3.0.r8575

* Tue Feb 08 2011 Egor Glukhov <kaman@altlinux.org> 0.6.2-alt2.git.56026bac
- Fixed for rebuilding against new fltk

* Sat Dec 18 2010 Egor Glukhov <kaman@altlinux.org> 0.6.2-alt1.git.56026bac
- New version from upstream git

* Fri Aug 06 2010 Egor Glukhov <kaman@altlinux.org> 0.6.0-alt1.git.0a15e5c2
- initial build for Sisyphus

