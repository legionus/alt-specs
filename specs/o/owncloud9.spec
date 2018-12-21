%define major 9

Name: owncloud%major
Version: 9.1.8
Release: alt3
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPLv3
Url: https://owncloud.org/

BuildRequires(pre): rpm-macros-webserver-common
BuildArch: noarch

Requires(pre): webserver-common

#https://doc.owncloud.org/server/9.1/admin_manual/installation/source_installation.html
Requires: php7-libs php7-dom php7-gd2 php7-mbstring php7-xmlreader php7-zip php7-curl php7-fileinfo
#For SQL DBs:
Requires: php7-pdo-driver

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%description
ownCloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name >= 9.1.0 apache2-mod_php7 apache2-mod_ssl

%description apache2
Apache 2.x web-server default configuration for %name.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name >= 9.1.0 nginx

%description nginx
nginx web-server default configuration for %name.

%prep
%setup

%install
mkdir -p %buildroot%installdir
cp -rp %name/* %buildroot%installdir/
cp %name/.htaccess %buildroot%installdir/
cp %name/.user.ini %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr
rm -f %buildroot%installdir/l10n/l10n.pl

mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%installdir/config/ %buildroot%_sysconfdir/%name/.
ln -s %_sysconfdir/%name/config %buildroot%installdir/config

mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

#install apache2
install -pD -m0644 apache2/default.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

#install nginx
install -pD -m0644 nginx/default.conf %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%dir %installdir
%installdir/3rdparty
%dir %attr(0775,root,_webserver) %installdir/apps
%installdir/apps/*
%installdir/core
%installdir/l10n
%installdir/lib
%installdir/ocs*
%installdir/resources
%installdir/settings
%installdir/themes
%installdir/updater
%dir %attr(0770,root,_webserver) %_sysconfdir/%name/config/
%_sysconfdir/%name
%installdir/config
%dir %attr(0770,root,_webserver) %_localstatedir/%name
%installdir/data
%installdir/*.php
%installdir/.htaccess
%installdir/.user.ini
%doc %installdir/AUTHORS
%doc %installdir/COPYING-AGPL
%installdir/*.xml
%installdir/index.html
%installdir/robots.txt
%installdir/occ

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf 

%changelog
* Thu Oct 25 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.8-alt3
- php5 -> php7

* Mon Sep 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.8-alt2
- fixed unowned files

* Mon Sep 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.8-alt1
- 9.1.8
- Updated requires for SQL DBs (closes: #35310)

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.6-alt3
- Fixed permissions - addition to previous release

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.6-alt2
- [major] Fixed permissions for installdir
- Fixed requires for subpackages

* Thu Jun 15 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.6-alt1
- 9.1.6

* Tue Apr 25 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.5-alt1
- 9.1.5

* Wed Mar 29 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.4-alt2
- Removed '.gitignore' from source

* Wed Mar 29 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.4-alt1
- 9.1.4

* Tue Jan 10 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt3
- Cleanup requires for *-nginx

* Fri Dec 30 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt2
- Added package *-nginx (default config)

* Thu Dec 29 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt1
- 9.1.3
- Added package *-apache2 (default config)

* Wed Nov 30 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.2-alt1
- 9.1.2

* Tue Oct 04 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt3
- Fix path to %installdir

* Mon Oct 03 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt2
- Fixed requires

* Thu Sep 29 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt1
- 9.1.1
