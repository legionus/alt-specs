# SPEC file for nikto web server scanner

Name: nikto
Version: 2.1.6
Release: alt1.git6f8c472

Epoch: 1

Summary: web server vulnerability scaner
Summary(ru_RU.UTF-8): сканер уязвимостей веб-серверов

License: %gpl2only
Group: Security/Networking
#URL: http://www.cirt.net/nikto2
URL: https://github.com/sullo/nikto

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-licenses

AutoReqProv: perl, yes

Requires: perl-Net-SSLeay openssl perl-bignum

%description
Nikto is an Open Source (GPL) web server scanner which performs
comprehensive tests  against  web servers  for multiple  items,
including  over 3500 potentially dangerous files/CGIs, versions
on over  900 servers, and version specific problems on over 250
servers.

%description -l ru_RU.UTF-8
Nikto  - это сканер веб-серверов, который производит подробное 
тестирование  веб-серверов по целому ряду параметров,  включая 
проверку на наличие свыше  3500 потенциально  опасных файлов и 
CGI-скриптов для более чем 900 версий серверов, а также других
проблем, специфичных для более чем 250 версий серверов.


%define execdir  %_datadir/%name
%define _perl_lib_path %execdir/plugins

%prep
%setup
%patch0 -p1

%build
pushd program

# Fix location of config file
sed -e 's@"nikto.conf"@"%_sysconfdir/%name/nikto.conf"@' -i nikto.pl

# Fix pathes in config.txt
sed -e 's@NIKTODTD=.*/nikto.dtd@NIKTODTD=%_sysconfdir/%name/nikto.dtd@' -i nikto.conf
sed -e 's@# EXECDIR=.*/nikto@EXECDIR=%execdir@' -i nikto.conf

sed -e 's@# PLUGINDIR=.*/plugins@# PLUGINDIR=%execdir/plugins@'         -i nikto.conf
sed -e 's@# DBDIR=.*/databases@# DBDIR=%execdir/databases@'             -i nikto.conf
sed -e 's@# TEMPLATEDIR=.*/templates@# TEMPLATEDIR=%execdir/templates@' -i nikto.conf
sed -e 's@# DOCDIR=.*/docs@# DOCDIR=%execdir/docs@'                     -i nikto.conf

popd

%install
pushd program

install -m 0755 -d -- %buildroot%_sysconfdir/%name
install -m 0644 -- nikto.conf     %buildroot%_sysconfdir/%name/nikto.conf
install -m 0644 -- docs/%name.dtd %buildroot%_sysconfdir/%name/%name.dtd

install -m 0755 -d -- %buildroot/%_bindir
install -D -m 0755 -- %name.pl    %buildroot%_bindir/%name

install -m 0755 -d -- %buildroot/%execdir/plugins
install -m 0644 -- plugins/* %buildroot%execdir/plugins/

install -m 0755 -d -- %buildroot/%execdir/templates
install -m 0644 -- templates/* %buildroot%execdir/templates/

install -m 0755 -d -- %buildroot/%execdir/databases
install -m 0644 -- databases/* %buildroot%execdir/databases/

popd

%files
%doc README.md program/docs/CHANGES.txt program/docs/LICENSE.txt program/docs/nikto_manual.html

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/nikto.conf
%config %_sysconfdir/%name/%name.dtd

%_bindir/%name
%dir %_datadir/%name
     %_datadir/%name/*

%changelog
* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 1:2.1.6-alt1.git6f8c472
- New version (Closes: 33319)

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1:2.1.5-alt1
- New version 2.1.5

* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1:2.1.4-alt1
- New version 2.1.4

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1:2.1.3-alt1
- New version 2.1.3

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.03-alt2
- Updating databases

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.03-alt1
- New version 2.03

* Wed May 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.02-alt1
- New version 2.02

* Sat Aug 11 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.36-alt3
- Updating databases to current state
- Added header of Microsof Office Web server to nikto_headers.plugin

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.36-alt2
- Updating databases to current state
- nikto_core.plugin 1.39, fix check/send update code for improperly 
  setting IP instead of name in Host header.

* Tue Mar 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.36-alt1
- New version 1.36
  - Added -404 option to specify a "404 string" on the command line 
  - Added plugin to chek for PUT and DELETE 
  - Additional checks for HTTP methods 
  - Additional checks for headers 
  - Other bugfixes, please see the CHANGES file for more details 
- Updating databases to current state
- spec file cleanup

* Mon Aug 14 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.35-alt2
- Updating databases to current state

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.35-alt1
- Initial build for ALT Linux

