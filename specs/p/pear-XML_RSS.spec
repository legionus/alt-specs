%define pear_name XML_RSS

Name: pear-XML_RSS
Version: 1.0.2
Release: alt1

Summary: RSS parser

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/XML_RSS

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_RSS-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-XML_Tree

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

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
%pear_dir/XML/
%pear_testdir/XML_RSS/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus

