Name: WMmp
Version: 0.10.0
Release: alt2.qa2

Summary: A (Window Maker) dock app for interfacing MPD
License: GPL
Group: Sound

Url: http://musicpd.org/
Source: %name-%version.tar.gz

BuildRequires: libXext-devel libXpm-devel

%description
A (Window Maker) dock app for interfacing MPD.

%prep
%setup

%build
%configure \
	--with-default-port=6600 \
	--with-default-host=localhost
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING INSTALL README
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 0.10.0-alt2.qa2
- NMU: fixed FTBFS.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.10.0-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt2
- fix build

* Mon Nov 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.10.0-alt1.1
-  #8419 fix.

* Wed May 25 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.10.0-alt1
- initial build.

