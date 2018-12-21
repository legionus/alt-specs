Name: trayer
Version: 1.1.5
Release: alt1
License: BSD

Group: Graphical desktop/Other

Summary: lightweight GTK2-based systray for UNIX desktop

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Url: https://github.com/sargon/trayer-srg

# Automatically added by buildreq on Sun Aug 15 2010
BuildRequires: libXext-devel libXmu-devel libgtk+2-devel

%description
trayer is a small program designed to provide systray functionality
present in GNOME/KDE desktop environments for window managers which
do not support that function. System tray is a place, where various
applications put their icons, so they are always visible presenting
status of applications and allowing user to control programs.

trayer code was extracted from fbpanel application, you can find more
about it on its homepage: http://fbpanel.sourceforge.net/

%prep
%setup
%build
%make_build
%install
%make_install PREFIX=%buildroot/usr install
install -D -m644 man/trayer.1 %buildroot%_man1dir/%name.1
%files
%_bindir/trayer
%_man1dir/*.1.*
%doc COPYING README

%changelog
* Sat Apr 20 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1.5-alt1
- 1.1.5
- use trayer-srg fork

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.5-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt2
- fix build

* Sun Aug 15 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt1
- first build for Sisyphus

