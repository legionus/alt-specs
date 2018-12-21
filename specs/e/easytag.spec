%define xdg_name org.gnome.EasyTAG
%def_enable nautilus

Name: easytag
Version: 2.4.3
Release: alt2

Summary: Audio files tag viewer/editor
Summary(ru_RU.UTF-8): Утилита для редактирования тегов звуковых файлов
Group: Sound
License: GPLv2+
Url: https://wiki.gnome.org/Apps/EasyTAG

Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires: rpm-build-gnome intltool gcc-c++
BuildRequires: xsltproc docbook-dtds docbook-style-xsl
BuildRequires: desktop-file-utils
BuildRequires: yelp-tools
BuildRequires: libappstream-glib-devel

BuildRequires: pkgconfig(gtk+-3.0) >= 3.2.1
BuildRequires: pkgconfig(ogg) >= 1.0 pkgconfig(vorbis) >= 1.0.1 pkgconfig(vorbisfile)
BuildRequires: pkgconfig(opus) >= 1.0 pkgconfig(opusfile)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(flac) >= 1.1.4
BuildRequires: pkgconfig(id3tag) id3lib-devel
BuildRequires: pkgconfig(taglib) >= 1.9.1
BuildRequires: pkgconfig(wavpack) >= 4.40
BuildRequires: pkgconfig(gio-2.0) >= 2.32.0
%{?_enable_nautilus:BuildRequires: libnautilus-devel}

%description
EasyTAG is a utility for viewing, editing and writing the tags of MP4, MP3,
MP2, FLAC, Ogg Opus, Ogg Speex, Ogg Vorbis, MusePack and Monkey's Audio files.

EasyTAG is an utility for viewing, editing easily and quickly the ID3v1 ,
ID3v2, APE and OGG tags of your audio files, using a nice GTK+2 user interface.

%description -l ru_RU.UTF-8
EasyTAG - это утилита для просмотра и редактирования тегов ID3v1 и ID3v2
файлов MP4, MP3 MP2, FLAC, Ogg Opus, Ogg Speex, Ogg Vorbis, MusePack и
Monkey's звуковых файлов.

%prep
%setup
#%patch -p1

%build
%autoreconf
%configure \
	%{?_enable_nautilus:--enable-nautilus-actions}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%check
%make check

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/metainfo/%name.appdata.xml

