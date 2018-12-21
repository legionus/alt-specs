
Name:		packageinstall
Version:	1.1.2
Release:	alt1
Summary:	GUI frontend for install packages using apt-get

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/PackageInstall

Packager:   	Andrey Cherepanov <cas@altlinux.org>

Requires: apt consolehelper

Source0:	%name-%version.tar.gz

BuildRequires(pre): libpam-devel
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-tools

%description
This application is GUI frontend for install package(s) using apt-get.

%prep
%setup -q
%qmake_qt5 PREFIX=%_prefix %name.pro

%build
%make_build
lrelease-qt5 %name.pro

%install
%installqt5
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/%name %buildroot%_sbindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -pD -m640 %name.pamd %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %name.security %buildroot%_sysconfdir/security/console.apps/%name
for f in *.qm; do install -m 0644 $f %buildroot/%_datadir/apps/%name/ ||: ; done

%files
%doc AUTHORS README
%_bindir/%name
%_sbindir/%name
%dir %_datadir/apps/%name/
%_datadir/apps/%name/
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
* Fri Nov 02 2018 Sergey V Turchin <zerg at altlinux dot org> 1.1.2-alt1
- port to Qt5

* Tue Oct 02 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.1-alt2
- spec cleanup

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.1.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Reset show details on show information

* Tue Jul 26 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Complete rewrite UI
- Append statistics to main dialog
- Copy apt output to console
- Use buffer read apt output (closes: #25882)
- Add support for debug script
- Do not show statistics if it is no additional packages to install

* Mon Sep 20 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- clear spec
- small fixes

* Thu Mar 19 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial release


