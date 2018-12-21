Name: mcabber
Version: 1.0.5
Release: alt1

Summary: console Jabber client
License: GPL
Group: Networking/Instant messaging
Url: http://www.lilotux.net/~mikael/mcabber/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Source2: %name.watch

BuildRequires: libenchant-devel libgpgme-devel libidn-devel libloudmouth-devel libncursesw-devel libotr-devel

%description
mcabber is a small Jabber console client for Linux, maintained by Mikael BERTHE.
mcabber includes features such as SSL support, history logging, commands completion
and external actions triggers. Please read the manual page (manpage link below)
for more information.

%package devel
Summary: %summary
Group: %group

%description devel
mcabber is a small Jabber console client for Linux, maintained by Mikael BERTHE.
mcabber includes features such as SSL support, history logging, commands completion
and external actions triggers. Please read the manual page (manpage link below)
for more information.

%prep
%setup

%build
%autoreconf
%configure --enable-aspell --with-ssl --enable-sigwinch --enable-otr --enable-xep0022 --enable-enchant
%make_build

%install
%makeinstall

%files
%doc contrib AUTHORS ChangeLog TODO mcabberrc.example
%_libdir/%name
%_bindir/*
%_man1dir/*
%_datadir/%name

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt1
- new version 1.0.5

* Wed Sep 21 2016 Denis Smirnov <mithraen@altlinux.ru> 1.0.3-alt1
- new version 1.0.3

* Sun Apr 03 2016 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- new version 1.0.2

* Mon Feb 01 2016 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- new version 1.0.1

* Wed Aug 19 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt2
- fix watch-file

* Wed Jul 01 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt1
- new version 1.0.0

* Sun Aug 24 2014 Denis Smirnov <mithraen@altlinux.ru> 0.10.3-alt1
- new version 0.10.3

* Tue Feb 05 2013 Denis Smirnov <mithraen@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 0.10.1-alt1
- 10.0.1

* Thu Sep 30 2010 Denis Smirnov <mithraen@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.4-alt0.1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.4-alt0.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.6.4-alt0.1
initial build for Sisyphus
