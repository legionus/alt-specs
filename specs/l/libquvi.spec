%define _name quvi
%define ver_major 0.4

Name: lib%_name
Version: %ver_major.1
Release: alt2.1

Summary: Command line tool for parsing video download links
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%name-%version.tar.xz

Requires: libquvi-scripts

BuildRequires: lib%_name-scripts-devel >= %version
BuildRequires: libcurl-devel lua-devel

# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

%description
%name is a library for parsing video download links. It supports Youtube
and other similar video websites.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%check
#%%make check

%install
%make DESTDIR=%buildroot install

%files
%_libdir/%name.so.*
%doc NEWS README

%files devel
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_includedir/%_name/
%_man3dir/%name.*

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.1
- rebuild with new lua 5.3

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2
- reqs: libquvi-scripts (ALT #31354)

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus

