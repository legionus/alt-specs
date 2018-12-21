%define beta beta-13
#define unpack tar
Name:         lgeneral
Summary:      Turn-based strategy inspired by Panzer General 
Version:      1.2
Release:      alt5.2
License:      GPL
Group:        Games/Strategy
URL:          http://lgames.sf.net
Packager:     Mikhail Pokidko <pma@altlinux.org>
Source:       %name-%version%beta.tar.gz
Source2:	%name.NOTES.ALT
Source3:	scenarios.tar.bz2
Source4:	nicolas.zip
Source5:	newcampaign.zip
Source6:	APP-6A.zip
Patch0:	      %name.patch
Patch1:		%name.build.patch
Patch2: lgeneral-1.2-alt-gettext.patch
Patch3: lgeneral-1.2-alt-link.patch
Patch4: %name-%version-alt-gcc6.patch

Obsoletes: pg-data

# Automatically added by buildreq on Wed Aug 29 2007
BuildRequires: libSDL-devel libSDL_mixer-devel unzip

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
Original data files can be downloaed from http://lgames.sourceforge.net/index.php?project=LGeneral

%prep
%setup -q -n %name-%version%beta
%patch0 -p2
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2

touch config.rpath

%build
%autoreconf
%configure \
	--disable-rpath \
	--with-libintl-prefix=%prefix


make

%install
mkdir -p %buildroot%_datadir/games/%name/pg-data
make install DESTDIR="%buildroot"
tar xvfj %SOURCE3
mv scenarios/* %buildroot%_datadir/games/%name/scenarios/
unzip %SOURCE4
cp -pr nicolas/* %buildroot%_datadir/games/%name/
unzip %SOURCE5
cp -pr  NewCampaign/* %buildroot%_datadir/games/%name/
unzip %SOURCE6 -d APP
cp -pr APP/* %buildroot%_datadir/games/%name/
#cp -pr APP/sounds/* %buildroot%_datadir/games/%name/
#cp -pr APP/units/* %buildroot%_datadir/games/%name/


cp %SOURCE2 %buildroot%_datadir/games/%name/NOTES.ALT

#post
#/usr/bin/lgc-pg -s /usr/share/games/lgeneral/pg-data -d /usr/share/games/lgeneral

%files
#attr(0755,-,-)
%_bindir/*
%_datadir/games/%name/*
%_datadir/locale/de/*
%_datadir/locale/en/*
%_man1dir/lgc-pg.*
%_man6dir/lgeneral.*


%changelog
* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt5.2
- Fix build with new toolchain

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5.1
- Built with external gettext

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt5
- fixed build for x86_64

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt4
- fixed NATO mod path

* Wed Dec 10 2008 Mikhail Pokidko <pma@altlinux.org> 1.2-alt3
- beta13 version. 
 + Added NATO mod.

* Tue Aug 28 2007 Pokidko Mikhail <pma@altlinux.org> 1.2-alt2
- Additional scenarios and 2 campains packed.
  Original data files can be downloaed from http://lgames.sourceforge.net/index.php?project=LGeneral

* Tue Mar 13 2007 Mikhail Pokidko <pma@altlinux.ru> 1.2-alt1
- initial ALT build

