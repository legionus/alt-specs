%define Theme School Master
%define codename Chariot
%define brand informika
%define Brand Informika Linux

Name: branding-%brand-schoolmaster
Version: 6.0.0
Release: alt47
BuildArch: noarch

%define theme %name
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-droid
BuildRequires: design-bootloader-source >= 5.0-alt2
%ifnarch %arm
BuildRequires: cpio gfxboot >= 4 
%endif

BuildRequires(pre): libqt4-core
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

%define Theme_ru Школьный Мастер
%define Brand_ru Информика Линукс
%define status %nil
%define status_en %nil
%define variants altlinux-kdesktop altlinux-desktop altlinux-office-desktop altlinux-office-server altlinux-lite altlinux-workbench school-master altlinux-gnome-desktop

Source: %name.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts


%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

%define grub_normal white/black
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
BuildArch: noarch
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme plymouth(system-theme)
Requires: plymouth-plugin-script
PreReq: plymouth

%description bootsplash
This package contains graphics for boot process, displayed via Plymouth


%package alterator
BuildArch: noarch
Summary: Design for alterator for %Brand %Theme 
License: GPL
Group: System/Configuration/Other
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt 

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-browser-qt ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server 
PreReq(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme

%package graphics
BuildArch: noarch
Summary: design for ALT
License: Different licenses
Group: Graphics
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Provides: design-graphics-%theme  branding-alt-%theme-graphics design-graphics-kdesktop
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme design-graphics-kdesktop
Provides: gnome-session-splash = %version-%release
PreReq(post,preun): alternatives >= 0.2

%description graphics
This package contains some graphics for ALT design.


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business

%package release
BuildArch: noarch

Summary: %distribution %Theme release file
License: GPL
Group: System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distribution %version %Theme release file.

%package notes
BuildArch: noarch
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes

%package kde4-settings
BuildArch: noarch
Summary: KDE4 settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/KDE
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-kde4-settings ";done )
PreReq: %name-graphics

%description kde4-settings
KDE4 settings for %Brand %version %Theme

%package kde3-settings

BuildArch: noarch
Summary: KDE3 settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/KDE
PreReq: %name-graphics
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-kde3-settings ";done )

%description kde3-settings
KDE3 settings for %Brand %version %Theme

%package fvwm-settings

BuildArch: noarch
Summary: FVWM2 settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/FVWM based
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-fvwm-settings ";done )

%description fvwm-settings
FVWM2 settings for %Brand %version %Theme

%package gnome-settings

BuildArch: noarch
Summary: GNOME settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/GNOME
Requires: gtk2-theme-mist
#PreReq: gnome-panel
Provides: gnome-theme-%brand-%theme = %version-%release
Provides: metacity-theme-%brand-%theme = %version-%release
Provides: metacity-theme
Provides: gnome-menus = 2.30.4
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )

%description gnome-settings
GNOME settings for %Brand %version %Theme


%package slideshow

BuildArch: noarch
Summary: Slideshow for %Brand %version %Theme installer
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml

BuildArch: noarch
Summary: %name -- ALT Linux html welcome page
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server

Requires: xdg-utils 
Requires(post): indexhtml-common

%description indexhtml
ALT Linux index.html welcome page.

%prep
%setup -n %name

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Theme' NAME_RU='%Theme_ru' BRAND_FNAME='%Brand' BRAND_FNAME_RU='%Brand_ru' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version X86='%x86' ./configure 
make

%install
%makeinstall

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

GRAPHICS_ALTPRIO=`printf '%%.3d%%.3d%%.3d%%.3d\n' %design_graphics_abi_epoch %design_graphics_abi_major %design_graphics_abi_minor %design_graphics_abi_bugfix`
install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/design-current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
%_datadir/design/current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
__EOF__


