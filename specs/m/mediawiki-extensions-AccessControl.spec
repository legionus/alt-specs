%define oname AccessControl
%define filename accesscontrol

Name: mediawiki-extensions-%oname
Version: 2.1
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Group Based Access Control for MediaWiki
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.20

Requires: mediawiki-extensions-SpecialNamespaces

Source: http://support.dce.felk.cvut.cz/%filename-%version.tar

Patch: %oname-ru.patch
Patch1: %oname-fix.patch

%description
Extension to restrict access to specific pages based on groups.

See also description in russian: http://kb.etersoft.ru/%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0:AccessControl_1.1

%prep
%setup -n %filename-%version
#patch -p2
#patch1 -p2

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 for 1.20 and above

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- add russian translation
- add fixes

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus
