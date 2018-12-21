#define _kde4_alternate_placement 1
%define rname cloudcity
%define svn_rev 1658

Name: kde4-styles-bespin
Summary: Bespin is a native style for QT/ KDE4
Version: 0.1.0.%svn_rev
Release: alt1.qa1
Url:     http://cloudcity.sourceforge.net/
Group:   Graphical desktop/KDE
License: LGPLv2

Source0: %rname.tar
Source1: screenshot.png
Source2: icons.tar
# MDV
Patch0: bespin-svn-mdv-fix-icon-and-comment-in-kde-icons-scripts.patch
Patch1: bespin-svn-mdv-fix-ksplash-themerc.patch
# ALT
Patch10: bespin-alt-gen-kde-icons.patch
Patch11: bespin-alt-find-kwin-headers.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ ghostscript-utils glib2-devel
BuildRequires: pstoedit
BuildRequires: kde4base-workspace-devel
BuildRequires: ImageMagick-tools
BuildRequires: inkscape
BuildRequires: bash
BuildRequires: /proc

Requires: plasma-applet-xbar = %version-%release
#Requires: bash-completion-bespin = %version-%release
Requires: %name-ksplash = %version-%release
Requires: %name-kdm = %version-%release
Requires: %name-kwin = %version-%release
Requires: %name-widgets = %version-%release
Requires: icon-theme-bespin = %version-%release

%description
Bespin is a native style for QT/ KDE4

The name is nothing about Quantum Mechanics, but just refers to the
Cloud City from StarWars - Episode V "The Empire Strikes Back"

Some presets can be found in /usr/share/doc/%name

%package common
Summary: %name common package
Group: System/Configuration/Other
%description common
%name common package

%package core
Summary: %name core package
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
%name core package

%package -n plasma-applet-xbar
Summary: Xbar applet for Bespin style
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
#Requires: %name-core = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
%description -n plasma-applet-xbar
The XBar is a Client/Server approach to a "mac-a-like" global menubar.
Currently it's only used by the Bespin Style to post apply clients to
Qt4 based applications.
The only currently existing Server is a Plasmoid.

%package -n bash-completion-bespin
Summary: Bash Completion for bespin
Group: Development/Other
Requires: %name-common
Requires: bash-completion
%description -n bash-completion-bespin
Bash completion for the "bespin" tool, written by Franz Fellner

%package ksplash
Summary: Bespin ksplash theme
Group: Graphical desktop/KDE
Requires: %name-common
%description ksplash
This package provide a bespin kdm theme

%package kdm
Summary: Bespin kdm theme
Group: Graphical desktop/KDE
Requires: %name-common
%description kdm
This package provide a Bespin kdm theme

%package kwin
Summary: Bespin kwin theme
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: %name-core = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
%description kwin
This package provide a Bespin kwin theme

%package widgets
Summary: Bespin widgets theme
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Requires: %name-core = %version-%release
Requires: kde4libs >= %{get_version kde4libs}
%description widgets
This package provide a Bespin widgets theme

%package -n icon-theme-bespin
Summary: Bespin icons theme
Group: Graphical desktop/KDE
Requires: %name-common
BuildArch: noarch
%description -n icon-theme-bespin
This package provide a Bespin icons theme

%prep
%setup -q -n %rname
tar xf %SOURCE2
%patch0 -p1
#%%patch1 -p0
#%%patch10 -p1
#%%patch11 -p1
pushd icons
for i in *.svgz;do
    gunzip -S '.svgz' "$i"
    mv "${i/.svgz/}" "${i/.svgz/.svg}"
done
popd

%build
%add_optflags -fpermissive
%K4build -DENABLE_ARGB=ON

# Generate splash screens
for splash in aperture bespin tibanna;do 
    pushd ksplash/$splash 
    ./generate.sh 800 600
    ./generate.sh 1024 768
    ./generate.sh 1280 1024
    ./generate.sh 1600 1200
    ./generate.sh 1680 1050
    ./generate.sh 1920 1200
    ./generate.sh 1920 1080
    popd
done

# Generate icons
pushd icons
bash ./generate_kde_icons.sh
popd

%install
%K4install

if [ -x %buildroot/%_K4datadir/bin/bespin ] ; then
    mkdir -p %buildroot/%_kde4_bindir
    mv %buildroot/%_K4datadir/bin/bespin %buildroot/%_kde4_bindir/
fi

# Installing necessary files for bespin-completion
mkdir -p %buildroot/%_sysconfdir/bash_completion.d
mkdir -p %buildroot/%_man1dir
cp man/bespin.1 %buildroot/%_man1dir
cp extras/bespin-compl %buildroot/%_sysconfdir/bash_completion.d

# Installing necessary files for kdm bespin theme
mkdir -p %buildroot/%_K4apps/kdm/themes/Bespin
cp -ar kdm/* %buildroot/%_K4apps/kdm/themes/Bespin
install -m 0644 %SOURCE1 %buildroot/%_K4apps/kdm/themes/Bespin/screenshot.png

# Installing necessary files for ksplash bespin theme
mkdir -p %buildroot/%_K4apps/ksplash/Themes/Bespin
pushd ksplash
cp -ar . %buildroot/%_K4apps/ksplash/Themes/Bespin/
rm -f %buildroot/%_K4apps/ksplash/Themes/Bespin/*.sh
popd

# Creating the icons package
pushd icons
mkdir -p %buildroot/%_iconsdir/
cp -ar Bespin %buildroot/%_iconsdir/
popd

%files
%files common

%files core
%doc README presets/
%_K4bindir/bespin
%_K4libdir/libQtBespin.so
%_man1dir/bespin.*

%files widgets
%_K4libdir/qt4/plugins/styles/libbespin.so
%_K4lib/kstyle_bespin_config.so
%_K4apps/kstyle/themes/bespin.themerc

%files kwin
%_K4apps/kwin/bespin.desktop
%_K4lib/kwin3_bespin.so
%_K4lib/kwin_bespin_config.so

%files -n plasma-applet-xbar
%doc XBar/xbar.txt
%_K4lib/plasma_applet_xbar.so
%_K4srv/plasma-applet-xbar.desktop

%files -n bash-completion-bespin
%config(noreplace) %_sysconfdir/bash_completion.d/bespin-compl

%files ksplash
%_K4apps/ksplash/Themes/*/

%files kdm
%_K4apps/kdm/themes/Bespin/

%files -n icon-theme-bespin
%_iconsdir/Bespin/

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0.1658-alt1.qa1
- NMU: applied repocop patch

* Mon Apr 08 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0.1658-alt1
- New SVN snapshot

* Mon Apr 08 2013 Andrey Cherepanov <cas@altlinux.org>  0.1.0.1228-alt1.2
- Remove duplicate dependencies

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0.1228-alt1.1
- Fixed build

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.0.1228-alt1
- update to svn r1228

* Mon Apr 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.0.1076-alt0.M51.1
- built for M51

* Fri Apr 23 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.0.1076-alt1
- initial build
