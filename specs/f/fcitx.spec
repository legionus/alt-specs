# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install pkgconfig(cairo-xlib) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(xkbcommon)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx.conf
%{!?gtk2_binary_version: %global gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
%{!?gtk3_binary_version: %global gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}

Name:			fcitx
Summary:		An input method framework
Version:		4.2.9.4
Release:		alt1_1
License:		GPLv2+
Group:			Graphical desktop/Other
URL:			https://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/fcitx/%{name}-%{version}_dict.tar.xz
Source1:		xinput-%{name}
BuildRequires:		gcc-c++
BuildRequires:		libpango-devel libpango-gir-devel, libdbus-devel, opencc-devel
BuildRequires:		wget, intltool, chrpath, sysconftool, opencc
BuildRequires:		ctest cmake, libtool, doxygen, libicu-devel
BuildRequires:		libqt4-declarative libqt4-devel qt4-designer gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel, libicu
BuildRequires:		xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-dri2proto-devel xorg-dri3proto-devel xorg-evieproto-devel xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-pmproto-devel xorg-presentproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel, xorg-xtrans-devel
BuildRequires:		gobject-introspection-devel, libxkbfile-devel
BuildRequires:		libenchant-devel, iso-codes-devel, libicu-devel
BuildRequires:		libX11-devel, libdbus-glib-devel, dbus-tools-gui
BuildRequires:		desktop-file-utils, libxml2-devel
BuildRequires:		lua-devel, extra-cmake-modules
BuildRequires:		xkeyboard-config-devel
Requires:		%{name}-data = %{version}-%{release}
Requires:		imsettings
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-gtk3 = %{version}-%{release}
Requires:		%{name}-gtk2 = %{version}-%{release}
Source44: import.info
#AutoReq: yes,noshell

%description
Fcitx is an input method framework with extension support. Currently it
supports Linux and Unix systems like FreeBSD.

Fcitx tries to provide a native feeling under all desktop as well as a light
weight core. You can easily customize it to fit your requirements.

%package data
Summary:		Data files of Fcitx
Group:			System/Libraries
BuildArch:		noarch
Requires:		icon-theme-hicolor
Requires:		dbus dbus-tools

%description data
The %{name}-data package provides shared data for Fcitx.

%package libs
Summary:		Shared libraries for Fcitx
Group:			System/Libraries
Provides:		%{name}-keyboard = %{version}-%{release}
Obsoletes:		%{name}-keyboard =< 4.2.3

%description libs
The %{name}-libs package provides shared libraries for Fcitx

%package devel
Summary:		Development files for Fcitx
Group:			Development/Other
Requires:		%{name}-libs = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx libraries.

%package table-chinese
Summary:		Chinese table of Fcitx
Group:			System/Libraries
BuildArch:		noarch
Requires:		%{name}-table = %{version}-%{release}

%description table-chinese
The %{name}-table-chinese package provides other Chinese table for Fcitx.

%package gtk2
Summary:		Fcitx IM module for gtk2
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}

%description gtk2
This package contains Fcitx IM module for gtk2.

%package gtk3
Summary:		Fcitx IM module for gtk3
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		imsettings-gsettings

%description gtk3
This package contains Fcitx IM module for gtk3.

%package qt4
Summary:		Fcitx IM module for qt4
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}

%description qt4
This package contains Fcitx IM module for qt4.

%package pinyin
Summary:		Pinyin Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Built-in_Pinyin
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}

%description pinyin
This package contains pinyin engine for Fcitx.

%package qw
Summary:		Quwei Engine for Fcitx
URL:			https://fcitx-im.org/wiki/QuWei
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}

%description qw
This package contains Quwei engine for Fcitx.

%package table
Summary:		Table Engine for Fcitx
URL:			https://fcitx-im.org/wiki/Table
Group:			System/Libraries
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{name}-data = %{version}-%{release}
Requires:		%{name}-pinyin = %{version}-%{release}

%description table
This package contains table engine for Fcitx.


%prep
%setup -q

%build
mkdir -p build
pushd build
%{fedora_cmake} .. -DENABLE_GTK3_IM_MODULE=On -DENABLE_QT_IM_MODULE=On -DENABLE_OPENCC=On -DENABLE_LUA=On -DENABLE_GIR=On -DENABLE_XDGAUTOSTART=Off
make VERBOSE=1 %{?_smp_mflags}

%install
%makeinstall_std INSTALL="install -p" -C build

find %{buildroot}%{_libdir} -name '*.la' -delete -print

install -pm 644 -D %{SOURCE1} %{buildroot}%{_xinputconf}

# patch fcitx4-config to use pkg-config to solve libdir to avoid multiarch
# confilict
sed -i -e 's:%{_libdir}:`pkg-config --variable=libdir fcitx`:g' \
  %{buildroot}%{_bindir}/fcitx4-config

