Summary: Firejail graphical user interface
Name: firetools
Version: 0.9.52
Release: alt1
License: GPLv2+
Group: Development/Tools
Source: %name-%version.tar
Url: https://github.com/netblue30/firetools

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
Requires: firejail
Requires: libqt5-svg

%description
Firetools is the graphical user interface of Firejail.
Firejail is a SUID sandbox program that reduces the risk of security breaches
by restricting the running environment of untrusted applications using Linux
namespaces, seccomp-bpf and Linux capabilities. It allows a process and all
its descendants to have their  own  private view of the globally  shared  kernel
resources, such as the network stack, process table, mount table.  Firejail can
work in a SELinux or AppArmor environment, and it is integrated with Linux
Control Groups.

%prep
%setup

%build
%configure --with-qmake=%_bindir/qmake-qt5
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_docdir/%name
%_libexecdir/%name
%_bindir/*
%_man1dir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 0.9.52-alt1
- new version 0.9.52

* Sat Nov 04 2017 Anton Midyukov <antohami@altlinux.org> 0.9.50-alt2
- Fix build error (Closes: 34129). Thanks Michael A. Kangin

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 0.9.50-alt1
- new version 0.9.50

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 0.9.46-alt1
- new version 0.9.46

* Fri Jan 06 2017 Anton Midyukov <antohami@altlinux.org> 0.9.40.1-alt1
- Initial build for ALT Linux Sisyphus.
