# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-templates
Summary: Templates projects for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): Примеры проектов для kicad (разработка печатных плат)
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

%name is a set of templates projects by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-library содержит примеры проектов для kicad.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%dir %_datadir/kicad
%_datadir/kicad/template/

%changelog
* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
