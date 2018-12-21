%define theme centaurus
%define Theme Centaurus
%define codename Pholus
%define brand altlinux
%define Brand ALT Linux

Name: branding-%brand-%theme
Version: 7.0.5
Release: alt1

BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-droid
BuildRequires: design-bootloader-source >= 5.0-alt2
%ifnarch %arm
BuildRequires: cpio gfxboot >= 4 
%endif

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

%define status_en %nil
%define status %nil
%define ProductName_ru Альт Линукс 7.0 Кентавр

# All existing branding without this branding
%define variants altlinux-backup-server altlinux-desktop altlinux-gnome-desktop altlinux-kdesktop altlinux-lite altlinux-lxdesktop altlinux-office-desktop altlinux-office-server altlinux-school-server altlinux-sisyphus altlinux-spt altlinux-tablet altlinux-workbench informika-schoolmaster ivk-chainmail lxde-desktop lxde-school-lite Platform6-server-light school-junior school-lite school-master school-server school-teacher school-terminal simply-linux sisyphus-server-light 

Packager: Anton V. Boyarshinov <boyarsh at altlinux dot org>

Source: branding.tar

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
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

%define grub_normal white/light-blue
%define grub_high black/light-gray

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
BuildArch: noarch
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
PreReq: plymouth

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootsplash ";done )
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

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes: branding-alt-%theme-graphics design-graphics-%theme
Provides: design-graphics = 12.0.0
Provides: gnome-session-splash = %version-%release
PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )

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

%package fvwm-settings

BuildArch: noarch
Summary: FVWM2 settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/FVWM based
Requires: altlinux-freedesktop-menu-gnomish-menu
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-fvwm-settings ";done )

%description fvwm-settings
FVWM2 settings for %Brand %version %Theme

%package mate-settings

BuildArch: noarch
Summary: MATE settings for %Brand %version %Theme
License: Distributable
Group:   Graphical desktop/GNOME
Requires: gksu
Requires: dconf
Requires: gtk3-theme-clearlooks-phenix
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )
PreReq(post): lightdm-gtk-greeter
PreReq(post): libgio

