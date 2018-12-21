Name: texmaker
Version: 5.0.2
Release: alt1

Summary: free cross-platform LaTeX editor with a Qt interface
License: GPLv2
Group: Publishing
Url: http://www.xm1math.net/texmaker/index.html

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Thu Apr 24 2008
BuildRequires: fontconfig gcc-c++ qt5-base-devel qt5-tools-devel libpoppler-devel libpoppler-qt5-devel qt5-script-devel

%description
Texmaker is a LaTeX editor that integrates many tools
needed to develop documents with LaTeX.

%prep
%setup

%build
/usr/share/qt5/bin/qmake -unix PREFIX=%prefix %name.pro
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_datadir/metainfo/%name.appdata.xml


%changelog
* Mon Aug 21 2017 Ilya Mashkin <oddity@altlinux.ru> 5.0.2-alt1
- 5.0.2

* Sun Jul 16 2017 Ilya Mashkin <oddity@altlinux.ru> 5.0-alt1
- 5.0

* Thu Nov 05 2015 Ilya Mashkin <oddity@altlinux.ru> 4.5-alt1
- 4.5

* Tue Dec 09 2014 Ilya Mashkin <oddity@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Sat Aug 02 2014 Ilya Mashkin <oddity@altlinux.ru> 4.3-alt1
- 4.3

* Sun May 04 2014 Ilya Mashkin <oddity@altlinux.ru> 4.2-alt1
- 4.2

* Sun Jan 05 2014 Ilya Mashkin <oddity@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Wed Oct 30 2013 Ilya Mashkin <oddity@altlinux.ru> 4.1-alt1
- 4.1

* Sat Aug 31 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Sun Aug 04 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Wed May 15 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Sat Mar 16 2013 Ilya Mashkin <oddity@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Tue Nov 06 2012 Ilya Mashkin <oddity@altlinux.ru> 3.5.2-alt1
- 3.5.2

* Thu Jul 26 2012 Ilya Mashkin <oddity@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Sat Jun 02 2012 Ilya Mashkin <oddity@altlinux.ru> 3.3.4-alt1
- 3.3.4

* Sun Apr 08 2012 Ilya Mashkin <oddity@altlinux.ru> 3.3.3-alt1
- 3.3.3

* Thu Mar 01 2012 Ilya Mashkin <oddity@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Sun Feb 12 2012 Ilya Mashkin <oddity@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Mon Jan 02 2012 Ilya Mashkin <oddity@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sun Dec 25 2011 Ilya Mashkin <oddity@altlinux.ru> 3.2-alt1
- 3.2

* Mon Aug 15 2011 Ilya Mashkin <oddity@altlinux.ru> 3.1-alt1
- 3.1

* Thu May 05 2011 Ilya Mashkin <oddity@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Thu Apr 21 2011 Ilya Mashkin <oddity@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Sat Apr 16 2011 Ilya Mashkin <oddity@altlinux.ru> 3.0-alt1
- 3.0

* Tue Mar 15 2011 Ilya Mashkin <oddity@altlinux.ru> 2.3-alt1
- 2.3

* Tue Feb 15 2011 Ilya Mashkin <oddity@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Feb 07 2011 Ilya Mashkin <oddity@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Dec 01 2010 Ilya Mashkin <oddity@altlinux.ru> 2.1-alt1
- 2.1

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.7.1-alt1
- new version

* Thu Apr 24 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.7-alt1
- resurect from orphaned

* Sat Dec 03 2005 Alex V. Myltsev <avm@altlinux.ru> 1.2.1-alt1
- Initial build for ALT Linux.

