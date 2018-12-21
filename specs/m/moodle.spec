# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define packagversion 1.9.19
%define packagedate 20130513
%define packagemoodleversion 2007101592.05
%define moodlebranch %nil
%define moodlepackagename %moodle_name%moodlebranch

#Name: %moodlepackagename
Name: moodle
Version: %packagversion.%packagedate
Release: %branch_release alt1

Summary: The Course Management System Moodle
License: %gpl2plus
Group: Networking/WWW

Url: http://www.moodle.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar
Source10: %moodle_name.httpd.conf
Source20: %moodle_name.httpd2.conf
Source21: %moodle_name.start.extra.conf
Source22: %moodle_name.start.mods.conf
Source23: %moodle_name.httpd2.inc.conf

Patch1: %name-alt-install-directorypermissions.patch
Patch2: %name-alt-install-datadir-fix.patch

Requires: %name-base = %version-%release
Requires: %name-auth-pam >= 1.9.19.2007101592.04.0.20130114-alt1
Requires: %name-mod-journal >= 1.9.19.20130114-alt1
Requires: %name-mod-hotpot >= 2.4.13.2007101513.0.20130114-alt1

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle >= 2.4
BuildRequires(pre): rpm-macros-apache2
BuildPreReq: rpm-macros-fonts
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses
BuildPreReq: perl-HTML-Parser

%description
Moodle is a course management system (CMS) - a free, Open Source software
package designed using sound pedagogical principles, to help educators create
effective online learning communities.

This package, with dependencies, install all the standard components
of Moodle.

%package base
Summary: Base part for Moodle CMS
Group: Networking/WWW

PreReq: webserver-common
PreReq: %_sbindir/web-condstop-rpm
PreReq: %_sbindir/web-condstart-rpm
PreReq: %_sbindir/mt-getCFG
PreReq: %_sbindir/mt-setCFG
PreReq: %_sbindir/mt-newdatadir
Requires: %webserver_webappsdir
Requires: php-engine php5-gd2 php5-openssl php5-xmlrpc php5-curl iconv php5-mbstring php5-ldap
Requires: texlive-base-bin ImageMagick
Provides: %moodle_dir
Provides: %moodle_admindir
Provides: %moodle_authdir
Provides: %moodle_blocksdir
Provides: %moodle_calendardir
Provides: %moodle_coursedir
Provides: %moodle_docdir
Provides: %moodle_enroldir
Provides: %moodle_filesdir
Provides: %moodle_filterdir
Provides: %moodle_langdir
Provides: %moodle_libdir
Provides: %moodle_logindir
Provides: %moodle_moddir
Provides: %moodle_pixdir
Provides: %moodle_questiondir
Provides: %moodle_questionformatdir
Provides: %moodle_themedir
Provides: %moodle_datadir
Provides: %moodle_name-version = %packagemoodleversion
Provides: moodle-lang-en_utf8 = %version-%release
Obsoletes: moodle-lang-en_utf8 < %version-%release
Conflicts: moodle-apache2 <= 1.9.10-alt2.cvs20101110
Conflicts: moodle-apache2 >= 2.0
Conflicts: moodle-lang >= 2.0
Conflicts: moodle-local-mysql >= 2.0
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-appfor >= 2.0
# Old moodle-lang-*
Conflicts: moodle-lang-be_utf8 < 1.9.10.20100526
Conflicts: moodle-lang-de_utf8 < 1.9.10.20110705
Conflicts: moodle-lang-es_utf8 < 1.9.10.20101112
Conflicts: moodle-lang-fr_utf8 < 1.9.10.20110718
Conflicts: moodle-lang-hy_utf8 < 1.9.10.20100526
Conflicts: moodle-lang-it_utf8 < 1.9.10.20110319
Conflicts: moodle-lang-ja_utf8 < 1.9.10.20110809
Conflicts: moodle-lang-pt_utf8 < 1.9.10.20100814
Conflicts: moodle-lang-ru_utf8 < 1.9.10.20100617
Conflicts: moodle-lang-uk_utf8 < 1.9.10.20100526
Conflicts: moodle-lang-uz_utf8 < 1.9.10.20100526
Conflicts: moodle-lang-zh_tw_utf8 < 1.9.10.20100526
Conflicts: moodle-lang-zh_cn_utf8 < 1.9.10.20100526

%description base
%summary

Part of the standard components of Moodle, is not included
in this package is moved to subpackages.

