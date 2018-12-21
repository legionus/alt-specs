%define _unpackaged_files_terminate_build 1

Name: waon
Version: 0.10
Release: alt4
License: GPLv2
Group: Sound
URL: http://sourceforge.net/projects/waon/
Summary: A Wave-to-Notes (MIDI) transcriber

Source: %name-%version.tar

BuildRequires: libfftw3-devel
BuildRequires: libsndfile-devel
BuildRequires: libao-devel
BuildRequires: libsamplerate-devel
BuildRequires: libgtk+2-devel
BuildRequires: libncurses-devel

%description
WaoN is a Wave-to-Notes transcriber (converts an audio file into MIDI
file) and some utility tools such as gWaoN, graphical visualization of
the spectra, and phase vocoder for time-stretching and pitch-shifting.

%prep
%setup

%build
%make_build

%install
install -D -m0755 waon  %buildroot%_bindir/waon
install -D -m0755 pv %buildroot%_bindir/waon-pv
install -D -m0755 gwaon %buildroot%_bindir/gwaon
install -D -m0644 waon.1 %buildroot%_man1dir/waon.1
install -D -m0644 pv.1 %buildroot%_man1dir/waon-pv.1
install -D -m0644 gwaon.1 %buildroot%_man1dir/gwaon.1

%files
%_bindir/waon
%_bindir/waon-pv
%_bindir/gwaon
%_man1dir/waon.1*
%_man1dir/waon-pv.1*
%_man1dir/gwaon.1*

%changelog
* Thu Jul 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt4
- Updated build dependencies.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt3
- Updated spec to allow any man pages compression.

* Mon Sep  1 2014 Evgenii Terechkov <evg@altlinux.org> 0.10-alt2
- pv -> waon-pv (ALT bug #30175)

* Thu Jun 06 2013 Paul Wolneykien <manowar@altlinux.org> 0.10-alt1
- Fresh up to v0.10 with the help of cronbuild and update-source-functions.
