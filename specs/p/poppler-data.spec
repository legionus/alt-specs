
Name: poppler-data
Version: 0.4.9
Release: alt1

Group: Publishing
Summary: Common data for poppler
Url: http://poppler.freedesktop.org/
License: GPLv2 / MIT / ADOBE

BuildArch: noarch

Source: %name-%version.tar
Patch1: alt-pkgconfig.patch

BuildRequires(pre): rpm-build-ubt

%description
This package consists of encoding files for use with poppler.  The
encoding files are optional and poppler will automatically read them
if they are present.  When installed, the encoding files enables
poppler to correctly render CJK and Cyrrilic properly.  While poppler
is licensed under the GPL, these encoding files are copyright Adobe
and licensed much more strictly, and thus distributed separately.


%prep
%setup -q
%patch1 -p1
rm -rf poppler-data.pc
#__autoreconf


%build
%make_build prefix=%prefix

%install
%makeinstall


%files
%doc COPYING* README
%_datadir/poppler
%_datadir/pkgconfig/%name.pc

%changelog
* Fri Nov 02 2018 Sergey V Turchin <zerg@altlinux.org> 0.4.9-alt1
- new version

* Mon Apr 23 2018 Sergey V Turchin <zerg@altlinux.org> 0.4.8-alt1%ubt
- new version

* Fri Nov 14 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.7-alt1
- new version

* Wed Feb 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.4.6-alt1
- new version

* Mon Sep 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.5-alt1
- new version

* Mon Nov 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.4-alt1
- new version

* Thu Aug 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.3-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt0.M51.1
- built for M51

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Mon Oct 13 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- new version

* Thu Dec 27 2007 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- new version

* Thu Nov 08 2007 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- new version

* Tue Oct 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt2
- make noarch

* Mon Oct 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial specfile
