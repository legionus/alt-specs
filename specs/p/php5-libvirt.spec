%define php5_extension libvirt

Name: php5-libvirt
Version: 0.5.2
Release: alt1.%php5_version.%php5_release

Summary: PHP language binding for Libvirt
Group: System/Servers
License: %gpl2plus
Url: http://libvirt.org/php

Source: %name-%version.tar
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

Patch: %name-%version.patch

BuildRequires(pre): rpm-build-php5 rpm-build-licenses
BuildRequires: php5-devel = %php5_version
BuildRequires: libvirt-devel >= 1.2.13
BuildRequires: libxml2-devel
BuildRequires: xsltproc
BuildRequires: xml-utils
Requires: php5-libs = %php5_version

%description
PHP language bindings for Libvirt API.
For more details see: http://www.libvirt.org/php/

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make install DESTDIR=%buildroot
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%php5_extconf/%php5_extension
%php5_extdir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Apr 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.6-alt3
- rebuild with php5 5.3.23.20130314-alt1

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt2
- rebuild with php5-5.3.18.20121017-alt1

* Thu Oct 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Mar 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.5-alt2
- git snapshot 22da0e3cfe42c0181c86ae334de713666fac774a
- rebuild with php5-5.3.10.20120202-alt1

* Tue Dec 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.5-alt1
- initial build for ALT Linux Sisyphus

