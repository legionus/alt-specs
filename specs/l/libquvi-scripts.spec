%define _name quvi
%define ver_major 0.4

Name: lib%_name-scripts
Version: %ver_major.19
Release: alt2.1

Summary: Lua scripts for parsing the media details
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%name-%version.tar.xz
Patch: %name-0.4.4-alt-pkgconfig.patch

Requires: lua5 lua-module-luasocket

BuildArch: noarch
BuildRequires: quvi

%description
%name contains the embedded lua scripts that libquvi uses for parsing
the media details. Some additional utility scripts are also included.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name.

%prep
%setup
%patch

%build
%autoreconf
%configure
%make_build

%check
#%%make check

%install
%makeinstall_std

%files
%_datadir/%name/
%exclude %_man7dir/%name.*
%doc NEWS README AUTHORS

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Mon Oct 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt2.1
- fixed file conflict with libquvi-scripts0.9 (ALT #31361)

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt2
- reqs: lua5 lua-module-luasocket (ALT #31354)

* Fri Oct 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.19-alt1
- 0.4.19

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.18-alt1
- 0.4.18

* Mon Jul 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.16-alt1
- 0.4.16

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.14-alt1
- 0.4.14

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.13-alt1
- 0.4.13

* Thu Nov 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.9-alt1
- 0.4.9

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus
