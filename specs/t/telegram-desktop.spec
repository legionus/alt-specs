# other variant: Debug
%define buildmode Release

# TODO: improve detection
BuildRequires(pre): rpm-build-ubt
%if %ubt_id == "M80P"
%def_with ffmpeg_static
%else
%def_without ffmpeg_static
%endif

# Precompiled supports only for gcc
%def_without clang
%def_without libcxx

Name: telegram-desktop
Version: 1.5.2
Release: alt1

Summary: Telegram is a messaging app with a focus on speed and security

License: %gpl3only
Group: Networking/Instant messaging
Url: https://telegram.org/

# Source-url: https://github.com/telegramdesktop/tdesktop/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-locales-%version.tar
Source2: CMakeLists.txt

Patch1: 0001_add-cmake.patch
Patch3: 0003_qt-plugins.patch
Patch5: 0005_Downgrade-Qt-version.patch
Patch6: 0006_fix-static-qt-functions.patch
Patch8: 0008_add_locales.patch
#Patch9: 0001-use-correct-executable-path.patch
Patch14: 0014-get-language-name-and-country-name-from-QLocale.patch
Patch15: 0015-disable-resource-fonts.patch
Patch16: 0016-fix-lzma.patch
Patch17: 0017-ligsl-microsoft-fix.patch
Patch18: 0018-fix-linking.patch

#ExclusiveArch: %ix86 x86_64
ExclusiveArch: %arm x86_64

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake
BuildRequires(pre): rpm-macros-kde-common-devel

BuildRequires(pre): rpm-build-compat >= 2.1.5
BuildRequires(pre): rpm-build-intro >= 2.1.5
# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000

BuildRequires: gcc-c++ libstdc++-devel gyp

# 3.13 due add_compiler_definitions
BuildRequires: cmake >= 3.13

BuildRequires: qt5-base-devel libqt5-core libqt5-network libqt5-gui qt5-imageformats
# needs for smiles and emojicons
Requires: qt5-imageformats

# for -lQt5PlatformSupport
BuildRequires: qt5-base-devel-static

# for autoupdater (included ever if disabled)
BuildRequires: liblzma-devel

# for SourceFiles/mtproto/connection.cpp
BuildRequires: libzip-devel

BuildRequires: zlib-devel >= 1.2.8

BuildRequires: libminizip-devel libpcre-devel libexpat-devel libssl-devel bison
#BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel
#BuildRequires: libXi-devel libSM-devel libICE-devel libdbus-devel libXfixes-devel
BuildRequires: libX11-devel

# GTK 3.0 integration
BuildRequires: libgtk+3-devel libappindicator-gtk3-devel
# TODO:
# libdee-devel

BuildRequires: libopenal-devel >= 1.17.2
# libportaudio2-devel libxcb-devel 
# used by qt imageformats: libwebp-devel
BuildRequires: libva-devel libdrm-devel

BuildRequires: libtgvoip-devel >= 2.4
BuildRequires: libcrl-devel >= 0.5

BuildRequires: libxxhash-devel

# C++ sugar
BuildRequires: libmicrosoft-gsl-devel >= 20180615
BuildRequires: libvariant-devel librange-v3-devel

# FIXME: libva need only for linking, extra deps?

Provides: tdesktop = %version-%release
Obsoletes: tdesktop

%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static
%else
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libswscale-devel libswresample-devel
%endif

%if_with clang
BuildRequires: clang6.0
%remove_optflags -frecord-gcc-switches
%endif
%if_with libcxx
%add_optflags -stdlib=libc++
%endif

Requires: dbus

# some problems with t_assert
%add_optflags -fpermissive

# disable some warnings
%add_optflags -Wno-strict-aliasing -Wno-unused-variable -Wno-sign-compare -Wno-switch

%description
Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free.
You can use Telegram on all your devices at the same time - your messages
sync seamlessly across any number of your phones, tablets or computers.

With Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc),
as well as create groups for up to 1000 people or channels for broadcasting to unlimited audiences.
You can write to your phone contacts and find people by their usernames.
As a result, Telegram is like SMS and email combined - and can take care of all your personal
or business messaging needs.


%prep
%setup -a1
%patch1 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
#patch9 -p1
%patch14 -p1
%patch15 -p1
%patch17 -p2
%patch18 -p2

