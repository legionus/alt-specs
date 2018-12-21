Name: alterator-net-shares
Version: 0.4
Release: alt1

Summary: Enable/disable mounting samba shares from "domain" server
License: GPL
Group: System/Configuration/Other

Source: %name-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
BuildArch: noarch

Requires: gettext
Requires: bind-utils
Requires: alterator >= 2.9
BuildPreReq: alterator >= 3.1

%description
%summary

%prep
%setup -q

%build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
/usr/lib/alterator/backend3/*

%changelog
* Thu Apr 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- Remove empty lines in domain controller lookup regexp

* Wed Aug 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- ignore ipv6 addresses determening server name

* Thu Nov 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- adapted to "p7 domain"

* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- dependence on bind-utils added

* Thu Apr 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- domain server address calculation fixed

* Wed Apr 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- debug output removed

* Fri Apr 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


