# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-symbols
Summary: schematic symbol libraries for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): Библиотеки электрических обозначений для kicad (разработка печатных плат)
Version: 5.0.1
Release: alt1
Source: %name-%version.tar
License: GPLv2+
Group: Engineering
Url: https://code.launchpad.net/kicad

Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++

Obsoletes: kicad-library

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of schematic symbols library needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе библиотеки с обозначения электронных компонентов
для kicad.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%dir %_datadir/kicad
%_datadir/kicad/library/
%dir %_datadir/kicad/template
%_datadir/kicad/template/sym-lib-table

%changelog
* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
