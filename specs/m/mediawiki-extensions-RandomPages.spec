%define oname RandomPages

Name: mediawiki-extensions-%oname
Version: 0.3
Release: alt1

Summary: RandomPages adds a new MediaWiki wiki parser for get random pages

License: GPL-3.0-only
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

# http://gitorious.org/randompages
Source: http://www.locknet.ro/files/%oname-%version.tar

%description
RandomPages adds a new MediaWiki wiki parser tag: <randompages />
Available options:
* limit int, to control how many links should be
  fetched randomly from the database, defaults to 150
* namespace bool, true to restrict only to the global namspace, defaults to false
* levels int, levels of CSS applyed to each entry, defaluts to 5

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- update version

* Sat Jun 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

