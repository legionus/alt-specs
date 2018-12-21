BuildRequires: desktop-file-utils

Name:		rpminstall
Version:	1.1.4
Release:	alt1
Summary:	Graphical application for install RPM packages using apt-get

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/Rpminstall

Packager:   	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-tools
Requires: packageinstall

%description
Graphical application for install RPM packages using apt-get.

%prep
%setup -q
export PREFIX=%_prefix
%qmake_qt5 %name.pro

%build
%make_build
lrelease-qt5 %name.pro

%install
%installqt5
install -Dm644 apturl.js %buildroot%_libdir/firefox/defaults/preferences/apturl.js
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=Settings \
	--add-category=PackageManager \
	%buildroot%_desktopdir/rpminstall.desktop
for f in *.qm; do install -m 0644 $f %buildroot/%_datadir/apps/%name/ ||: ; done

%files
%doc AUTHORS README
%_bindir/%name
%dir %_datadir/apps/%name/
%_datadir/apps/%name/*
%_desktopdir/%name.desktop
%_datadir/services/apt.protocol
%_niconsdir/%name.png
%_libdir/firefox/defaults/preferences/apturl.js

%changelog
* Fri Nov 02 2018 Sergey V Turchin <zerg at altlinux dot org> 1.1.4-alt1
- port to Qt5

* Tue Oct 02 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.3-alt2
- spec cleanup

* Tue Aug 28 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for rpminstall

* Thu Dec 08 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- Move menu entry to System menu (like Synaptic)

* Mon Aug 29 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Remove apt:// prefix from arguments (thanks viy@) (closes: #26170)

* Mon Aug 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Complete support of apt:// protocol in Firefox (thanks viy@)

* Tue Jul 26 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Use for support apt:// protocol
- Hide interactive bar by default

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for rpminstall

* Mon Dec 27 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- unhide desktop entry

* Wed Nov 10 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- hide desktop entry in menu
- fix URL of project site (thanks Lenar Shakirov)

* Sun Sep 19 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial release to Sisyphus
