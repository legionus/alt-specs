%define apache_moduledir %apache2_moduledir

Name: apache2-mod_dnssd
Version: 0.6
Release: alt3

Summary: Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.
License: Apache 2.0
Group: System/Servers
Url: http://0pointer.de/lennart/projects/mod_dnssd

Requires: %apache2_name-base >= 2.4.7-alt1
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr

Source: %name-%version-%release.tar
Patch0: mod_dnssd-0.6-httpd24.patch
BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires: libavahi-devel lynx

%description
An Apache 2.0 module which adds Zeroconf support via DNS-SD using Avahi.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --with-apr-config --with-apxs=$(dirname %apache2_apxs)
make

%install
install -pm0644 -D src/.libs/mod_dnssd.so %buildroot/%apache_moduledir/mod_dnssd.so
install -pm0644 -D alt/dnssd.conf %buildroot%apache2_mods_available/dnssd.conf
install -pm0644 -D alt/dnssd.load %buildroot%apache2_mods_available/dnssd.load
sed -i 's,@apache_moduledir@,%apache_moduledir,' %buildroot%apache2_mods_available/dnssd.load
install -pm0644 -D alt/dnssd.start %buildroot%apache2_mods_start/100-dnssd.conf

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/dnssd.conf
touch %buildroot%apache2_mods_enabled/dnssd.load

%files
%doc LICENSE README
%apache_moduledir/mod_dnssd.so
%config(noreplace) %apache2_mods_available/*.load
%config(noreplace) %apache2_mods_available/*.conf
%config(noreplace) %apache2_mods_start/*.conf
%ghost %apache2_mods_enabled/*.load
%ghost %apache2_mods_enabled/*.conf

%changelog
* Fri May 06 2016 Sergey Alembekov <rt@altlinux.ru> 0.6-alt3
- fix dnssd.load config file

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 0.6-alt2
- Rebuild with new apache2

* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt1
- New version

* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1.1
- Rebuild with apache2-2.2.22-alt16 (fix unmets).
- Add %%apache2_mods_start/100-dnssd.conf file for auto loading module.
- Add %%ghost for %%apache2_mods_enabled/*.{load,conf}.

* Mon Aug 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- Initial build.
