Name: steam
Version: 1.0.0.59
Release: alt1%ubt

Summary: Launcher for the Steam software distribution service
License: Proprietary
Group: Games/Other

URL: http://www.steampowered.com/
Packager: Nazarov Denis <nenderus@altlinux.org>
Vendor: Valve Corporation

ExclusiveArch: %ix86

Source0: http://repo.steampowered.com/%name/pool/%name/s/%name/%{name}_%version.tar.gz
Patch0: %name-apt-alt.patch
Patch1: %name-bash4-alt.patch
Patch2: %name-desktop-alt.patch
Patch3: %name-udev-alt.patch

BuildPreReq: rpm-build-ubt

Requires: curl
Requires: glibc-pthread >= 2.15
Requires: glibc-nss >= 2.15
Requires: libGL
Requires: libnss
Requires: xz

BuildRequires: bash4
BuildRequires: ca-certificates

%description
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%install
%makeinstall_std
%__rm -rf %buildroot%_bindir/%{name}deps
%__install -Dp -m0644 lib/udev/rules.d/60-%name-input.rules %buildroot%_udevrulesdir/60-%name-input.rules
%__install -Dp -m0644 lib/udev/rules.d/60-%name-vr.rules %buildroot%_udevrulesdir/60-%name-vr.rules

# Fix use bash4
%__mkdir_p %buildroot%_libexecdir/%name/bin
%__ln_s /bin/bash4 %buildroot%_libexecdir/%name/bin/bash

# Fix connection via SSL
%__mkdir_p %buildroot%_sysconfdir/ssl/certs
%__ln_s %_sysconfdir/pki/tls/certs/ca-bundle.crt %buildroot%_sysconfdir/ssl/certs/ca-certificates.crt

%files
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*
%_desktopdir/*
%_docdir/*
%_miconsdir/*
%dir %_iconsdir/hicolor/24x24
%dir %_iconsdir/hicolor/24x24/apps
%_iconsdir/hicolor/24x24/apps/*
%_niconsdir/*
%_liconsdir/*
%dir %_iconsdir/hicolor/256x256
%dir %_iconsdir/hicolor/256x256/apps
%_iconsdir/hicolor/256x256/apps/*
%_man6dir/*
%_pixmapsdir/*
%config %_udevrulesdir/60-%name-input.rules
%config %_udevrulesdir/60-%name-vr.rules
%dir %_sysconfdir/ssl
%dir %_sysconfdir/ssl/certs
%_sysconfdir/ssl/certs/ca-certificates.crt

%changelog 
* Fri Dec 14 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.59-alt1%ubt
- Version 1.0.0.59

* Thu Aug 30 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.56-alt1%ubt
- Version 1.0.0.56

* Mon Jul 30 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.55-alt1%ubt
- Version 1.0.0.55

* Wed Sep 06 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt6%ubt
- Fix connection via SSL (ALT #33849)

* Fri Sep 01 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt5%ubt
- Fix use bash4

* Sat Aug 19 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt4%ubt
- Add patch for desktop-file (ALT #33771)

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt0.M80P.1
- Build for branch p8

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt3
- Fix udev rules for correctly emulation gamepad with Steam Controller after reconnect

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt2
- Add patch to fix udev rules for correctly emulation gamepad with Steam Controller

* Thu Nov 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt1
- Version 1.0.0.54

* Sat Oct 29 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.53-alt0.M70P.1
- Build for branch p7

* Thu Oct 27 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0.53-alt0.M80P.1
- Backport new version to p8 branch

* Wed Oct 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.53-alt1
- Version 1.0.0.53

* Sat Apr 02 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.52-alt0.M70P.1
- Build for branch p7

* Sat Apr 02 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.52-alt1
- Version 1.0.0.52

* Sat Nov 28 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.51-alt0.M70P.1
- Build for branch p7

* Fri Nov 27 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.51-alt1
- Version 1.0.0.51

* Wed May 06 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.50-alt0.M70P.1
- Build for branch p7

* Wed May 06 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.50-alt1
- Version 1.0.0.50

* Fri Sep 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt1.M70P.1
- Build for branch p7

* Fri Sep 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt2
- Added require on libnss (fix error "Failed to load NSS libraries")

* Fri Aug 29 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt0.M70P.1
- Build for branch p7

* Thu Aug 28 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt1
- Version 1.0.0.49

* Fri Jun 20 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.48-alt0.M70P.1
- Build for branch p7

* Thu Jun 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.48-alt1
- Version 1.0.0.48

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.47-alt0.M70P.1
- Build for branch p7

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.47-alt1
- Version 1.0.0.47

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt0.M70P.1
- Build for branch p7

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt1
- Version 1.0.0.45

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70P.1
- Build for branch p7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70T.1
- Build for branch t7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt1
- Version 1.0.0.44

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt0.M70P.1
- Build for branch p7

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt1
- Version 1.0.0.43

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt0.M70P.1
- Build for branch p7

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt1
- Version 1.0.0.42

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt0.M70P.1
- Build for branch p7 (ALT #29322)

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt1
- Version 1.0.0.41

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt0.M70P.1
- Build for branch p7

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt1
- Version 1.0.0.40

* Sun May 12 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt0.M70P.1
- Build for branch p7

* Sat May 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt1
- Version 1.0.0.39

* Sun May 05 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt0.M70P.1
- Build for branch p7

* Sat Apr 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt1
- Version 1.0.0.38

* Wed Apr 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.37-alt1
- Version 1.0.0.37

* Wed Mar 13 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.36-alt1
- Version 1.0.0.36

* Wed Mar 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt2
- Fix resolved DNS on x86_64 (ALT #28640)

* Sat Mar 02 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt1
- Version 1.0.0.35

* Mon Feb 25 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.34-alt1
- Version 1.0.0.34
- Added requires on curl and xz

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt2
- Fix summary title

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt1
- Version 1.0.0.33

* Wed Feb 20 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.29-alt1
- Version 1.0.0.29

* Sat Feb 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.28-alt1
- Version 1.0.0.28
- Added require on mozilla-plugin-adobe-flash

* Fri Feb 15 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.27-alt1
- Version 1.0.0.27

* Mon Feb 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt2
- Fix end of line in desktop file

* Sun Feb 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt1
- Initial build for ALT Linux

