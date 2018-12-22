%define		php5_extension	imagick
%define 	real_name	imagick
%define		real_version	3.2.0RC1

Name:	 	php5-%{php5_extension}2
Version:	%php5_version
Release:	%php5_release.3

Summary:	PHP5 wrapper to the ImageMagick library

License:	PHP
Group:		System/Servers
URL:		http://pecl.php.net/package/imagick

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libImageMagick-devel

Conflicts: php5-imagick

%description
Imagick is a native PHP extension to create and modify images
using the ImageMagick API.

This package contains Imagick with version 2.x API.

%prep
%setup -T -c
tar xvf %SOURCE0
# ./imagick-2.x.x -> ./
mv -- %real_name-%real_version/* .
rm -fr -- %real_name-%real_version

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
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
%doc CREDITS
%doc examples*

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 5.6.31.20170607-alt1.S1.2
- updated to 3.4.3

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 5.5.10.20140305-alt1.1
- rebuild with ImageMagick 6.8.8.10-alt1

* Mon May 20 2013 Aleksey Avdeev <solo@altlinux.ru> 5.3.25.20130509-alt1.3
- Updated to 3.1.0RC2

* Mon May 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.3.25.20130509-alt1.2
- Rebuild with php5-5.3.25.20130509-alt1

* Thu Apr 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.3.24.20130412-alt2
- Rebuild with ImageMagick.git 6.8.4.10-alt1
- updated to 3.0.1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1.1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1.1
- Rebuild with php5-5.3.17.20120913-alt1

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with new libImageMagick

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Nov 25 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
- rebuild with new ImageMagick

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1.1
- Rebuild with php5-5.2.14.20100721-alt1

* Fri Apr 23 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1.1
- Rebuild with new libImageMagick

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- Rebuild with new php (5.2.12.20091216-alt1)

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Wed Mar 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1.1
- Rebuild with ImageMagick 6.5.0.0

* Thu Feb 12 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1
- New version 2.2.2
- Rebuild with php5-5.2.9.20090205-alt1

* Sun Oct 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild for PHP 5.2.7.20080920

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080627-alt1
- New version 2.2.0

* Sat May 17 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1
- Initial build for ALT Linux Sisyphus
