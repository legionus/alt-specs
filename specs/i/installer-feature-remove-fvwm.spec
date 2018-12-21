Name: installer-feature-remove-fvwm
Version: 0.6
Release: alt3

Summary: Remove Fvwm if Gnome installed
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Remove Fvwm if Gnome installed


%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue May 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- stderr redirected to /dev/null

* Wed Feb 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- checking for dms fixed

* Tue Feb 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- remove fvwm if any /usr/sbin/*[^an]dm exists

* Tue Jul 05 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- remove also xterm

* Sun Oct 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- fix fix

* Fri Oct 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- fix

* Thu Oct 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- simplify

* Wed Oct 13 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build