#release
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/ignore.d/
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%distribution %version %Theme %status_en (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

#notes
pushd notes
%makeinstall
popd

#kde4-settings
pushd kde4-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde4
cp -a kde4/* %buildroot%_sysconfdir/skel/.kde4/
mkdir -p %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
install -m 0644 menu/*.menu %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
popd

#kde3-settings
pushd kde3-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde
cp -a kde/* %buildroot%_sysconfdir/skel/.kde/
mkdir -p %buildroot%_sysconfdir/skel/.kde/share
mkdir -p %buildroot%_sysconfdir/skel/.kde/share/config
mkdir -p %buildroot%_sysconfdir/skel/.kde/share/apps
cp -a config/* %buildroot%_sysconfdir/skel/.kde/share/config/
cp -a apps/* %buildroot%_sysconfdir/skel/.kde/share/apps/
popd

#kde3-splash
pushd kde3-styles-splash
mkdir -p "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme"
install -m 644 *.jpg "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
install -m 644 *.png "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
install -m 644 *.rc "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
popd

#fwvm-settings
mkdir -p %buildroot/etc/skel
install -m 644 fvwm-settings/.fvwm2rc %buildroot/etc/skel/

#gnome-settings
%define XdgThemeName %Brand %Theme
pushd gnome-settings
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName'
install -m 644  panel-default-setup.entries '%buildroot/%_datadir/themes/%XdgThemeName/'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
install -m 644 gtkrc '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1'
install -m 644 metacity-theme-1.xml '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1/'
install -m 644 index.theme '%buildroot/%_datadir/themes/%XdgThemeName/'
mkdir -p '%buildroot/etc/gnome/xdg/menus/'
install -m 644 gnome-applications.menu '%buildroot/etc/gnome/xdg/menus/'
install -m 644 settings.menu '%buildroot/etc/gnome/xdg/menus/'
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install -m 0644 slideshow/*  %buildroot/usr/share/install2/slideshow/

#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high


%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%ifnarch %arm
%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme
/boot/grub/themes/%theme
%endif

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

%post gnome-settings
%gconf2_set string /desktop/gnome/interface/font_name Sans 11
%gconf2_set string /desktop/gnome/interface/monospace_font_name Monospace 10
cat '/%_datadir/themes/%XdgThemeName/panel-default-setup.entries' > \
/etc/gconf/schemas/panel-default-setup.entries
/usr/bin/gconftool-2 --direct --config-source=$(/usr/bin/gconftool-2 --get-default-source) \
--load='/%_datadir/themes/%XdgThemeName/panel-default-setup.entries'
/usr/bin/gconftool-2 --direct --config-source=$(/usr/bin/gconftool-2 --get-default-source) \
--load='/%_datadir/themes/%XdgThemeName/panel-default-setup.entries' /apps/panel



%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files bootsplash
%_datadir/plymouth/themes/%theme/*

%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde4-settings
%_sysconfdir/kde4/xdg/menus/applications-merged/*.menu
%_sysconfdir/skel/.kde4

%ifnarch %arm
%files kde3-settings
%_sysconfdir/skel/.kde
%_datadir/apps/ksplash/Themes/*
%endif

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files gnome-settings
%_datadir/themes/*
/etc/gnome/xdg/menus/*

%files slideshow
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/images
%_desktopdir/indexhtml.desktop
%_datadir/kde4/apps/kio_desktop/DesktopLinks/indexhtml.desktop

%changelog
* Mon Sep 25 2017 Sergey V Turchin <zerg at altlinux dot org> 6.0.0-alt47
- don't require ksplash-engine-moodin

* Mon Apr 08 2013 Sergey V Turchin <zerg at altlinux dot org> 6.0.0-alt46
- fix requires

* Thu Aug 30 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt44.M60P.1
- built for M60P

* Thu Aug 30 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt45
- translate installer notes and license titles into russian

* Tue Aug 21 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt43.M60P.1
- built for M60P

* Tue Aug 21 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt44
- update indexhtml css

* Fri Aug 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt42.M60P.1
- built for M60P

* Fri Aug 17 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt43
- translate indexhtml and indexhtml.desktop titles into russian

* Wed Aug 15 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt41.M60P.1
- built for M60P

* Wed Aug 15 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt42
- fix grub terminal-box background color

* Fri Aug 10 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt40.M60P.1
- built for M60P

* Fri Aug 10 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt41
- gix license content-type (ALT#27521)

* Tue Jul 31 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt39.M60P.1
- built for M60P

* Tue Jul 31 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt40
- fix bootloader menu items color
- bump release

* Wed Jul 04 2012 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- convert from KDesktop branding
