
Name: phpipam
Version: 1.32.000
Release: alt1%ubt
Summary: PHP-based virtual machine control tool
Group: Networking/WWW
License: GPLv3
Url: http://phpipam.net
Source: %name-%version.tar
Source2: php-saml.tar
Source3: PHPMailer.tar
Source4: captcha.tar
Source11: %name-apache.conf

# Patch: %name-%version-%release.patch

BuildArch: noarch
PreReq: webserver-common

BuildRequires(pre): rpm-build-ubt
BuildPreReq: rpm-macros-webserver-common rpm-macros-apache2

%description
phpipam is an open-source web IP address management application. Its goal is to provide light and simple IP address management application.
It is ajax-based using jQuery libraries, it uses php scripts and javascript and some HTML5/CSS3 features, so some modern browser is preferred
to be able to display javascript quickly and correctly.

Features and tools:
- Section / Subnet separation
- Subnet nesting
- IPv4/IPv6 support
- REST API
- Subnet ICMP/telnet scanning and automatic status updates
- Displays free range and number of clients
- Subnet statistics
- User management
- AD/LDAP/OpenLDAP/NetIQ/Radius authentication support (multiple servers)
- E-Mail notification with IP details
- Import IP addresses from XLS / CSV file
- Export IP database to XLS file
- IPv4/IPv6 calculator
- Search IP database
- IP request module
- Custom IP address fields
- and much more...
- PowerDNS integration (3.4+);

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %version-%release
Requires: %name-php
Requires: apache2-httpd-prefork-like php-engine

%description apache2
%summary

%package php5
Group: Networking/WWW
BuildArch: noarch
Summary: php5 virtual package for %name
Provides: %name-php
Requires: %name = %version-%release
Requires: php5-gmp php5-ldap php5-sockets php5-openssl php5-pdo php5-pdo_mysql php5-pcntl php5-mbstring php5-mcrypt php5-snmp php5-gd2 pear-core

%description php5
%summary

%package php7
Group: Networking/WWW
BuildArch: noarch
Summary: php7 virtual package  for %name
Provides: %name-php
Requires: %name = %version-%release
Requires: php7-gmp php7-ldap php7-sockets php7-openssl php7-pdo php7-pdo_mysql php7-pcntl php7-mbstring php7-mcrypt php7-snmp php7-gd2 pear-core

%description php7
%summary

%prep
%setup
tar -xf %SOURCE2 -C functions/php-saml
tar -xf %SOURCE3 -C functions/PHPMailer
tar -xf %SOURCE4 -C app/login/captcha
#%patch -p1

%install
mkdir -p %buildroot%webserver_webappsdir
cp -r ../%name-%version %buildroot%webserver_webappsdir/%name
#cleaup
#rm -rf %buildroot%webserver_webappsdir/%name/misc
rm -f %buildroot%webserver_webappsdir/%name/{INSTALL.txt,README,UPDATE}
rm -f %buildroot%webserver_webappsdir/%name/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/.gitmodules

install -pDm644 %SOURCE11 %buildroot%apache2_extra_available/%name.conf
%__subst 's|--dir--|%webserver_webappsdir/%name|g' %buildroot%apache2_extra_available/%name.conf

chmod 644 INSTALL.txt README.md UPDATE misc/CHANGELOG misc/Roadmap

# Cleanup PHPMailer
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.scrutinizer.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.travis.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/travis.phpunit.xml.dist
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/docs
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/examples
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/test

%files
%doc INSTALL.txt README.md UPDATE misc/CHANGELOG misc/Roadmap
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
%webserver_webappsdir/%name/.htaccess
%dir %attr(0770, root, _webserver) %webserver_webappsdir/%name/app/admin/import-export/upload
%dir %attr(0770, root, _webserver) %webserver_webappsdir/%name/app/subnets/import-subnet/upload

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%files php5
%files php7

%changelog
* Fri Jul 06 2018 Alexey Shabalin <shaba@altlinux.ru> 1.32.000-alt1%ubt
- 1.3.2 release

* Fri Dec 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.31.000-alt1%ubt
- 1.3.1 release

* Thu Jun 15 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt1%ubt
- 1.3 release

* Wed May 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.6
- git snapshot of master branch  66d0e19ebea1fd6e670a75a5cfb9897f7010d6e6

* Wed Apr 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.5
- set permitions for upload dirs

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.4
- git snapshot of master branch 377139d7489376ac3622d936dbce16b1823358a1

* Thu Mar 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.3
- git snapshot of master branch 80c3f0614ed9d9d694592f7d0cb38e0b731892e7

* Mon Feb 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.2
- git snapshot of master branch cfda8c9b3a20ee60e693ae7cbcf87c61c109bbe9

* Wed Feb 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.1
- 1.3

* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.29.011-alt2
- git snapshot of master branch 7edd5343ddd878de97eb41f3340fcce4fcd3a510
- add php5 and php7 subpackages

* Thu Jan 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.29.011-alt1
- git snapshot of master branch 84916b3c3add90b9cb1c39c9623cf04bb0f3bcd6

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.27.002-alt1
- git snapshot of master branch d55883ff28a3cf347f18e0cc717cf64b7556706a
- update PHPMailer to 5.2.22 (fixed CVE-2017-5223)

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.26.050-alt1
- git snapshot of master branch b99412648829471f3a336036f5cd138b8f131721
- install PHPMailer from upstream (fixed CVE-2015-8476,CVE-2016-10033,CVE-2016-10045)

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt2
- git snapshot of branch 1.2 - 7a5cb1a2ea065096d1d393ccc5b52a5bb7983c39

* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
