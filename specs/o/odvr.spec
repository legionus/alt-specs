Summary: Odvr is a user-space driver for Olympus digital voice recorders
Name: odvr
Version: 0.1.5
Release: alt1.qa2
License: GPLv3
Group: System/Configuration/Hardware
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://code.google.com/p/odvr
Source: %name-%version.tar.gz

# Automatically added by buildreq on Sat Dec 11 2010
BuildRequires: libgtk+2-devel libsndfile-devel libusb-compat-devel

%description
odvr is a user-space driver for Olympus digital voice recorders that do not
support USB Mass Storage. Not all formats are directly supported 
(sandec/PULCOD), and functionality is limited, but basic download and listing
capabilities are implemented.

%prep
%setup

%build
%make_build

%install
install -D %name %buildroot%_bindir/%name
install -D %name-gui %buildroot%_bindir/%name-gui
install -D 41-odvr.rules %buildroot%_udevrulesdir/41-odvr.rules

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Name=odvr
GenericName=Get wav from Olympus DVRs
Comment=%summary
Exec=%name-gui
Icon=%name
Terminal=false
Type=Application
Categories=AudioVideo;Recorder;
EOF

%files
%doc COPYING README
%_bindir/*
%config %_udevrulesdir/*
%_datadir/applications/%name.desktop

%changelog
* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.5-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for odvr
  * postclean-03-private-rpm-macros for the spec file

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Dec 11 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.5-alt1
- Build for ALT
