Name: midish
Version: 1.2.1
Release: alt1
Summary: MIDI sequencer/filter
Group: Sound
Url: http://www.midish.org/
License: BSD

Source: %name.tar

# Automatically added by buildreq on Wed Aug 02 2017
BuildRequires: libalsa-devel libreadline-devel

%description
Midish is an open-source MIDI sequencer/filter for Unix-like operating
systems. Implemented as a simple command-line interpreter, it's intended to
be lightweight, fast and reliable for real-time performance.

Important features:
	- multiple MIDI devices handling
	- synchronization to external audio/MIDI hardware/software
	- real-time MIDI filtering/routing (controller 
	  mapping, keyboard splitting, ...)
	- track recording, metronome
	- basic track editing (insert, copy, delete, ...)
	- progressive track quantisation
	- import and export of standard MIDI files
	- tempo and time-signature changes
	- system exclusive messages handling

%prep
%setup -n %name

%build
./configure --prefix=/usr \
	--enable-rmidish \

make

%install
%makeinstall_std
mv %buildroot/usr/{,share/}man
mv %buildroot/usr/share/examples/midish examples
mv %buildroot/usr/share/doc/midish inst_docs

%files
%_bindir/*
%_man1dir/*
%doc README manual.html examples

%changelog
* Wed Aug 02 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
