Name: nted
Version: 1.10.18
Release: alt3

Summary: A new musical score editor for Linux

License: GPL
Group: Sound
Url: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://vsr.informatik.tu-chemnitz.de/staff/jan/nted/sources/%name-%version.tar
Patch1: %name-%version-alt-gcc6.patch

# manually removed: kdesdk-misc 
# Automatically added by buildreq on Wed Mar 10 2010
BuildRequires: gcc-c++ libalsa-devel libgtk+2-devel xmlto yelp
BuildRequires: desktop-file-utils

%description
NtEd is a new musical score editor for Linux.

%prep
%setup
%patch1 -p2

%build
%add_optflags -fsigned-char -fpermissive
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Music \
	%buildroot%_desktopdir/nted.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	--add-category=GTK \
	%buildroot%_desktopdir/nted.desktop

%files -f %name.lang
%doc README
%_datadir/doc/%name/
%_bindir/%name
%_desktopdir/*
%_pixmapsdir/%name.png
%_datadir/%name/
%_man1dir/*

%changelog
* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.18-alt3
- fixed build on arm arches

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.18-alt2
- Updated build with gcc-6

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.18-alt1
- new version 1.10.18 (with rpmrb script)

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.17-alt1.qa3
- Fixed build with gcc 4.7

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.10.17-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for nted

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.10.17-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for nted

* Fri Jan 21 2011 Vitaly Lipatov <lav@altlinux.ru> 1.10.17-alt1
- new version 1.10.17 (with rpmrb script)

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- new version (1.9.18) import in git

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.24.1-alt1
- initial build for ALT Linux Sisyphus