cp %SOURCE2 Telegram/
# MacOS things will conflicts with binary name, so delete Telegram dir
rm -rf Telegram/Telegram/


%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif
cd Telegram
%if_with clang
export CC=clang
export CXX=clang++
%endif
%cmake_insource \
%if_with libcxx
    -DLLVM_ENABLE_LIBCXX=ON
%else
    %nil
%endif
# due precompiled headers
export CCACHE_SLOPPINESS=pch_defines,time_macros
%make_build

%install
# XDG files
install -m644 -D lib/xdg/telegramdesktop.desktop %buildroot%_desktopdir/%name.desktop
install -m644 -D lib/xdg/tg.protocol %buildroot%_Kservices/tg.protocol
install -m644 -D lib/xdg/telegramdesktop.appdata.xml %buildroot%_datadir/appdata/telegram-desktop.appdata.xml
for i in 16 32 48 64 128 256; do
    install -m644 -D Telegram/Resources/art/icon$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/telegram.png
done

#cd out/%buildmode
install -D Telegram/Telegram %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/Telegram
ln -s %name %buildroot%_bindir/telegram

%files
%_bindir/%name
%_bindir/Telegram
%_bindir/telegram
%_desktopdir/%name.desktop
%_Kservices/tg.protocol
%_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/16x16/apps/telegram.png
%_iconsdir/hicolor/32x32/apps/telegram.png
%_iconsdir/hicolor/48x48/apps/telegram.png
%_iconsdir/hicolor/64x64/apps/telegram.png
%_iconsdir/hicolor/128x128/apps/telegram.png
%_iconsdir/hicolor/256x256/apps/telegram.png
#_man1dir/*
%doc README.md

%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Tue Dec 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version (1.5.1) with rpmgs script
- disable build on i586

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- new version 1.4.8 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version (1.4.0) with rpmgs script

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version (1.3.16) with rpmgs script
 + Update libtgvoip, fix crash in calls.
 + Improved local caching for images and GIF animations.
 + Control how much disk space is used by the cache
   and for how long the cached files are stored.

* Tue Aug 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.14-alt1
- new version 1.3.14 (with rpmrb script)

* Thu Aug 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.12-alt1
- new version 1.3.12 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt2
- restrict __nprocs with _tune_parallel_build_by_procsize
- drop libpixman-devel buildreq

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt1
- new version 1.3.9 (with rpmrb script)

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.8-alt1
- new version 1.3.8 (with rpmrb script)

* Thu Jun 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.7-alt1
- new version 1.3.7 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script)

* Fri Jun 01 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.23-alt1
- new version 1.2.23 (with rpmrb script)

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version (1.2.8) with rpmgs script

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26 (with rpmrb script)

* Thu Nov 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24 (with rpmrb script)
- build with librange-v3-include
- disable GTK integration (ALT bug 34182)

* Sat Oct 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt3
- fix old lang code in settings
- fix CVE-2016-10351: Insecure cWorkingDir permissions
- sync CMakeLists.txt with Gentoo, fix build with new Qt 5.9.2

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt2
- add support for build with static ffmpeg

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)
- add qt5-imageformats (fixes missed smiles and emojicons)

* Wed Aug 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.19-alt1
- new version 1.1.19 (with rpmrb script)

* Sun Jul 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18 (with rpmrb script)
- update translations

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- cleanup build requires (drop opus, pulseaudio, webp, xcb, exif, X*)

* Fri Jul 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14 (with rpmrb script)
- build with custom API ID
- update translations
- language list now downloading from cloud

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- use correct executable path (fix restart)
- open localized FAQ for ru/uk/be
- get initial language name and country name from QLocale
- fix crash in video player seeking (66662e02a)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- new version (1.1.7) with rpmgs script

* Thu May 18 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt5
- add /usr/bin/telegram-desktop, fix icons name (ALT bug #33001)

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt4
- get language name and country name from QLocale
- disable user desktop file generation
- fix hack for restart via Updater, use direct /usr/bin path

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt3
- add Belarusian Russian Ukrainian French Turkish Czech languages

* Mon Dec 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt2
- add desktop file, icons
- cleanup spec

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt1
- new version 0.10.19 (with rpmrb script)

* Sun Dec 20 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.9.15-alt1
- initial build for ALT Linux Sisyphus
