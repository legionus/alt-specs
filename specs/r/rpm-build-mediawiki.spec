Name: rpm-build-mediawiki
Version: 0.6
Release: alt1

Summary: RPM helper scripts for packaging mediawiki extensions
License: GPL
Group: Development/Other

URL: http://www.altlinux.org/MediaWiki_Policy
Source: %name-%version.tar

BuildArch: noarch

%description
RPM helper scripts for package mediawiki extensions.
It introduced mediawiki_ext_install macro.

See %url for detailed mediawiki extension packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/mediawiki

%files
%doc EXAMPLE.ALT
%_rpmmacrosdir/mediawiki

%changelog
* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- support mediawiki 1.24 or newer
- add setup_mediawiki_ext, mediawikiext_dir macros

* Wed Apr 01 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- remove ?> in the last config line

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- add set_required_mediawiki macro

* Fri May 21 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- fix Url, Source and Summary

* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- do not pack temp. *.files file

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- fix spec, fix generated path to extension

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
