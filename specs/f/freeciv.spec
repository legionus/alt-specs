Name: freeciv
Version: 2.5.11
Release: alt1

Summary: Turn-based strategy game inspired by the history of human civilization
License: GPLv2+
Group: Games/Strategy
Url: http://www.freeciv.org/

%define srcname %name-%version%{?beta_ver:-beta%beta_ver}
# http://download.sourceforge.net/freeciv/%srcname.tar.bz2
Source0: %srcname.tar
Source1: freeciv-wrapper
# git://git.altlinux.org/gears/f/freeciv.git
Patch: freeciv-%version-%release.patch

Requires: %name-client = %version-%release
Requires: %name-server = %version-%release

%def_enable gtk2
%def_disable gtk3

%{?_enable_gtk2:BuildPreReq: libgtk+2-devel}
%{?_enable_gtk3:BuildPreReq: libgtk+3-devel}

# Automatically added by buildreq on Tue Aug 09 2011 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: bzlib-devel gcc-c++ hardlink libcurl-devel liblzma-devel libreadline-devel zlib-devel

%package common
Summary: The Freeciv multi-player strategy game common files
Group: Games/Strategy
BuildArch: noarch
Provides: /usr/lib/freeciv/wrapper
Obsoletes: %name-manual < %version

%package -n lib%name
Summary: The Freeciv multi-player strategy game common library
Group: Games/Strategy

%package server
Summary: The Freeciv multi-player strategy game server
Group: Games/Strategy
Requires: %name-common = %version-%release
Requires: lib%name = %version-%release
Requires: %name-server-data = %version-%release

%package server-data
Summary: The Freeciv multi-player strategy game server data files
Group: Games/Strategy
BuildArch: noarch
Conflicts: %name-server < %version-%release

%package client
Summary: The Freeciv multi-player strategy game client
Group: Games/Strategy
Requires: %name-common = %version-%release
Requires: lib%name = %version-%release
Requires: %name-client-data = %version-%release
Provides: %name-client-gui = %version-%release
%if_enabled gtk2
Provides: %name-client-gtk2 = %version-%release
Obsoletes: %name-client-gtk2 < %version-%release
%endif
%if_enabled gtk3
Provides: %name-client-gtk3 = %version-%release
Obsoletes: %name-client-gtk3 < %version-%release
%endif

%package client-data
Summary: The Freeciv multi-player strategy game client data files
Group: Games/Strategy
BuildArch: noarch
Conflicts: %name-client < %version-%release

%description
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

%description common
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains files common for client ans server.

%description -n lib%name
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains a shared library for client ans server.

%description server
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains the Freeciv server.

%description server-data
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains the Freeciv server data files.

%description client
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains the Freeciv client.

%description client-data
Freeciv is a turn-based, multi-player, X based strategy game.  Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R).  In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

This package contains the Freeciv client data files.

%prep
%setup -n %srcname
%patch -p1

%build
rm *.m4
%autoreconf

%configure \
	--enable-shared \
	--disable-static \
	--enable-server \
	--enable-client=no%{?_enable_gtk2:,gtk2}%{?_enable_gtk3:,gtk3} \
	--without-freeciv-manual \
	--disable-silent-rules
%make_build MSUBDIRS=

%install
%makeinstall_std MSUBDIRS=
rm %buildroot%_libdir/libfreeciv.so

install -pD -m755 %_sourcedir/freeciv-wrapper \
	%buildroot%_libexecdir/%name/wrapper
sed -i 's,@LIBEXECDIR@,%_libexecdir,g' \
	%buildroot%_libexecdir/%name/wrapper
mv %buildroot%_bindir/freeciv-server %buildroot%_libexecdir/%name/
ln -rs %buildroot%_libexecdir/%name/wrapper %buildroot%_bindir/freeciv-server

rm %buildroot%_man6dir/freeciv-{gtk2,gtk3,manual,qt,sdl,xaw}.6
rm %buildroot%_man6dir/freeciv-mp-{cli,gtk2,gtk3,qt}.6
%if_enabled gtk2
ln -s freeciv-client.6 %buildroot%_man6dir/freeciv-gtk2.6
ln -s freeciv-modpack.6 %buildroot%_man6dir/freeciv-mp-gtk2.6
%endif
%if_enabled gtk3
ln -s freeciv-client.6 %buildroot%_man6dir/freeciv-gtk3.6
ln -s freeciv-modpack.6 %buildroot%_man6dir/freeciv-mp-gtk3.6
%endif

