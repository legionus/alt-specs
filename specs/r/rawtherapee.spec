%def_disable snapshot
%define rev %nil
%if_enabled snapshot
%define git_distance 1175
%endif

Name: rawtherapee
Version: 5.5%{?_enable_snapshot:.%git_distance}
Release: alt1

Summary: THe Experimental RAw Photo Editor
License: GPLv3+
Group: Graphics
URL: http://www.rawtherapee.com/

%if_enabled snapshot
# use full archive not git-archive to avoid dancing around version
Source: rawtherapee-%version.tar
%else
Source: http://rawtherapee.com/shared/source/%name-%version.tar.xz
%endif

%define gtk_ver 3.24.2
%define tiff_ver 4.0.3

Requires: %name-data = %version-%release
Requires: libgtk+3 >= %gtk_ver

BuildRequires(pre): cmake >= 2.8.8
%{?_enable_snapshot:BuildRequires: git}
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libtiff-devel >= %tiff_ver
BuildRequires: bzlib-devel gcc-c++ libgomp-devel libgtkmm3-devel libiptcdata-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libfftw3-devel
BuildRequires: libexpat-devel libpixman-devel libcanberra-gtk3-devel
BuildRequires: libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libexiv2-devel libharfbuzz-devel
BuildRequires: liblensfun-devel

%description
Raw Therapee is a free RAW converter and digital photo processing software.

%package data
Summary: Arch independent files for Raw Therapee
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for Raw Therapee to work.

%prep
%setup
# Do not install useless rtstart:
subst "s|install (PROGRAMS rtstart|\#install (PROGRAMS rtstart|" CMakeLists.txt

# downgrade libtiff version (see below)
subst "s|libtiff-4>=4.0.4|libtiff-4>=4.0.3|" CMakeLists.txt

%build
%define optflags -O3 -g
# https://bugzilla.altlinux.org/34677
# from tiff-0.4.9/libtiff/tiff.h
%add_optflags -DPHOTOMETRIC_CFA=32803
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	%{?_disable_snapshot:-DCACHE_NAME_SUFFIX=""} \
	%{?_enable_snapshot:-DCACHE_NAME_SUFFIX="5-dev"}
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

rm -f %buildroot/%_datadir/doc/rawtherapee/*.txt

%files
%_bindir/%name
%_bindir/%name-cli
%doc AUTHORS.txt LICENSE.txt RELEASE_NOTES.txt

%files data
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/metainfo/%name.appdata.xml

%changelog
* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 5.5-alt1
- 5.5

* Wed Mar 21 2018 Yuri N. Sedunov <aris@altlinux.org> 5.4-alt1
- 5.4

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 5.3-alt1
- 5.3

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2

* Wed May 17 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.r1
- 5.0-r1

* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0 (gtk3)

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Mon Jan 13 2014 Yuri N. Sedunov <aris@altlinux.org> 4.0.12-alt1
- 4.0.12

* Wed Dec 18 2013 Yuri N. Sedunov <aris@altlinux.org> 4.0.11-alt1
- 4.0.11

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1.1
- Rebuilt with libpng15

* Mon Mar 26 2012 Victor Forsiuk <force@altlinux.org> 4.0.7-alt1
- 4.0.7

* Fri Dec 16 2011 Victor Forsiuk <force@altlinux.org> 4.0.5-alt1
- 4.0.5

* Tue Jun 14 2011 Victor Forsiuk <force@altlinux.org> 3.0-alt2.20110614
- Mercurial repository snapshot from 2011-06-14.

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 3.0-alt1.alpha1
- Initial build.
