%define	php5_extension	gd
%define	gd_ver	2

Name:	 	php5-%php5_extension%gd_ver
Version:	%php5_version
Release:	%php5_release

Summary:	GD library support for PHP5
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php5_extension%gd_ver.ini
Source2:	php-%php5_extension%gd_ver-params.sh

BuildRequires(pre): rpm-build-php5
# Automatically added by buildreq on Thu Jan 28 2010
BuildRequires: glibc-devel-static libfreetype-devel libjpeg-devel libpng-devel php5-devel t1lib-devel

BuildRequires:	php5-devel = %php5_version

%description
The %name includes a dynamic shared object (DSO) that adds
GD support to PHP. GD is a library that enables you to create PNG,
JPEG, XPM, and WBMP graphics. It is linked with freetype and t1lib so
you can use TrueType fonts. PHP is an HTML-embedded scripting language.
If you need GD support for PHP applications, you will need to install
this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--enable-gd-native-ttf \
	--without-xpm \
	--with-jpeg-dir=%_prefix \
	--with-t1lib \
	--with-ttf=%_prefix \
	--with-png-dir=%_prefix \
	--with-zlib-dir=%_prefix \
	--with-freetype-dir=%_prefix \
	--with-libdir=%_lib \
	--enable-exif \
	--with-%php5_extension
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

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-5.3.17.20120913-alt1

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

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

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- disabled xpm support (closes #22622)
- rebuild with new php build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- rebuild with new php5 stable release 5.2.12 (20091216)
- minor spec cleanup (Sergey Kurakin)

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with new php snapshot.

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild with new php snapshot.

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- new version (5.2.7).

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- Rebuild with new php(5.2.5).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- rebuild for new php (5.2.3).

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- rebuild for new php (5.2.2).

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- Rebuild due libmm soname change.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- rebuild with new version (5.2.1).

* Tue Nov 07 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- new version (5.2.0)

* Fri Aug 18 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- new version (5.1.5)

* Tue Aug 15 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new version (5.1.4)

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new snapshot.

* Sun Dec 25 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- new version.

* Tue Oct 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.6-alt0.cvs20051003
- new version;

* Thu Aug 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.5-alt0.cvs20050729
- new cvs snapshot.

* Wed Jul 13 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.M24.1
- Built for 5.0.4-alt0.M24.1

* Mon Jul 04 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.4
- rebuilt with alt0.4

* Fri Jul 01 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.3
- built for php5-5.0.4
