Name: lostsky
Version: 1.0.1
Release: alt1
%setup_python_module %name
Summary: Turn based strategy RPG with gameplay similar to Fire Emblem
BuildArch: noarch
License: BSD
Group: Games/Strategy
Source: lost-sky-project-public-1.0.1.tar
Url: https://bitbucket.org/featheredmelody/lost-sky-project-public

# Automatically added by buildreq on Tue Aug 23 2011
# optimized out: python-base
BuildRequires: fonts-ttf-dejavu fonts-ttf-vera

BuildRequires: python-devel rpm-macros-fonts

%add_python_req_skip py2exe

%description
Story of a Lost Sky is a Turn Based Strategy RPG with gameplay that is
similar to Fire Emblem. Units are placed on a tile map and each side
takes turns moving and attacking. Outside the battle map, the player is
able to customize their characters and equip new spells and traits. The
game is developed in Python using the Pygame library.

%package -n %packagename
Group: Games/Strategy
Summary: Python module for %name, %summary
%description -n %packagename
Python module for %name, %summary

%prep
%setup -n lost-sky-project-public-%version
cd "Story of a Lost Sky"
cat > %name.sh <<@@@
#!/bin/sh -e
cd "%_gamesdatadir/%name"
python srpg.py
@@@

%build
cd "Story of a Lost Sky"
# use system fonts instead of local ones
for f in *.ttf; do
  ls %_ttffontsdir/*/$f && ln -sf %_fontsdir/ttf/*/$f $f
done

%install
cd "Story of a Lost Sky"
install -D -m755 %name.sh %buildroot%_gamesbindir/%name
mkdir -p %buildroot%python_sitelibdir_noarch
cp -a %name %buildroot%python_sitelibdir_noarch/
mkdir -p %buildroot%_gamesdatadir/%name
cp -a [^l]* %buildroot%_gamesdatadir/%name/
# Stupid case insensivity
ln -s prerendered_spells %buildroot%_gamesdatadir/%name/images/anim/prerendered_Spells

%files
%doc */*.txt
%_gamesbindir/%name
%_gamesdatadir/%name

%files -n %packagename
%python_sitelibdir_noarch/%name

%changelog
* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1
- Autobuild version bump to 0.9.0
- Drop ~/.lostsky usage: game use ~/.local and ~/.config now

* Mon Feb 18 2013 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Autobuild version bump to 0.8.0

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 0.7.0-alt2
- Build from bugfix hg tip

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 0.7.0-alt1
- Autobuild version bump to 0.7.0
- Move to hg upstream update scheme

* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 0.6.1-alt1
- Autobuild version bump to 0.6.1
- Fix build

* Mon Aug 22 2011 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Initial 'old version' build from scratch

