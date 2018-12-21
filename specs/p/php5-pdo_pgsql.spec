%define		php5_extension	pdo_pgsql

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release.1

Summary:	PostgreSQL driver for PHP5 Data Objects Interface

Group:		System/Servers
License:	PHP Licence
URL:		http://www.php.net/manual/en/ref.pdo-pgsql.php
#		http://pecl.php.net/package/PDO_PGSQL

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

#Source0:	standart PHP module
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: gcc-c++ postgresql-devel
BuildRequires: php5-devel = %php5_version

Requires: php5-pdo = %php5_version
Provides: php5-pdo-driver

%description
PHP5 PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
This package contains a PostgreSQL driver for PDO.

%prep
%setup -T -c
cp -pr -- %php5_extsrcdir/%php5_extension/* .

# Fix path to pdo*.h
subst 's@php/ext@php/%_php5_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php5_version/ext@g' configure

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

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
- Rebuild with php5-%php5_version-%php5_release

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1.1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1.1
- Rebuild with php5-5.3.17.20120913-alt1

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1.1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1.1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2.1
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1.1
- Rebuild with php5-5.3.5.20110105-alt1

* Mon Dec 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3.1
- Rebuild with PostgreSQL 9

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- Rebuild with new php build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- Rebuild with new php (5.2.12.20091216-alt1)

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Thu Feb 12 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with php5-5.2.9.20090205-alt1

* Sun Oct 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild for PHP 5.2.7.20080920 

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080627-alt1
- Rebuild for PHP 5.2.7

* Fri May 16 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1.2
- Fix Requires (#15580)

* Tue Apr 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1.1
- pdo_pgsql is a standart PHP extention now, use sources from PHP distribution

* Sun Apr 06 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1
- Rebuild for PHP 5.2.5-alt1

* Wed Jun 06 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.3-alt1
- Rebuild for PHP 5.2.3-alt1

* Tue May 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.2-alt1
- Rebuild for PHP 5.2.2-alt1

* Wed Apr 18 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.1-alt2
- Initial build for ALT Linux Sisyphus


