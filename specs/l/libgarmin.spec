%set_automake_version 1.11

%define svn_ver svn20081215

Name: libgarmin
Version: 0.1.0
Release: alt2.1
Summary: Libgarmin is an open source (GPLv2) for Garmin image format maps.
License: GPL-2.0-only
Group: Sciences/Geosciences
Url: http://libgarmin.sourceforge.net
Source: %name-%svn_ver.tar.bz2

# Automatically added by buildreq on Mon Dec 15 2008
BuildRequires: libGConf-devel rpm-build-java rpm-macros-fillup rpm-macros-xmms subversion

%description
Garmin is a leader in the gps navigation, so learn from
the best. Open source community is moving towards.
www.openstreetmap.org data. Understanding Garmin's format
will allow creation of Garmin compatible maps from OSM data
and creation/design of a new map format for OSM data.

#%package devel
#Summary: Libraries and headers needed for developing with SynCE
#Group: Development/C
#Requires: %name = %version
#
#%description devel
#Libraries and headers needed for developing with SynCE

%prep
%setup -q -n %name
svn upgrade

%build
./autosh.sh
%configure
%make

%install
%makeinstall
%__mkdir_p %buildroot%_docdir
%__mv %buildroot%_datadir/%name %buildroot%_docdir/

#%post
#%post_ldconfig

#%postun
#%postun_ldconfig

%files
%dir %_docdir/%name
%_docdir/%name/*
%_bindir/*
%_includedir/*
%_libdir/*.a
%_pkgconfigdir/*
#%_libdir/*.so.*

#%files devel
#%_includedir/*
#%_libdir/*.so
#%_pkgconfigdir/*
#%_man3dir/*
#%_man7dir/*

%changelog
* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.1
- Fixed build

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2
- Fix build with new Subversion

* Mon Dec 15 2008 Grigory Milev <week@altlinux.ru> 0.1.0-alt1
- Initital build for ALT Linux
