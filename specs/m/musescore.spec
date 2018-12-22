%define rname mscore
%define mversion 2.3

Name: musescore
Version: 2.3.2
Release: alt1

Summary: Music notation and composition software

License: GPL-2.0-only
Group: Sound
Url: https://musescore.org

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildPreReq: chrpath rpm-build-xdg

# Automatically added by buildreq on Thu Jan 06 2011
BuildRequires: ccmake doxygen gcc-c++ ghostscript-utils graphviz latex2html
BuildRequires: libalsa-devel libjack-devel libportaudio2-devel libsndfile-devel
BuildRequires: qt5-designer qt5-base-devel libpulseaudio-devel libfreetype-devel
BuildRequires: liblame-devel qt5-tools-devel qt5-webkit-devel qt5-declarative-devel
BuildRequires: qt5-script-devel qt5-xmlpatterns-devel qt5-quick1-devel qt5-svg-devel
BuildRequires: qt5-tools-devel-static zlib-devel libvorbis-devel libportmidi-devel

%description
Music notation and composition software

* WYSIWYG design, notes are entered on a "virtual notepaper"
* TrueType font(s) for printing & display allows for high quality scaling to all sizes
* easy & fast note entry
* many editing functions
* MusicXML import/export
* Midi (SMF) import/export
* MuseData import
* Midi input for note entry
* integrated sequencer and software synthesizer to play the score
* print or create pdf files

%prep
%setup
%patch -p1

#for f in `grep -qrl ":/fonts" *`; do
#	sed -i 's@":/fonts@"%_datadir/mscore-%mversion/fonts@g' "$f";
#done

%build
export PATH=$PATH:%%_qt5dir/bin
echo $PATH
mkdir build.debug && cd build.debug
cmake \
	-DCMAKE_BUILD_TYPE=RELEASE \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DBUILD_SCRIPTGEN=FALSE \
	..

make lrelease
make manpages
make mops1 mops2
%make_build

%install
cd build.debug
%makeinstall_std
for f in ../fonts/*.ttf ../fonts/*.xml; do
     install -D $f %buildroot%_datadir/mscore-%mversion/fonts/$(basename $f)
done
for f in ../fonts/bravura/*.otf ../fonts/bravura/*.json; do
     install -D $f %buildroot%_datadir/mscore-%mversion/fonts/bravura/$(basename $f)
done
for f in ../fonts/gootville/*.otf ../fonts/gootville/*.json; do
     install -D $f %buildroot%_datadir/mscore-%mversion/fonts/gootville/$(basename $f)
done
for f in ../fonts/mscore/*.ttf ../fonts/mscore/*.otf ../fonts/mscore/*.json; do
     install -D $f %buildroot%_datadir/mscore-%mversion/fonts/mscore/$(basename $f)
done

chrpath -d %buildroot%_bindir/mscore

%files
%_bindir/*
%_desktopdir/mscore.desktop
%_datadir/mscore-%mversion
%_man1dir/*
%_xdgmimedir/packages/musescore.xml
%_iconsdir/hicolor/*/mimetypes/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Sep 12 2018 Grigory Ustinov <grenka@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt3
- Fix FTBFS (Add missing rpm-build-xdg).

* Thu Nov 23 2017 Fr. Br. George <george@altlinux.ru> 2.1.0-alt2
- Fix sf3 coredump

* Thu Nov 16 2017 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Feb 16 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.2-alt1
- 2.0.2
- build from upstream git repo

* Mon Apr 15 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up
- Fix broken fonts usage in 1.2

* Sat Jun  2 2012 Terechkov Evgenii <evg@altlinux.org> 1.2-alt1
- 1.2

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.3-alt1.1
- Removed bad RPATH

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.6.3-alt1
- new version (ALT bug 23626), update buildreqs
- fix dependencies (ALT bug #21884)

* Tue Apr 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script), fix bug #19710
- update buildreqs

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus

* Sun Feb 10 2008 - Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.9.1

* Tue Jul 31 2007 - Carlos Goncalves <cgoncalves@opensuse.org>
- updated to version 0.6.1
 * This is a bugfix release fixing the midi import crash and adding some small usability enhancements.

* Sun Jul 29 2007 - Carlos Goncalves <cgoncalves@opensuse.org>
- initial package
