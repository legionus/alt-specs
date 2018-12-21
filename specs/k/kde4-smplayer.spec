
%def_enable mpv

%define rname smplayer
%define svn 8242
%define xde kde4
%define XDE KDE4
%define xapp kde4
Name: %xde-%rname
Version: 16.11.0.%svn
Release: alt1

%define qt_bin_dir %_qt4dir/bin
%define configure_qmake %qmake_qt4
%define qt_qmake %qt_bin_dir/qmake

Summary: A great MPlayer/MPV front-end
Summary(ru_RU.UTF8): Мощный интерфейс для MPlayer/MPV
Summary(uk_UA.UTF8): Потужний інтерфейс для MPlayer/MPV
Group: Video
#Url: http://www.smplayer.es/
#Url: http://www.smplayer.info/
Url: http://smplayer.sourceforge.net
License: GPLv2

Requires: %name-backend %name-common = %EVR
#Provides: %xde-video-player

Source: %rname-%version.tar
Patch1: alt-defines.patch
Patch2: alt-defaults.patch
Patch3: alt-ui-defaults.patch
Patch4: alt-config-dir.patch
Patch5: alt-youtube-browser.patch

BuildRequires: gcc-c++ libqt4-devel
BuildRequires: libXext-devel zlib-devel

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%if %xde == "kde4"
Conflicts: kde4-smplayer < 14.9.0.7049
%endif

%package backend-2-mpv
Group: System/Libraries
Summary: MPV %name backend
Provides:  %name-backend = %version-%release
Provides:  %name-backend-mpv = %version-%release
Requires: %name-common = %EVR
Requires: mpv

%package backend-4-mplayer
Group: System/Libraries
Summary: MPlayer %name backend
Provides:  %name-backend = %version-%release
Provides:  %name-backend-mplayer = %version-%release
Requires: %name-common = %EVR
Requires: mplayer

%description
smplayer intends to be a complete front-end for MPlayer/MPV, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for MPlayer/MPV filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.
%description -l ru_RU.UTF8
SMPlayer стремится быть как можно более полным интерфейсом для MPlayer/MPV,
от базовых функций проигрывания видео, DVD, VCDs до самого продвинутого
функционала MPlayer/MPV по поддержке фильтров и т.п. Одна из главных
особенностей - способность запоминать положение проигрываемого файла для
того, чтобы при следующем его открытии Вы могли смотреть его дальше с
того же места и с теми же параметрами настроек. SMPlayer разработан на
инструментарии Qt и является мультиплатформенным.
%description -l uk_UA.UTF8
SMPlayer направлений на те, щоб стати як можна більш повним інтерфейсом
для MPlayer/MPV, від базових функцій відтворення відео, DVD, VCD до самого
продвинутого функціонала MPlayer/MPV по підтримці фільтрів і т.і. Одна з
головних особливостей - здатність запам'ятовувати положення файлу, що
відтворюється, для того, щоб при наступному його відкритті Ви мали змогу
переглядати його далі з того ж місця і з тими ж параметрами налаштувань.
SMPlayer розробено на інструментарії Qt і є мультиплатформним.
%description common
%name common package
%description backend-2-mpv
MPV %name backend
%description backend-4-mplayer
MPlayer %name backend

%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's|@APP_PREFIX@|%xde|' src/paths.cpp

export PATH=%qt_bin_dir:$PATH

sed -i 's|^PREFIX=.*|PREFIX=%_prefix|' Makefile
sed -i 's|^DATA_PATH=.*|DATA_PATH=%_datadir/%name|' Makefile
sed -i 's|^TRANSLATION_PATH=.*|TRANSLATION_PATH=%_datadir/%name/translations|' Makefile
sed -i 's|^DOC_PATH=.*|DOC_PATH=%_docdir/%name-%version|' Makefile
sed -i 's|^THEMES_PATH=.*|THEMES_PATH=%_datadir/smplayer/themes|' Makefile
sed -i 's|^SHORTCUTS_PATH=.*|SHORTCUTS_PATH=%_datadir/%name/shortcuts|' Makefile

pushd src
echo '#define SVN_REVISION "%svn"' > svn_revision.h
%configure_qmake smplayer.pro
popd


%build
export PATH=%qt_bin_dir:$PATH
export QMAKE=%qt_qmake
%make_build src/smplayer


%install
%make DESTDIR=%buildroot install

# renames
mv %buildroot/%_bindir/smplayer %buildroot/%_bindir/%name
mkdir -p %buildroot/%_desktopdir/%xapp/
mv %buildroot/%_desktopdir/*.desktop %buildroot/%_desktopdir/%xapp/
find %buildroot/%_desktopdir/ -type f -name \*.desktop | \
while read f; do
    sed -i 's|^Exec=\(.*\)|Exec=%xde-\1|' $f
    sed -i 's|^Icon=\(.*\)|Icon=%xde-\1|' $f
    sed -i 's|SMPlayer|SMPlayer %XDE|g' $f
done
find %buildroot/%_iconsdir/ -type f | \
while read f; do
    oldname=`basename $f`
    newname="%xde-$oldname"
    filedir=`dirname $f`
    mv $f $filedir/$newname
done

%find_lang --without-mo --with-qt smplayer

%files common -f smplayer.lang
%dir %_datadir/%name
%dir %_datadir/%name/translations/

%if_enabled mpv
%files backend-2-mpv
%endif
%files backend-4-mplayer

%files
%_bindir/%name
%_desktopdir/%xapp/*.desktop
%_docdir/%name-%version
%_datadir/%name/*
%exclude %_datadir/%name/translations
%_iconsdir/hicolor/*/apps/%name.*


%changelog
* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.11.0.8242-alt1
- new version

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.9.0.8142-alt1
- new version

* Thu Aug 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.8.0.8066-alt1
- new version

* Thu Apr 07 2016 Sergey V Turchin <zerg@altlinux.org> 16.4.0.7558-alt1
- new version

* Mon Feb 08 2016 Sergey V Turchin <zerg@altlinux.org> 16.1.0.7385-alt1
- update for upstream fixes

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 16.1.0.7318-alt2
- disable reminder

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 16.1.0.7318-alt1
- new version

* Fri Nov 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.9.0.7213-alt3
- allow smplayer themes

* Fri Nov 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.9.0.7213-alt2
- set default youtube browser

* Mon Nov 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.9.0.7213-alt1
- update for mplayer 1.2 detection

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.9.0.7148-alt1
- new version

* Thu Jul 30 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7049-alt1
- update to r7049
- allow to use with mpv and without mplayer

* Wed Jul 29 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt4
- fix package translations

* Fri Jul 24 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt2.M70P.1
- built for M70P

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt3
- separate configs with smplayer

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt2
- update UI defaults

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt1
- update to r7046

* Mon Jul 20 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.6748-alt1
- initial build