%if_enabled nautilus
%nautilus_extdir/*.so
%exclude %nautilus_extdir/*.la
%_datadir/metainfo/%name-nautilus.metainfo.xml
%endif

%_man1dir/%name.1*
%doc ChangeLog HACKING README THANKS TODO

%changelog
* Tue Feb 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.3-alt2
- Updated appstream files location.

* Tue Dec 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Mon Feb 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Tue Jan 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Sat Aug 29 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 2.2.6-alt1
- 2.2.6

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2
- build with gtk+-3
- update BR:

* Sun Nov 03 2013 Afanasov Dmitry <ender@altlinux.org> 2.1.8-alt2
- drop libmp4v2 buildreq

* Fri Nov 01 2013 Afanasov Dmitry <ender@altlinux.org> 2.1.8-alt1
- 2.1.8 release
  + try to update ru translation
  + use TagLib for MP4 tag editing

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.6-alt7.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 10 2009 Denis Koryavov <dkoryavov@altlinux.org> 2.1.6-alt7
- Really fix russian translation.

* Mon Sep 28 2009 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt6
- fix russian translation file.

* Sat Sep 26 2009 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt5
- fresh russian translation (closes: #21704)
- merge ru-translation and ru-settings patches into alt-ru patch.

* Tue Jun 09 2009 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt4
- fix icon visibility (closes: #20389)

* Tue Nov 18 2008 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt3
- update translation (fix #15959)
- fix desktop-mime-entry, update_menus repocop warnings 
  (rpm triggers)

* Wed Nov 12 2008 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt2
- fix iconsdir repocop warning

* Sun Nov 09 2008 Afanasov Dmitry <ender@altlinux.org> 2.1.6-alt1
- 2.1.6 release.
- update buildreq.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * desktop-mime-entry for easytag

* Tue May 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.1-alt1
- 2.1 release (should fix #11766).

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.2-alt1
- 2.0.2 release.
= Defaults from 2.0.1 are only applied if user locale is either
  ru_RU, be_BY or uk_UA.
- Enabled wavpack support.

* Fri Apr 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.1-alt1
- 2.0.1 release.
- Added sane defaults for /russian/ users as suggested by mike@ in #7567.

* Mon Feb 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt1
- 2.0 release.
- Fixed Summary.

* Wed Jan 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.99.13-alt2
- Fixed BuildRequires.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.99.13-alt1
- 1.99.13 release.
- Removed translation file as it merged upstream.
- Some spec cleanup.
- Removed old-style debian menu.

* Sat Jun 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.99.12-alt2
- Stricted BuildRequires and Requires to id3lib >= 3.8.3-alt3,
  fixes #9714.

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.99.12-alt1
- 1.99.12.
- Added libmpeg4ip-devel to BuildRequires, needed for FAAD.
- Added patch for configure (author needs a lobotomy).
- Corrected %%files icon section.

* Wed Dec 07 2005 Andrey Astafiev <andrei@altlinux.ru> 1.99.10-alt1
- 1.99.10

* Thu Jun 30 2005 Andrey Astafiev <andrei@altlinux.ru> 1.99.6-alt1
- 1.99.6

* Tue Jun 14 2005 Andrey Astafiev <andrei@altlinux.ru> 1.99.5-alt1
- 1.99.5

* Wed May 04 2005 Andrey Astafiev <andrei@altlinux.ru> 1.99.4-alt1
- 1.99.4

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 1.99.3-alt1
- 1.99.3

* Fri Nov 05 2004 Andrey Astafiev <andrei@altlinux.ru> 1.99.1-alt1
- 1.99.1
- First build with GTK+2 interface.

* Tue Jun 29 2004 Andrey Astafiev <andrei@altlinux.ru> 0.31-alt1
- 0.31

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 0.30-alt1
- 0.30

* Fri Sep 05 2003 Andrey Astafiev <andrei@altlinux.ru> 0.29-alt1
- 0.29

* Mon Jun 02 2003 Andrey Astafiev <andrei@altlinux.ru> 0.28-alt1
- 0.28

* Fri Mar 21 2003 Andrey Astafiev <andrei@altlinux.ru> 0.27-alt2
- rebuilt with id3lib-3.8.3

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 0.27-alt1
- 0.27

* Mon Jan 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.26-alt1
- 0.26
- rebuilt with id3lib-3.8.2

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.25-alt2
- 0.25
- rebuilt with id3lib-3.8.1

* Wed Sep 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.24-alt1
- 0.24, gcc-3.2 used

* Wed Aug 21 2002 Andrey Astafiev <andrei@altlinux.ru> 0.23-alt1
- 0.23

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 0.22-alt1.1
- rebuild with new vorbis

* Thu Jul 18 2002 Andrey Astafiev <andrei@altlinux.ru> 0.22-alt1
- 0.22

* Tue May 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.21-alt1
- 0.21 
- build with id3lib-3.8pre2.1 

* Mon May 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.20-alt1
- 0.20

* Thu Apr 04 2002 Andrey Astafiev <andrei@altlinux.ru> 0.18-alt1
- 0.18

* Mon Mar 11 2002 Andrey Astafiev <andrei@altlinux.ru> 0.17-alt1
- 0.17

* Tue Feb 26 2002 Andrey Astafiev <andrei@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Wed Feb 06 2002 Andrey Astafiev <andrei@altlinux.ru> 0.16-alt1
- 0.16

* Wed Dec 26 2001 Andrey Astafiev <andrei@altlinux.ru> 0.15.6-alt1
- 0.15.6

* Fri Dec 21 2001 Andrey Astafiev <andrei@altlinux.ru> 0.15.5-alt1
- 0.15.5

* Tue Sep 25 2001 Andrey Astafiev <andrei@altlinux.ru> 0.15.1-alt1
- Autoconf and automake are used to make package.
- Updated russian translations.
- Fixed tooltips.

* Wed Aug 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.15-alt2
- Fixed build.
- Used %%find_lang macro for translations.
- Added icons and menu entry.
- Set group to Sound.

* Mon Aug 20 2001 Andrey Astafiev <andrei@altlinux.ru>
- First version of RPM package.
