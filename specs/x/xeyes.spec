Name: xeyes
Version: 1.1.2
Release: alt1

Summary: display the X Window System logo
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Tue Sep 21 2010
BuildRequires: libXext-devel libXmu-devel libXrender-devel

BuildRequires: xorg-proto-devel xorg-util-macros

%description
The xeyes program displays the X Window System logo. That's all.

%prep
%setup

%build
%autoreconf
%configure --disable-xprint

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.0.99-alt1
- Initial build from scratch