%description mate-settings
MATE settings for %Brand %version %Theme

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
%setup -n branding

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%ProductName_ru' CODENAME='%codename' X86='%x86' ./configure 
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

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
%_datadir/design/current	%_datadir/design/%theme	10
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%distribution %version %Theme %status_en (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
install -m 0644 components/systemd/os-release %buildroot%_sysconfdir/os-release

#notes
pushd notes
%makeinstall
popd

#kde4-settings
pushd kde4-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde4
cp -a kde4/* %buildroot%_sysconfdir/skel/.kde4/
popd


#fwvm-settings
mkdir -p %buildroot/etc/skel
install -m 644 fvwm-settings/.fvwm2rc %buildroot/etc/skel/

#mate-settings
pushd mate-settings
install -m 644 -D 50_mate-background.gschema.override '%buildroot%_datadir/glib-2.0/schemas/50_mate-background.gschema.override'
install -m 644 -D 60_mate-theme.gschema.override '%buildroot%_datadir/glib-2.0/schemas/60_mate-theme.gschema.override'
install -m 644 -D Trolltech.conf '%buildroot%_sysconfdir/skel/.config/Trolltech.conf'
mkdir -p '%buildroot%_sysconfdir/skel/.cache/thumbnails'
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/*  %buildroot/usr/share/install2/slideshow/

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

%post mate-settings
subst 's/#theme-name=/theme-name=Clearlooks-Phenix/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

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
%_sysconfdir/skel/.kde4

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*.gschema.override
%_sysconfdir/skel/.config/Trolltech.conf
%_sysconfdir/skel/.cache

%files slideshow
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/alt-docs
%indexhtmldir/documentation
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/images
%_desktopdir/indexhtml.desktop

%changelog
* Thu Apr 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.5-alt1
- bump version

* Tue Mar 04 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.4-alt1
- bump version

* Wed Jan 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.3-alt1
- licence fixed

* Thu Jan 09 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.2-alt2
- .cache/thumbnails added to etcskel

* Wed Nov 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.2-alt1
- version change

* Wed Jul 24 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.1-alt2
- VERSION_ID in os-release fixed

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.1-alt1
- version change

* Mon Jul 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.0-alt5
- images for plymouth have been downscaled 

* Mon Jul 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.0-alt4
- png file for grub reverted to rgb

* Wed Jul 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.0-alt3
- png files converted to use indexed colors

* Thu Jul 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.0-alt2
- os-release fixed

* Tue Jun 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.0-alt1
- release version

* Tue Jun 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.9-alt6
- slideshow added

* Thu Jun 06 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt5
- Fix window close icon size

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt4
- Set correct size for typical graphical buttons
- Set appropriate indent for small hint of fields

* Tue Apr 30 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.9-alt3
- wallpaper from Ark Desktop added

* Fri Apr 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.9-alt2
- codename changed to Pholus

* Fri Apr 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.9-alt1
- set beta state

* Tue Apr 23 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt23
- Disable white color for step title in LiveCD installer

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt22
- Set different qss style file for LiveCD
- Colorize bootloader bottom bar
- Really use overrided settings in Mate
- Set 'mate' icon theme in Mate
- Set 'Clearlooks-Phenix' window manager theme in Mate

* Wed Apr 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.0-alt21
- lightdm theme setup added to mate-settings
- setting GTK+ QT style added to mate-settings

* Tue Apr 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.0-alt20
- gnome2 settings removed

* Thu Apr 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.0-alt19
- kde3 settings removed

* Fri Mar 22 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt18
- Cleanup MATE settings
- Expand GRUB menu
- Set gtk3-theme-clearlooks-phenix as default GTK+2/3 theme

* Tue Feb 26 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt17
- Fix Name in os-release

* Fri Dec 28 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt16
- Set correct URL to indexhtml

* Fri Dec 28 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt15
- Really set Unicode black circle for password character
- Remove white artifacts around QLineEdit on blue wallpaper

* Wed Dec 12 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt14
- Create mate-settings subpackage
- Set light-blue background for GRUB console

* Wed Dec 05 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt13
- Small fixes in Alterator stylesheet

* Tue Dec 04 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt12
- Set grayed table borders and header selection in Alterator web-interface
- Use only existed fonts in grub2
- Make indexhtml more narrow

* Mon Dec 03 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt11
- Set Misc Fixed in grub2 console font
- Add os-release for systemd compatibility
- Fix small typo in style name for English version of indexhtml

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt10
- Set default wallpaper in Mate
- Fix section border in subdialogs
- Remove obsoleted slideshow and some files
- Set non-wide grub wallpaper
- Set correct Russian product name from spec
- Add links to useful resources
- Fix grub console background

* Thu Nov 29 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt9
- Set compatible stylesheet for alterator-browser-qt
- Set correct background for Mate
- More contrast colors for gfxboot
- Fix grub colors
- Set Plymouth wallpapers with logotypes

* Mon Nov 26 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt8
- Set favicon for Alterator

* Mon Nov 26 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt7
- Set official Centaurus 7.0 wallpapers
- Remove obsoleted group icons
- Set new icons of Platform 7 for acc
- Draw allerator-browser-qt background from top left corner
- Draw title as 100% white and other labels in 80% white
- Replace all steps icons by transparent icon

* Tue Nov 20 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt6
- Set TraditionalOk theme for Mate
- Grow section width, set attention box as block

* Thu Nov 15 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt5
- Fix grub2 console font
- Fix attribute name for meta http-equiv
- Adapt indexhtml to use from httpd2
- Add gksu for apt-indicator in GNOME
- Modernize appearance of Alterator web interface

* Tue Nov 13 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt4
- Set wallpapers for Centaurus 7.0
- Set product logo for Centaurus 7.0
- Fix search entry background
- Don't overwrite specific product-logo.png

* Fri Nov 09 2012 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt3
- New design of indexhtml
- Set fill list of available variant

* Tue Sep 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.0-alt2
- installer background resizing removed
- status set

* Fri Sep 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9.0-alt1
- full-size installer background

* Fri Sep 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt18
- theme-livecd.qrc for livecd

* Mon Sep 19 2011 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt17
- New design of indexhtml

* Fri Sep 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt16
- gtk theme fix from mex3@

* Tue Aug 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt15
- tooltip color in browser-qt really fixed

* Mon Aug 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt14
- indexhtml design and links fixed
- tooltip color in browser-qt fixed

* Wed Aug 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt13
- yet another slide added

* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt12.1
- rebuild with design-bootloader-source 6.0

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt12
- Style=Cleanlooks in alterator

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt11
- images with p6 logo

* Mon Jun 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt10
- automatic 800x600 for virtualbox

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt9
- setup default gnome panel
- .gconf deleted from etcskel

* Mon May 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt8
- dependence on altlinux-menus dropped

* Sat May 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt7
- beta status deleted
- rebuild with design-bootloader-source 5.9-alt4

* Wed Apr 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt6
- settings menu translation fixed

* Tue Apr 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt5
- arm buildabulity
- gnome menus customization

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt4
- indexhtml colors changed (mex3)

* Thu Feb 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt3
- fixed logo in web interface
- boot colors changed

* Thu Feb 03 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt2
- install menu position changed
- web design from mex3@

* Fri Jan 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt1
- production slideshow
- installer wallpaper changed
- grub theme

* Wed Dec 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt11
- fvwm settings added

* Thu Nov 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt10
- gfxboot colors changed

* Tue Nov 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt9
- plymouth: scaling for non 4:3 or 16:9 resolutions fixed

* Sat Nov 13 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt8
- typo in plymouth script fixed

* Fri Nov 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt7
- migration from bootsplash to plymouth

* Fri Oct 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt6
- menu bar size fixed

* Wed Sep 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt5
- setup grub colors added

* Tue Aug 31 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt4
- status changed to beta
- background changed

* Mon Aug 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt3
- fonts changed

* Tue May 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2.2
- rebuld with design-bootloader-source 5.9

* Fri May 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2.1
- rebuild with gfxboot.git-4.1.47

* Tue Apr 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt2
- product-logo.png changed

* Thu Mar 04 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9.9-alt1
- Centaurus branding

* Wed Mar 03 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.1-alt1
- OO.o desktop files names changed

* Mon Oct 26 2009 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt22
- provide design-graphics and gnome-session-splash to avoid wrong 
  graphics package installation

* Thu Oct 22 2009 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt21
- fix Russian name and copyright years
- fix images
- remove beta status

* Mon Sep 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt20
- beep on boot disabled

* Thu Aug 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt19
- production images, slides (and colors?)

* Sun Jul 12 2009 Alexey Rusakov <ktirf@altlinux.org> 5.0.0-alt18.1.1
- fix unexpanded autoconf substitute (closes bug 20757)
- beautify theme names in -gnome-settings

* Thu Jun 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt18.1
- titles removed from wallpater and installer 

* Wed Jun 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt18
- sources restructure 

* Thu Jun 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt17
- ksplashrc added for kde4
- kde3-settings and splash for kde3 added (mex@)
- gnome-settngs added (mex@)

* Wed May 13 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt16
- \%setup fixed from boyarsh@
- remove package name from .gear-rules from boyarsh@

* Fri Apr 24 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt15
- minor fixes of strange merge
- changes in alterator.css.in from inger@

* Fri Apr 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt14
- better quality background image for installer

* Thu Apr 16 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt13
- alterator.css = alterator.css+menu.css
- some strange results of merge fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt12
- gear-rules fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt11
- web logo - white and smaller;
  labels on buttons - darker;
  disabled elements - lighter;

* Fri Apr 10 2009 Alxandra Panyukova <mex3@altlinux.ru> 5.0.0-alt10
- some misspells fixed

* Thu Apr 09 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt9
- darker text and new logo for web

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt8
- gradients and some colors in css fixed by mex3@

* Tue Apr 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt7
- fixes for installer design from mex3@ 

* Fri Apr 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt6
- default gray design from mex3@
- \%status_en intorduces for release file 

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt5
- logo in www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt4
- www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt3
- conflicts for -alterator subpackages added
- design for web alterator changed

* Mon Mar 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt2
- -browser-qt subpackage remaned to -alterator as it really is

* Fri Mar 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- addes \%status to altlinux-release
- images for verbose bootsplash mode from one source

* Wed Mar 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt24
- added versioned provides for indexhtml 

* Tue Mar 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt23
- indexhtml subpackage added 

* Mon Mar 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt22
- nepomukserverrc added into kde4 

* Wed Mar 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt21
- other images for browser-qt added
- gtkrcs added into kde4-settings
- plasma-applet-networkmanagenemt removed from kde4 by default
- conflicts bitween different brandings added

* Thu Mar 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt20
- steps icons added 

* Fri Feb 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- sample slideshow added

* Wed Feb 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- 1024x768 removed :D
- more transparent menu selection bar

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- 1024x768 added 
- fonts changed

* Thu Feb 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- not setup language in bootloader during install (when it is 'C') 

* Wed Feb 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- rebuild with new bootloader-source with support of real language change 

* Tue Feb 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- auto set default language for bootloader from /etc/sysconfig/i18n 

* Mon Feb 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- rebuild for fix oversized /boot/splash/message 

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- default language set to ru_RU for system boot 

* Wed Feb 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- fixed conflict of notes subpackage with itself 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- more kde4 settings from zerg@ 
- alternative and obsoletes for graphics added

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- rebuild with new translations 

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- added kde4-settings subpackage 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- added conflicts for notes 

* Mon Jan 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- xdm background fixed 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- added 'notes' subpackage 

* Thu Jan 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- fixed problem with owerwritten alternative 

* Wed Jan 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- release subpackage added 

* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