#%package apache
#Summary: apache-related config for Moodle CMS
#Group: Networking/WWW
#Requires: %name = %version-%release
#Requires: apache apache-mod_php5

#%description apache
#%summary

%package apache2
Summary: apache2-related config for Moodle CMS
Group: Networking/WWW
Requires: apache2-base > 2.2.17-alt2
Requires: %apache2_extra_available
Requires: %apache2_extra_enabled
Requires: %apache2_extra_start
Requires: %apache2_mods_start
Requires: %apache2_confdir_inc
Requires: %name-base < 2.0
Requires: %moodle_dir
Requires: %moodle_datadir
Requires: apache2-mod_php5
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

%description apache2
%summary

%package local-mysql
Summary: installed mysql-server on localhost for Moodle
Group: Networking/WWW
Requires: %name-base < 2.0
Requires: /usr/sbin/mysqld
Requires: php5-mysql
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

%description local-mysql
%summary

#%package local-pgsql
#Summary: installed postgresql-server on localhost for Moodle
#Group: Networking/WWW
#Requires: %name = %version-%release
#Requires: postgresql8.2-server php5-pgsql

#%description local-pgsql
#%summary

%define auth_pam_moodlerequires %(echo %packagemoodleversion | sed -r 's/(^[0-9]+)(\..*)?/\1/')
%define auth_pam_packagemoodleversion %packagemoodleversion
%define auth_pam_packagemoodlerelease %packagversion
%package auth-pam
Version: %auth_pam_packagemoodlerelease.%auth_pam_packagemoodleversion.0.%packagedate
Summary: PAM authentication for Moodle
Group: Networking/WWW

Requires: pecl-pam
Requires: %moodle_name-base < 2.0
Requires: %moodle_authdir
Requires: %moodle_name-version >= %auth_pam_moodlerequires
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-auth-pam-version = %auth_pam_packagemoodleversion
Provides: %moodle_name-auth-pam-appfor = %auth_pam_moodlerequires
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

%description auth-pam
PAM (Pluggable Authentication Modules) authentication methods for Moodle

%define mod_journal_moodlerequires 2007101509
%define mod_journal_packagemoodleversion 2007101509
%package mod-journal
Summary: Module Journal for Moodle
Group: Networking/WWW

Requires: %moodle_name-base < 2.0
Requires: %moodle_moddir
Requires: %moodle_name-version >= %mod_journal_moodlerequires
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-mod-journal-version = %mod_journal_packagemoodleversion
Provides: %moodle_name-mod-journal-appfor = %mod_journal_moodlerequires
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

%description mod-journal
This module allows a teacher to ask students to reflect on a particular
topic. The students can edit and refine their answer over time.

%define mod_hotpot_moodlerequires 2007101509
%define mod_hotpot_packagemoodleversion 2007101513
%define mod_hotpot_packagemoodlerelease 2.4.13
%package mod-hotpot
Version: %mod_hotpot_packagemoodlerelease.%mod_hotpot_packagemoodleversion.0.%packagedate
Summary: HotPot module for Moodle
Group: Networking/WWW

Requires: %moodle_name-base < 2.0
Requires: %moodle_moddir
Requires: %moodle_questionformatdir
Requires: %moodle_name-version >= %mod_hotpot_moodlerequires
Provides: %moodle_name-appfor = 1.9
Provides: %moodle_name-mod-hotpot-version = %mod_hotpot_packagemoodleversion
Provides: %moodle_name-mod-hotpot-appfor = %mod_hotpot_moodlerequires
Conflicts: %moodle_name >= 2.0
Conflicts: %moodle_name-base >= 2.0

%description mod-hotpot
The Hotpot activity module allows teachers to administer Hot Potatoes
and TexToys quizzes via Moodle. These quizzes are created on
the teacher's computer and then uploaded to the Moodle course. After
students have attempted the quizzes, a number of reports are available
which show how individual questions were answered and some statistical
trends in the scores.

%add_perl_lib_path %moodle_filterdir/algebra
%define filter_from_reqprov /^perl(\\(AlgParser\\.pm\\|algebra2tex\\.pl\\))/d
%filter_from_provides %filter_from_reqprov
%filter_from_requires %filter_from_reqprov

%prep
%setup -q
%patch1 -p1
%patch2 -p1

