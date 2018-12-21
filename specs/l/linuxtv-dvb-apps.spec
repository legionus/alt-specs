Name: linuxtv-dvb-apps
Version: 1.1.1
Release: alt2.2

Summary: LinuxTV DVB utils for setup and manage different devices for recieve DVB broadcasting
Summary(ru_RU.UTF-8): Утилиты LinuxTV для настройки и управления различными устройствами приёма DVB вещания

License: GPL
Group: System/Configuration/Hardware
Url: http://www.linuxtv.org/wiki/index.php/LinuxTV_dvb-apps

Source0: http://linuxtv.org/download/dvb/%name-%version.tar.gz
Source1: CHANGES
Patch1: %name-makefile.patch
Patch2: %name-1.1.1-alt-v4l.patch

BuildPreReq: libv4l-devel

Provides: dvb-modules-apps
Conflicts: dvb-tools

%description
 This package contains utils for setup and manage different devices for 
 receive DVB broadcasting (includes SkyStar1 and 2) using LinuxTV DVB
 driver family. Supports old and new driver series.
 
%description -l ru_RU.UTF-8
 Этот пакет содержит утилиты для настройки и управления различными
 устройствами приёма DVB вещания (в том числе SkyStar1 и 2) через драйвера LinuxTV DVB.
 Поддерживаются как старые так и новые драйверы. 

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p2
cp %SOURCE1 ./

%build
make "ARCH= %optflags" DESTDIR=%buildroot \
   bindir=%_bindir libdir=%_libdir sysconfdir=%_sysconfdir datadir=%_datadir

%install

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/dvb/{av7110_loadkeys,dvbnet,scan,szap}
install -p util/av7110_loadkeys/*.rcmm %buildroot%_datadir/dvb/av7110_loadkeys/
install -p util/av7110_loadkeys/*.rc5 %buildroot%_datadir/dvb/av7110_loadkeys/
install -p util/dvbnet/{*.pl,*.sh} %buildroot%_datadir/dvb/dvbnet/
cp -ar util/scan/{dvb-c,dvb-s,dvb-t} %buildroot%_datadir/dvb/scan/
install -p util/szap/channels.conf-* %buildroot%_datadir/dvb/szap/

install -p util/av7110_loadkeys/av7110_loadkeys %buildroot%_bindir/
install -p util/dvbdate/dvbdate %buildroot%_bindir/
install -p util/dvbnet/dvbnet %buildroot%_bindir/
install -p util/dvbtraffic/dvbtraffic %buildroot%_bindir/
install -p util/scan/scan %buildroot%_bindir
install -p util/szap/{czap,femon,szap,tzap} %buildroot%_bindir/

# ensure dvb prefix for binaries
#(cd %buildroot%_bindir ; for exe in * ; do \
# test -d $exe && continue ; test -x $exe || continue ; case "$exe" in \
# dvb*|av7110*) : ;; \
# *) mv $exe dvb$exe ; ln -s dvb$exe $exe ;; esac ; done)

# fetch all READMEs
for i in `find . -name README` ; do test "$i" = "./README" && continue
    cp $i `echo $i | sed -e 's|./||' -e 'y|/|.|'` 
done



%files
%doc README *.README TODO CHANGES
%_bindir/*
%dir %_datadir/dvb/
%_datadir/dvb/*

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2.2
- NMU: added URL

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.1
- Fixed build

* Sun Oct 21 2007 Andrew Kornilov <hiddenman@altlinux.ru> 1.1.1-alt2
- Removed /usr/bin/evtest (it's in the input-utils package now: #13178)

* Tue Oct 10 2006 Andrew Kornilov <hiddenman@altlinux.ru> 1.1.1-alt1
- New version
- Added changelog

* Sat Aug 13 2005 Andrew Kornilov <hiddenman@altlinux.ru> 1.1.0-alt3
- Spec cleanups
- Updated russian spec translation

* Wed Aug 03 2005 Andrew Kornilov <hiddenman@altlinux.ru> 1.1.0-alt2
- Added russian description (stolen from dvb-tools spec :)

* Mon Aug 01 2005 Andrew Kornilov <hiddenman@altlinux.ru> 1.1.0-alt1
- Based on Mandrake's spec
- Sisyphus adaptation
- Patch for Makefile
- Removed old patches
