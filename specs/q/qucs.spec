Name: qucs
Version: 0.0.19
Release: alt2
Summary: Circuit simulator
License: GPL
Group: Education
Url: http://qucs.sourceforge.net/

Source0: https://sourceforge.net/projects/%name/files/%name/%version/%name-%version.tar.gz
Source1: %name.desktop
Source2: qucs-tango-icons.tar.bz2
Source3: qucs-icons.tar.bz2
Patch: qucs-0.0.17-norecode.patch
#Patch1: %name-%version-alt-build.patch

# WTF libqt4-devel
BuildRequires: libqt4-devel
BuildRequires: mot-adms
BuildRequires: chrpath

# Automatically added by buildreq on Tue Jan 14 2014
# optimized out: fontconfig libICE-devel libSM-devel libX11-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libstdc++-devel xorg-xproto-devel
BuildRequires: flex gcc-c++ gperf imake xorg-cf-files

Requires: %name-data = %version-%release

%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%package data
Group:	 Education
Summary: Data files for Qucs, a circuit simulator
Buildarch: noarch

%description data
Data files  for Qucs, a circuit simulator.

%package -n libqucs
Group:	 Education
Summary: Supplemental library for Qucs, a circuit simulator

%description -n libqucs
Supplemental library for Qucs, a circuit simulator.

%package -n libqucs-devel
Group:	Development/C++
Summary: Development environment for Qucs, a circuit simulator

%description -n libqucs-devel
Development environment for Qucs, a circuit simulator.

%prep
%setup
tar -xjf %SOURCE2 -C qucs
##sed -i '\@<tr1/complex>@d' qucs-core/configure
##patch -p1
#patch1 -p2

%build
./bootstrap
%configure --disable-doc
%make_build RCC=rcc-qt4

%install
mkdir -p %buildroot%_defaultdocdir/%name-%version

%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_iconsdir
tar -xjf %SOURCE3 -C %buildroot%_iconsdir

for l in $(find %buildroot%_datadir/%name/lang -name \*.qm); do
    echo -n $l | sed 's,.*_\(.*\)\.qm,%%lang\(\1\) ,'
    echo $l | sed "s,%buildroot,,"
done > %name.lang

chrpath -d %buildroot%_bindir/qucsconv
chrpath -d %buildroot%_bindir/qucsator

%files -f %name.lang
%doc NEWS.md README.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%files data
%dir %_datadir/%name
%dir %_datadir/%name/lang
# XXX GONE?
##_datadir/%name/bitmaps
%_datadir/%name/library
%_datadir/%name/tline
%_datadir/%name/octave
%dir %_datadir/%name/docs
#_datadir/%name/docs/???*
%_datadir/%name-core
%_datadir/%name/examples
%_datadir/%name/docs/en
%lang(de) %_datadir/%name/docs/de
%lang(es) %_datadir/%name/docs/es
%lang(fr) %_datadir/%name/docs/fr
%lang(ru) %_datadir/%name/docs/ru
%lang(uk) %_datadir/%name/docs/uk
%lang(cs) %_datadir/%name/docs/cs
%lang(pt) %_datadir/%name/docs/pt

%files -n libqucs
%_libdir/*.so.*

%files -n libqucs-devel
%_libdir/*.so
%_includedir/qucs-core

%changelog
* Tue Aug 07 2018 Vladislav Zavjalov <slazav@altlinux.org> 0.0.19-alt2
- github/master snapshot 2018-08-07 (Closes: 35217)

* Sun Aug 06 2017 Anton Midyukov <antohami@altlinux.org> 0.0.19-alt1
- New version 0.0.19

* Thu Jul 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.18-alt2
- Fixed build with new toolchain

* Tue Sep 30 2014 Fr. Br. George <george@altlinux.ru> 0.0.18-alt1
- Autobuild version bump to 0.0.18
- Separate lib packages
- Do not build 3d-party projects

* Mon Jan 13 2014 Fr. Br. George <george@altlinux.ru> 0.0.17-alt1
- Autobuild version bump to 0.0.17
- Drop inactual patch
- Patch out UTF->UTF recoding

* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 0.0.16-alt3
- QnD fix qucsdigi (Closes: 28560)

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.16-alt2
- Fix build on i586

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 0.0.16-alt1
- Autobuild version bump to 0.0.16
- Switch to gcc3.4 to avoid C++ error messages

* Thu Jul 01 2010 Fr. Br. George <george@altlinux.ru> 0.0.15-alt1.1
- Rebuild for Sisyphus

* Sun May 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.0.15-alt1
- 0.0.15

* Wed Jan 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.13-alt1
- 0.0.13

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.12-alt1
- 0.0.12

* Wed Jun 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.11-alt1
- initial build
