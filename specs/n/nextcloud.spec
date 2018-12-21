Name: nextcloud
Version: 13.0.8
Release: alt1
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPLv3
Url: https://nextcloud.com/

BuildArch: noarch

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: python3-base
Requires(pre): webserver-common

# https://docs.nextcloud.com/server/13/admin_manual/installation/source_installation.html#ubuntu-installation-label
Requires: php7 php7-libs php7-dom php7-gd2 php7-mbstring php7-xmlreader php7-zip
# Highly recommended:
Requires: php7-curl php7-fileinfo php7-openssl
# For SQL DBs
Requires: php7-pdo-driver

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%description
Nextcloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name >= 12.0.0 apache2-mod_php7 apache2-mod_ssl

%description apache2
Apache 2.x web-server default configuration for %name.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name >= 12.0.0 nginx
#Requires: php5-cgi php5-fpm-fcgi php5-apcu

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
#%installdir/l10n
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
%installdir/index.html
%installdir/robots.txt
%installdir/occ

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%changelog
* Wed Dec 05 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.8-alt1
- version 13.0.8 (Nov 22 2018)

* Thu Oct 25 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.7-alt1
- version 13.0.7 (Oct 11 2018)
- update requires for apache2 (php5 -> php7)

* Mon Sep 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.6-alt1
- version 13.0.6 (Aug 30 2018)
- update requires for SQL DBs

* Tue Jun 19 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.4-alt1
- version 13.0.4 (Jun 11 2018)
- update requires: php5 > php7
  (php5-xmlreader there is not for aarch64)

* Mon May 28 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.2-alt1
- version 13.0.2 (Apr 26 2018)

* Wed Mar 21 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.1-alt1
- version 13.0.1 (Mar 15 2018)

* Wed Feb 28 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 13.0.0-alt1
- version 13.0.0 (Feb 6 2018)

* Tue Jan 30 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.5-alt1
- version 12.0.5 (Jan 24 2018)

* Wed Dec 06 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.4-alt1
- version 12.0.4 (Dec 4 2017)

* Thu Sep 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.3-alt1
- version 12.0.3 (Sep 20 2017)
- fixed unowned files

* Mon Aug 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.2-alt1
- version 12.0.2 (Aug 14 2017)

* Wed Aug 09 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.1-alt1
- version 12.0.1 (Aug 7 2017)
- update requires (PHP >= 5.6)

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt4
- fixed permissions - addition to previous release

* Thu Jul 13 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt3
- [major] fixed permissions for installdir

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt2
- added missing files
- fixed requires for subpackages

* Thu Jun 15 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 12.0.0-alt1
- version 12.0.0 (May 22 2017)
- initial build
