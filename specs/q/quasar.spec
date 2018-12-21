Name: quasar
Summary: User and groups for asterisk-related packages
Version: 2.0.2
Release: alt2.qa1
License: GPL
Group: System/Servers

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Requires(pre): asterisk-base

%description
%summary

%prep
%setup

%build
pushd ecfg
%make_build
popd

sed 's/quasar/quasarm/' < quasar.rules > quasarm.rules

%install
install -d %buildroot%_sysconfdir/emcfg
install -d %buildroot%_sysconfdir/ecfg
install -d %buildroot%_udevrulesdir/
install -D -m 755 ecfg/ecfg %buildroot%_sbindir/ecfg
install -D -m 755 ecfg/emcfg %buildroot%_sbindir/emcfg
install -D -m 644 quasar.rules %buildroot%_udevrulesdir/quasar.rules
install -D -m 644 quasarm.rules %buildroot%_udevrulesdir/quasarm.rules

%files
%_sysconfdir/ecfg
%_sysconfdir/emcfg
%_sbindir/ecfg
%_sbindir/emcfg
%_udevrulesdir/quasar.rules
%_udevrulesdir/quasarm.rules
%changelog
* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for quasar

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.0.2-alt2
- auto rebuild

* Tue Dec 09 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0.2-alt1
- first build for Sisyphus
