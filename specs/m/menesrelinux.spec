Name: menesrelinux
Version: 1.0.2
Release: alt1.1
Summary: Menesre is GUI for Speech Systems
Summary(ru_RU.UTF-8): Графическая программа для озвучки художественных текстов
License: GPL
Group: Sound
Url: http://menestrel.sourceforge.net/

Packager: Anton Midyukov <antohami@altlinux.org>

Source: menesrelinux-1.0.2.tar.gz
Source1: %name.desktop
Source2: %name.png
Patch0: alt.patch

# Automatically added by buildreq on Tue Oct 13 2015
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libstdc++-devel phonon-devel zlib-devel
BuildRequires: gcc-c++ libqt4-devel libstdc++-devel zlib-devel
Requires: antiword unzip sox festvox_msu_ru_nsh_clunits

%description
Menesre is GUI for Speech Systems
 
%description -l ru_RU.UTF-8
Менестрель - это программа предназначенная для озвучки различных текстов,
но преимущественно на русском языке и имеющая графический интерфейс. Тексты
предполагаются художественного содержания.
Используется Festival.

%prep
%setup -n %name-%version
%patch0 -p1

%build
qmake-qt4 MenestreLinux.pro PREFIX=%buildroot/usr
%make_build

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_desktopdir
mkdir -p %buildroot/%_iconsdir
cp build/target/MenestreLinux %buildroot/%_bindir/%name
install -Dp -m0644 %SOURCE1 %buildroot/%_desktopdir
install -Dp -m0644 %SOURCE2 %buildroot/%_iconsdir

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/*

%changelog
* Wed Oct 14 2015 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1.1
- Small fix in spec file. 

* Tue Oct 13 2015 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1
- Initial build for ALT Linux Sisyphus.
