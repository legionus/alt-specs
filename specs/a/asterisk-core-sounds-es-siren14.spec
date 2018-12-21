%define sound_dir	%_datadir/asterisk/sounds/
%define sound_lang  es

Name: asterisk-core-sounds-es-siren14
Summary: sounds for Asterisk
Version: alt1.1
Release: alt1.1
License: GPL
Group: System/Servers
BuildArch: noarch
Obsoletes: asterisk-sounds-es-siren14 < %version-%release 
Conflicts: asterisk-sounds-es-siren14 
Requires(pre): asterisk-sounds-es-base

Url: http://downloads.asterisk.org/pub/telephony/sounds/releases/%name-%version.tar.gz

Source: %name-%version.tar

BuildRequires: asterisk-build-sounds

%description
%summary

%prep
%setup

%install
ast-install-core-sounds es siren14 %buildroot
%files -f sounds.list

%changelog
* Fri Mar 31 2017 Denis Smirnov <mithraen@altlinux.ru> alt1.1-alt1.1
- update build scripts for prevent core/extra sounds conflicts

* Sun May 10 2015 Cronbuild Service <cronbuild@altlinux.org> 1.4.27-alt1
- new version 1.4.27

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 1.4.26-alt1
- new version 1.4.26

* Fri Nov 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.25-alt1
- new version 1.4.25

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.24-alt1
- new version 1.4.24

* Fri Jan 11 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.23-alt1
- new version 1.4.23

* Tue Jan 01 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.22-alt1
- new version 1.4.22

* Tue Jan 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt5
- fix cronbuild support

* Fri Dec 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt4
- add watch-file and cronbuild support

* Sat Sep 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt3
- add Obsoletes to old sounds packages

* Sun Jul 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt2
- add requires to asterisk-sounds-es-base

* Tue Jul 19 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt1
- first build


