# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _localstatedir %_var
Summary: Real-time Convolution Engine
Name: jconvolver
Version: 1.0.0
Release: alt1
License: GPLv2+
Group: Sound
Url: http://www.kokkinizita.net/linuxaudio/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://www.kokkinizita.net/linuxaudio/downloads/%name-%version.tar.bz2

Obsoletes: jace <= 0.2.0
Provides: jace = %EVR
Obsoletes: jconv <= 0.8.1
Provides: jconv = %EVR

BuildRequires: gcc-c++
BuildRequires: clthreads-devel
BuildRequires: jackit-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-convolver-devel >= 4.0.0

%description
Jconvolver is a real-time convolution engine. It can execute up to a 64 by 64
convolution matrix (i.e. 4096 simultaneous convolutions) as long as your CPU(s)
can handle the load. It is designed to be efficient also for sparse (e.g.
diagonal) matrices. Unused matrix elements do not take any CPY time.

%prep
%setup

# fix paths of configuration files
find config-files/ -name \*.conf \
  -exec sed -i -e "s|/audio/reverbs|%_datadir/%name/reverbs|g" {} \; \
  -exec sed -i -e "s|^#/cd |/cd |g" {} \;

%build
%make_build -C source

%install
%makeinstall_std PREFIX=%prefix -C source

# install configuration files and demo reverbs
mkdir -p %buildroot%_datadir/%name
cp -a config-files/* %buildroot%_datadir/%name

%files
%doc AUTHORS README* COPYING
%_bindir/*
%_datadir/%name/

%changelog
* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sun May 21 2017 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- Initial build for ALT Linux Sisyphus.
