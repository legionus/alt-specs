%def_disable kactivities

Name:         rekonq
Version:      2.4.2
Release:      alt4

Group:        Networking/WWW
Summary:      Web browser easy for use
License:      GPLv3
Url: http://rekonq.sourceforge.net/

PreReq(post,preun): alternatives >= 0.2
Provides: webclient

Source:      %name-%version.tar
Source10: ru.po

# Automatically added by buildreq on Wed Mar 23 2011 (-bi)
#BuildRequires: cvs gcc-c++ git-core glib2-devel kde4libs-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel mercurial openssh-common qt4-designer subversion valgrind zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt4-devel zlib-devel qoauth-devel libqca2-devel
BuildRequires: libalternatives-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel
BuildRequires: libXt-devel libXtst-devel libXv-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel desktop-file-utils
%if_enabled kactivities
BuildRequires: kde4-kactivities-devel
%endif

%description
Web browser easy for use.

%prep
%setup -q
mkdir -p po/ru/
cp -ar po/de/CMakeLists.txt po/ru/
sed -i 's|GETTEXT_PROCESS_PO_FILES.*INSTALL_DESTINATION|GETTEXT_PROCESS_PO_FILES(ru ALL INSTALL_DESTINATION|' po/ru/CMakeLists.txt
echo 'add_subdirectory(ru)' >> po/CMakeLists.txt
install -m 0644 %SOURCE10 po/ru/rekonq.po

%if_disabled kactivities
sed -i 's|.*FIND_PACKAGE.*KActivities.*||' CMakeLists.txt
%endif


%build
%K4cmake
%K4make


%install
%K4install

# install alternative
mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K4bindir/rekonq      101
%_bindir/x-www-browser       %_K4bindir/rekonq      101
__EOF__

# add mime types categories
desktop-file-install --dir %buildroot/%_K4xdg_apps --add-mime-type=x-scheme-handler/http --add-mime-type=x-scheme-handler/https --add-mime-type=x-scheme-handler/ftp %buildroot/%_K4xdg_apps/rekonq.desktop

%K4find_lang --with-kde %name
#%K4find_lang --with-kde --append --output=%name.lang kwebapp


%files -f %name.lang
%doc AUTHORS ChangeLog TODO
%config %_sysconfdir/alternatives/packages.d/%name
%_K4bindir/%name
#%_K4bindir/kwebapp
%_K4libdir/libkdeinit4_rekonq.so
%_K4xdg_apps/%name.desktop
%_K4apps/%name/
%_K4iconsdir/hicolor/*/apps/%name.*
%_K4cfg/%name.kcfg

%changelog
* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt4
- disable Activities support

* Mon Dec 07 2015 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt2.M70P.1
- built for M70P

* Mon Dec 07 2015 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt3
- add Russian translation; thanks Koi@forum.altlinux (ALT#31595)

* Tue Jun 24 2014 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt2
- built with Activities support

* Mon Jan 13 2014 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt0.M70P.1
- built for M70P

* Mon Jan 13 2014 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt1
- new version

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt0.M70P.1
- built for M70P

* Fri Nov 22 2013 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt1
- new version

* Thu Jul 25 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt1
- new version

* Fri Mar 15 2013 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt1
- new version

* Thu Mar 07 2013 Sergey V Turchin <zerg@altlinux.org> 2.2-alt1
- new version

* Mon Jan 28 2013 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- new version

* Wed Jan 09 2013 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1
- new version

* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Mon Oct 08 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon Jul 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M60P.1
- built for M60P

* Mon Jul 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- new version

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt0.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt0.M60P.1
- built for M60P

* Mon Apr 02 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Thu Mar 22 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Sat Jan 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt0.M60P.1
- built for M60P

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version
- add x-www-browser alternative

* Mon Oct 17 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Sep 22 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.92-alt1
- new version

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt2
- add x-scheme-handler mimetypes

* Mon Apr 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.95-alt1
- 0.7 RC

* Wed Oct 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- initial build