chmod +x %{buildroot}%{_datadir}/%{name}/data/env_setup.sh

%find_lang %{name}

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-skin-installer.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_fcitx<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_xinputconf}	55
EOF

sed -i -e '1,1s/env bash$/env bash4/' %{buildroot}%{_bindir}/fcitx-diagnose

%files -f %{name}.lang
%_altdir/xinputrc_fcitx
%doc AUTHORS ChangeLog THANKS TODO
%doc COPYING
%config %{_xinputconf}
%{_bindir}/fcitx-*
%{_bindir}/fcitx
%{_bindir}/createPYMB
%{_bindir}/mb2org
%{_bindir}/mb2txt
%{_bindir}/readPYBase
%{_bindir}/readPYMB
%{_bindir}/scel2org
%{_bindir}/txt2mb
%{_datadir}/applications/%{name}-skin-installer.desktop
%dir %{_datadir}/%{name}/dbus/
%{_datadir}/%{name}/dbus/daemon.conf
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-fskin.xml
%{_mandir}/man1/createPYMB.1*
%{_mandir}/man1/fcitx-remote.1*
%{_mandir}/man1/fcitx.1*
%{_mandir}/man1/mb2org.1*
%{_mandir}/man1/mb2txt.1*
%{_mandir}/man1/readPYBase.1*
%{_mandir}/man1/readPYMB.1*
%{_mandir}/man1/scel2org.1*
%{_mandir}/man1/txt2mb.1*

%files libs
%doc COPYING
%{_libdir}/libfcitx*.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}-[!pqt]*.so
%{_libdir}/%{name}/%{name}-punc.so
%{_libdir}/%{name}/%{name}-quickphrase.so
%{_libdir}/%{name}/qt/
%{_libdir}/%{name}/libexec/
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Fcitx-1.0.typelib

%files data
%doc COPYING
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/24x24/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/skin/
%dir %{_datadir}/%{name}/addon
%{_datadir}/%{name}/addon/%{name}-[!pqt]*.conf
%{_datadir}/%{name}/addon/%{name}-punc.conf
%{_datadir}/%{name}/addon/%{name}-quickphrase.conf
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/spell/
%dir %{_datadir}/%{name}/imicon/
%dir %{_datadir}/%{name}/inputmethod/
%dir %{_datadir}/%{name}/configdesc/
%dir %{_datadir}/%{name}/table/
%{_datadir}/%{name}/configdesc/[!ft]*.desc
%{_datadir}/%{name}/configdesc/fcitx-[!p]*.desc
%{_datadir}/dbus-1/services/org.fcitx.Fcitx.service

%files devel
%doc COPYING
%{_bindir}/fcitx4-config
%{_libdir}/libfcitx*.so
%{_libdir}/pkgconfig/fcitx*.pc
%{_includedir}/fcitx*
%{_datadir}/cmake/%{name}/
%{_docdir}/%{name}/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Fcitx-1.0.gir

%files table-chinese
%doc
%{_datadir}/%{name}/table/*
%{_datadir}/%{name}/imicon/[!ps]*.png

%files pinyin
%doc
%{_datadir}/%{name}/inputmethod/pinyin.conf
%{_datadir}/%{name}/inputmethod/shuangpin.conf
%{_datadir}/%{name}/pinyin/
%{_datadir}/%{name}/configdesc/fcitx-pinyin.desc
%{_datadir}/%{name}/configdesc/fcitx-pinyin-enhance.desc
%{_datadir}/%{name}/addon/fcitx-pinyin.conf
%{_datadir}/%{name}/addon/fcitx-pinyin-enhance.conf
%{_datadir}/%{name}/imicon/pinyin.png
%{_datadir}/%{name}/imicon/shuangpin.png
%{_libdir}/%{name}/%{name}-pinyin.so
%{_libdir}/%{name}/%{name}-pinyin-enhance.so
%{_datadir}/%{name}/py-enhance/

%files qw
%doc
%{_datadir}/%{name}/inputmethod/qw.conf
%{_libdir}/%{name}/%{name}-qw.so
%{_datadir}/%{name}/addon/fcitx-qw.conf

%files table
%doc
%{_datadir}/%{name}/configdesc/table.desc
%{_libdir}/%{name}/%{name}-table.so
%{_datadir}/%{name}/addon/fcitx-table.conf

%files gtk2
%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/im-fcitx.so

%files gtk3
%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/im-fcitx.so

%files qt4
%{_libdir}/qt4/plugins/inputmethods/qtim-fcitx.so

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.9.4-alt1_1
- update by fc import

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt2.1.1
- rebuild with new lua 5.3

* Mon Feb 29 2016 Andrey Cherepanov <cas@altlinux.org> 4.2.7-alt2.1
- rebuild with new icu

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 4.2.7-alt2
- build for Sisyphus

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_4
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1_1
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.6.1-alt1_2
- initial fc import

