Name: flatcam
Version: 8.5
Release: alt3.20170702
Summary: 2D Computer-Aided PCB Manufacturing
Group: Engineering
License: MIT
Url: https://bitbucket.org/jpcgt/flatcam.git
BuildArch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Buildrequires(pre): rpm-build-python
Buildrequires: python-module-setuptools desktop-file-utils
Requires: python-module-svg-path
Requires: python-module-matplotlib-qt4

%description
FlatCAM is a program for preparing CNC jobs for making PCBs on
a CNC router. Among other things, it can take a Gerber file
generated by your favorite PCB CAD program, and create G-Code
for Isolation routing.

%prep
%setup

%build
%python_build

%install
%python_install

# Install icons
for x in 16 24 32 48 128; do
    install -pD -m 0644 share/flatcam_icon$x.png \
	%buildroot%_iconsdir/hicolor/$x'x'$x/apps/flatcam.png
done

### == desktop file
cat>%name.desktop<<END
[Desktop Entry]
Name=%name
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Development;Engineering;
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

%files
%doc LICENSE README.md
%_datadir/%name/
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%python_sitelibdir/*
%exclude %python_sitelibdir/descartes

%changelog
* Sun Sep 03 2017 Anton Midyukov <antohami@altlinux.org> 8.5-alt3.20170702
- Fix conflict with python-module-descartes.

* Sat Jul 29 2017 Anton Midyukov <antohami@altlinux.org> 8.5-alt2.20170702
- Added missing requires: python-module-matplotlib-qt4.

* Wed Jul 26 2017 Anton Midyukov <antohami@altlinux.org> 8.5-alt1.20170702
- Initial build for ALT Sisyphus.