hardlink -cv %buildroot
%find_lang --output=%name.lang %name %name-nations

%files

%files common -f %name.lang
%dir %_libexecdir/%name
%_libexecdir/%name/wrapper
%dir %_datadir/%name
%_docdir/%name/

%files -n lib%name
%_libdir/libfreeciv.*

%files server
%config /etc/freeciv/database.lua
%_bindir/freeciv-server
%dir %_libexecdir/%name
%_libexecdir/%name/freeciv-server

%files server-data
%_datadir/appdata/%name-server.appdata.xml
%_desktopdir/%name-server.desktop
%_iconsdir/hicolor/*/apps/%name-server.png
%_man6dir/freeciv-server.*
%_datadir/%name/cimpletoon*
%_datadir/%name/civ*
%_datadir/%name/classic*
%_datadir/%name/default*
%_datadir/%name/experimental*
%_datadir/%name/multiplayer*
%_datadir/%name/nation
%_datadir/%name/scenarios

%files client
%if_enabled gtk2
%_bindir/freeciv-gtk2
%_bindir/freeciv-mp-gtk2
%endif
%if_enabled gtk3
%_bindir/freeciv-gtk3
%_bindir/freeciv-mp-gtk3
%endif

%files client-data
%if_enabled gtk2
%_datadir/appdata/%name-gtk2.appdata.xml
%_desktopdir/%name-gtk2.desktop
%_man6dir/freeciv-gtk2.*
%_datadir/%name/freeciv.rc*
%endif
%if_enabled gtk3
%_datadir/appdata/%name-gtk3.appdata.xml
%_desktopdir/%name-gtk3.desktop
%_man6dir/freeciv-gtk3.*
%endif
%_iconsdir/hicolor/*/apps/%name-client.png
%_iconsdir/hicolor/*/apps/%name-modpack.png
%_pixmapsdir/%name-client.png
%_man6dir/freeciv-client.*
%_datadir/appdata/%name-mp-*.appdata.xml
%_desktopdir/%name-mp-*.desktop
%_man6dir/freeciv-modpack.*
%_man6dir/freeciv-mp-*
%_datadir/%name/amplio*
%_datadir/%name/buildings*
%_datadir/%name/flags
%_datadir/%name/gtk*
%_datadir/%name/helpdata.txt
%_datadir/%name/hex2t*
%_datadir/%name/isophex*
%_datadir/%name/misc
%_datadir/%name/stdsounds*
%_datadir/%name/themes
%_datadir/%name/*trident*
%_datadir/%name/wonders*

%changelog
* Sat Mar 24 2018 Dmitry V. Levin <ldv@altlinux.org> 2.5.11-alt1
- 2.5.3 -> 2.5.11 (closes: #33777, #33779).

* Sun Mar 13 2016 Dmitry V. Levin <ldv@altlinux.org> 2.5.3-alt1
- Updated to 2.5.3 release.

* Sat Feb 22 2014 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt1
- Updated to 2.4.2 release.

* Sat Nov 30 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.1-alt1
- Updated to 2.4.1 release.

* Sun Sep 22 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0 release.

* Sat Feb 16 2013 Dmitry V. Levin <ldv@altlinux.org> 2.3.4-alt1
- Updated to 2.3.4 release.

* Sat Dec 08 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3.3-alt1
- Updated to 2.3.3 release.

* Tue Sep 18 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt1
- Updated to 2.3.2 release.

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1 release.

* Tue Aug 09 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0 release.

* Fri Mar 11 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.5-alt1
- Updated to 2.2.5 release.
- Tweaked interpackage dependencies to workaround a bug in rpmbuild.

* Sun Dec 26 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt1
- Updated to 2.2.4 release.

* Tue Sep 14 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3 release.

* Fri Aug 13 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- Updated to 2.2.2 release.
- Split out noarch part of -client and -server subpackages to
  -client-data and -server-data subpackages.

* Sat Jun 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1 release.

* Fri Mar 12 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0 release.
- Linked with system liblua.

* Sat Mar 06 2010 Dmitry V. Levin <ldv@altlinux.org> 2.1.11-alt1
- Updated to 2.1.11 release.

* Sat Nov 28 2009 Dmitry V. Levin <ldv@altlinux.org> 2.1.10-alt1
- Updated to 2.1.10 release.

* Mon Apr 13 2009 Dmitry V. Levin <ldv@altlinux.org> 2.1.9-alt1
- Updated to 2.1.9 release (closes: #19251).
- Obsoletes freeciv-manual (closes: #17010).

* Sat Dec 13 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.8-alt2
- freeciv-common: Provide /usr/lib/freeciv/wrapper.

* Fri Dec 12 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.8-alt1
- Updated to 2.1.8 release.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.6-alt1
- Updated to 2.1.6 release.

* Sat Apr 26 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.4-alt1
- Updated to 2.1.4 release.

* Thu Apr 10 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.3-alt2
- Use %%update_menus/%%clean_menus (reported by repocop).
- Drop %%update_desktopdb/%%clean_desktopdb (reported by Igor Vlasenko).
- Do not package developer docs (reported by Slava Semushin).

* Fri Feb 08 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.3-alt1
- Updated to 2.1.3 release.
- Dropped outdated manual (#14145).

* Mon Jan 07 2008 Dmitry V. Levin <ldv@altlinux.org> 2.1.2-alt1
- Updated to 2.1.2 release.

* Fri Nov 30 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1.1-alt1
- Updated to 2.1.1 release.

* Fri Nov 02 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0 release.
- Switched from menu files to desktop files.

* Sun Apr 22 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.1.0-alt0.b4
- NMU:
  + Updated to 2.1.0-beta4
    + New default tileset: "amplio"
    + New default port: 5556
  + Removed revolt patch (changed patch was merged)
  + Removed reveal patch
  + Used %%make_install instead of %%makeinstall

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.8-alt1
- Updated to 2.0.8 release.
- Updated build dependencies.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.7-alt2.1
- Rebuilt with libreadline.so.5.

* Wed Nov 30 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt2
- Relocated helpers from %%_libdir to %%_libexecdir (#8573).

* Thu Nov 10 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt1
- Updated to 2.0.7 release.

* Fri Sep 30 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.6-alt1
- Updated to 2.0.6 release.

* Thu Jun 16 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt1
- Updated to 2.0.2 release.

* Fri Apr 29 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- Updated to 2.0.1 release.

* Mon Apr 18 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt1
- Updated to 2.0.0 release.
- Updated stdsounds.
- Removed merged upstream patches.
- Updated patches.

* Sat Dec 18 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt0.3.b5
- Fixed upgrade from <= 2.0.0-alt0.1.b4 (#5733).

* Sat Dec 11 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt0.2.b5
- Updated to 2.0.0-beta5.
- Merged gtk2 client into -client subpackage,
  simplified build, removed alternatives.

* Thu Nov 25 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt0.1.b4
- Updated to 2.0.0-beta4.

* Sun Sep 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.14.2-alt1
- Updated to 1.14.2 release.
- Updated manual to 1.13.0-2.

* Sun Feb 29 2004 Dmitry V. Levin <ldv@altlinux.org> 1.14.1-alt2
- Fixed build with fresh autotools.

* Thu Dec 11 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.1-alt1
- Updated to 1.14.1 release.

* Fri Oct 31 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.1-alt0.1.b2
- Updated to 1.14.1-beta2
- Updated russian translation.

* Wed Apr 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1.14.0-alt4
- change alternatives config format

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 1.14.0-alt3
- move to new alternatives scheme

* Mon Feb 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.0-alt2
- Enhanced server wrapper a bit (#0002086).

* Sun Jan 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0 release.

* Mon Jan 13 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.0-alt0.2.b3
- Added %%triggerpostun (#0001910).
- Updated buildrequires (#0001916).

* Tue Jan 07 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.0-alt0.1.b3
- stdsounds2.
- manual-1.13.0-1.
- Fixed tinfo support.
- Added server wrapper to increase chance that cwd is writable.
- Added sound, menu and icons from MDK package.
- Set aifill to 5 on new servers to get some opponents (RH idea).
- Be a bit more verbose about revolution.
- Corrected russian translation a bit.
- Packaged server as separate subpackage.
- Packaged clients as separate subpackages.

* Fri Jan 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.14.0-alt0.0.1.b3
- freeciv-1.14.0-beta3.
