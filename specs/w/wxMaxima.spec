Name: wxMaxima
Version: 17.05.0
Release: alt2

Summary: GUI for the computer algebra system Maxima
License: GPL
Group: Sciences/Mathematics
URL: http://wxmaxima.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: wxmaxima-Version-%version.tar.gz
Source1: %name-16.xpm
Source2: %name-32.xpm
Source3: %name-48.xpm
Source5: wxmaxima-ru.po.bz2

ExcludeArch: aarch64

Requires: maxima

#BuildRequires: autoconf_2.60
BuildRequires: gcc-c++ libwxGTK3.0-devel libpango-devel libxml2-devel zlib-devel makeinfo

%description
wxMaxima is a wxWidgets GUI for the computer algebra system Maxima. 

Since it is written with wxWidgets, it runs on multiple platforms 
in native widget sets.  Most of maxima functions are accessible through 
menus, some have dialogs.  The input line has command history (up-key, 
down-key) and completion based on previous input (tab-key). 
wxMaxima provides 2d formated display of maxima output.


%prep
%setup -q -n wxmaxima-Version-%version

bzcat %SOURCE5 >locales/ru.po

%build

#set_automake_version 1.10
#set_autoconf_version 2.60

./bootstrap

#configure --disable-xmltest
%configure \
  --with-wx-config=/usr/bin/wx-config

%make

makeinfo info/wxmaxima.texi

%install
# icons
install -D -m644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -D -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -D -m644 %SOURCE3 %buildroot%_liconsdir/%name.xpm
%makeinstall

install -D -m644 wxmaxima.info %buildroot%_infodir/wxmaxima.info
%find_lang %name


%files -f %name.lang
%_bindir/wxmaxima
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm
%dir %_datadir/%name
%_datadir/%name/*

%{_datadir}/appdata/wxMaxima.appdata.xml
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/pixmaps/wxmaxima*
%{_datadir}/pixmaps/*wxma*svg
%{_datadir}/mime/packages/x-wxmathml.xml
%{_datadir}/mime/packages/x-wxmaxima-batch.xml
%{_docdir}/wxmaxima/
%{_mandir}/man1/wxmaxima.1*
%{_infodir}/wxmaxima.info*


%changelog
* Fri Sep 21 2018 Anton Midyukov <antohami@altlinux.org> 17.05.0-alt2
- rebuilt with libwxGTK3.0
- exclude aarch64

* Tue Jun 20 2017 Ilya Mashkin <oddity@altlinux.ru> 17.05.0-alt1
- 17.05.0

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 16.04.2-alt2
- Use upstream desktop file
- Package info file

* Sun Jul 03 2016 Ilya Mashkin <oddity@altlinux.ru> 16.04.2-alt1
- 16.04.2

* Tue Dec 01 2015 Ilya Mashkin <oddity@altlinux.ru> 15.08.2-alt1
- 15.08.2
- missing files added

* Mon Jan 12 2015 Ilya Mashkin <oddity@altlinux.ru> 14.12.1-alt1
- 14.12.1

* Tue Sep 30 2014 Ilya Mashkin <oddity@altlinux.ru> 14.09.0-alt1
- 14.09.0

* Sat Nov 15 2013 Ilya Mashkin <oddity@altlinux.ru> 13.04.2-alt1
- 13.04.2

* Sat Sep 14 2013 Ilya Mashkin <oddity@altlinux.ru> 13.04.1-alt1
- 13.04.1

* Fri Mar 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.09.0-alt1.1
- Rebuilt (ALT #28734)

* Sun Dec 16 2012 Ilya Mashkin <oddity@altlinux.ru> 12.09.0-alt1
- 12.09.0

* Sat Jun 02 2012 Ilya Mashkin <oddity@altlinux.ru> 12.04.0-alt1
- 12.04.0

* Tue Aug 16 2011 Ilya Mashkin <oddity@altlinux.ru> 11.08.0-alt1
- 11.08.0

* Thu Jun 16 2011 Ilya Mashkin <oddity@altlinux.ru> 11.04.0-alt1
- 11.04.0

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.6-alt0.M51.1
- Build for 5.1

* Thu Sep 23 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Sat Sep 04 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.5-alt2
- update Russian translation (Closes: #23838)

* Wed Jun 02 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.3-alt2
- fix icons locations

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.3-alt1
- 0.8.3
- fix desktop file

* Mon Apr 20 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.2-alt1
- Version 0.8.2

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Dec 09 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.0-alt1
- 0.8.0
- apply repocop patch

* Wed Sep 10 2008 Ilya Mashkin <oddity@altlinux.ru> 0.7.5-alt0.1
- 0.7.5

* Tue Jan 01 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.4-alt1
- Version 0.7.4.

* Sun Sep 23 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.3a-alt1
- Vaersion 0.7.3a.
- Remove Russian description and summary.
- Desktop menu entry changed to Science;Math;

* Sun May 06 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.2-alt1
- Version 0.7.2.

* Fri Dec 22 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.1-alt1
- Version 0.7.1. 

* Sat Oct 14 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.0-alt2
- Rebuilt with new toolchain.

* Fri Sep 01 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.7.0-alt1
- Version 0.7.0.

* Sun May 07 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.5-alt1
- Version 0.6.5.

* Sat Apr 01 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt3
- Desktop menu file.

* Tue Nov 29 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt2
- Requires: maxima.

* Sat Nov 26 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.4-alt1
- Maxima 5.9.2 comptibility fixes.

* Sun Nov 06 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.6.2-alt1
- Initial ALT Linux release.
