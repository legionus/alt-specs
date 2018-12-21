Name:		viking
Version:        1.6.0
Release:	alt1

Summary:	GPS data editor and analyzer

Group:		Sciences/Geosciences
License:	GPLv2
URL:		http://sourceforge.net/projects/viking/
Source0:	%{name}-%{version}.tar

BuildRequires: libcurl-devel libexpat-devel libgps-devel perl-XML-Parser intltool zlib-devel
BuildRequires: gnome-doc-utils libgtk+2-devel gtk-doc libgexiv2-devel bzlib-devel libmagic-devel
BuildRequires: libsqlite3-devel

Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

%description
Viking is a free/open source program to manage GPS data. You can import and
plot tracks and waypoints, show Terraserver maps under it, add coordinate
lines, make new tracks and waypoints, hide different things, etc. It is written
in C with the GTK+ 2.

%prep
%setup -q

%build
ln -s /usr/share/gnome-doc-utils/gnome-doc-utils.make
%autoreconf
%configure --disable-mapnik
%make

%install
%makeinstall
find %buildroot/usr/share/gnome/help/viking/ -type l -delete

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/
%{_bindir}/viking
/usr/share/applications/viking.desktop
/usr/share/icons/hicolor/48x48/apps/viking.png
/usr/share/gnome/help/viking
/usr/share/omf/viking
/usr/share/viking/


%changelog
* Mon Jun 01 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Thu Jul 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt2
- build fixed

* Tue Jun 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt1
- new version

* Wed Mar 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- new version
- build fixed

* Wed Jun 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.93-alt1
- new version

* Mon Jun 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.8-alt1
- new version
- unworking Google maps removed

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.6-alt1
- new version

* Fri Apr 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.4-alt1
- first build for Sisyphus

* Thu Feb 21 2008 Michael A. Peters <mpeters@mac.com> - 0.9.3.20080220-1
- change License field from GPL to GPLv2
- BR gpsd-devel
- BR gettext perl(XML::Parser) - needed for intltool
- use find_land macro to package mo files

* Sun Sep  4 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9.2-1
- Update to upstream version 0.9.2.

* Sun Sep  2 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9.1-1
- Update to upstream version 0.9.1.

* Fri Jul 13 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.9-1
- Update to upstream version 0.9.

* Thu May 18 2007 Quy Tonthat <qtonthat@gmail.com>
- Added curl-devel to BuildRequires list.

* Thu May 15 2007 Guilhem Bonnefille <guilhem.bonnefille> - 0.1.3-1
- Update to upstream version 0.1.3.

* Wed Feb 14 2007 Michael A. Peters <mpeters@mac.com> - 0.1.2-1
- Initial Fedora style spec file.
