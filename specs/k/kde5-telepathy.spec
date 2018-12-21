Name: kde5-telepathy
Version: 16.12.0
Release: alt1%ubt

Group: Graphical desktop/KDE
Summary: KDE Telepathy handler
Url: http://projects.kde.org/projects/extragear/network/telepathy/
License: GPLv2+

BuildArch: noarch

Requires: mjpegtools
#
Requires: telepathy-accounts-signon
Requires: telepathy-mission-control
Requires: telepathy-gabble
Requires: telepathy-haze
Requires: telepathy-idle
Requires: telepathy-rakia
Requires: telepathy-salut
#
Requires: kde5-ktp-accounts-kcm
Requires: kde5-ktp-approver
Requires: kde5-ktp-auth-handler
Requires: kde5-ktp-desktop-applets
Requires: kde5-ktp-contact-list
Requires: kde5-ktp-contact-runner
Requires: kde5-ktp-filetransfer-handler
Requires: kde5-ktp-kded-module
Requires: kde5-ktp-send-file
Requires: kde5-ktp-text-ui
Requires: kde5-ktp-call-ui
#
Requires: kde5-signon-kwallet-extension
Requires: kde5-kaccounts-providers

BuildRequires(pre): rpm-build-ubt

%description
%summary

%files

%changelog
* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.0-alt1%ubt
- update requires

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt3
- update requires

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt2
- update requires

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
