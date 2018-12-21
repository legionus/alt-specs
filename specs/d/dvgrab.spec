Name: dvgrab
Version: 3.5
Release: alt3

Summary: A program to copy Digital Video data from a DV camcorder
Group: Video
License: GPL

Url: http://www.kinodv.org
# VCS: https://github.com/ddennedy/dvgrab.git
# commit e46042e0c7b3523b6854ee547b0534e8310b7460
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ libiec61883-devel libavc1394-devel libjpeg-devel libdv-devel

Summary(ru_RU.UTF-8): Программа для копирования видео с DV-камеры

%description
dvgrab copies digital video data from a DV camcorder.

%description -l ru_RU.UTF-8
dvgrab копирует цифровое видео с DV-видеокамеры на жёсткий диск
или другой носитель.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Wed Jun 20 2018 Anton Farygin <rider@altlinux.ru> 3.5-alt3
- disabled quicktime support

* Tue Feb 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.5-alt2
- updated from new source (https://github.com/ddennedy/dvgrab.git)

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 3.5-alt1.qa2
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 3.5-alt1
- 3.5
- patch merged upstream

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 3.4-alt2
- fixed FTBFS with gcc-4.4

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 3.4-alt1
- 3.4

* Fri Aug 15 2008 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- 3.2
- removed patches (applied upstream)
- buildreq
- removed optional libquicktime-devel (no reason not to use)

* Sun Dec 24 2006 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- 2.1 (fixes for Stopmotion)
- added optional quicktime support, enabled by default
- FIXME/TODO: apply patch to enable ffmpeg support

* Wed Dec 20 2006 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- align arches (x86_64 had 1.8 still)
- --as-needed patch sent upstream

* Sat Nov 11 2006 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- 2.0
- updated Url:
- added Packager:
- build requires libiec61883 now
- fixed build with -Wl,--as-needed (patch1)
- built against libquicktimehv (thanks viy@ for a hint!)

* Mon Jun 26 2006 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt2
- fix build with new libquicktime-devel

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- NMU: new version, rebuild with libraw1394.so.5

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.7-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Dec 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.7-alt1
- 1.7

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5-alt1.1
- rebuild against libdv-0.102

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5-alt1
- 1.5

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4-alt1
- new version.

* Mon Feb 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2-alt1
- First build for Sisyphus.

