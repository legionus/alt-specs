Name: tong
Version: 1.3
Release: alt1

Summary: Tetris meets Pong
Summary(ru_RU.KOI8-R): ������, ����ݣ���� � ������

License: %gpl3plus
Group: Games/Arcade
Url: http://www.nongnu.org/tong/

Requires: %name-data = %version-%release

Source: %name-%version.tar.gz
Source1: %name.desktop
Patch1: %name-1.3-fix-link-as-needed.patch

BuildRequires: rpm-build-licenses
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel

%description
Tetris and Pong are classics. TONG is the result of mixing the two,
capitalizing on the essential qualities of each classic and adding new
twists of its own to make an explosive chemical reaction out of it all.

%description -l ru_RU.KOI8-R
Tetris � Pong - ��� ��������. TONG - ��� ��������� �� ����������
� �������� �� ������� �������� ������ �� ������������ ���� � �����������
����������� ��������. ��������� ��������� �������� ������������� :)

%package data
Summary: Tetris meets Pong
Group: Games/Arcade
Requires(pre): %name = %version-%release
BuildArch: noarch

%description data
This package contains data files for Tong game. You don't need to install
this package explicitly - it will be installed along with the main package
as a dependency.

%prep
%setup
%patch1
subst "s|media/|%_gamesdatadir/%name/media/|" *.cpp option.h
rm -rf media/gp2x media/wii

%build
%make_build

%install
mkdir -p %buildroot%_gamesdatadir/%name/media
install -pD -m755 %name %buildroot%_gamesbindir/%name
install -pD -m644 media/* %buildroot%_gamesdatadir/%name/media/
install -pD -m644 media/icon.png %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_gamesbindir/%name
%_niconsdir/%name.png
%_desktopdir/%name.desktop
%doc CHANGELOG COPYING CREDITS README

%files data
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/media

%changelog
* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Autobuild version bump to 1.3
- Fix build

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sat Aug 22 2009 Alexey Rusakov <ktirf@altlinux.org> 1.0-alt3
- Put the game data to a separate noarch subpackage.
- Massive spec cleanup:
  + obsolete post/postun scripts removed
  + .desktop file no more upsets repocop
  + the icon is no more installed in a deprecated location
  + %%__ macros removed
  + License tag fixed (GPL -> %gpl2plus)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for tong

* Thu Mar 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.0-alt2
- Fixed linking with --as-needed.
- Removed Debian menu support.

* Tue Feb 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.0-alt1
- Initial Sisyphus package.

