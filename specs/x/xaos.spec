# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/msgmerge /usr/bin/nasm libICE-devel libSM-devel pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) 
# END SourceDeps(oneline)

Name: xaos
Version: 3.6
Release: alt2
Summary: A real-time fractal zoomer
Serial: 1

License: GPL

Group: Sciences/Mathematics
Url: http://xaos.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://prdownloads.sourceforge.net/xaos/xaos-%version.tar.gz
Source1: xaos.png
Source10: %name.16.xpm.bz2
Source11: %name.32.xpm.bz2
Source12: %name.48.xpm.bz2

Patch1: xaos-3.6-upstream-desktop.patch
Patch2: xaos-3.6-upstream-fortify.patch
Patch3: xaos-3.6-upstream-gcc.patch
Patch4: xaos-3.6-upstream-parallel-build.patch
Patch5: xaos-3.6-upstream-qt5.patch

Provides : XaoS = %version, %name-aalib = %version
Obsoletes: XaoS, %name-aalib

BuildRequires: aalib-devel imake libICE-devel libXxf86dga-devel zlib-devel  gettext
BuildRequires: libXxf86vm-devel libgpm-devel libXext-devel libX11-devel libXt-devel libgsl-devel
BuildRequires: libncurses-devel libpng12-devel libslang-devel nasm xorg-cf-files libgtk+2-devel libXext-devel
BuildRequires:	texlive-base-bin
# explicitly added texinfo for info files
BuildRequires: texinfo


%description
XaoS is a real-time fractal zoomer. It is highly optimized. It features an
advanced help system and nice tutorial about a lot different fractals.

This package holds the binary that runs with X11.

%prep
%setup -q -n xaos-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# disable stripping binaries when installing
sed -i 's| -s | |' Makefile.in
sed -i 's,\$x_includes/X11/extensions/XShm.h,/usr/include/X11/extensions/XShm.h,' configure.in configure

%build
%ifarch %ix86 x86_64
%define long_double --with-long-double
%endif
%configure \
   --with-x11-driver \
    --with-gsl=yes \
    --with-sffe=yes \
    --with-gtk-driver=yes \
    --with-aa-driver=yes \
    --with-pthread=yes \
    %{long_double}
# due to the buggy configure it has the opposite effect
#    --with-png=yes \
%make

%install
mkdir -p %buildroot%_infodir
%makeinstall LOCALEDIR=%buildroot%_datadir/locale

pushd doc
make xaos.dvi
dvipdfm xaos.dvi
popd
pushd help
make html
popd

%if_with aalib
install -m755 xaos-aalib %buildroot%_bindir
%endif

%if_with svgalib
install -m755 xaos-svgalib %buildroot%_bindir
%endif

install -m644 help/xaos.hlp %buildroot%_datadir/XaoS/catalogs

# menu entry
sed -i 's:Exec=xaos:Exec=xaos -driver "GTK+ Driver":' src/xdg/xaos.desktop
echo 'Encoding=UTF-8' >> src/xdg/xaos.desktop
echo 'Version=1.0' >> src/xdg/xaos.desktop

install -m755 -d %buildroot%_desktopdir/
install -m644 src/xdg/xaos.desktop %buildroot%_desktopdir/%name.desktop

# icon
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir
bzcat %SOURCE10 > %buildroot%_miconsdir/%name.xpm
bzcat %SOURCE11 > %buildroot%_niconsdir/%name.xpm
bzcat %SOURCE12 > %buildroot%_liconsdir/%name.xpm
cp %SOURCE1 %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%doc README COPYING TODO ChangeLog NEWS
%doc AUTHORS doc/xaos.pdf

%_bindir/%name
%_datadir/XaoS
%_mandir/man6/*
%_infodir/*.info*
%_desktopdir/%name.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_liconsdir/%name.png

%changelog
* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.6-alt2
- Rebuilt with new libgsl.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.6-alt1.1.1
- NMU: added BR: texinfo

* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.6-alt1.1
- Built with libgsl90 instead of libgsl

* Sat Mar 01 2014 Ilya Mashkin <oddity@altlinux.ru> 1:3.6-alt1
- 3.6

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.5-alt3
- bugfix release

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.5-alt2
- resurrected from orphaned

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.5-alt1.qa1
- NMU: converted menu to desktop file

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1:3.5-alt1
- 3.5
- fix icons locations

* Fri Feb 28 2009 Ilya Mashkin <oddity@altlinux.ru> 1:3.4-alt1
- 3.4

* Tue Mar 18 2008 Alex Karpov <karpov@altlinux.ru> 1:3.3-alt1
- 3.3

* Mon Jan 15 2007 Alex Karpov <karpov@altlinux.ru> 1:3.2.3-alt1
- picked from orphaned
- new version

* Thu Jan 20 2005 Stanislav Ievlev <inger@altlinux.org> 1:3.1-alt4
- fix building with gcc3.4

* Thu Apr 22 2004 Stanislav Ievlev <inger@altlinux.org> 1:3.1-alt3
- change internal font to font with russian letters

* Wed Apr 21 2004 Stanislav Ievlev <inger@altlinux.org> 1:3.1-alt2
- remove aalib subpackage
- added russian translation by Valentina Vaneeva

* Tue May 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1:3.1-alt1
- 3.1 final

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1pre5-alt1
- pre5
- sync with MDK

* Fri Oct 12 2001 Stanislav Ievlev <inger@altlinux.ru> 3.1pre1-ipl18mdk
- spec cleanup.
- rebuild with new libpng.

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-16mdk
- some forgotten `obsoletes' tags

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-15mdk
- change name to xaos (e.g. uppercase names suck)

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-14mdk
- fixed missing install_info

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-13mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.1pre1-12mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-11mdk
- rebuild for buggy %% clean_menus

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-10mdk
- BM
- macros for menu/icons

* Mon Jul 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-9mdk
- macros

* Fri May 26 2000 Adam Lebsack <adam@mandrakesoft.com> 3.1pre1-8mdk
- added ppc ExclusiveArch

* Tue May  9 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-7mdk
- added exclusivearch with the help of S. Van der Eijk

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-6mdk
- added 32x32 icons, fixed hardcoded path in menu entries
- added lacking [ $1 = 0 ] in postun script

* Fri Apr 14 2000 David BAUDENS <baudens@mandrakesoft.com> 3.1pre1-5mdk
- Don't own shared directiries
- Use $RPM_OPT_FLAGS, don't build for i686 when I say i586

* Fri Apr 14 2000 David BAUDENS <baudens@mandrakesoft.com> 3.1pre1-4mdk
- Fix group

* Mon Apr 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-3mdk
- added icon

* Mon Mar 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-2mdk
- add menu entry

* Sat Mar 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1pre1-1mdk
- 3.1pre1
- holy patch to remove crash when invoking help
