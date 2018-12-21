%define pear_name HTML_Template_PHPLIB

Name: pear-HTML_Template_PHPLIB
Version: 1.6.0
Release: alt1

Summary: preg_* based template system

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/HTML_Template_PHPLIB

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Template_PHPLIB-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The popular Template system from PHPLIB ported to PEAR. It has some
features that can't be found currently in the original version like
fallback paths. It has minor improvements and cleanup in the code as
well as some speed improvements.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%_bindir/*
%pear_dir/HTML/
%pear_testdir/HTML_Template_PHPLIB/tests/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Feb 18 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- initial build for ALT Linux Sisyphus

