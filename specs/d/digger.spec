Name: digger
Version: 20130313
Release: alt1.qa1

Summary: A Game of Digger

License: Distributable
Group: Games/Arcade
Url: http://www.digger.org

Source: %url/%name-%version.tar.gz
Patch: digger-20020314-alt-gcc34.patch

Source11: %name-16x16.png
Source12: %name-32x32.png
Source13: %name-48x48.png

#Packager: Sergey Balbeko <balbeko@altlinux.org>
#Packager: Michael Shigorin <mike@altlinux.ru>
#Packager: Dima Pashko <troll@watersport.com.ua>

# Automatically added by buildreq on Thu Apr 14 2016
# optimized out: cmake-modules libX11-devel libgpg-error libjson-c python-base xorg-xproto-devel
BuildRequires: cmake libSDL-devel zlib-devel

BuildRequires(pre): rpm-macros-cmake

%description
Digger is one of most popular games on IBM PC.

%prep
%setup
#patch -p1

%build
%cmake_insource
%make_build

%install
install -pD -m755 digger %buildroot%_gamesbindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Digger
GenericName=The Digger
Comment=%{summary}
Icon=%{name}
Exec=%_gamesbindir/%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

echo "Please see %url/faq.html" >> FAQ

install -m644 %SOURCE11 -D %buildroot%_miconsdir/%name.png
install -m644 %SOURCE12 -D %buildroot%_iconsdir/%name.png
install -m644 %SOURCE13 -D %buildroot%_liconsdir/%name.png

%files
%doc digger.txt FAQ
%_gamesbindir/*
%_desktopdir/*
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Apr 14 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 20130313-alt1.qa1
- Removed libaudio fron BR.
- Updated BR with buildreq.

* Tue Dec 22 2015 Vitaly Lipatov <lav@altlinux.ru> 20130313-alt1
- upgrade source to 20130313 (ALT bug #31573)
- build with cmake, add icons

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20020314-alt4.qa3
- NMU: rebuilt for updated dependencies.

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 20020314-alt4.qa2
- converted debian menu to freedesktop

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20020314-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for digger
  * postclean-05-filetriggers for spec file

* Mon Mar 31 2008 Sergey Balbeko <balbeko@altlinux.org> 20020314-alt4
- rebuilt with xorg

* Sat Feb 26 2005 Michael Shigorin <mike@altlinux.ru> 20020314-alt3
- rebuilt with gcc3.4

* Tue Mar 23 2004 Michael Shigorin <mike@altlinux.ru> 20020314-alt2
- built with gcc3.2

* Wed Sep 24 2003 Michael Shigorin <mike@altlinux.ru> 20020314-alt1
- cleaned up for Sisyphus as Dima seems to be too busy
- added menu file

* Wed Feb 12 2003 Dima Pashko <troll@watersport.com.ua> 0.0.1-alt1
- initial build