rm -f filter/tex/*mimetex*
#rm -f filter/algebra/*
rm -f lib/default.ttf

%build

%install
# install moodle
mkdir -p %buildroot%moodle_dir/
mkdir -p %buildroot%moodle_datadir/
cp -rp * %buildroot%moodle_dir/

# create config.php
touch %buildroot%moodle_dir/config.php

%define mimetexlinux_filter %moodle_filterdir/tex/mimetex.linux
ln -s -f $(relative %buildroot%webserver_cgibindir/mimetex.cgi \
	%buildroot%mimetexlinux_filter) \
	%buildroot%mimetexlinux_filter

%define default_ttf %moodle_libdir/default.ttf
ln -s -f $(relative %buildroot%_ttffontsdir/freefont/FreeSans.ttf \
	%buildroot%default_ttf) \
	%buildroot%default_ttf

# install apache config
install -pD -m0644 %SOURCE10 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

# install apache2 config
install -pD -m0644 %SOURCE20 %buildroot%apache2_extra_available/%name.conf
install -pD -m0644 %SOURCE21 %buildroot%apache2_extra_start/100-%name.conf
install -pD -m0644 %SOURCE22 %buildroot%apache2_mods_start/100-%name.conf
install -pD -m0644 %SOURCE23 %buildroot%apache2_confdir_inc/Directory_%{moodle_name}_default.conf

mkdir -p %buildroot%apache2_extra_enabled/
touch %buildroot%apache2_extra_enabled/%name.conf

#Disclosure of the macros
find %buildroot%moodle_dir/install.php %buildroot%_sysconfdir -type f -print0 \
	| xargs -r0 sed -ri "
s@%%(\{name\}|name([[:space:]/'\"=]))@%name\2@g
s@%%(\{webserver_datadir\}|webserver_datadir([[:space:]/'\"=]))@%webserver_datadir\2@g
s@%%(\{moodle_name\}|moodle_name([[:space:]/'\"=]))@%moodle_name\2@g
s@%%(\{moodle_dir\}|moodle_dir([[:space:]/'\"=]))@%moodle_dir\2@g
s@%%(\{moodle_datadir\}|moodle_datadir([[:space:]/'\"=]))@%moodle_datadir\2@g
"

%triggerun base -- moodle <= 1.9.13.20110817-alt2.1, moodle-base <= 1.9.16.20120217-alt3, moodle-apache <= 1.9.10-alt2.cvs20101110, moodle-apache2 <= 1.9.10-alt2.cvs20101110
if ls -l %moodle_dir/ | egrep -qsm1 '^([^[:space:]]+[[:space:]]+){3}(apache2?|root)[[:space:]]'; then
	echo "Warning: GUD directory %moodle_dir/ changed to %webserver_group."
	chgrp %webserver_group %moodle_dir/
fi
if [ -e "%moodle_dir/config.php" ]; then
	%_sbindir/web-condstop-rpm

	old_moodle_directorypermissions="`%_sbindir/mt-getCFG --file=%moodle_dir/config.php --format='%%05o' directorypermissions`"
	if [ "$old_moodle_directorypermissions" != "02770" ]; then
		new_moodle_directorypermissions="02770"
		echo "Warning: In the file %moodle_dir/config.php"
		echo "    \$CFG->directorypermissions value varies with the $old_moodle_directorypermissions on the $new_moodle_directorypermissions."
	else
		new_moodle_directorypermissions="$old_moodle_directorypermissions"
	fi

	old_moodle_dataroot="`%_sbindir/mt-getCFG --file=%moodle_dir/config.php dataroot`"
	if (echo "$old_moodle_dataroot" | \
			egrep -q '^[[:space:]]*(%moodle_olddatadir|%moodle_olddatadir2)(/+)?[[:space:]]*$'); then
		new_moodle_dataroot="%moodle_datadir"
		rpmold_moodle_dataroot="`echo "$old_moodle_dataroot" | \
			sed -r 's@^[[:space:]]([^[:space:]]+[^/[:space:]])/*[[:space:]]*$@\1.rpmold@'`"
		echo "Warning: In the file %moodle_dir/config.php"
		echo "    path $old_moodle_dataroot replaced by %moodle_datadir."
	else
		new_moodle_dataroot="$old_moodle_dataroot"
		rpmold_moodle_dataroot=
	fi

	if [ "$old_moodle_dataroot" != "$new_moodle_dataroot" ] \
			|| [ "$old_moodle_directorypermissions" != "$new_moodle_directorypermissions" ]; then
		echo 'Original file %moodle_dir/config.php is saved as %moodle_dir/config.php.rpmold.'
		cp -fa --backup=t "%moodle_dir/config.php" "%moodle_dir/config.php.rpmold"

		if [ "$old_moodle_dataroot" != "$new_moodle_dataroot" ] \
				&& [ -e "$old_moodle_dataroot" ] \
				&& [ -d "$old_moodle_dataroot" ] \
				&& ( \
					( \
						[ -e "$new_moodle_dataroot" ] \
						&& [ -d "$new_moodle_dataroot" ] \
						&& [ "x`find "$new_moodle_dataroot" -mindepth 1 -maxdepth 1`" = "x" ] \
					) \
					|| ( \
						[ ! -e "$new_moodle_dataroot" ] \
					) \
				); then
			echo "Original directory $old_moodle_dataroot is renamed as $rpmold_moodle_dataroot."
			mv "$old_moodle_dataroot" "$rpmold_moodle_dataroot"

			echo "All contents of the directory $old_moodle_dataroot"
			echo "is copied to the $new_moodle_dataroot."
			%_sbindir/mt-newdatadir --file=%moodle_dir/config.php \
				-m 'rpm update to %name-base-%version-%release' \
				"$new_moodle_dataroot"
			pushd "$rpmold_moodle_dataroot"
				find . -mindepth 1 -maxdepth 1 -printf '%%f\0' \
					| xargs -r0 cp -af --target-directory="$new_moodle_dataroot/"
			popd

			chmod $new_moodle_directorypermissions "%moodle_domainsdir"
			chown root:%webserver_group "%moodle_domainsdir"
		fi

		if [ "$old_moodle_directorypermissions" != "$new_moodle_directorypermissions" ]; then
			%_sbindir/mt-setCFG --file=%moodle_dir/config.php --no-quote \
				-m 'rpm update to %name-base-%version-%release' \
				directorypermissions $new_moodle_directorypermissions
		fi
	fi

	if [ -e "$new_moodle_dataroot" ] \
			&& [ -d "$new_moodle_dataroot" ]; then
		if [ "x`find "$new_moodle_dataroot" -mindepth 1 -type d ! -perm $new_moodle_directorypermissions`" != "x" ]; then
			echo "Warning: Change permissions of subdirectories"
			echo "    $new_moodle_dataroot on the $new_moodle_directorypermissions."
			find "$new_moodle_dataroot" -mindepth 1 -type d ! -perm $new_moodle_directorypermissions -print0 \
				| xargs -0 chmod $new_moodle_directorypermissions
		fi

		if [ "x`find "$new_moodle_dataroot" -mindepth 1 ! -group %webserver_group`" != "x" ]; then
			echo "Warning: GUD files and subdirectories"
			echo "    $old_moodle_dataroot changed to %webserver_group."
			find "$new_moodle_dataroot" -mindepth 1 ! -group %webserver_group -print0 \
				| xargs -0 chgrp %webserver_group
		fi
	fi

	%_sbindir/web-condstart-rpm
fi
exit 0

%triggerun apache2 -- moodle-apache2 <= 1.9.10-alt2.cvs20101110
if [ -e %apache2_addonconfdir/A.%name.conf ]; then
	echo "Warning: The configuration file %apache2_addonconfdir/A.%name.conf"
	echo "   outdated and was saved as %apache2_addonconfdir/N.%name.conf.rpmold."
	echo "   Use %apache2_extra_available/%name.conf."
	mv %apache2_addonconfdir/A.%name.conf %apache2_addonconfdir/N.%name.conf.rpmold
fi
exit 0

#%post apache
#chown root:apache %moodle_dir/
#control apache-mod_php5 relaxed
#%_initdir/httpd reload

#%postun apache
#%_initdir/httpd reload

%files

%files base
%dir %attr(2775,root,%webserver_group) %moodle_dir/
%ghost %config(noreplace) %moodle_dir/config.php
%moodle_dir/*
%exclude %moodle_authdir/pam/
%exclude %moodle_moddir/journal/
%exclude %moodle_moddir/hotpot/
%exclude %moodle_questionformatdir/hotpot/
%dir %attr(2770,root,%webserver_group) %moodle_datadir/

#%files apache
#%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf
%ghost %apache2_extra_enabled/%name.conf
%config(noreplace) %apache2_confdir_inc/Directory_%{moodle_name}_default.conf
%config(noreplace) %apache2_extra_start/100-%name.conf
%config(noreplace) %apache2_mods_start/100-%name.conf

%files local-mysql

#%files local-pgsql

%files auth-pam
%moodle_authdir/pam/

%files mod-journal
%moodle_moddir/journal/

%files mod-hotpot
%moodle_moddir/hotpot/
%moodle_questionformatdir/hotpot/

%changelog
* Wed May 15 2013 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20130513-alt1
- repocop cronbuild 20130515. At your service.
- 1.9.19+ (Build: 20130513)

* Mon May 13 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9.19.20130125-alt2
- Change requires: MySQL-server to /usr/sbin/mysqld for mariadb
  compatibility in moodle-local-mysql

* Sat May 11 2013 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20130125-alt1
- repocop cronbuild 20130511. At your service.
- 1.9.19+ (Build: 20130125)

* Tue Apr 16 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9.19.20130114-alt2
- Fix requires for %%name subpackage

* Sat Jan 12 2013 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20130114-alt1
- repocop cronbuild 20130112. At your service.
- 1.9.19+ (Build: 20130114)

* Fri Dec 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20121220-alt1
- repocop cronbuild 20121221. At your service.
- 1.9.19+ (Build: 20121220)

* Sat Nov 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20121112-alt1
- repocop cronbuild 20121110. At your service.
- 1.9.19+ (Build: 20121112)

* Fri Aug 24 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20120823-alt1
- repocop cronbuild 20120824. At your service.
- 1.9.19+ (Build: 20120823)

* Fri Aug 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20120809-alt1
- repocop cronbuild 20120810. At your service.
- 1.9.19+ (Build: 20120809)

* Thu Jul 19 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20120719-alt1
- repocop cronbuild 20120719. At your service.
- 1.9.19+ (Build: 20120719)

* Sat Jul 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.19.20120706-alt1
- repocop cronbuild 20120707. At your service.
- 1.9.19 (Build: 20120706)

* Mon Jun 25 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.18.20120624-alt1
- repocop cronbuild 20120625. At your service.
- 1.9.18+ (Build: 20120624)

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.18.20120612-alt1
- repocop cronbuild 20120613. At your service.
- 1.9.18+ (Build: 20120612)

* Sat May 26 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.18.20120525-alt1
- repocop cronbuild 20120526. At your service.
- 1.9.18+ (Build: 20120525)

* Sun May 20 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.18.20120519-alt1
- repocop cronbuild 20120520. At your service.
- 1.9.18+ (Build: 20120519)

* Sat May 12 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.18.20120514-alt1
- repocop cronbuild 20120512. At your service.
- 1.9.18 (Build: 20120514)

* Tue May 08 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.17.20120504-alt2
- Move plugins to subpackage:
  + %%name-auth-pam

* Fri May 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.17.20120504-alt1
- repocop cronbuild 20120504. At your service.
- 1.9.17+ (Build: 20120504)

* Fri Apr 20 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.17.20120419-alt1
- repocop cronbuild 20120420. At your service.
- 1.9.17+ (Build: 20120419)

* Thu Apr 12 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.17.20120412-alt1
- repocop cronbuild 20120412. At your service.
- 1.9.17+ (Build: 20120412)

* Thu Mar 29 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.17.20120329-alt1
- repocop cronbuild 20120329. At your service.
- 1.9.17+ (Build: 20120329)

* Fri Mar 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.17.20120315-alt1
- repocop cronbuild 20120316. At your service.
- 1.9.17+ (Build: 20120315)

* Fri Mar 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120309-alt1
- repocop cronbuild 20120309. At your service.
- 1.9.16+ (Build: 20120309)

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120301-alt1
- repocop cronbuild 20120301. At your service.
- 1.9.16+ (Build: 20120301)

* Tue Feb 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.16.20120217-alt4
- Fix %%triggerun for %%name-base

* Tue Feb 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.16.20120217-alt3
- Set %%ghost %%config(noreplace) for %%moodle_dir/config.php

* Sat Feb 18 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.16.20120217-alt2
- Moodle datadir is moved to
  %%_localstatedir/%%moodle_name/%%moodle_defaultdatadirname

* Fri Feb 17 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120217-alt1
- repocop cronbuild 20120217. At your service.
- 1.9.16+ (Build: 20120217)

* Fri Feb 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120202-alt1
- repocop cronbuild 20120203. At your service.
- 1.9.16+ (Build: 20120202)

* Mon Jan 23 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.16.20120119-alt2
- Fix for cronbuild use

* Fri Jan 20 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120119-alt1
- repocop cronbuild 20120120. At your service.
- 1.9.16+ (Build: 20120119)

* Fri Jan 20 2012 Aleksey Avdeev <solo@altlinux.ru> 1.9.16.20120112-alt2
- Update cronbuild use

* Sat Jan 14 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120112-alt1
- repocop cronbuild 20120114. At your service.
- 1.9.16+ (Build: 20120112)

* Wed Jan 11 2012 Cronbuild Service <cronbuild@altlinux.org> 1.9.16.20120109-alt1
- repocop cronbuild 20120111. At your service.
- 1.9.16 (Build: 20120109)

* Sat Dec 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.15.20111223-alt1
- repocop cronbuild 20111224. At your service.
- 1.9.15+ (Build: 20111223)

* Fri Dec 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.15.20111209-alt1
- repocop cronbuild 20111209. At your service.
- 1.9.15+ (Build: 20111209)

* Tue Dec 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.15.20111205-alt1
- repocop cronbuild 20111206. At your service.
- 1.9.15+ (Build: 20111205)

* Sat Dec 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.15.20111201-alt1
- repocop cronbuild 20111203. At your service.
- 1.9.15+ (Build: 20111201)

* Wed Nov 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.15.20111128-alt1
- repocop cronbuild 20111130. At your service.
- 1.9.15 (Build: 20111128)

* Sun Nov 27 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111125-alt1
- repocop cronbuild 20111127. At your service.
- 1.9.14+ (Build: 20111125)

* Fri Nov 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111118-alt1
- repocop cronbuild 20111118. At your service.
- 1.9.14+ (Build: 20111118)

* Tue Nov 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111115-alt1
- repocop cronbuild 20111115. At your service.
- 1.9.14+ (Build: 20111115)

* Wed Nov 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111102-alt1
- repocop cronbuild 20111102. At your service.
- 1.9.14+ (Build: 20111102)

* Fri Oct 28 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.14.20111027-alt2
- Update for cronbuild use

* Thu Oct 27 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111027-alt1
- repocop cronbuild 20111027. At your service.
- 1.9.14+ (Build: 20111027)

* Mon Oct 24 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.14.20111019-alt2
- Fix for cronbuild use

* Wed Oct 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111019-alt1
- repocop cronbuild 20111019. At your service.
- 1.9.14+ (Build: 20111019)

* Sat Oct 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.14.20111012-alt1
- repocop cronbuild 20111015. At your service.
- 1.9.14+ (Build: 20111012)

* Sat Oct 15 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.14.20111010-alt2
- Fix for cronbuild use

* Wed Oct 12 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.14.20111010-alt1
- Fix package version
- Fix %%name-mod-hotpot subpackage version

* Tue Oct 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.9.13.20111010-alt1
- repocop cronbuild 20111011. At your service.
- 1.9.14 (Build: 20111010)

* Tue Oct 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110928-alt7
- Fix for cronbuild use

* Mon Oct 10 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110928-alt6
- Fix for cronbuild use

* Sat Oct 08 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110928-alt5
- Fix for cronbuild use

* Thu Oct 06 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110928-alt2
- Fix for cronbuild use

* Wed Oct 05 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110928-alt1
- 1.9.13+ (Build: 20110928)

* Fri Sep 23 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110921-alt1
- 1.9.13+ (Build: 20110921)

* Wed Sep 21 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110916-alt1
- 1.9.13+ (Build: 20110916)

* Mon Sep 05 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110831-alt1
- 1.9.13+ (Build: 20110831)

* Tue Aug 30 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110826-alt1
- 1.9.13+ (Build: 20110826)
- Move modules to subpackage:
  + %%name-mod-hotpot

* Thu Aug 25 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110817-alt4
- Fix subpackage requires

* Thu Aug 25 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110817-alt3
- Base part of Moodle highlighted in the %%name-base subpackage
- Move modules to subpackage:
  + %%name-mod-journal

* Sat Aug 20 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110817-alt2
- Add trigger for set $CFG->directorypermissions to 02770
- Fix trigger for update apache2 config

* Fri Aug 19 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110817-alt1
- 1.9.13+ (Build: 20110817)
- Settings directory %%moodle_dir moved to the
  %%apache2_confdir_inc/Directory_%%{moodle_name}_default.conf

* Fri Aug 12 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110811-alt1
- 1.9.13+ (Build: 20110811)

* Thu Aug 11 2011 Aleksey Avdeev <solo@altlinux.ru> 1.9.13.20110803-alt1
- 1.9.13+ (Build: 20110803)
- GUD directory %%moodle_dir/ changed to %%webserver_group
- Moodle datadir is moved to %%_localstatedir/%%moodle_name
- To configure apache2 using %%apache2_extra_available/%%name.conf,
  instead of %%apache2_addonconfdir/A.%%name.conf
- Return return lang/en_utf8 to package

* Tue Nov 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt2.cvs20101110
- inheritance fixed

* Thu Nov 11 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.9.10-alt1.cvs20101110
- new version

* Tue Oct 27 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.6-alt1.cvs20091021
- new security and bugfix version

* Tue Jul 28 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt4.cvs20090726
- fix spec in section post preun

* Tue Jul 28 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt2.cvs20090726
- fix spec

* Sun Jul 26 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.5-alt1.cvs20090726
- security fix cvs update

* Sat Apr 18 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.4-alt1.cvs20090415
- security fix cvs update

* Sun Apr 12 2009 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.4-alt1.cvs20090408
- security fix version

* Mon Dec 15 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt2.cvs20081210
- set permissions on /var/webapps/moodlemata to root:_webmaster by WebPolicy

* Thu Dec 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1.cvs20081210
- weekly bug fix build from cvs

* Thu Oct 16 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.3-alt1
- security fix version

* Mon Oct 13 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20081008
- weekly bug fix build from cvs

* Mon Sep 08 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080903
- build from cvs
- remove lang/en_utf8 to package

* Wed Aug 27 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080827
- build from cvs
- MDL-16061   Remove 'username' from the $moodleattributes array
- MDL-14453   Smilies from HTML editor seem to be relative URLs and thus break in email
- MDL-15304   Labels with nothing but tags in them don't work
- MDL-9983    trigger certain events out of the core to modules
- MDL-14565   Give modules the ability to add whole trees of settings pages to the admin menu of they want.
- MDL-8912    Review 17_STABLE and 18_STABLE 19_STABLE Unmerged Files before July 1.9.2 release
- MDL-14201   Summary graph
- MDL-13861   lib/statslib SQL errors under Oracle
- MDL-15203   Theme credits require updating
- MDL-12809   $CATEGORY label doesn't work in GIFT
- MDL-14697   Participants page OK button is redundant
- MDL-15473   Moodle Format image tags are ignored if there is no image (base_64) information
- MDL-12392   Manual grading report does not recognise global role assignments of students
- MDL-14200   Add group and course averages
- MDL-7772    Quiz results overview: not all combinations of Show attempts with ... & Groups settings work properly
- MDL-13678   Change default number of rows per page on quiz reports
- MDL-14764   Imported multichoice questions may have a blank answernumbering value, which results in an "ERR" prefix to all answers' text.
- MDL-13927   Indicate missing parent languages on lang pack import page

* Thu Jul 31 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1.cvs20080730
- build from cvs
- MDL-15787   Using hidden feedbacks on front page
- MDL-8270    Full block backup/restore routine with code
- MDL-14261   User denied access to view site logs when moodle/site:viewreports allowed in the system context
- MDL-15544   Disable email signup in new installation - add danger warning
- MDL-14932   Improve  accessibility of 'assign role' button and the consistency of the UI in bulk user actions page
- MDL-15610   mtable entry for \mod\label\db\install.xml should be label not quiz
- MDL-15601   Check for things before trying to use them to avoid notices
- MDL-15198   non-standard sql in reportlib.php
- MDL-15034   course restore as admin overwrites front page
- MDL-15689   Backup/restore process does not keep the categories in the gradebook
- MDL-15080   char to int cast problem in get_recent_enrolments()
- MDL-13942   Cannot restore course that contains groups
- MDL-14453   Smilies from HTML editor seem to be relative URLs and thus break in email
- MDL-13261   get_context_users_by_cap has some problems
- MDL-13811   Add a confirmation step when a user changes their own email address in their profile.
- MDL-14233   Make bulk user picture upload handle subdirectories in zip files (with patch)
- MDL-14279   Use get_file_url instead of manual slasharguments check
- MDL-14035   Grader report doesn't respect the user->picture field...
- MDL-13343   When deleting a course category, it will also delete all courses in that category
- MDL-14999   Patch fixing various HTMLarea issues
- MDL-15389   add info concerning spam dangers of open profiles
- MDL-8912    Review 17_STABLE and 18_STABLE 19_STABLE Unmerged Files before July 1.9.2 release
- MDL-10586   $table->head of admin/user.php needs some fix.
- MDL-10633   Event names in Calendar are not properly escaped with recursive_stripslashes
- MDL-14838   Bad packaging of /mod/wiki/overridelock.php

* Fri Jul 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.2-alt1
- new security fix version
- MDL-15184: sql injection in HotPot module
- MDL-15413: Potential webroot disclosures warning
- MDL-15079: Potential non-persistent XSS when searching for group members (MSSQL and Oracle only)
- MDL-15552: potential sql injection in events handling code
- MDL-15516: profiles of deleted users were accessible
- MDL-13811: Email could be changed in profile without confirmation

* Fri Jul 11 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt6.cvs20080711.1
- build from last week cvs
- MDL-14820   Bad XHTML when deleting directory
- MDL-14173   Oracle NLS_NUMERIC_CHARACTERS break TESTs, config settings from Oct/07 help!
- MDL-11629   Oracle can't store multiple choice fractional value questions.
- MDL-10974   Infinite loop in enrol/database/enrol.php syncronization code
- MDL-13860   ADL Scorm 2004 LMS Conformance Test
- MDL-13343   When deleting a course category, it will also delete all courses in that category
- MDL-14378   When deleting course category deal with everything that depends on its context
- MDL-14439   Drop down menus not usable and not accessible in IE using keyboard only
- MDL-9655    database module preset importer eats html
- MDL-9684    sort field in database preset import/export
- MDL-13618   Restore: Gradebook - fix restore so that individual grade exclusions are restored to 1.9 gradebook as excluded
- MDL-12842   Gradebook fails to properly calculate score when using "drop X lowest" and "exclude assignment"
- MDL-13900   Course-access partially not working correctly
- MDL-14466   Preset importer throws error
- MDL-15524   Manual grade items with calculations not restoring properly.
- MDL-14841   Grade item calculation formula not restored properly

* Mon Jul 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt6.cvs20080702
- fix path to moodledata
- fix mimetex filter

* Fri Jul 04 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt5.cvs20080702
- fix httpd.conf

* Wed Jul 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt4.cvs20080702
- fix httpd(2).conf

* Wed Jul 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt3.cvs20080702
- remove .httaccess and add config php to http(2).conf
- last week cvs
- MDL-15029   Create an enrollment plug-in to create a group for each new user
- MDL-13321   Improve forum tracking related code in cron
- MDL-14525   bad result in the Excel after download
- MDL-14439   Drop down menus not usable and not accessible in IE using keyboard only
- MDL-12300   message window does not show date
- MDL-13796   Captcha element for registration form
- MDL-7407    Add turing number into email signup form

* Fri Jun 27 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt2.cvs20080625
- add .htaccess

* Fri Jun 27 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.1.cvs20080625
- rebuild with fix moodle.spec

* Thu Jun 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080625
- new version from cvs
- change install path to /var/www/webapps
- MDL-14342   Quotes mismatch leads to print "$cid" instead of the value of  $cid
- MDL-14525   bad result in the Excel after download
- MDL-15029   Create an enrollment plug-in to create a group for each new user
- MDL-15331   Feedback fails to remove slashes when editing questions in 1.9.
- MDL-14336   mdl_data's defaultsort ID not set properly at importing preset.zip
- MDL-14378   When deleting course category deal with everything that depends on its context
- MDL-14525   bad result in the Excel after download
- MDL-10038   Forum Tracking - Logic and Links are wrong
- MDL-14328   Global Search : Initial settings when installing do not allow finding the converters, even if additional libs have been copied in.
- MDL-14804   question_list_instances is broken
- MDL-14223   Add a column for the user's idnumber, controllable by a site-wide setting
- MDL-15234   exported questions from moodle 1.8 will not be imported correctly on moodle 1.9
- MDL-14104   Make generate_password() respect password complexity policies (with patch)
- MDL-15029   Create an enrollment plug-in to create a group for each new user
- MDL-13900   Course-access partially not working correctly
- MDL-9907    Make it possible to have the ##user## (=author) a sortable and searchable field
- MDL-15202   The item textarea print out a notice while the excelexport if there are no values
- MDL-14235   On logging in an image appeary instead of the moodle page. always works correctly the second try.
- MDL-15186   when editing questions, fields appears blank on php4
- MDL-14557   PostgreSQL+empty integer problem: user/editadvanced_form.php
- MDL-12531   Add "institution" to lockable fields (admin/auth_config.php)

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.1.cvs20080528
- rebuild with spec correction

* Mon Jun 02 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.9.1-alt1.cvs20080528
- new version from cvs

* Tue Jun 05 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.8.1-alt1
- built for ALT Linux
