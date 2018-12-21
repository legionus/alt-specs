# Package name without php prefix
%define		php7_extension	memcache
###############################################################
Name:	 	php7-%php7_extension
Version:	3.0.8
Release:	alt%php7_version.%php7_release

Summary:	memcached extension for php7

License:	PHP Licence
Group:		System/Servers
URL:		https://github.com/websupport-sk/pecl-memcache

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version zlib-devel

Requires: php7-libs = %php7_version

# Source0-url:	https://pecl.php.net/get/memcache-%version.tgz
Source0:	php7-%php7_extension-%version.tar
Source1:	php7-%php7_extension.ini
Source2:	php7-%php7_extension-params.sh
Patch:		php7-memcache-alt-inc.patch

%description 
The php7-%php7_extension package contains a dynamic shared object (DSO) for php7. The
php-%php7_extension module allows you to work with memcached through handy OO
and procedural interfaces. If you need memcached(1) support for php7
applications, you will need to install this package and php7.

%prep
%setup -n php7-%php7_extension-%version
%patch -p2

%build
phpize

export LDFLAGS=-lphp-%_php7_version

%configure --enable-memcache --with-zlib-dir=/usr
%php7_make

%install
%php7_make_install
%__install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
%__install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS README

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Sat Jan 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.8-alt1
- new version (3.0.8) with rpmgs script

* Sat Jan 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- initial build 2.2.7 for ALT Sisyphus
