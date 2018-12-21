Name: freedink-dfarc
Version: 3.12
Release: alt2
Summary: Frontend and .dmod installer for GNU FreeDink

Group: Games/Adventure
License: GPLv3+
Url: http://www.freedink.org/
Source0: ftp://ftp.gnu.org/gnu/freedink/dfarc-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

BuildRequires(pre): rpm-build-xdg
BuildRequires: bzlib-devel gcc-c++ intltool libwxGTK3.0-devel xdg-utils

%description
DFArc2 makes it easy to play and manage the Dink Smallwood game and
it's numerous Dink Modules (or D-Mods).

%prep
%setup -n dfarc-%version
sed -i 's/BZ2_compressBlock/BZ2_bzDecompress/' configure.ac

%build
%autoreconf
%configure
%make

%install
%makeinstall
%find_lang dfarc
install -D share/pixmaps/dfarc.png %buildroot%_niconsdir/dfarc.png
install -D share/%name.desktop %buildroot%_desktopdir/%name.desktop
install -D share/freedink-mime.xml %buildroot%_xdgmimedir/packages/freedink-mime.xml

%files -f dfarc.lang
%doc AUTHORS COPYING NEWS README THANKS TODO TRANSLATIONS.txt ChangeLog doc
%_bindir/*
%_niconsdir/*
%_xdgmimedir/packages/*
%_desktopdir/*
%_datadir/pixmaps/*
%_mandir/man1/*

%changelog
* Mon Aug 27 2018 Anton Midyukov <antohami@altlinux.org> 3.12-alt2
- rebuilt with wxGTK3.0

* Sat Jun 02 2018 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1.3
- rebuild with rebuilt wxGTK3.1

* Mon Jul 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt1.2
- Rebuilt with gcc5

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt1.1
- Rebuilt with new wxGTK3.1

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 3.12-alt1
- Autobuild version bump to 3.12
- Update buildreq

* Mon Dec 17 2012 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10

* Mon May 24 2010 Fr. Br. George <george@altlinux.ru> 3.6-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Initial build from FC

* Fri Sep 18 2009 Sylvain Beucler <beuc@beuc.net> - 3.4-1
- New upstream release

* Wed Sep 16 2009 Sylvain Beucler <beuc@beuc.net> - 3.2.4-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Sylvain Beucler <beuc@beuc.net> - 3.2.3-1
- New upstream release

* Wed Jun 03 2009 Sylvain Beucler <beuc@beuc.net> - 3.2.2-1
- New upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 3.2.1-2
- Fix update-mime-database call (was conditional due to typo)
- Fix macros in comments
- Tidy changelog

* Tue Sep 23 2008 Sylvain Beucler <beuc@beuc.net> - 3.2.1-1
- New upstream release
- Fix source URI
- Clarify wxGlade upstream developer-only dependency
- Use 'install -p' to preserve timestamps
- Validate desktop files> * Desktop file
- Rebuild MIME cache after installing desktop files
- Add ChangeLog to the docs
- Don't own _datadir/icons/hicolor directories

* Sun Sep 20 2008 Sylvain Beucler <beuc@beuc.net> - 3.2-1
- New upstream release

* Thu Aug 28 2008 Sylvain Beucler <beuc@beuc.net> 3.0-1
- Initial package
