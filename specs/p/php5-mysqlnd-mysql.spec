%define		php5_extension	mysql

Name:	 	php5-mysqlnd-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	MySQL database module for PHP5 with mysqlnd support
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version
Conflicts: php5-mysql
Provides: php5-mysql = %php5_version-%php5_release

%description
The %name package includes a dynamic shared object (DSO) that adds MySQL
database support to PHP.  MySQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an HTML-embedded
scripting language. If you need back-end support for MySQL, you should
install this package in addition to the main php package.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--with-openssl=/usr \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Wed Oct 08 2014 Anton Farygin <rider@altlinux.ru> 5.5.17.20140916-alt1
- first build for Sisyphus, based on php5-mysql
