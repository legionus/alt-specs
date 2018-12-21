%define		php7_extension	pdo_odbc

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	ODBC driver for PHP Data Objects Interface

Group:		System/Servers
License:	PHP Licence
URL:		http://www.php.net/manual/en/ref.pdo-odbc.php
#		http://pecl.php.net/package/PDO_ODBC

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: gcc-c++ libunixODBC-devel
BuildRequires: php7-devel = %php7_version

PreReq: php7-pdo = %php7_version-%php7_release
Provides: php7-pdo-driver

%description
PHP PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
This package contains a ODBC driver for PDO.

%prep
%setup -T -c
cp -pr -- %php7_extsrcdir/%php7_extension/* .

# Fix path to pdo*.h
subst 's@php/ext@php/%_php7_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

# Fix for config.m4 in %%prep would't work for some reason
%__subst 's@php/ext@php/%_php7_version/ext@g' configure

# Fix PHP bug #48913 (buffer overflow due too long error code string)
%__subst 's#IM0001#IM001#g' odbc_stmt.c

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--with-pdo-odbc=unixODBC,%_usr \
	#

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release
