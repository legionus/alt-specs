# vim: set ft=spec: -*- spec -*-
%def_with kde
%def_disable sound
%define program_prefix rss-

Name: rss_glx
Version: 0.9.1
Release: alt8

Summary: Really Slick Screensavers
License: GPL-1.0-only
Group: Graphical desktop/Other

Url: http://rss-glx.sourceforge.net
Source: %name-%version-%release.tar
Patch0: rss-glx-0.9.1-debian-configure.patch
Patch1: rss-glx-0.9.1-debian-pixelcity-cpp.patch
Patch2: rss-glx-0.9.1-debian-readme.patch
Packager: Michael Shigorin <mike@altlinux.org>
# git://git.altlinux.org/people/mike/packages/rss_glx.git

BuildRequires(pre): rpm-build-xscreensaver
%{?_with_kde:BuildRequires(pre): kde-common-devel}

# Automatically added by buildreq on Sun Nov 09 2008 (-bi)
BuildRequires: bzlib-devel gcc-c++ libImageMagick-devel libXt-devel libglew-devel

%description
The Really Slick Screensavers GLX port.
A collection of fancy OpenGL screensavers ported from Windows to X
for use with xscreensaver.

%package -n xscreensaver-hacks-%name
Summary: Really Slick Screensavers - xscreensaver modules
Group: Graphical desktop/Other
Requires: %name = %version-%release
PreReq: xscreensaver >= 4.09-alt1
Provides: xscreensaver-hack

%description -n xscreensaver-hacks-%name
The Really Slick Screensavers GLX port.
A collection of fancy OpenGL screensavers ported from Windows to X
for use with xscreensaver.

This package contains xscreensaver modules configs.

%package kde
Summary: Really Slick Screensavers - KDE modules
Group: Graphical desktop/KDE
Requires: %name = %version-%release
PreReq: kde-common

%description kde
The Really Slick Screensavers GLX port.
A collection of fancy OpenGL screensavers ported from Windows to X
for use with xscreensaver.

This package contains KDE menu entries.

%prep
%setup -n %name-%version-%release
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	--program-prefix=%program_prefix \
	--with-configdir=%xss_conf_dir \
%if_with kde
	--with-kdessconfigdir=%_Kapplnk/System/ScreenSavers \
%endif
	%{subst_enable sound} \
	#
%make_build

# Get xscreensaver config
grep '^\$screensavers' utils/rss-glx_install.pl |
	sed -e 's,^\$screensavers-.*= '\''\(.*\)'\'';,\1,; s,\\\(.\),\1,g; s,\([A-Za-z0-9_-]\+\) --root,%program_prefix\1 --root,' > %name.xss
sed -i 's,%{program_prefix}matrixview --root,& -i %_datadir/%name-matrixvew,' %name.xss

# Fixup KDE desktop files
find . -name '*.desktop' -print0 |
	xargs -r0 sed -i 's,^\(Exec=\),\1%program_prefix,; s,^\(Exec=\)\(%program_prefix\)\(kxs\(config\|run\)\) ,\1\3 \2,;' --

%install
mkdir -p %buildroot%xss_ad_dir
%makeinstall_std
rm -f %buildroot%_bindir/*_install.pl

for i in %buildroot%xss_conf_dir/*.xml; do
	d="${i%%/*}"
	f="${i##*/}"
	mv "$i" "$d/%program_prefix$f"
done

mkdir -p %buildroot%_desktopdir/screensavers

install -pm644 %name.xss %buildroot%xss_ad_dir/%name.xss

%files
%doc COPYING INSTALL README
%_bindir/*
%_man1dir/*

%files -n xscreensaver-hacks-%name
%doc README.xscreensaver
%config %xss_ad_dir/%name.xss
%config %xss_conf_dir/*.xml

%if_with kde
%files kde
%_Kapplnk/System/ScreenSavers/*.desktop
%endif

%changelog
* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt8
- Rebuilt for ImageMagick.

* Wed Aug 23 2017 Michael Shigorin <mike@altlinux.org> 0.9.1-alt7
- replaced our patch with debian's one (adding two more while at that)
  to fix pixelcity FTBFS

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 0.9.1-alt6
- Rebuilt for ImageMagick.

* Fri Aug 04 2017 Michael Shigorin <mike@altlinux.org> 0.9.1-alt5
- BOOTSTRAP: introduced kde knob (on by default),
  sound knob (off by default just as it was)

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.9.1-alt4.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.9.1-alt4
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.9.1-alt3
- Rebuild with new libImageMagick

* Thu Jun 14 2012 Anton Farygin <rider@altlinux.ru> 0.9.1-alt2
- Rebuild with new libImageMagick

* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1
- Fixed build

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- 0.9.1
  + added port of Pixel City, originally by Shamus Young
  + replaced methods deprecated by ImageMagick
- dropped gnome subpackage (following upstream)

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.9.0-alt4
- rebuild with new ImageMagick

* Fri Apr 23 2010 Anton Farygin <rider@altlinux.ru> 0.9.0-alt3
- rebuild with new ImageMagick

* Tue Dec 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.0-alt2
- GNOME integration files added

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Fri Mar 20 2009 Michael Shigorin <mike@altlinux.org> 0.8.2-alt2
- adopted an orphan
- fixed build with a patch from http://bugs.gentoo.org/213643
- applied hyperspace gentoo patch

* Sun Nov 09 2008 Sir Raorn <raorn@altlinux.ru> 0.8.2-alt1
- [0.8.2]
- Disabled sound in skyrocket due to OpenAL breakage

* Thu Apr 17 2008 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt2
- Add -i %%_datadir/%%name-matrixvew to default matrixview
  options (closes: #12934)

* Wed Oct 11 2006 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt1
- [0.8.1]
- Added KDE desktop files (-kde subpackage)
- Prefix all binaries with "rss-" (closes: #4608)
- Generate xscreensaver AD module from rss-glx_install.pl
- xscreensaver-hackes should PreReq xscreensaver package
- Updated build dependencies
- New hacks:
 + colorfire
 + hyperspace
 + matrixview
 + spirographx

* Fri Aug 12 2005 Sir Raorn <raorn@altlinux.ru> 0.7.4-alt3.1.2
- Another rebuild with another new xscreensaver

* Tue Aug 02 2005 Sir Raorn <raorn@altlinux.ru> 0.7.4-alt3.1.1
- Rebuilt with new xscreensaver

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.4-alt3.1
- Rebuilt with libstdc++.so.6.

* Wed Feb 11 2004 Sir Raorn <raorn@altlinux.ru> 0.7.4-alt3
- Fix gcc 3.3 build

* Tue Apr 15 2003 Sir Raorn <raorn@altlinux.ru> 0.7.4-alt2
- Rebuilt with new xscreensaver
- Split to rss_glx and xscreensaver-hacks-rss_glx

* Thu Apr 03 2003 Alexander Bokovoy <ab@altlinux.ru> 0.7.4-alt1
- Initial build for Sisyphus

