# We don't build with Gnome support by default to avoid a GConf dependency.
# If you would like to set the Gnome background image with Viewnior, rebuild
# the srpm with:
#   rpmbuild --rebuild viewnior-*-src.rpm --with gnome
%def_without gnome

Name: viewnior
Version: 1.6
Release: alt2

Summary: Elegant image viewer
License: GPLv3+
Group: Graphics

Url: http://xsisqox.github.com/Viewnior
Source0: %name-%version.tar.gz
Source1: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Apr 13 2014
# optimized out: fontconfig fontconfig-devel glib2-devel gnu-config libatk-devel libcairo-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server perl-Encode perl-XML-Parser pkg-config
BuildRequires: gcc-c++ intltool libexiv2-devel libgtk+2-devel

%if_with gnome
BuildRequires: libGConf-devel
%endif

%description
Viewnior is an image viewer program. Created to be simple, fast
and elegant.  It's minimalistic interface provides more screen
space for your images. Among its features are:
* Fullscreen & Slideshow
* Rotate, flip, save, delete images
* Animation support
* Browse only selected images
* Navigation window
* Simple interface
* Configurable mouse actions

%prep
%setup -n Viewnior-%name-%version
# fix spurious executable perms
chmod 644 AUTHORS COPYING NEWS README TODO src/*

%build
%autoreconf
%configure \
%if_with gnome
   --enable-wallpaper
%endif
# this line intentionally left in
%make_build V=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/%name
%_man1dir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/%name/

%changelog
* Mon Oct 23 2017 Michael Shigorin <mike@altlinux.org> 1.6-alt2
- rebuilt against current libexiv2

* Fri Dec 18 2015 Michael Shigorin <mike@altlinux.org> 1.6-alt1
- new version (watch file uupdate)

* Tue Jun 30 2015 Michael Shigorin <mike@altlinux.org> 1.5-alt1.2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Sun May 03 2015 Michael Shigorin <mike@altlinux.org> 1.5-alt1
- new version (watch file uupdate)
- NB: source hosted on github had to be repackaged by hand :-\

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.1
- NMU: fixed watch file

* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 1.4-alt1
- added watch file
- new version (watch file uupdate)
- NB: source hosted on dropbox had to be downloaded by hand :-/

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- 1.3

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 1.1-alt1
- 1.1 (thanks force@)

* Fri Apr 02 2010 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- built for ALT Linux
  + based on Fedora package
  + *heavily* cleaned up spec

* Wed Mar 31 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0-1
- Update to 1.0

* Tue Feb 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-2
- Add patch to fix DSO linking (#565018)
- Switch to %%bcond macro

* Mon Sep 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-1
- Update to 0.7

* Sat Sep 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6-2
- Spec file cleanups from review.

* Mon Aug 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6-1
- Initial package
