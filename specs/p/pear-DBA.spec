%define pear_name DBA

Name: pear-DBA
Version: 1.1.1
Release: alt3

Summary: Berkely-style database abstraction class

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/DBA

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DBA-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
DBA is a wrapper for the php DBA functions. It includes a file-based
emulator and provides a uniform, object-based interface for the
Berkeley-style database systems.

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
%pear_dir/DBA
%pear_testdir/DBA/
%pear_dir/DBA.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

